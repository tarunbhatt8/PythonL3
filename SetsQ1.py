''' Q.1- Create two set using user defined values. 

1. Calculate difference between two sets.
2. Compare two sets.
3. Print the result of intersection of two sets. '''


set1=set()

set2=set()

n1=int(input("Enter no. of elements in set 1"))


for i in range(n1):
    
	n=int(input("Enter " +str(i+1)+ "value"))
    
	set1.add(n)


num2=int(input("Enter no. of elements in set 2"))


for i in range(num2):
    
	n=int(input("Enter " +str(i+1)+ "value"))
    
	set2.add(n)


print("Difference of sets=",set1-set2)

print("Set comparison=", set1^set2)

print("Intersection=",set1&set2)

