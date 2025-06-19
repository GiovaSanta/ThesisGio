import matplotlib.pyplot as plt

# Load the data
abs_diff = []
b0_values = []

with open("abs_diff_vs_b0_cleaned.txt", "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) == 2:
            abs_d, b0 = map(float, parts)
            abs_diff.append(abs_d)
            b0_values.append(b0)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(b0_values, abs_diff, 'o', markersize=3, alpha=0.7)
plt.title("Dot Product Error vs B0 Operand (FP8)")
plt.xlabel("B0 Value (decimal)")
plt.ylabel("Absolute Error (Abs_Diff)")
plt.grid(True)
plt.tight_layout()

plt.savefig("error_vs_b0_plot.png", dpi=300)

plt.show()

