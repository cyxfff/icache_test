from .mixed_region import MixedRegionBuilder

try:
    from old_modules.block_loop import BlockLoopBuilder
    from old_modules.call_ret_chain import CallRetChainBuilder
    from old_modules.data_cache import DataCacheBuilder
    from old_modules.hot_region import HotRegionBuilder
    from old_modules.indirect_target_set import IndirectTargetSetBuilder
    from old_modules.plt_stub_chain import PltStubChainBuilder
    from old_modules.tlb_region import TLBRegionBuilder
except ImportError:
    from ..old_modules.block_loop import BlockLoopBuilder
    from ..old_modules.call_ret_chain import CallRetChainBuilder
    from ..old_modules.data_cache import DataCacheBuilder
    from ..old_modules.hot_region import HotRegionBuilder
    from ..old_modules.indirect_target_set import IndirectTargetSetBuilder
    from ..old_modules.plt_stub_chain import PltStubChainBuilder
    from ..old_modules.tlb_region import TLBRegionBuilder


class SynthesisModuleManager:
    def __init__(self):
        self.cold_block_sequence = BlockLoopBuilder()
        self.block_loop = self.cold_block_sequence
        self.fetch_amplifier = BlockLoopBuilder()
        self.hot_region_loop = HotRegionBuilder()
        self.hot_region = self.hot_region_loop
        self.mixed_region_loop = MixedRegionBuilder()
        self.mixed_region = self.mixed_region_loop
        self.data_cache = DataCacheBuilder()
        self.data_stream = self.data_cache
        self.data_pointer_chase = self.data_cache
        self.data_page_stride = self.data_cache
        self.data_indirect_gather = self.data_cache
        self.data_hot_stride = self.data_cache
        self.data_cold_stride = self.data_cache
        self.data_tlb_indirect = self.data_cache
        self.tlb_region = TLBRegionBuilder()
        self.call_ret_chain = CallRetChainBuilder()
        self.plt_stub_chain = PltStubChainBuilder()
        self.indirect_target_set = IndirectTargetSetBuilder()
