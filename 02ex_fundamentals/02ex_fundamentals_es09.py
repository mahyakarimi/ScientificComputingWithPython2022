# Commented out IPython magic to ensure Python compatibility.
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
def fibo_end2end(num):
  for i in range(num):
    print(fibo(i))

# %timeit fibo_end2end(20)

# Commented out IPython magic to ensure Python compatibility.
#This implementation is approximately 2x faster than the one by recursive function.
def fibo_while(num):
  a, b, j = 0, 1, 1
  print(a)
  while j < num:
    print(a + b)
    c = a #save a -> temporary variable
    a = a + b
    b = c
    j = j + 1

# %timeit fibo_while(20)