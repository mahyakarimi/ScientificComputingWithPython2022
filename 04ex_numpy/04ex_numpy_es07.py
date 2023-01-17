import numpy as np
def prime_num(N=100):
  results = np.array([True if (i!=0 and i!=1) else False for i in range(N)])#ignoring 0 and 1
  for i in range(2, N):
    for j in range(i+1, N):
      if j % i == 0:
        results[j] = False
  prime_numbers = np.where(results==True)[0]
  return prime_numbers
print(prime_num(N=100))

# Commented out IPython magic to ensure Python compatibility.
Ns = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
for N in Ns:
  print("N =",N)
  %timeit prime_num(N=N)
  print("-"*80)
#The complexity if O(n log log n):
#Check:
#(a0=16, a9=8192, n=a9/a0=512) => (n log log n =~ 512 * 3 =~ 1500)
#(t0=1.78e-5 s, t9=2.56 s) => t9/t0 =~ 150000
#constant = 150000 / 1500 = 100
#Complexity ~ (100 n log log n)
