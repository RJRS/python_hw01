a = int(input ("Please input an integer: "))
ans = 0
for b in range(1, a+1):
    d = 1
    for c in range(1, (b+1)):
      d = c * d
    ans = ans + d
print (ans)
