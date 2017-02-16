input1=input("")
res=0
list1=input1.split()
for x in range(0,len(list1)):
    try:
        res=res+int(list1[x])
    except ValueError:
        print ("Invalid Input")
        exit()
print (res)
