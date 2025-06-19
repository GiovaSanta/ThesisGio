import sys
import random
import numpy as np
from sfpy import Posit8, Posit16
from ml_dtypes import float8_e4m3

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

def generate_test_vector(fmt):
    fmt_info = formats[fmt]
    bw = fmt_info["bit_width"]

    # Floating point and ML float8 formats
    if fmt.startswith("ieeefp") or fmt == "float8_e4m3":
        dtype = fmt_info["class"]
        ops = [dtype(np.random.uniform(-10, 10)) for _ in range(9)]

        try:
            result = ops[0]*ops[4] + ops[1]*ops[5] + ops[2]*ops[6] + ops[3]*ops[7] + ops[8]
            result_bytes = dtype(result).tobytes()
            result_bits = result_bytes.hex().upper()
        except:
            result_bits = "FF" * (bw // 8)

        hex_ops = [dtype(x).tobytes().hex().upper() for x in ops]
        return " ".join(hex_ops + [result_bits])

    elif fmt == "int8_int16out":
        # Generate random inputs
        a_vals = [np.random.randint(-128, 128, dtype=np.int8) for _ in range(4)]
        b_vals = [np.random.randint(-128, 128, dtype=np.int8) for _ in range(4)]
        c0     = np.random.randint(-32768, 32768, dtype=np.int16)

        # Do the computation in int16
        products = [np.int16(a_vals[i]) * np.int16(b_vals[i]) for i in range(4)]
        result = np.int16(sum(products) + c0)

        def to_hex(val, width):
            if width == 8:
                return np.array([val], dtype=np.int8).tobytes().hex().upper()
            elif width == 16:
                return np.array([val], dtype=np.int16).tobytes().hex().upper()

        hex_ops = [to_hex(x, 8) for x in a_vals + b_vals]
        hex_ops.append(to_hex(c0, 16))
        hex_ops.append(to_hex(result, 16))

        return " ".join(hex_ops)



    # Posit formats
    else:
        fmt_class = fmt_info["class"]
        ops = [random.choice(special_values) if random.random() < 0.1 else random.randint(0, fmt_info["max_val"]) for _ in range(9)]
        ps = [fmt_class.from_bits(x) for x in ops]
        try:
            result = ps[0]*ps[4] + ps[1]*ps[5] + ps[2]*ps[6] + ps[3]*ps[7] + ps[8]
            result_bits = f"{fmt_class(result).bits:0{bw//4}X}"
        except:
            result_bits = "FF" * (bw // 8)
        return " ".join(f"{x:0{bw//4}X}" for x in ops) + f" {result_bits}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python dotproduct_generator.py <format>")
        print(f"Supported formats: {', '.join(formats.keys())}")
        return
    fmt = sys.argv[1]
    if fmt not in formats:
        print(f"Unknown format: {fmt}")
        return
    filename = f"dotproduct_{fmt}_tests.txt"
    with open(filename, "w") as f:
        for _ in range(10000):
            f.write(generate_test_vector(fmt) + "\n")
    print(f"✅ Generated 10000 test vectors in '{filename}'.")

if __name__ == "__main__":
    main()

