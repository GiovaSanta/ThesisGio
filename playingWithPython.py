import sys
import random
import numpy as np
from sfpy import Posit8, Posit16
from ml_dtypes import float8_e4m3
from sfpy import Float32

special_values = [0x00, 0x80, 0xFF, 0x40, 0xC0, 0x01, 0x7F]

formats = {
    "softposit8": {
        "class": Posit8,
        "bit_width": 8,
        "max_val": 255,
    },
    "posit16": {
        "class": Posit16,
        "bit_width": 16,
        "max_val": 65535,
    },
    "ieeefp16": {
        "class": np.float16,
        "bit_width": 16,
        "max_val": None,
    },
    "float8_e4m3": {
        "class": float8_e4m3,
        "bit_width": 8,
        "max_val": None,
    },
    "ieeefp32": {
        "class": np.float32,
        "bit_width": 32,
        "max_val": None,
    },
    "int8_int16out": {
        "bit_width": 8,
        "input_type": "int8",
        "acc_type": "int16",
        "max_val": 127,
        "min_val": -128,
    }
}

fmt= ieeefp32;

fmt_info = formats[fmt]
bw = fmt_info["bit_width"]

# Floating point and ML float8 formats
if fmt.startswith("ieeefp") or fmt == "float8_e4m3":
    dtype = fmt_info["class"]
    ops = [dtype(np.random.uniform(-10, 10)) for _ in range(9)]
    print(ops)

    try:
        result = ops[0]*ops[4] + ops[1]*ops[5] + ops[2]*ops[6] + ops[3]*ops[7] + ops[8]
        result_bytes = dtype(result).tobytes()
        result_bits = result_bytes.hex().upper()
    except:
        result_bits = "FF" * (bw // 8)

    hex_ops = [dtype(x).tobytes().hex().upper() for x in ops]
    return " ".join(hex_ops + [result_bits])
        
        
      
