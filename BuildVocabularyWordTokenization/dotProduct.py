import pandas as pd

v1 = pd.np.array([6,2,3])
v2 = pd.np.array([2,3,4])

print(v1.dot(v2))

print('-----------')

print((v1 * v2).sum())
# 1 Multiplication of numpy arrays is a "vectorized" operation that is very efficient


print('-----------')

print(sum([x1 * x2 for x1, x2 in zip(v1, v2)]))
# 2 You should not iterate through vectors this way unless you want to slow down
# your pipeline
