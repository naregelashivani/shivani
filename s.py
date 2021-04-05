#3.Write a Python program to read a file line by line store it into a variable.

l="0"
with open('test.txt','r') as f:
    a=f.readlines()
    for i in a:
        c=l+str(i)
        print(c)
    

    

