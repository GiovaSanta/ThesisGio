import matplotlib.pyplot as plt
import numpy as np
import ml_dtypes

# Initialize lists
golden_results = []
sim_results = []
abs_errors = []

# Initialize error matrix for heatmap (a0 x b0)
error_matrix = np.zeros((256, 256))

# Files
input_file = "output_file.txt"  # DPU output file
debug_output = "float8_dpu_debug_log.txt"
heatmap_output = "fp8_dpu_error_heatmap.png"

with open(input_file, "r") as f, open(debug_output, "w") as log:
    # Header for debug log
    log.write("a0 a1 a2 a3 b0 b1 b2 b3 c0 sim_hex sim_val golden_val abs_error\n")

    for line_num, line in enumerate(f):
        parts = line.strip().split()
        if len(parts) != 10:
            continue  # Skip malformed lines

        try:
            # Decode hex to uint8, then reinterpret as float8_e4m3
            def decode_float8(hex_str):
                byte = np.array([int(hex_str, 16)], dtype=np.uint8)
                return byte.view(ml_dtypes.float8_e4m3)[0]

            a = [decode_float8(parts[i]) for i in range(4)]
            b = [decode_float8(parts[i]) for i in range(4, 8)]
            c = decode_float8(parts[8])
            sim = decode_float8(parts[9])

            # Compute golden result
            golden = (float(a[0]) * float(b[0])) + (float(a[1]) * float(b[1])) + \
                     (float(a[2]) * float(b[2])) + (float(a[3]) * float(b[3])) + float(c)

            golden_val = float(golden)
            sim_val = float(sim)
            error = abs(golden_val - sim_val)

            # Store error in heatmap
            a0_idx = int(parts[0], 16)
            b0_idx = int(parts[4], 16)
            error_matrix[b0_idx, a0_idx] = error

            # Write debug log
            log.write(
                f"{parts[0]} {parts[1]} {parts[2]} {parts[3]} "
                f"{parts[4]} {parts[5]} {parts[6]} {parts[7]} "
                f"{parts[8]} {parts[9]} "
                f"{sim_val:.6f} {golden_val:.6f} {error:.6f}\n"
            )

        except Exception as e:
            print(f"❌ Error on line {line_num + 1}: {line.strip()} --> {e}")
            continue

# ✅ Plot the heatmap
plt.figure(figsize=(10, 8))
heatmap = plt.imshow(error_matrix, extent=[0, 255, 0, 255], origin='lower',
                     cmap='inferno', aspect='auto')
plt.colorbar(heatmap, label='Absolute Error')
plt.xlabel('a0 (bit pattern)')
plt.ylabel('b0 (bit pattern)')
plt.title('FP8 DPU Error Heatmap: a0 vs b0')
plt.tight_layout()
plt.savefig(heatmap_output)
plt.show()

