import sys
import math
from sfpy import Posit8
import matplotlib.pyplot as plt

def parse_line(line):
    parts = line.strip().split()
    if len(parts) != 3:
        return None
    a_hex, b_hex, sim_hex = parts
    return int(a_hex, 16), int(b_hex, 16), int(sim_hex, 16)

def main():
    if len(sys.argv) != 2:
        print("Usage: python visualize_error.py posit8_multiplier_tests.txt")
        return

    filename = sys.argv[1]
    with open(filename, "r") as f:
        lines = f.readlines()

    x_vals = []
    errors = []

    for line in lines:
        parsed = parse_line(line)
        if not parsed:
            continue
        a_val, b_val, sim_val = parsed

        p1 = Posit8.from_bits(a_val)
        p2 = Posit8.from_bits(b_val)
        sim = Posit8.from_bits(sim_val)

        expected_float = float(p1) * float(p2)
        sim_float = float(sim)


        if math.isnan(expected_float) or math.isnan(sim_float):
            continue  # skip NaRs

        error = abs(expected_float - sim_float)

        x_vals.append(expected_float)  # X-axis is the expected result
        errors.append(error)           # Y-axis is the absolute error
        
        print(f"A={a_val:02X}, B={b_val:02X}, expected={expected_float}, sim={sim_float}, error={error}")

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(x_vals, errors, s=1, alpha=0.6)
    plt.title("SoftPosit8 Multiplier Error")
    plt.xlabel("Expected Value (float)")
    plt.ylabel("Absolute Error |expected - simulated|")
    plt.grid(True)
    #plt.yscale('log')  # Optional: shows tiny errors better
    plt.xscale('linear')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

