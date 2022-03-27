list = list(range(10))
even = []
odd = []
print (list)

for a in list:
  if a % 2 == 0:
    even.append(a)
  else:
    odd.append(a)
print (odd + even)
