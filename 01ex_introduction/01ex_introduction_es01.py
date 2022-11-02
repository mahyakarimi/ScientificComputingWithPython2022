#a)
for idx in range(1, 101):
  if idx % 3 == 0 and idx % 5 != 0:
    print("Hello")
  elif idx % 5 == 0 and idx % 3 != 0:
    print("World")
  elif idx % 15 == 0:
    print("HelloWorld")
  else:
    print(idx)

#b)
result = ()#Initialize a tuple
for idx in range(1, 101):
  if idx % 3 == 0 and idx % 5 != 0:
    result = result + ("Hello",)
  elif idx % 5 == 0 and idx % 3 != 0:
    result = result + ("World",)
  elif idx % 15 == 0:
    result = result + ("HelloWorld",)
  else:
    result = result + (idx,)

result = tuple(map(lambda x:x.replace("Hello","Python") if "Hello" in str(x) \
                  else(x.replace("World","Works") if "World" in str(x) else x), result))
print(result)
