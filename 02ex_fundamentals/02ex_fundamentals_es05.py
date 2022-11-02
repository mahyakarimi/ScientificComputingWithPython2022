language_scores = [('Python', 97), ('Cplusplus', 81), ('Php', 45), ('Java', 32)]
f = lambda x:x[0]
language_scores.sort(key=f)
print(language_scores)