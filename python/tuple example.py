# tuple examples
t=(12,34,12,56)
print(type(t))
print(t)
print(t.count(12))

#accessing tuple with slice operator & index position
t=(78,65,12,34,12,56)
print(t[0:5])
print(t[0:5:2])

#converts from  tuple to list
t=(78,65,12,34,12,56)
lst=list(t)
lst.insert(0,111)
t=tuple(lst)# converts from list to tuple
print(t)