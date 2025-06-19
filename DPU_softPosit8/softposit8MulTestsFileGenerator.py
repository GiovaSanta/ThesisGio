import sys
import random
from itertools import combinations_with_replacement

try:
    from sfpy import Posit8, Posit16
except ImportError:
    print("ERROR: 'softposit' package is required. Install it with: pip install softposit")
    sys.exit(1)

def hex_value(val, width):
    return f"{val:0{width}X}"

def main():
    if len(sys.argv) != 2:
        print("Usage: python generate_posit_tests.py [softposit8 | softposit16]")
        return

    mode = sys.argv[1]
    if mode == "softposit8":
        PositClass = Posit8
        bit_width = 8
        max_val = 2 ** 8
        output_file = "posit8_multiplier_tests.txt"

        print("Generating all combinations for softposit8...")
        pairs = combinations_with_replacement(range(max_val), 2)

    elif mode == "softposit16":
        PositClass = Posit16
        bit_width = 16
        max_val = 2 ** 16
        output_file = "posit16_multiplier_tests.txt"

        print("Generating 10,000 random test cases for softposit16...")
        random.seed(42)  # reproducible tests
        pairs = [ (random.randint(0, max_val - 1), random.randint(0, max_val - 1)) for _ in range(10000) ]

    else:
        print("Only 'softposit8' and 'softposit16' are supported.")
        return

    with open(output_file, "w") as f:
        for a, b in pairs:
            try:
                p1 = PositClass.from_bits(a)
                p2 = PositClass.from_bits(b)
                result = p1 * p2
                result_val = PositClass(result).bits

                f.write(f"{hex_value(a, bit_width // 4)} {hex_value(b, bit_width // 4)} {hex_value(result_val, bit_width // 4)}\n")
            except Exception as e:
                print(f"Error on inputs a={a}, b={b}: {e}")

    print(f"File '{output_file}' successfully written.")

if __name__ == "__main__":
    main()

