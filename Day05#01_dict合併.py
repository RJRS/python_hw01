#練習：請將不同的 dict 元素合併成一個 dict
d1 = {1:10, 2:20}
d2 = {3:30, 4:40}
d3 = {5:50, 6:60}
d = dict(list (d1.items()) + list (d2.items()) + list (d3.items()))
print(d)
e = {**d1, **d2, **d3}
print(e)
# f = d1 | d2 | d3
# print(f) #3.9版本才可使用
