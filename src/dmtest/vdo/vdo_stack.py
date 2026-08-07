from typing import Any

import dmtest.device_mapper.dev as dmdev
import dmtest.device_mapper.table as table
import dmtest.device_mapper.targets as targets
import dmtest.utils as utils
from dmtest.device_mapper.dev import Dev
from dmtest.process import run


class VDOStack:
    def __init__(self, data_dev: str | Dev, **opts: Any) -> None:
        self._data_dev = data_dev
        self._physical_size: int = opts.pop("physical_size", utils.dev_size(data_dev) * 512)
        self._mode: int = opts.pop("block_size", 4096)
        self._block_map_cache: int = opts.pop("block_map_cache", 128 * 1024 * 1024)
        self._block_map_period: int = opts.pop("block_map_period", 16380)
        self._format: bool = opts.pop("format", True)
        self._logical_size: int = opts.pop("logical_size", 20 * 1024 * 1024 * 1024)
        self._alb_mem: float = opts.pop("albireo_mem", 0.25)
        self._alb_sparse: bool = opts.pop("albireo_sparse", False)
        self._slab_bits: int | None = opts.pop("slab_bits", None)
        self._opts = opts

        if self._format:
            logical_size = "--logical-size=" + str(self._logical_size) + "B"
            mem = "--uds-memory-size=" + str(self._alb_mem)
            sparse = ""
            if self._alb_sparse:
                sparse = " --uds-sparse"
            slab = ""
            if self._slab_bits is not None:
                slab = f" --slab-bits={self._slab_bits}"
            dev = self._data_dev
            run(f"vdoformat --force {logical_size} {mem}{sparse}{slab} {dev}")

    def _vdo_table(self) -> table.Table:
        return table.Table(
            targets.VDOTarget(
                self._logical_size // 512,
                self._data_dev,
                self._physical_size // 4096,
                self._mode,
                self._block_map_cache // 4096,
                self._block_map_period,
                self._opts
            )
        )

    def activate(self) -> dmdev.Dev:
        return dmdev.dev(self._vdo_table())
