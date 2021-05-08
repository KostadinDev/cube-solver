import time
import random
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from collections import deque
from dataloader import DataLoader
import pycuber as pc
from constants import Constants
from cube import Cube


import numpy as np
import tensorflow as tf
from tensorflow import keras
from copy  import deepcopy
import datetime
from model import buildModel, compile_model
from cubeAgent import CubeAgent
import os

class Actor(nn.Module):

    def __init__(self, state_dim, action_dim):
        super(Actor, self).__init__()

        self.layer_1 = nn.Linear(state_dim, 100)
        self.layer_2 = nn.Linear(100, 50)
        self.layer_3 = nn.Linear(50, action_dim)

    def forward(self, x):
        x = F.relu(self.layer_1(x))
        x = F.relu(self.layer_2(x))
        x = self.layer_3(x)
        return x


# Selecting the device (CPU or GPU)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# Building the whole Training Process into a class

def ADI(iterations):
    for it in range(iterations):
        print(it)
        l = 100
        k = 20

        data = DataLoader(num_cubes=l, num_batches=k)
        data.scramble(l, k)

        cubes = np.array(data.cubes).flatten()

        encodings = np.empty((k * l, 20 * 24))
        values = np.empty((k * l, 1))
        policies = np.empty(k * l)
        print(values)
        print(policies)

        for idx, state in enumerate(cubes):
            current_values = np.zeros(len(state.actions()))
            encodings[idx] = state.cube.flatten()
            actions = Constants.actions

            next_state = Cube(state.cube)

            for i, action in enumerate(actions):
                next_state.rotate(action)
                reward = state.reward()
                next_encoding = next_state.cube.flatten()

                value, policy = model(next_state)
                current_values[i] = value + reward
        values[idx] = np.array(current_values.max())
        policies[i] = current_values.argmax()



if __name__ == '__main__':
    # ADI(1)
    print(pc.Cube())
