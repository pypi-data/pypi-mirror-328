'''Discoverer that uses static configuration.'''

# Copyright (c) 2024 Carnegie Mellon University
# This code is subject to the license terms contained in the LICENSE file.

import logging
from queue import Queue
from typing import Dict, List

from ..communicators.impl.communicator import Communicator
from ..config_components.distributed_config import DistributedConfig
from ..neighbor_manager.event import NewNeighbor
from ..neighbor_manager.node_id import NodeID
from .impl.discoverer import Discoverer
from .impl.discoverer_catalog import DiscovererCatalog

from ..wrangler.logger import Logger

log = Logger(__file__, level=logging.DEBUG).logger()


class StaticDiscoverer(Discoverer):
    '''Discoverer that uses static configuration.'''
    name = 'static'
    tags: Dict[str, List[str]] = {}

    def __init__(self, config: DistributedConfig,
                 communicator: Communicator):
        super().__init__(config=config, communicator=communicator)
        neighbors = self._config.get_static_adjacency(my_id=communicator.my_id)
        assert neighbors is not None, (
            'BUG: Attempt to define StaticDiscoverer with no static config.')
        self._neighbors = neighbors
        known = self._communicator.known_neighbors
        log.debug('StaticDiscoverer: known_neighbors=%s, adding=%s', known, neighbors)
        known.update(neighbors)

    def start(self, queue: Queue):
        for node in self._neighbors:
            queue.put(NewNeighbor(neighbor=NodeID(node)))
        self._communicator.start(
            queue=queue
        )


def register(catalog: DiscovererCatalog) -> None:
    '''Register all objects in this file.'''
    catalog.register(StaticDiscoverer)
