import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import helper

train_path = '/home/zeus/Code/Arm-Sim/dataset/trainset.csv'
test_path = '/home/zeus/Code/Arm-Sim/dataset/testset.csv'

train_X, train_Y = helper.dataset(train_path)
test_X, test_Y = helper.dataset(test_path)

model = LinearRegression()

model.fit(train_X, train_Y)
score = model.score(train_X, train_Y)
pred = model.predict(test_X)
mean_squared_error(test_Y, pred)



