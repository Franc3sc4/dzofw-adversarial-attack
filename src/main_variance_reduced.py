from algorithms import *
from utils import *
import numpy as np

data_workers, y, lenet5, data, labels,  test_x, test_y = get_data(dim=800)

# Parameters
T = 20
M = 10  # num workers; we consider a number of workers <=10
d = 28*28
epsilon = 0.25
S1 = len(data_workers[0])
S2 = 3
n = 5
q = 7

for q in [5, 7, 9]:
    for n in [5, 8, 10]:
        delta = decentralized_variance_reduced_zo_FW(data_workers, y, lenet5.negative_loss, T, M, d, epsilon, S1, S2, n, q)
        np.save(f"../../data/perturbations/reduced_variance/perturbation_variance_n{n}_q{q}", delta[-1])

# Test
delta = delta[-1]
perturbation = np.tile(delta, data.shape[0])
perturbation = perturbation.reshape((data.shape[0], 28, 28, 1))
perturbated_data = data + perturbation
perturbated_data = np.clip(perturbated_data, 0., 1.)

loss = lenet5.model.evaluate(perturbated_data, labels)
