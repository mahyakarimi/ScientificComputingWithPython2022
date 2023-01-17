a, b, j = 0, 1, 1
print(a)
while j < 20:
  print(a + b)
  c = a #save a -> temporary variable
  a = a + b
  b = c
  j = j + 1