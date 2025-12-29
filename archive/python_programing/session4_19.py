# 値わたしと参照渡し
i = [1,2,3,4,5]
j = i
j[0] =100
print('j = ', j)
print('i = ', i)

# 上記を避ける方法
x = [1, 2, 3, 4, 5]
# y = x.copy()
y = x[:] # copyを使った方が分かりやすい
y[0] = 100
print('y =', y)
print('x =', x)

X = 20
Y =  X
Y = 5
print(id(X))
print(id(Y))
print(X)
print(Y)

X = ['a', 'b']
Y = X
Y[0] = 'p'
print(id(X))
print(id(Y))
print(X)
print(Y)