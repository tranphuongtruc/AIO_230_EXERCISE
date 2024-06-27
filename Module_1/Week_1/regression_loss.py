import random
import math


def mae(n):
    total = 0
    for i in range(n):
        predict = random.uniform(0.0, 10.0)
        target = random.uniform(0.0, 10.0)
        loss = abs(target - predict)
        total += loss
        print(f'loss name: MAE, sample: {i}, pred: {
              predict}, target: {target}, loss: {loss}')
    print(f'final MAE {(1/n) * total}')


def mse(n):
    total = 0
    for i in range(n):
        predict = random.uniform(0.0, 10.0)
        target = random.uniform(0.0, 10.0)
        loss = (target - predict) ** 2
        total += loss
        print(f'loss name: MSE, sample: {i}, pred: {
              predict}, target: {target}, loss: {loss}')
    print(f'final MSE {(1/n) * total}')


def rmse(n):
    total = 0
    for i in range(n):
        predict = random.uniform(0.0, 10.0)
        target = random.uniform(0.0, 10.0)
        loss = (target - predict) ** 2
        total += loss
        print(f'loss name: RMSE, sample: {i}, pred: {
              predict}, target: {target}, loss: {loss}')
    print(f'final RMSE: {math.sqrt((1/5) * total)}')


def regression_loss():
    # Checking if n is an integer number
    n = input()
    if not n.isnumeric():
        print('number of samples must be an integer number')
        exit()
    n = int(n)

    # Processing
    reply = input('Loss name ( MAE | MSE | RMSE ): ').strip().upper()
    if reply == 'MAE':
        mae(n)
    elif reply == 'MSE':
        mse(n)
    elif reply == 'RMSE':
        rmse(n)

# regression_loss()
