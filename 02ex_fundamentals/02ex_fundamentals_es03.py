def short_words(array, n):
  sh_w = list(filter(lambda x:x if len(list(x)) < n else None, array))
  return sh_w

words = ['hello', 'world', 'python lover', 'god', 'orange']
n = 6
print(short_words(words, n))