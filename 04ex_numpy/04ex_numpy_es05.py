import numpy as np
array = [[i*j for i in range(1, 11)] for j in range(1, 11)]
trace = np.trace(array)
anti_dig = [array[i][::-1][i] for i in range(len(array))]
dig_offset = [array[i][i+1] for i in range(len(array)-1)]
print(trace)
print(anti_dig)
print(dig_offset)