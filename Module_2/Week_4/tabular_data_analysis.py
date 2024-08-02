import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from basic_probability import compute_correlation_cofficient
data = pd.read_csv("advertising.csv")

# Q5


def correlation(x, y):
    return compute_correlation_cofficient(x, y)


x = data['TV']
y = data['Radio']
corr_xy = correlation(x, y)
print(f"Correlation between TV and Radio: {round(corr_xy, 2)}")


# Q6


features = ['TV', 'Radio', 'Newspaper']

for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {
              feature_2}: {round(correlation_value, 2)}")


# Q7


x = data['Radio']
y = data['Newspaper']
result = np.corrcoef(x, y)
print(result)


# Q8


print(data.corr())
'''
                 TV     Radio  Newspaper     Sales
TV         1.000000  0.054809   0.056648  0.901208
Radio      0.054809  1.000000   0.354104  0.349631
Newspaper  0.056648  0.354104   1.000000  0.157960
Sales      0.901208  0.349631   0.157960  1.000000
'''

# Q9


data_corr = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show()
