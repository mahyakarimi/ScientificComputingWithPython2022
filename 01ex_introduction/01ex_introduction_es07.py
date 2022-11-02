#a)for loop
cubes = []
for i in range(11):
  cubes.append(i**3)
print(cubes)
#b)list comprehension
cubes = [i**3 for i in range(11)]
print(cubes)