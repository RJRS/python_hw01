# 1. 建立一個列表（List ）初始化為 1, 2... 9 的元素
# 2. 利用程式將最左邊的元素移動到最右邊
# 3. 最後請將移動的結果印出
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
L = L[1:] + [L[0]]
print(L)
