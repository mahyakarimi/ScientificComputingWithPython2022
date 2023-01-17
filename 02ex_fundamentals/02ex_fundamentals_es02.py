ans = list(map(lambda x: x * x, filter(lambda x: x % 2 == 1, range(10))))
print(ans)
###########################################################################
ans = [i**2 for i in range(1,10,2)]
print(ans)