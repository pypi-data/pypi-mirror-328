"""
Base classes

SAMS Software accounting
Copyright (C) 2018-2021  Swedish National Infrastructure for Computing (SNIC)

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; If not, see <http://www.gnu.org/licenses/>.
"""

import logging
import os
import queue
import select
import socket
import threading
import time
from abc import ABC, abstractmethod
from typing import List

from sams.core import Config

logger = logging.getLogger(__name__)


class PIDFinder:
    """PIDFinder base class"""

    def __init__(self, id, jobid, config):
        self.id = id
        self.jobid = jobid
        self.config = config

    # pylint: disable=no-self-use
    def find(self):
        raise NotImplementedError("Not implemented")
        # return []


class SamplerException(Exception):
    pass


class Sampler(threading.Thread):
    """Sampler base class"""

    def __init__(self, id, outQueue, config):
        super(Sampler, self).__init__()
        self.id = id
        self._most_recent_sample = None
        self.outQueue = outQueue
        self.config = config
        self.jobid = self.config.get(["options", "jobid"])
        self.pidQueue = queue.Queue()
        self.pids = []
        self.sampler_interval = self.config.get([self.id, "sampler_interval"], 60)

    def init(self):  # pylint: disable=no-self-use
        pass

    def run(self):
        try:
            self.init()
        except Exception:
            logger.exception("Failed to do self.init in %s", self.id)
        while True:
            try:
                pids = self.pidQueue.get(timeout=self.sampler_interval)
                if not pids:
                    self.pidQueue.task_done()
                    break
                logger.debug("Received new pids: %s", pids)
                self.pids.extend(pids)
                self.pidQueue.task_done()
            except queue.Empty:
                logger.debug("%s queue.Empty timeout", self.id)
            try:
                if self.do_sample():
                    self.sample()
            except Exception:
                logger.exception("Failed to do self.sample in %s", self.id)

        try:
            self.store(self.final_data(), "final")
        except Exception:
            logger.exception("Failed to do self.final_data in %s", self.id)
        self.outQueue.join()

    def _storage_wrapping(self, data, type="now"):
        """
        Convenience method for wrapping data into a dictionary used
        by several other methods.
        """
        return {"id": self.id, "data": data, "type": type}

    def store(self, data, type="now"):
        self.outQueue.put(self._storage_wrapping(data, type))

    @property
    def most_recent_sample(self):
        """The most recently sample or set of samples stored by a call
        to ``self.sample()``."""
        return self._most_recent_sample

    # this should be implemented in the real Sampler..
    # pylint: disable=no-self-use
    def sample(self):
        raise NotImplementedError("Not implemented")

    # this should be implemented in the real Sampler..
    # pylint: disable=no-self-use
    def final_data(self):
        raise NotImplementedError("Not implemented")

    def do_sample(self):
        return len(self.pids) > 0

    def exit(self):
        logger.debug("%s exit", self.id)
        self.pidQueue.put(None)


class AggregatorException(Exception):
    pass


class Aggregator:
    """Aggregator base class"""

    def __init__(self, id, config):
        self.id = id
        self.config = config

    # pylint: disable=no-self-use
    def aggregate(self, data):
        raise NotImplementedError("Not implemented")


class Loader:
    """Loader base class"""

    def __init__(self, id, config):
        self.id = id
        self.config = config

    # pylint: disable=no-self-use
    def load(self):
        raise NotImplementedError("Not implemented")

    # pylint: disable=no-self-use
    def next(self):
        raise NotImplementedError("Not implemented")

    # pylint: disable=no-self-use
    def commit(self):
        raise NotImplementedError("Not implemented")


class BackendException(Exception):
    pass


class Backend:
    """Backend base class"""

    def __init__(self, id, config):
        self.id = id
        self.config = config

    # pylint: disable=no-self-use
    def update(self, software):
        raise NotImplementedError("Not implemented")

    # pylint: disable=no-self-use
    def extract(self):
        raise NotImplementedError("Not implemented")


class Software:
    """Software base class"""

    def __init__(self, id, config):
        self.id = id
        self.config = config

    # pylint: disable=no-self-use
    def update(self):
        raise NotImplementedError("Not implemented")


class Output(threading.Thread):
    """Output base class"""

    def __init__(self, id, config):
        super(Output, self).__init__()
        self.id = id
        self.config = config

        self.dataQueue = queue.Queue()
        self.jobid = self.config.get(["options", "jobid"])

    def run(self):
        while True:
            data = self.dataQueue.get()
            if data is None:
                self.dataQueue.task_done()
                break
            try:
                self.store({data["id"]: data["data"]})
            except Exception:
                logger.exception("Failed to store")
            if "type" in data and data["type"] == "final":
                try:
                    self.final({data["id"]: data["data"]})
                except Exception:
                    logger.exception("Failed to do self.final in %s", self.id)
            self.dataQueue.task_done()

        for _ in range(int(self.config.get([self.id, "retry_count"], 3))):
            try:
                self.write()
                break
            except Exception:
                logger.exception("Failed to do self.write in %s", self.id)
            time.sleep(int(self.config.get([self.id, "retry_sleep"], 3)))

    # pylint: disable=no-self-use
    def store(self, data):
        raise NotImplementedError("Not implemented")

    def final(self, data):
        self.store(data)

    # pylint: disable=no-self-use
    def write(self):
        raise NotImplementedError("Not implemented")

    def exit(self):
        self.dataQueue.put(None)


class XMLWriter:
    """XMLWriter base class"""

    def __init__(self, id, config):
        self.id = id
        self.config = config

    # pylint: disable=no-self-use
    def write(self, data):
        raise NotImplementedError("Not implemented")


class Listener(ABC):
    """Base class for listening to sockets and sending encoded data."""

    def __init__(self, id: str, config: Config, samplers: List):
        self.id = id
        self.config = config
        self.samplers = samplers
        socket_directory = self.config.get([self.id, "socketdir"], "/tmp/softwareaccounting")
        self.job_id = self.config.get(["options", "jobid"], 0)
        self.server_socket = socket.socket(socket.AF_UNIX)
        self.is_finished = False
        if not os.path.isdir(socket_directory):
            os.mkdir(socket_directory)
        self.socket_path = f"{socket_directory}/{self.id}_{self.job_id:d}.socket"
        logger.debug(f"Socket path: {self.socket_path}")
        if os.path.exists(self.socket_path):
            os.unlink(self.socket_path)
        self.server_socket.bind(self.socket_path)
        self.thread = threading.Thread(target=self._listen)

    def start(self):
        """Starts listening on thread."""
        self.thread.start()
        logger.debug("Launching listening thread...")

    def exit(self):
        """Sets finished flag to True to kill thread, joins and cleans up."""
        if not self.is_finished:
            self.is_finished = True
            if self.thread.is_alive:
                self.thread.join(1)
            self.server_socket.close()
            os.unlink(self.socket_path)

    def _listen(self):
        """Listens to the socket for connections."""
        self.server_socket.listen(5)
        while not self.is_finished:
            logger.debug("Waiting for connections...")
            readable, _, _ = select.select([self.server_socket], [], [], 1)
            if len(readable) > 0:
                try:
                    connection, address = self.server_socket.accept()
                    logger.debug(f"Connected to {address}")
                except Exception as e:
                    logger.debug(f"Sending data failed due to {e}!")
                with connection:
                    try:
                        connection.sendall(self.encoded_data)
                    except Exception as e:
                        logger.debug(f"Sending data to {address} failed due to {e}!")

    @property
    @abstractmethod
    def encoded_data(self) -> str:
        """Encoded data to be sent to client."""
        raise NotImplementedError
