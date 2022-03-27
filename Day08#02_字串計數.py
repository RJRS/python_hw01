str = str(input("Please insert any string: "))
str_list = list(str)
dict = {}
for x in str_list:  
  dict[x] = str_list.count(x) 
print(dict)
