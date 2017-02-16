#!/usr/bin/python
input2=int(input(""))
list2=[]
for y in range(0,input2):
    input1=input("")
    res=0
    list1=input1.split()
    for x in range(0,len(list1)):
        try:
            res=res+int(list1[x])
        except ValueError:
            res="Invalid Input"
            break
    list2.append(res)
for x in range(0,len(list2)):
               print (list2[x])

