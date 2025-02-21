# ruff: noqa: F403, F405, E402
from __future__ import annotations
from ccdexplorer_fundamentals.GRPCClient.types_pb2 import *
from ccdexplorer_fundamentals.enums import NET
from enum import Enum
from ccdexplorer_fundamentals.GRPCClient.queries._SharedConverters import (
    Mixin as _SharedConverters,
)
import os
import sys

sys.path.append(os.path.dirname("ccdexplorer_fundamentals"))
from ccdexplorer_fundamentals.GRPCClient.CCD_Types import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ccdexplorer_fundamentals.GRPCClient import GRPCClient


class Mixin(_SharedConverters):
    def get_consensus_detailed_status(
        self: GRPCClient,
        gen_index: Optional[int] = None,
        net: Enum = NET.MAINNET,
    ) -> CCD_ConsensusDetailedStatus:
        result = {}
        consensus_detailed_status_query = (
            self.generate_consensus_detailed_status_query()
        )

        grpc_return_value: ConsensusDetailedStatus = self.stub_on_net(
            net, "GetConsensusDetailedStatus", consensus_detailed_status_query
        )

        for descriptor in grpc_return_value.DESCRIPTOR.fields:
            key, value = self.get_key_value_from_descriptor(
                descriptor, grpc_return_value
            )
            if type(value) in self.simple_types:
                result[key] = self.convertType(value)

        return CCD_ConsensusDetailedStatus(**result)
