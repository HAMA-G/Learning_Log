weekday1 = ["Sun", "Mon", "Tue"]
weekday2 = ["日", "月", "火", "水", "木", "金", "土"]

for (eng, jpn) in zip(weekday1,weekday2):
	print(eng +"： " + jpn)