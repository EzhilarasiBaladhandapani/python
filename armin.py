a=int(input())
b=int(input())
for i in range(a+1,b):
	l=len(str(i))
	sum=0
	temp=i
	while(temp!=0):
		digit=temp%10
		sum=sum+(digit**l)
		temp=temp//10
	if(i==sum):
		print(i)