''' #Q.3- Count the number of occurrence of each letter in word "MISSISSIPPI". 
Store count of every letter with the letter in a dictionary.'''

str="MISSISSIPPI"

dict={}

l=list(str)

for j in l:

    p=l.count(j)

    dict[j]=p

print(dict)
