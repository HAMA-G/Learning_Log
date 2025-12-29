
try:
	heisei = int(input("平成の年を入力してください："))
except:
	print("半角数字で入力してください")

if 1 <= heisei <= 31:
	print("平成{}年は西暦{}です".format(heisei, heisei + 1988))
else:
	print("1から31までの数字を入力してください")