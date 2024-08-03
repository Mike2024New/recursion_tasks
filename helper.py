x = [2, 3, 1]
res = not all(isinstance(element, (float, int)) for element in x)
print(res)
