s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My') # Myから始まるかを確認する。正しい場合はTrueを返す
print(is_start)

is_start = s.startswith('x') # Myから始まるかを確認する。正しい場合はTrueを返す
print(is_start)

print('#######################')

print(s.find('Mike')) # 前から何文字めにMikeがあるかを数字で返す(数え方は0からスタート）
print(s.rfind('Mike')) # 後ろのMikeが何文字目にあるかを数字で返す（数え方は前から0スタートで数える）
print(s.count('Mike')) # Mikeという文字がいくつあるかを数える
print(s.capitalize()) # 一番最初の文字以外が小文字になる関数
print(s.title()) # 単語の頭文字がすべて大文字になる
print(s.upper()) # 全ての文字を大文字にする
print(s.lower()) # 全ての文字を小文字にする
print(s.replace('Mike', 'Nancy')) # 文字を置換する（例：MikeをNancyに変更）