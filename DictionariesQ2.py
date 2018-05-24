#Q.2-Sort the dictionary created in previous question according to marks. 

dict={}

num=int(input("Enter no. of elements for adding in  dictionary"))

for j in range(num):

    n=input("Enter name and marks as name:marks of student" +str(j+1)+": ")

    li=n.split(':')

    dict[li[0]]=li[1]

print(dict)
print(sorted(dict.values()))
 
