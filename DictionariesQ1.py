#Q.1- Create a dictionary to store name and marks of 10 students by user input.



dict={}

num=int(input("Enter no. of elements for adding in  dictionary"))

for j in range(num):

    n=input("Enter name and marks as name:marks of student" +str(j+1)+": ")

    li=n.split(':')

    dict[li[0]]=li[1]

print(dict)
    
    
                
