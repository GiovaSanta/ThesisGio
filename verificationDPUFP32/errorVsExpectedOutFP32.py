import matplotlib.pyplot as plt
from sfpy import Float32
import numpy as np

# Initialize lists
golden_results = []
sim_results = []
abs_errors = []

# Files
input_file = "dpu_simulated_output.txt"
debug_output = "float32_dpu_debug_log.txt"

with open(input_file, "r") as f, open(debug_output, "w") as log:
    # Header
    log.write("a0 a1 a2 a3 b0 b1 b2 b3 c0 sim_hex sim_val golden_val abs_error\n")

    for line_num, line in enumerate(f):
        parts = line.strip().split()
        if len(parts) != 10:
            continue  # Skip malformed lines

        try:
            # Decode operands from hex as Float32 (32-bit words)
            a = [Float32.from_bits(int(parts[i], 16)) for i in range(4)]
            b = [Float32.from_bits(int(parts[i], 16)) for i in range(4, 8)]
            c = Float32.from_bits(int(parts[8], 16))
            sim = Float32.from_bits(int(parts[9], 16))

            # Compute golden reference
            golden = (float(a[0])* float(b[0])) + (float(a[1])*float(b[1])) + (float(a[2])*float(b[2])) + (float(a[3])*float(b[3])) + float(c) 
            
            # Convert to float
            golden_val = float(golden)
            sim_val = float(sim)
            error = abs(golden_val - sim_val)
            
            # Store for plot
            golden_results.append(golden_val)
            sim_results.append(sim_val)
            abs_errors.append(error)
            
            # Write debug info
            log.write(
                f"{parts[0]} {parts[1]} {parts[2]} {parts[3]} "
                f"{parts[4]} {parts[5]} {parts[6]} {parts[7]} "
                f"{parts[8]} {parts[9]} "
                f"{sim_val:.6f} {golden_val:.6f} {error:.6f}\n"
            )

            # Print if error is large
            if error > 10:
                print("\n⚠️  High error detected!")
                print(f"Line #{line_num + 1}: {line.strip()}")
                print(f"  a: {parts[0:4]}")
                print(f"  b: {parts[4:8]}")
                print(f"  c: {parts[8]}")
                print(f"  Simulated (hex): {parts[9]} → float: {sim_val}")
                print(f"  Golden: {golden_val}")
                print(f"  Absolute Error: {error}")

        except Exception as e:
            print(f"❌ Error on line {line_num + 1}: {line.strip()} --> {e}")
            continue

# Convert to NumPy arrays
golden_results = np.array(golden_results)
abs_errors = np.array(abs_errors)

# Plotting
plt.figure(figsize=(10, 5))
plt.scatter(golden_results, abs_errors, s=4, alpha=0.6, color='orange')
plt.title("Absolute Error vs Expected Output (Float32 DPU)")
plt.xlabel("Golden Result (Float32)")
plt.ylabel("Absolute Error")
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("float32_dot_product_error_plot.png", dpi=300)

print("\n✅ Plot saved as 'float32_dpu_error_plot.png'")
print("📄 Debug log saved as 'float32_dpu_debug_log.txt'")

