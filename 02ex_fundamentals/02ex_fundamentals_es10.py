class polygon:
  def __init__(self, inp):
    self.inp = inp
    self.sides = [0 for _ in range(len(self.inp))]
  def set_sides(self):
    for i in range(len(self.inp)):
      self.sides[i] = self.inp[i]
  def perimeter(self):
    return sum(self.sides)
  def getOrderedSides(self, increasing):
    if increasing:
      self.sides.sort(reverse=True)
      return tuple(self.sides)
    self.sides.sort(reverse=False)
    return tuple(self.sides)
  
input = (1,6,8,2,4,9)
POL = polygon(input)
POL.set_sides()
per = POL.perimeter()
ord1 = POL.getOrderedSides(increasing=True)
print(per)
print(ord1)

POL = polygon(input)
POL.set_sides()
per = POL.perimeter()
ord2 = POL.getOrderedSides(increasing=False)
print(per)
print(ord2)