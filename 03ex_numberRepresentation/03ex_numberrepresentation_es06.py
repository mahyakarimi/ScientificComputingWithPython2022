#a)
def f(x):
  return x*(x-1)
gamma = 1e-2
x0 = 1.0
derivative = (f(x0+gamma) - f(x0)) / gamma
print(derivative)
#it is not perfectly equal to 1.00 because gamma is not small
#enough.

#b)
powers = [-4, -6, -8, -10, -12, -14]
x0 = 1.0
for pw in powers:
  gamma = 10**pw
  derivative = (f(x0+gamma) - f(x0)) / gamma
  print("derivative with a gamma equal to", gamma, ": ", derivative)
  print("the difference with the real derivative: ",abs(derivative-1))
  print("-"*50)
#by decreasing gamma, the accuracy first improves so that the best error happens
#when gamma = 1e-8. After that it falls again and gets worse. The reason is that
#in those areas, gamma is so small that the calculation is approximated. This is
#because of the limits of python. Otherwise, in the real world, when decreasring
#gamma, the result gets more and more accurate and never gets worse.