print('hello')
print("hello")
print("I don't know")
# print('I don't know')文字列がどこまでかわからないためエラーとなる
print('I don\'t know') # 上記のエラーを解消するためにバックスラッシュを追加
print('say "I don\'t know"') # シングルクオテーションの中にダブルクオテーションを入れても文字として認識される
print("say \"I don\'t know\"") #　ダブルクオテーションの中にダブルクオテーションの場合は文字とは認識されないのでバックスラッシュ追加

print('hello. \nHow are you?') # \nで改行を表す
print('C:\name\name') #パスを記載しようとしても改行と認識される
print(r'C:\name\name') # 生データであることを示すrawの頭文字のrを頭につけると上記の問題を解決できる

print("""
line1
line2
line3
""") #改行を\nで記載すると見辛くなるため視認性を上げる目的に『"""」でくくると改行ありの状態で出力される

# 「#」とlineの間に改行が入ってしまう
print("###################")
print("""
line1
line2
line3
""")
print("###################")

# 上記を解決するためにバックスラッシュをline1の前とline3の前に追加
print("###################")
print("""\
line1
line2
line3\
""")
print("###################")

print('Hi.' * 3) #演算子で文字列を複数回表示させることが可能
print('Hi.' * 3 + 'Mike.')
print('Py' + 'thon')
prefix = 'Py'
# print(prefix  'thon') #一度変数に入れたものと組み合わせる時には+が必要
print(prefix + 'thon')

# +を使わず繋げるのに適しているのは下記のように組み合わせたいリテラルが長い時に視認性が上がるため使える
s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
print(s)

#上記と同じ結果となる
s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
     'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
print(s)

word = 'python'
print(word[0]) #1文字目出力
print(word[1]) #2文字目出力
print(word[-1]) #語尾を出力
print(word[0:2]) #1文字目から2文字目まで出力
print(word[2:5]) #3文字目から5文字目まで出力
print(word[:2]) #1文字目から2文字目まで
print(word[2:]) #2文字目から最後まで
#文字の置き換えをする方法
word = 'j' + word[1:] #jysonが出力される
print(word)
n = len(word)
print(n)