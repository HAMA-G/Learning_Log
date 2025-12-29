import sys

sum = 0
for i in range(1, len(sys.argv)):
	sum += float(sys.argv[i])

print(f"総和： {sum}")