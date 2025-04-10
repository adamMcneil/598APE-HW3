import matplotlib.pyplot as plt
import numpy as np
# ./main.exe 1000 5000
# final location 4221.875063 -2827.830995
base_line_mid = [12.486, 12.30, 12.32]
copy = [11.90, 12.39, 12.17]
rust_rw = [7.85, 8.05, 7.93]
masses = [7.71, 7.75, 7.93]
init = [5.399, 5.506]
mid_data = [base_line_mid, copy, masses, init]


# ./main.exe 5 100000000
# final location -246420916.320709 327085378.139325
base_line_small = [8.774, 8.33, 8.42]
reduce_work_small = [6.63, 6.93, 6.61]
rust_rw = [5.27, 5.33]
masses = [4.38, 4.31, 4.33]
init = [5.23, 5.15]
small_data = [base_line_small, reduce_work_small, masses, init]

# ./main.exe 1000 10000
# final location 9740.442359 -5365.206700
base_line_large = [25.872, 24.72, 24.56]
reduce_work_large = [24.03, 24.79]
rust_rw = [15.93, 16.56]
masses = [15.82, 15.68, 15.39]
init = [11.02, 11.08]
large_data = [base_line_large, reduce_work_large, masses, init]

# Calculate the means and standard deviations
mid_means = [np.min(data) for data in mid_data]
mid_std_devs = [np.std(data) for data in mid_data]

small_means = [np.min(data) for data in small_data]
small_std_devs = [np.std(data) for data in small_data]

large_means = [np.min(data) for data in large_data]
large_std_devs = [np.std(data) for data in large_data]

# Define categorical x-axis labels
x_labels = ["baseline", "copy", "physics", "init"]
x = np.arange(len(x_labels))  # Numeric positions for categorical labels

plt.errorbar(x, small_means, yerr=small_std_devs, capsize=5, linestyle='--', marker='o', color='blue', label='p=5, t=100000000')
plt.errorbar(x, mid_means, yerr=mid_std_devs, capsize=5, linestyle='-', marker='^', color='red', label='p=1000, t=5000')
plt.errorbar(x, large_means, yerr=large_std_devs, capsize=5, linestyle='-.', marker='D', color='green', label='p=1000, t=10000')

plt.xticks(x, x_labels)  # Set the categorical labels
plt.xlabel('Optimization Stage')
plt.ylabel('Time (sec)')
plt.title('Min Execution Time')
plt.ylim(bottom=0)

plt.legend()
plt.legend(loc='upper right')  # Places the legend in the upper-right corner
plt.grid(True)

plt.show()
