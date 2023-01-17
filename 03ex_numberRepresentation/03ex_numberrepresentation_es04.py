new_var1 = 0.0
mem_new_var1 = new_var1
small_val1 = 1e+300
j = 0
while True:
  new_var1 -= small_val1
  if new_var1 - small_val1 == mem_new_var1 - small_val1: break
  else: mem_new_var1 = new_var1
  j += 1

new_var2 = 0.0
mem_new_var2 = new_var2
small_val2 = 1e+300
k = 0
while True:
  new_var2 += small_val2
  if new_var2 + small_val2 == mem_new_var2 + small_val2: break
  else: mem_new_var2 = new_var2
  k += 1

print("underflow limit: ", mem_new_var1)
print("overflow limit: ", mem_new_var2)