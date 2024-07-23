import numpy as np
import pandas as pd

# 4.1 create train data


def create_train_data():
    data = pd.read_csv('tennis_data.csv')
    return np.array(data)


train_data = create_train_data()
print(train_data)


# 4.2 Compute prior probability


def compute_prior_probablity(train_data):
    y_unique = ['No', 'Yes']
    prior_probability = np.zeros(len(y_unique))
    tennis = train_data[:, -1]

    # return each val and its frequency
    _, count = np.unique(tennis, return_counts=True)
    prior_probability[0] = count[0]/len(train_data)
    prior_probability[1] = count[1]/len(train_data)

    return prior_probability


prior_probability = compute_prior_probablity(train_data)
print("P(play tennis = No) =", prior_probability[0])
print("P(play tennis = Yes) =", prior_probability[1])


# 4.3 Compute conditional probability


def compute_conditional_probability(train_data):
    y_unique = ['No', 'Yes']
    conditional_probability = []
    list_x_name = []
    for i in range(train_data.shape[1]-1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
        for j in range(0, len(y_unique)):
            for k in range(0, len(x_unique)):
                x_conditional_probability[j, k] = len(np.where((train_data[:, i] == x_unique[k]) & (
                    train_data[:, 4] == y_unique[j]))[0])/len(np.where(train_data[:, 4] == y_unique[j])[0])
        conditional_probability.append(x_conditional_probability)
    '''
    NOTE
    This is the result of conditional_probability (with each first row of the array if the probability when PlayTennis is No and each second row of the array is when PlayTennis is Yes)
    
    [array([ [0.25      , 0.25      , 0.5       ],
             [0.33333333, 0.5       , 0.16666667]]), 
     array([ [0.25      , 0.5       , 0.25      ],      
             [0.5       , 0.16666667, 0.33333333]]), 
     array([ [0.75      , 0.25      ],
             [0.33333333, 0.66666667]]), 
     array([ [0.5       , 0.5       ],
             [0.16666667, 0.83333333]])]
    '''

    return conditional_probability, list_x_name


train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
print("x1 = ", list_x_name[0])
print("x2 = ", list_x_name[1])
print("x3 = ", list_x_name[2])
print("x4 = ", list_x_name[3])


# 4.4 Get index from value


# This function is used to return the index of the feature name
def get_index_from_value(feature_name, list_features):
    return np.where(list_features == feature_name)[0][0]


train_data = create_train_data()
_, list_x_name = compute_conditional_probability(train_data)
outlook = list_x_name[0]

i1 = get_index_from_value("Overcast", outlook)
i2 = get_index_from_value("Rain", outlook)
i3 = get_index_from_value("Sunny", outlook)

print(i1, i2, i3)


conditional_probability, list_x_name = compute_conditional_probability(
    train_data)


# Compute P("Outlook"="Sunny"|Play Tennis"="Yes")
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'='Sunny'|Play Tennis'='Yes') = ",
      np.round(conditional_probability[0][1, x1], 2))


# Compute P("Outlook"="Sunny"|Play Tennis"="No")
x1 = get_index_from_value("Sunny", list_x_name[0])
print("P('Outlook'='Sunny'|Play Tennis'='No') = ",
      np.round(conditional_probability[0][0, x1], 2))


# 4.5 Train Naive Bayes Model

def train_naive_bayes(train_data):

    # Step 1: Calculate Prior Probability
    prior_probability = compute_prior_probablity(train_data)

    # Step 2: Calculate Conditional Probability
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


# 4.6 Make Prediction

def prediction_play_tennis(x, list_x_name, prior_probability, conditional_probability):

    x1 = get_index_from_value(x[0], list_x_name[0])
    x2 = get_index_from_value(x[1], list_x_name[1])
    x3 = get_index_from_value(x[2], list_x_name[2])
    x4 = get_index_from_value(x[3], list_x_name[3])

    p0 = prior_probability[0] \
        * conditional_probability[0][0, x1] \
        * conditional_probability[1][0, x2] \
        * conditional_probability[2][0, x3] \
        * conditional_probability[3][0, x4]

    p1 = prior_probability[1]\
        * conditional_probability[0][1, x1]\
        * conditional_probability[1][1, x2]\
        * conditional_probability[2][1, x3]\
        * conditional_probability[3][1, x4]

    if p0 > p1:  # No is higher than Yes
        y_pred = 0
    else:
        y_pred = 1

    return y_pred


X = ['Sunny', 'Cool', 'High', 'Strong']
data = create_train_data()
prior_probability, conditional_probability, list_x_name = train_naive_bayes(
    data)
pred = prediction_play_tennis(
    X, list_x_name, prior_probability, conditional_probability)

if (pred):
    print("Ad should go!")
else:
    print("Ad should not go!")
