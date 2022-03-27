def f(*a):
  sum_num=0
  for i in a:
    sum_num += i
  return sum_num  

num_tuple = tuple(map(int, input("Please input list, divid by ',': ").split(',')))
print(f(*num_tuple))
