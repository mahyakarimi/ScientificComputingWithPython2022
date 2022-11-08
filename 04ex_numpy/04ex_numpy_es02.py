import numpy as np
u = np.array([1, 3, 5, 7])
v = np.array([2, 4, 6, 8])
ot_pr = np.outer(u, v)
print(ot_pr)

ot_pr = [[i*j for j in v] for i in u]
ot_pr = np.array(ot_pr)
print(ot_pr)

ot_pr = u[:, np.newaxis] * v
print(ot_pr)