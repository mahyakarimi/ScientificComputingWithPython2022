def unq_char_counting(string):
  string = string.lower()
  unq_chars = tuple(list(string))
  result = {i:0 for i in unq_chars}
  for ch in unq_chars:
    result[ch] = string.count(ch)
  return result

s1 = "Write a program that prints the numbers from 1 to 100. \
But for multiples of three print Hello instead of the number and for the multiples of five print World. \
For numbers which are multiples of both three and five print HelloWorld."
s2 = "The quick brown fox jumps over the lazy dog"

print(unq_char_counting(s1))
print(unq_char_counting(s2))