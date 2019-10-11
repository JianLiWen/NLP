import numpy as np
vector = np.array([1, 2, 3, 4])
matrix = np.array([[1, 'Tim'], [2, 'Joey'], [3, 'Johnny'], [4, 'Frank']])
print(vector)
print(matrix)
print(matrix[1][1])
print(matrix[:, 1])

# 自动构架一个多行多列的array对象
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)  # 获取numpy中数组的维度

# nfl = np.genfromtxt("E:/numpy/data/price.csv", dtype='U75', skip_header=1, delimiter=",")
# print(nfl)

mat = np.array([
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
])
m = (mat == 25)
print(m)
second_matrix_25 = (mat[:, 1] == 25)
print(second_matrix_25)
print(mat[second_matrix_25, :])
print(mat.sum(axis=1))
print(mat.sum(axis=0))
