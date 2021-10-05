x = [0.0, 3.0, 5.0, 2.5, 3.7]
print(type(x))

#remove third element 
x.pop(2)
print(x)

#remove the element equal to 2.5 
x.remove(2.5)
print(x)

#add an element to the end 
x.append(1.2)
print(x)

#add a copy
y=x.copy()
print(y)

#how many elements are 0.0
print(y.count(0.0))

#print index with value 3.7
print(y.index(3.7))

#sort list 
y.sort()
print(y)

#reverse sort 
y.reverse()
print(y)

#remove alle lements 
y.clear()
print(y)
