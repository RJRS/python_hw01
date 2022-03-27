#練習：試著用 Python 將網址當中的 domain 取出來。
s = "https://www.facebook.com/dscareer"
print ((s.split("://", 1))[1])
