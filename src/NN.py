import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import torch.optim as optim
import numpy as np
import pandas as pd

path = '/home/zeus/Code/Arm-Sim/dataset'
learning_rate = 0.01
batch_size = 32

train_df = pd.read_csv(path + '/trainset.csv')
test_df = pd.read_csv(path + '/testset.csv')

train_data = 
test_data

train_set = DataLoader(train_data, batch_size=batch_size, shuffle=True)
test_set = DataLoader(test_data, batch_size=batch_size, shuffle=True)


class NN(nn.Module):
    def __init__(self):
        super(NN, self).__init__()

        self.fc1 = nn.Linear(100, 128)
        self.fc2 = nn.Linear(128,512)
        self.fc3 = nn.Linear(512, 5)

    def forward(self, x):
        x = nn.ReLU(self.fc1(x))        
        x = nn.ReLU(self.fc2(x))
        x = nn.Tanh(self.fc3(x))

        return x


model = NN()
optimizer = optim.Adam(model.parameters(), lr=learning_rate)



