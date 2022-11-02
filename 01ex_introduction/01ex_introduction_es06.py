inp1 = input("Enter the first input: ")
inp2 = input("Enter the second input: ")
counter1, counter2 = 0, 0
try:
  inp1 = eval(inp1) if inp1 not in "inp1,inp2,counter1,counter2".split(',') else inp1
  counter1 = 1 # inp1 is not a string
except:
  pass

try:
  inp2 = eval(inp2) if inp2 not in "inp1,inp2,counter1,counter2".split(',') else inp2
  counter2 = 1 # inp2 is not a string
except:
  pass

if counter1 + counter2 == 2:
  print(inp1 + inp2)
elif counter1 + counter2 == 1:
  print("ERROR: types mismatch...")
else:
  print(inp1 + inp2)