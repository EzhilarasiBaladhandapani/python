a=int(input())
l=len(str(a))
sum=0
temp=a
while(temp!=0):
	digit= temp%10
	sum= sum+(digit**l)
	temp=temp//10
	if(a==sum):
		print("yes")
		break
else:
	print("no")