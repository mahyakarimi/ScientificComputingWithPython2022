result = []
for a in range(1, 100):
  for b in range(a, 100):#to make the triples unique
    c = (a**2 + b**2) ** 0.5
    flag = (c == int(c))
    if c >= 100:
      break
    elif flag:
      result.append((a,b,int(c)))
print(result)