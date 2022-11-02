import math

def euc_dis(u, v):
  return math.sqrt(((u[0] - v[0])**2 + (u[1] - v[1])**2))

u = (3, 0)
v = (0, 4)
print(euc_dis(u, v))