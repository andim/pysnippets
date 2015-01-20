import numpy as np

# Simulate L two-state Markov processes
# parameters: switching rates alpha, beta

L = 100
beta = 0.05
alpha = 0.05
rand = np.random.rand(L)

# simple looping timestepping of the dynamics
def step(env, alpha, beta, rand):
    for i in range(L):
        if env[i]:
            env[i] = True if rand[i] < 1-beta else False
        else:
            env[i] = True if rand[i] < alpha else False
    return env

# vectorized timestepping of the dynamics using bitwise operators
def step_vectorized(env, alpha, beta, rand):
    return (env & (rand < 1-beta)) | (~env & (rand < alpha))

# ensure that both give the same result
print np.all(~(step(np.ones(L, dtype = bool), alpha, beta, rand) ^ step_vectorized(np.ones(L, dtype = bool), alpha, beta, rand)))
print np.all(~(step(np.zeros(L, dtype = bool), alpha, beta, rand) ^ step_vectorized(np.zeros(L, dtype = bool), alpha, beta, rand)))

# benchmark run times
import timeit
print min(timeit.repeat('step(np.zeros(L, dtype = bool), alpha, beta, rand)',
        'from __main__ import np, step, L, beta, alpha, rand', repeat = 3, number = 100))
print min(timeit.repeat('step_vectorized(np.zeros(L, dtype = bool), alpha, beta, rand)',
        'from __main__ import np, step_vectorized, L, beta, alpha, rand', repeat = 3, number = 100))
