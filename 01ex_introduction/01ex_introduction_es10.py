def normalize(array):
  length = sum([i**2 for i in array]) ** 0.5
  normalized = [i/length for i in array]
  return normalized

normalize([1, 2, 2])