import itertools

# Define fixed values for A1, A2, A3, B1, B2, B3, C0 (all zero by default)
fixed_values = {
    "A1": "00",
    "A2": "00",
    "A3": "00",
    "B1": "00",
    "B2": "00",
    "B3": "00",
    "C0": "0000"
}

# Create output file
output_file = "fp8e4m3_dpu_test_vectors.txt"

# Generate all combinations of A0 and B0 (0x00 to 0xFF)
a0_vals = range(0x00, 0x100)
b0_vals = range(0x00, 0x100)

with open(output_file, "w") as f:
    for a0, b0 in itertools.product(a0_vals, b0_vals):
        vector = [
            f"{a0:02X}",                  # A0
            fixed_values["A1"],          # A1
            fixed_values["A2"],          # A2
            fixed_values["A3"],          # A3
            f"{b0:02X}",                  # B0
            fixed_values["B1"],          # B1
            fixed_values["B2"],          # B2
            fixed_values["B3"],          # B3
            fixed_values["C0"]           # C0
        ]
        f.write(" ".join(vector) + "\n")

print(f"Test vector file written to: {output_file}")

