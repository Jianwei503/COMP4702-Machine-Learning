import numpy as np
import scipy.spatial as sp
import matplotlib.pyplot as plt

# Load Test Data
test_inputs = np.loadtxt('test_inputs').reshape((-1,1))
train_inputs = np.loadtxt('train_inputs').reshape((-1,1))
train_outputs = np.loadtxt('train_outputs').reshape((-1,1))
n = 150
train_inputs = train_inputs[:n]
train_outputs = train_outputs[:n]
# train_outputs = train_outputs[:n]


def K(X, X_star, length_scale, P):
    dist = sp.distance.cdist(X, X_star)
    return np.exp(-dist ** 2 / (2 * length_scale ** 2)) * np.exp((-2 * (np.sin(np.pi * dist / P))**2) / (length_scale**2))

def predictive_mean(X, y, X_star, length_scale, sigma, P):
    n = X.shape[0]
    K_xstar_x = K(X_star, X, length_scale, P)
    K_x_x = K(X, X, length_scale, P)
    return np.matmul(K_xstar_x, np.matmul(np.linalg.inv(K_x_x + sigma**2 * np.eye(n)), y))

def predictive_cov(X, y, X_star, length_scale, sigma, P):
    n = X.shape[0]
    K_xstar_xstar = K(X_star, X_star, length_scale, P)
    K_xstar_x = K(X_star, X, length_scale, P)
    K_x_x = K(X, X, length_scale, P)
    return K_xstar_xstar - np.matmul(K_xstar_x, np.matmul(np.linalg.inv(K_x_x + sigma**2 * np.eye(n)), K_xstar_x.T))

# Q1
P = 3
l = 2
sigma = 1

mean = predictive_mean(train_inputs, train_outputs, test_inputs, l, sigma, P).reshape((-1,))

cov = predictive_cov(train_inputs, train_outputs, test_inputs[:, :], l, sigma, P)

samples = np.random.multivariate_normal(mean, cov, 5)
plt.plot(train_inputs, train_outputs, 'k*')
[plt.plot(test_inputs, samples[i, :]) for i in range(5)]
