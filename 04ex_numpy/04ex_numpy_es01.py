import numpy as np

m = np.arange(12).reshape((3,4))
total = np.mean(m)
row = np.mean(m, axis=1)
col = np.mean(m, axis=0)
print(m)
print(total)
print(row)
print(col)