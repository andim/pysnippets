import numpy as np

# Simulate L two-state Markov processes
# parameters: switching rates a, b

L = 100
b = 0.05
a = 0.05
rand = np.random.rand(L)

# simple looping timestepping of the dynamics
def step(env, a, b, rand):
    for i in range(L):
        if env[i]:
            env[i] = True if rand[i] < 1-b else False
        else:
            env[i] = True if rand[i] < a else False
    return env

# vectorized timestepping of the dynamics using bitwise operators
def step_vectorized(env, a, b, rand):
    return (env & (rand < 1-b)) | (~env & (rand < a))

# ensure that both give the same result
print np.all(~(step(np.ones(L, dtype = bool), a, b, rand) ^ 
    step_vectorized(np.ones(L, dtype = bool), a, b, rand)))
print np.all(~(step(np.zeros(L, dtype = bool), a, b, rand) ^
    step_vectorized(np.zeros(L, dtype = bool), a, b, rand)))

# benchmark run times
import timeit
print min(timeit.repeat('step(np.zeros(L, dtype = bool), a, b, rand)',
        'from __main__ import np, step, L, b, a, rand', repeat = 3, number = 100))
print min(timeit.repeat('step_vectorized(np.zeros(L, dtype = bool), a, b, rand)',
        'from __main__ import np, step_vectorized, L, b, a, rand', repeat = 3, number = 100))
