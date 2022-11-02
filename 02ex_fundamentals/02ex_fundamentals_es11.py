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
  
class rectangle(polygon):
  def __init__(self, inp_rec):
    super().__init__(inp_rec) 
    self.unq_sides = len(set(inp_rec))
    if len(inp_rec) != 4: 
      print("ERROR: Rectangle has 4 sides...")
      raise("ERROR")
    if not (self.unq_sides <= 2 and self.unq_sides > 0):
      print("ERROR: Rectangle's geometry is violated...")
      raise("ERROR")
  def area(self):
    sides = self.getOrderedSides(True)
    s1, s2 = sides[0], sides[-1]
    return s1 * s2

#testcase1
input_rectangle = (1, 2, 3)
REC = rectangle(input_rectangle)
REC.set_sides()
per = REC.perimeter()
area = REC.area()
print("Rectangle check: approved")
print("Perimeter", per)
print("Area", area)

#testcase2
input_rectangle = (1, 2, 3, 4)
REC = rectangle(input_rectangle)
REC.set_sides()
per = REC.perimeter()
area = REC.area()
print("Rectangle check: approved")
print("Perimeter", per)
print("Area", area)

#testcase3
input_rectangle = (8, 2, 2, 8)
REC = rectangle(input_rectangle)
REC.set_sides()
per = REC.perimeter()
area = REC.area()
print("Rectangle check: approved")
print("Perimeter", per)
print("Area", area)

#testcase4
input_rectangle = (5, 5, 5, 5)
REC = rectangle(input_rectangle)
REC.set_sides()
per = REC.perimeter()
area = REC.area()
print("Rectangle check: approved")
print("Perimeter", per)
print("Area", area)

#testcase5
input_rectangle = (1.5, 3.5, 3.5, 1.5)
REC = rectangle(input_rectangle)
REC.set_sides()
per = REC.perimeter()
area = REC.area()
print("Rectangle check: approved")
print("Perimeter", per)
print("Area", area)