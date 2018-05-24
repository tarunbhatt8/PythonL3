#Q.3- Write a program to find the product of all elements of a tuple.

t1=(1,2,3,4,5,6,7,8,9)
product=1
for num in t1:
	product=product*num
print("product of all elements of tuple= %d" %(product))
