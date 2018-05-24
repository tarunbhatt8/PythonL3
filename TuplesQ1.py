''' Q.1- Take 20 integer inputs from user and print the following:
(Use the basic logic of loops) 

1. number of positive numbers
2. number of negetive numbers
3. number of odd numbers
4. number of even numbers
5. number of 0s '''

print("Enter 20 integers")
i=0
l1=[]

while(i<20):
	element=input("Enter Integer No. %d" % (i+1))
	l1.append(int(element))
	i=i+1

t1=tuple(l1)
positive,negative,odd,even,zeros=0,0,0,0,0

for num in t1:
	if num>0:
		positive=positive+1
	if num<0:
		negative=negative+1
	if num==0:
		zeros=zeros+1
	if num%2==0:
		even=even+1
	if num%2!=0:
		odd=odd+1

print("number of positive numbers= %d" %(positive))
print("number of negative numbers= %d" %(negative))
print("number of odd numbers= %d" %(odd))
print("number of even numbers= %d" %(even))
print("number of zeros numbers= %d" %(zeros))


	