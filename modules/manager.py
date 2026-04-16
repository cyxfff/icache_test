from .block_loop import BlockLoopBuilder
from .call_ret_chain import CallRetChainBuilder
from .hot_region import HotRegionBuilder
from .indirect_target_set import IndirectTargetSetBuilder
from .plt_stub_chain import PltStubChainBuilder
from .tlb_region import TLBRegionBuilder


class SynthesisModuleManager:
    def __init__(self):
        self.cold_block_sequence = BlockLoopBuilder()
        self.block_loop = self.cold_block_sequence
        self.fetch_amplifier = BlockLoopBuilder()
        self.hot_region_loop = HotRegionBuilder()
        self.hot_region = self.hot_region_loop
        self.tlb_region = TLBRegionBuilder()
        self.call_ret_chain = CallRetChainBuilder()
        self.plt_stub_chain = PltStubChainBuilder()
        self.indirect_target_set = IndirectTargetSetBuilder()
