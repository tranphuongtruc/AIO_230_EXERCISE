'''
Data Table
Age   | Likes English | Likes AI | Raise Salary
-----------------------------------------------
23    |      0        |    0     |      0
25    |      1        |    1     |      0
27    |      1        |    0     |      1
29    |      0        |    1     |      1
29    |      0        |    0     |      0

Question 1: Under what condition is the Entropy measure equal to 1 for dataset D classified into two classes?

Answer: a) When the number of data points in both classes is equal.

Question 2: Calculate the Gini index for the samples in the label column D = ‘Raise Salary’?

Explanation:
The Gini index measures the impurity of a dataset and is calculated as:
Gini(D) = 1 - Σ(p_i^2)
where p_i is the proportion of each class in the dataset D.

For the 'Raise Salary' column:
There are 2 instances of '1' (Raise Salary) and 3 instances of '0' (No Raise Salary).
p_1 = 2/5 (proportion of '1's)
p_0 = 3/5 (proportion of '0's)

Gini(D) = 1 - (p_1^2 + p_0^2)
        = 1 - ((2/5)^2 + (3/5)^2)
        = 1 - (0.16 + 0.36)
        = 1 - 0.52
        = 0.48

Answer: c) Gini(D) = 0.48

Question 3: Calculate the Gini index when the attribute 'Likes English' is chosen as the root node.

Explanation:
To calculate Gini for 'Likes English' as the root node, we split the data into subsets where 'Likes English' = 0 and 'Likes English' = 1.

To calculate the Gini impurity for the dataset when 'Likes English' is chosen as the root node,
we need to understand the Gini impurity formula:

Gini = 1 - sum(p_i^2)

where p_i is the proportion of each class in the subset.

Step 1: Split the dataset by the attribute 'Likes English'
Group 1: Likes English = 0
-----------------------------------------------
| Age | Likes English | Likes AI | Raise Salary |
|-----|---------------|----------|--------------|
|  23 |       0       |     0    |      0       |
|  29 |       0       |     1    |      1       |
|  29 |       0       |     0    |      0       |
-----------------------------------------------
Total samples in Group 1 = 3
Raise Salary (1) = 1, No Raise Salary (0) = 2

Calculate the proportions:
p_Raise Salary = 1/3, p_No Raise Salary = 2/3

Gini impurity for Group 1:
Gini(0) = 1 - ((1/3)^2 + (2/3)^2)
       = 1 - (1/9 + 4/9)
       = 1 - 5/9
       = 4/9 ≈ 0.444

Group 2: Likes English = 1
-----------------------------------------------
| Age | Likes English | Likes AI | Raise Salary |
|-----|---------------|----------|--------------|
|  25 |       1       |     1    |      0       |
|  27 |       1       |     0    |      1       |
-----------------------------------------------
Total samples in Group 2 = 2
Raise Salary (1) = 1, No Raise Salary (0) = 1

Calculate the proportions:
p_Raise Salary = 1/2, p_No Raise Salary = 1/2

Gini impurity for Group 2:
Gini(1) = 1 - ((1/2)^2 + (1/2)^2)
       = 1 - (1/4 + 1/4)
       = 1 - 2/4
       = 2/4 = 0.5

Step 2: Calculate the Weighted Gini Impurity for the entire dataset
Weighted Gini = (3/5) * 0.444 + (2/5) * 0.5

Calculating the weighted Gini:
Weighted Gini = 0.2664 + 0.2
              = 0.4664 ≈ 0.47

Conclusion:
The Gini impurity of the dataset when 'Likes English' is chosen as the root node is approximately 0.47.
Therefore, the correct answer is:
d) Gini(Likes English) = 0.47

Question 4: Calculate the Gini index when the attribute 'Age' is chosen as the root node with the condition split 'Age <= 26'.

Explanation:
For 'Age <= 26':
There are 2 instances: [0, 0] in 'Raise Salary' (2 '0's)
Gini(Age <= 26) = 1 - (p_0^2 + p_1^2)
               = 1 - (1^2 + 0^2)
               = 1 - 1
               = 0

For 'Age > 26':
There are 3 instances: [1, 1, 0] in 'Raise Salary' (2 '1's and 1 '0')
p_1 = 2/3, p_0 = 1/3
Gini(Age > 26) = 1 - (p_0^2 + p_1^2)
              = 1 - ((1/3)^2 + (2/3)^2)
              = 1 - (1/9 + 4/9)
              = 1 - 5/9
              = 4/9

Weighted Gini Index for 'Age':
Gini(Age) = (2/5) * Gini(Age <= 26) + (3/5) * Gini(Age > 26)
          = (2/5) * 0 + (3/5) * (4/9)
          = 0 + (12/45)
          = 12/45
          ≈ 0.27

Answer: c) Gini(Age <= 26) ≈ 0.27

Question 5: Calculate the Entropy of the samples in the label column D = ‘Raise Salary’.

Explanation:
Entropy measures the disorder or uncertainty in a dataset and is calculated as:
Entropy(D) = -Σ(p_i * log2(p_i))
where p_i is the proportion of each class in the dataset D.

For the 'Raise Salary' column:
p_1 = 2/5, p_0 = 3/5

Entropy(D) = -(p_1 * log2(p_1) + p_0 * log2(p_0))
           = -((2/5) * log2(2/5) + (3/5) * log2(3/5))
           ≈ 0.97

Answer: b) Entropy(D) ≈ 0.97

Question 6: Calculate the Gain of the dataset when the attribute 'Likes English' is chosen as the root node.

To calculate the Gain for the attribute 'Likes English':

1. Calculate the Entropy of the Entire Dataset:
   - Total instances: 5
   - Instances with 'Raise Salary' = 1: 2
   - Instances with 'Raise Salary' = 0: 3
   - Proportions: p(1) = 2/5 = 0.4, p(0) = 3/5 = 0.6
   - Entropy(S) = - (0.4 * log2(0.4) + 0.6 * log2(0.6))
   - Entropy(S) ≈ 0.971

2. Calculate the Entropy for Each Subset of 'Likes English':
   For 'Likes English' = 1:
   - Total instances in this subset: 2
   - Instances with 'Raise Salary' = 1: 1
   - Instances with 'Raise Salary' = 0: 1
   - Proportions: p(1) = 1/2 = 0.5, p(0) = 1/2 = 0.5
   - Entropy(S1) = - (0.5 * log2(0.5) + 0.5 * log2(0.5))
   - Entropy(S1) = 1.0

   For 'Likes English' = 0:
   - Total instances in this subset: 3
   - Instances with 'Raise Salary' = 1: 1
   - Instances with 'Raise Salary' = 0: 2
   - Proportions: p(1) = 1/3 ≈ 0.333, p(0) = 2/3 ≈ 0.667
   - Entropy(S0) = - (0.333 * log2(0.333) + 0.667 * log2(0.667))
   - Entropy(S0) ≈ 0.918

3. Compute the Weighted Average Entropy:
   - Proportions: 0.4 for 'Likes English' = 1, 0.6 for 'Likes English' = 0
   - Weighted Entropy = (0.4 * Entropy(S1) + 0.6 * Entropy(S0))
   - Weighted Entropy ≈ (0.4 * 1.0 + 0.6 * 0.918)
   - Weighted Entropy ≈ 0.951

4. Calculate the Information Gain:
   - Gain = Entropy(S) - Weighted Entropy
   - Gain ≈ 0.971 - 0.951
   - Gain ≈ 0.020

Comparing with provided options:
a) Gain(Likes English) = 0.048
b) Gain(Likes English) = 0.038
c) Gain(Likes English) = 0.028
d) Gain(Likes English) = 0.018

The calculated Gain is closest to option d) 0.018.

'''

