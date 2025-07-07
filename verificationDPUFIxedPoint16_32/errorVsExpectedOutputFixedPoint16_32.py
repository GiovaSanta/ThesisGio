import matplotlib.pyplot as plt
from fxpmath import Fxp
import numpy as np

# Initialize lists
golden_results = []
sim_results = []
abs_errors = []

# Files
input_file = "FixedPoint16_32_dpu_output_from_HDL_circuit_.txt"
debug_output = "FixedPoint16_32_dpu_debug_log.txt"

with open(input_file, "r") as f, open(debug_output, "w") as log:
    # Header for debug log
    log.write("a0 a1 a2 a3 b0 b1 b2 b3 c0 sim_hex sim_val golden_val abs_error\n")

    for line_num, line in enumerate(f):
        parts = line.strip().split()
        if len(parts) != 10:
            continue  # Skip malformed lines

        try:
            # Decode operands from hex
            a = [Fxp(signed=True, n_word=16, n_frac=10) for _ in range(4)]
            b = [Fxp(signed=True, n_word=16, n_frac=10) for _ in range(4)]
            for i in range(4):
                a[i].set_val("0x" + parts[i], raw=True)
                b[i].set_val("0x" + parts[i+4], raw=True)

            c = Fxp(signed=True, n_word=32, n_frac=20)
            c.set_val("0x" + parts[8], raw=True)

            sim = Fxp(signed=True, n_word=32, n_frac=20)
            sim.set_val("0x" + parts[9], raw=True)

            # Compute golden result
            golden =  ( float(a[0])* float(b[0]) ) + ( float(a[1])* float(b[1]) )+ ( float(a[2])* float(b[2]) ) + ( float(a[3])* float(b[3]) ) + float(c)

            # Convert to float
            golden_val = float(golden)
            sim_val = float(sim)
            error = abs(golden_val - sim_val)

            # Store values
            golden_results.append(golden_val)
            sim_results.append(sim_val)
            abs_errors.append(error)

            # Write debug log
            log.write(
                f"{parts[0]} {parts[1]} {parts[2]} {parts[3]} "
                f"{parts[4]} {parts[5]} {parts[6]} {parts[7]} "
                f"{parts[8]} {parts[9]} " #parts[9] is the value of the result from the vhdl dpu
                f"{sim_val:.6f} {golden_val:.6f} {error:.6f}\n"
            )

            # Print if error is high (adjust threshold if needed)
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

# Convert to numpy arrays
golden_results = np.array(golden_results)
abs_errors = np.array(abs_errors)

# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(golden_results, abs_errors, s=4, alpha=0.6, color='blue')
plt.title("Absolute Error vs Expected Output (FixedPoint16_32 DPU)")
plt.xlabel("Expected Output (Golden Value)")
plt.ylabel("Absolute Error")
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("FixedPoint16_32_dpu_error_plot.png", dpi=300)

print("\n✅ Plot saved as 'FixedPoint16_32_dpu_error_plot.png'")
print("📄 Debug log saved as 'FixedPoint16_32_dpu_debug_log.txt'")

