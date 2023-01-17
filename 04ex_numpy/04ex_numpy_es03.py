import numpy as np
matrix = np.random.uniform(low=0.0, high=3.0, size=(10, 6))
mask = np.where(matrix < 0.3, 0, matrix)
print(mask)