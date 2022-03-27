# 1. 讓使用者輸入一個整數 n
# 2. 請分別定義兩個 Function: isPrime(n) 回傳 n 是否為質數、primes(n) 回傳小於 n 質數
def isPrime(a):
    if a > 1:
        for b in range(2, a//2+1):
            while a % b == 0:
              return False
              break
            else:
              b +=1
        else:
          return True
      

def Prime(c):
    prime = []
    for d in range(2, c):
        if isPrime(d):
            prime.append(d)
        else:
          continue
    return prime

num = int(input("Please input a integer: "))
print("Output：",", ".join(str(x) for x in Prime(num)))
