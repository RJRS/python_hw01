l1 = [1, 1, 3, 9, 7, 8, 8, 8]
l2 = []
for i in l1:
if i not in l2:
l2.append(i)
print(l2)
l3 = list(set(l1))
print(l3)
l4 = sorted((list(set(l1))), reverse = True)
print(l4)
