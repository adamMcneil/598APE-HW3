import matplotlib.pyplot as plt
import numpy as np
# ./main.exe 1000 5000
# final location 4221.875063 -2827.830995
base_line_mid = [12.486]
reduce_work_mid = [8.207]
rust_rw = [7.85, 8.05, 7.93]
masses = [7.65, 7.80]
init = [5.399, 5.506]
mid_data = [base_line_mid, reduce_work_mid, masses]

# ./main.exe 5 100000000
# final location -246420916.320709 327085378.139325
base_line_small = [8.774]
reduce_work_small = [4.944]
rust_rw = [5.27, 5.33]
masses = [4.95, 5.11]
init = [5.23, 5.15]
small_data = [base_line_small, reduce_work_small, masses]

# ./main.exe 1000 10000
# final location -763.433705 1203.599962
base_line_large = [25.872]
reduce_work_large = [14.223737]
rust_rw = [15.93, 16.56]
masses = [16.34, 16.38]
init = [11.02, 11.08]
large_data = [base_line_large, reduce_work_large, masses]

# Calculate the means and standard deviations
mid_means = [np.min(data) for data in mid_data]
mid_std_devs = [np.std(data) for data in mid_data]

small_means = [np.min(data) for data in small_data]
small_std_devs = [np.std(data) for data in small_data]

large_means = [np.min(data) for data in large_data]
large_std_devs = [np.std(data) for data in large_data]

# Define categorical x-axis labels
x_labels = ["baseline", "reduced work", "rust"]
x = np.arange(len(x_labels))  # Numeric positions for categorical labels

plt.errorbar(x, mid_means, yerr=mid_std_devs, capsize=5, linestyle='-', marker='^', color='red', label='Mid')
plt.errorbar(x, small_means, yerr=small_std_devs, capsize=5, linestyle='--', marker='o', color='blue', label='Small')
plt.errorbar(x, large_means, yerr=large_std_devs, capsize=5, linestyle='-.', marker='D', color='green', label='Large')

plt.xticks(x, x_labels)  # Set the categorical labels
plt.xlabel('Optimization Stage')
plt.ylabel('Time (sec)')
plt.title('Speed Increase')
plt.ylim(bottom=0)

plt.legend()
plt.legend(loc='upper right')  # Places the legend in the upper-right corner
plt.grid(True)

plt.show()
