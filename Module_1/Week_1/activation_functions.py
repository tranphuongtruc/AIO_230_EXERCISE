import math


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + math.e ** -x)


def relu(x):
    if x <= 0:
        return 0
    else:
        return x


def elu(x):
    if x <= 0:
        return 0.01 * (math.e ** x - 1)
    else:
        return x


def activation_function():
    # Checking if x is a number
    x = input()
    if not is_number(x):
        print('x must be a number')
        exit()
    x = float(x)

    # Processing
    reply = input(
        'Activation Function ( sigmoid | relu | elu ): ').strip().lower()
    if reply == 'sigmoid':
        print(f'sigmoid: f({x}) = {sigmoid(x)}')
    elif reply == 'relu':
        print(f'relu: f({x}) = {relu(x)}')
    elif reply == 'elu':
        print(f'elu: f({x}) = {elu(x)}')
    else:
        print(f'{reply} is not supported')

# activation_function()
