import numpy as np
import math

# 1. Mean


def compute_mean(x):
    return np.mean(x)


x = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
print("Mean:", compute_mean(x))


# 2. Median


def compute_median(x):
    size = len(x)
    x = np.sort(x)
    print(x)
    if size % 2 == 0:
        median_value = (x[size // 2 - 1] + x[size // 2]) / 2
    else:
        median_value = x[size // 2]
    return median_value


x = [1, 5, 4, 4, 9, 13]
print("Median:", compute_median(x))


# 3. Standard deviation


def compute_std(x):
    mean = compute_mean(x)
    variance = 0
    for i in x:
        variance += (i-mean)**2
    variance = variance / len(x)
    return math.sqrt(variance)


x = [171, 176, 155, 167, 169, 182]
print(compute_std(x))


# 4. Correlation coefficient


def compute_correlation_cofficient(x, y):
    numerator = np.mean((x-compute_mean(x))*(y-compute_mean(y)))
    denominator = compute_std(x)*compute_std(y)
    return np.round(numerator / denominator, 2)


x = np.asarray([-2, -5, -11, 6, 4, 15, 9])
y = np.asarray([4, 25, 121, 36, 16, 225, 81])
print("Correlation:", compute_correlation_cofficient(x, y))
