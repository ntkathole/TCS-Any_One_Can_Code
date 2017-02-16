#!/usr/bin/python
file1=input("")
print ("File content of",file1,":")
file=open(file1)
r=file.read()
print (r)
res=0
list1=r.split()
for x in range(0,len(list1)):
    try:
        res=res+int(list1[x])
    except ValueError:
        print ("Invalid Input")
        exit()
print (res)

