var1, var2 = 1.0, 1.0
mem1, mem2 = var1, var2
j, k = 0, 0

while True:
  var1 /= 2
  if var1/2 == mem1/2: break
  else: mem1 = var1
  j += 1

while True:
  var2 *= 2
  if var2*2 == mem2*2: break
  else: mem2 = var2
  k += 1
print(j)
print(k)
print("underflow limit: ", f"{mem1} which is 2^-{j}")
print("overflow limit: ", f"{mem2} which is 2^+{k}")

5e-324 == 2**-1074

5e-324 / 2

8.98846567431158e+307 == 2**1023

8.98846567431158e+307 * 2