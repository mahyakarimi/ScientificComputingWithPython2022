#a)
def quadratic_roots(a, b, c):
  delta = b**2 - 4*a*c
  x1 = (-b + delta**0.5) / (2*a)
  x2 = (-b - delta**0.5) / (2*a)
  return (x1, x2)

a = 0.001
b = 1000
c = 0.001
x1, x2 = quadratic_roots(a,b,c)
print("first root", x1)
print("second root", x2)

#b)
def quadratic_roots_mul(a,b,c):
  delta = b**2 - 4*a*c
  numerator = 4 * a * c
  denominat1 = (2 * a) * (-b - delta**0.5)
  denominat2 = (2 * a) * (-b + delta**0.5)
  x1 = numerator / denominat1
  x2 = numerator / denominat2

  return x1, x2

a = 0.001
b = 1000
c = 0.001
x1, x2 = quadratic_roots_mul(a,b,c)
print("first root", x1)
print("second root", x2)
#The answers are slightly differenet from we obtained on a). The reason is that
#we are making the denominators too big or too small. As a result underflowing/
#overflowing happen and produce inaccurate solutions.

#c)
def quadratic_roots_acc(a,b,c):
  delta = b**2 - 4*a*c
  mul1 = -b - delta**0.5
  mul2 = -b + delta**0.5

  numerator1 = (-b + delta**0.5) * mul1
  denominat1 = (2*a) * mul1
  numerator2 = (-b - delta**0.5) * mul2
  denominat2 = (2*a) * mul2

  x1 = numerator1 / denominat1
  x2 = numerator2 / denominat2

  return (x1, x2)

a = 0.001
b = 1000
c = 0.001
x1, x2 = quadratic_roots_acc(a,b,c)
print("first root", x1)
print("second root", x2)