import matplotlib.pyplot as plt
import numpy as np
# ./main.exe 1000 5000
base_line_diabetes = [12.486]
para_diabetes = [1.12, 1.13, 1.15]
stack = [0.62, 0.59]
sort = [0.58, 0.53, 0.53]
flag = [0.13, 0.12, 0.15]
diabetes_data = [base_line_diabetes, para_diabetes, stack, sort, flag]

# ./main.exe 500 5000
base_line_cancer = [3.124]
para_cancer = [21.87, 22.18, ]
stack = [17.59, 17.85]
sort = [10.74, 10.55, 10.93]
flag = [3.89, 3.93, 3.89]
cancer_data = [base_line_cancer, para_cancer, stack, sort, flag]

# ./main.exe 5000 500
base_line_housing = [31.864]
para_housing = [43.20, ]
stack = [17.59, 25.40, 22.98]
sort = [15.59, 15.82, 17.33]
flag = [3.95, 3.98, 4.07]
housing_data = [base_line_housing, para_housing, stack, sort, flag]

# Calculate the means and standard deviations
diabetes_means = [np.min(data) for data in diabetes_data]
diabetes_std_devs = [np.std(data) for data in diabetes_data]

cancer_means = [np.min(data) for data in cancer_data]
cancer_std_devs = [np.std(data) for data in cancer_data]

housing_means = [np.min(data) for data in housing_data]
housing_std_devs = [np.std(data) for data in housing_data]

# Define categorical x-axis labels
x_labels = ["baseline", "parallelism", "stack", "sort", "flag"]
x = np.arange(len(x_labels))  # Numeric positions for categorical labels

plt.errorbar(x, diabetes_means, yerr=diabetes_std_devs, capsize=5, linestyle='-', marker='^', color='red', label='Diabetes')
plt.errorbar(x, cancer_means, yerr=cancer_std_devs, capsize=5, linestyle='--', marker='o', color='blue', label='Cancer')
plt.errorbar(x, housing_means, yerr=housing_std_devs, capsize=5, linestyle='-.', marker='D', color='green', label='Housing')

plt.xticks(x, x_labels)  # Set the categorical labels
plt.xlabel('Optimization Stage')
plt.ylabel('Time (sec)')
plt.title('Speed Increase')
plt.ylim(bottom=0)

plt.legend()
plt.legend(loc='upper right')  # Places the legend in the upper-right corner
plt.grid(True)

plt.show()
