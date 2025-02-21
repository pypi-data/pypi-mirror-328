"""Module for calculating Adler32 checksums."""

from __future__ import annotations

import struct
import zlib
from collections.abc import Iterable
from typing import Any

from ..logger import APP_LOGGER_NAME, get_logger
from ._base import Checksum

log = get_logger(APP_LOGGER_NAME)


class Adler32(Checksum):
    """Adler32 checksum
    from https://github.com/snafus/cephsum/blob/master/cephsum/adler32.py"""

    name: str = "adler32"

    def hexdigest(self, value: int) -> str:
        """Converts an integer to a hex string"""
        # return hex(value)[2:]
        return "".join([f"{x:02x}" for x in struct.pack(">I", value)]).lower()

    def calculate(self, file_buffer: Iterable[Any]) -> str:
        value = 1
        bytes_read = 0
        number_of_buffers_read = 0
        for buffer in file_buffer:
            value = zlib.adler32(buffer, value)
            bytes_read += len(buffer)
            number_of_buffers_read += 1
            log.trace(
                "%s: %s %s %s",
                self.name,
                self.hexdigest(value),
                len(buffer),
                bytes_read,
            )

        self.value = self.hexdigest(value)
        self.bytes_read = bytes_read
        self.number_of_buffers_read = number_of_buffers_read

        return self.value
