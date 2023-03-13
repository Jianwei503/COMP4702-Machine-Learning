import numpy as np
import matplotlib.pyplot as plt

# Load Test Data
test_inputs = np.loadtxt('test_inputs').reshape((-1,1))


def K(X, X_star, c, d):

    return (np.dot(X, X_star.T) + c)**d

def sample_prior(X, c, N, d):
    n = X.shape[0]
    k = K(X, X, c, d)
    # print(k)
    samples = np.random.multivariate_normal([0]*n, k, N)
    return samples

# Q2-1

samples = sample_prior(test_inputs, 5, 5, 1)

[plt.plot(test_inputs, samples[i, :]) for i in range(5)]
plt.xticks(np.arange(-6, 7))

# Q2-2

samples = sample_prior(test_inputs, 5, 5, 2)

[plt.plot(test_inputs, samples[i, :]) for i in range(5)]

# Q2-3

samples = sample_prior(test_inputs, 5, 5, 3)

[plt.plot(test_inputs, samples[i, :]) for i in range(5)]