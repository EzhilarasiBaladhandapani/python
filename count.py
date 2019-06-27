a=input()
count=0
for c in a:
	if c.isspace()!=True:
		count=count+1
		print(count)