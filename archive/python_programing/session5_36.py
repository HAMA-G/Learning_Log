y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

# よくない書き方
if not a == b:
    print('Not equal')

# 上記の修正
if a != b:
    print('Not equal')

# よくない書き方
if not a > b:
    print('Not equal')

# 上記の修正
if a <= b:
    print('Not equal')

is_ok = False

if not is_ok:
    print('hello')