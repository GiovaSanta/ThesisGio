import numpy as np
import matplotlib.pyplot as plt
from sfpy import Posit8

# Input and output file paths
input_file = "output_file.txt"
debug_output = "posit8_dpu_debug_log.txt"
heatmap_output = "posit8_dpu_error_heatmap.png"

# Error matrix: B0 (rows) vs A0 (columns)
error_matrix = np.zeros((256, 256))

# Open files
with open(input_file, "r") as fin, open(debug_output, "w") as fout:
    fout.write("A0 A1 A2 A3 B0 B1 B2 B3 C0 SimResult TrueResult AbsError\n")

    for line in fin:
        parts = line.strip().split()
        if len(parts) != 10:
            continue  # skip malformed lines

        try:
            # Raw A0 and B0 bits for indexing
            a0_raw = int(parts[0], 16)
            b0_raw = int(parts[4], 16)

            # Decode operands
            A0 = float(Posit8.from_bits(a0_raw))
            A1 = float(Posit8.from_bits(int(parts[1], 16)))
            A2 = float(Posit8.from_bits(int(parts[2], 16)))
            A3 = float(Posit8.from_bits(int(parts[3], 16)))
            B0 = float(Posit8.from_bits(b0_raw))
            B1 = float(Posit8.from_bits(int(parts[5], 16)))
            B2 = float(Posit8.from_bits(int(parts[6], 16)))
            B3 = float(Posit8.from_bits(int(parts[7], 16)))
            C0 = float(Posit8.from_bits(int(parts[8], 16)))
            SimResult = float(Posit8.from_bits(int(parts[9], 16)))

            # Compute true result and error
            TrueResult = (A0 * B0) + (A1 * B1) + (A2 * B2) + (A3 * B3) + C0
            AbsError = abs(SimResult - TrueResult)

            # Save to debug file
            fout.write(f"{A0:.6f} {A1:.6f} {A2:.6f} {A3:.6f} ")
            fout.write(f"{B0:.6f} {B1:.6f} {B2:.6f} {B3:.6f} ")
            fout.write(f"{C0:.6f} {SimResult:.6f} {TrueResult:.6f} {AbsError:.6f}\n")

            # Update error heatmap
            error_matrix[b0_raw, a0_raw] = AbsError

        except Exception as e:
            continue  # skip decoding errors silently

# Plot heatmap
plt.figure(figsize=(10, 8))
heatmap = plt.imshow(error_matrix, extent=[0, 255, 0, 255], origin='lower',
                     cmap='inferno', aspect='auto')
plt.colorbar(heatmap, label='Absolute Error')
plt.xlabel('A0 (bit pattern)')
plt.ylabel('B0 (bit pattern)')
plt.title('DPU Simulation Error Heatmap: A0 vs B0')
plt.tight_layout()
plt.savefig(heatmap_output)
plt.show()

