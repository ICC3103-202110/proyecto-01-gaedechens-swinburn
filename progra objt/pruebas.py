list1 = [1,2,3,4,5,6,7,8]
#for i in list:
#    if list[1] 
inpu = 2
print (list1[inpu])
value = list(str(list1[inpu]))
print (list1[:inpu]+list1[inpu+1:])
listh = []
listd = []
for i in list1[:inpu]:
    listh.append("*")
for i in list1[inpu+1:]:
    listd.append("*")
listrep = listh + value + listd
print (listrep)