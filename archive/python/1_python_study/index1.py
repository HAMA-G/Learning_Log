words = ["空", "秘密", "電柱", "ひらけごま", "海", "ギター"]
str = input("文字列を入力してください")

try:
	index = words.index(str)
	print(f'"{str}"のインデックスは{index}です')
except ValueError:
	print(f'"{str}"は見つかりませんでした')