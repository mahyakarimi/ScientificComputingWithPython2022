import numpy as np
import matplotlib.pyplot as plt
array = np.random.randint(low=0, high=2, size=(1000, 200))
array[array==0] = -1
walking_distance = np.sum(array, axis=1)
sq_array = array ** 2
mean_sq_dis = np.mean(array, axis=0)
plt.plot(abs(mean_sq_dis))
plt.show()
