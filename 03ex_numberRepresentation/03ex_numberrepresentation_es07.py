from math import pi
PI = pi

def f(x):
  return (1 - x**2) ** 0.5

def integral(N, f=f, lower=-1, upper=+1):
  length = upper - lower #2 in 2 / N
  h = length / N
  I = 0
  for i in range(N):
    height = f(x = lower + h/2)
    I += h * height
    lower = lower + h
  return I

print("The integral is: ", integral(N = 100))
print("The difference with the actual number: ", abs(integral(N = 100) - PI/2))

#for 1 second
import timeit
limit, time = 1.0, 0.0
N = 2000000#big enough
num = 20
while time < limit:
  time = timeit.timeit('integral(N)', 'from __main__ import integral, N', number=num)/num
  print("N = ", N, "Time: ", time)
  N += 50000

N = 2375000
time = timeit.timeit('integral(N)', 'from __main__ import integral, N', number=num)/num
print(time)

#for 1 minute
import timeit
limit, time = 60.0, 0.0
N = 130000000#big enough
num = 1
while time < limit:
  time = timeit.timeit('integral(N)', 'from __main__ import integral, N', number=num)/num
  print("N = ", N, "Time: ", time)
  N += 8000000

N = 142000000
time = timeit.timeit('integral(N)', 'from __main__ import integral, N', number=num)/num
print(time)

#1 second
print("The integral is: ", integral(N = 2375000))
print("The difference with the actual number: ", abs(integral(N = 2375000) - PI/2))