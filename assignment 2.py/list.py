items = ['apple', 'banana', 'cherry',1,2,3]
p=[ ]
print("Empty list ",type(p))
print(type(items))
items.append("adarsh")
items.append(12)
items.extend([13,14,"pranav"])
items.insert(12,"pratik")
items.remove("pratik")
items.pop()
print(items.pop())
print(items)

l1=[11,22,33,44,55]
print(l1)

l1=[1,34.5,"python",12,44,6.8,"list"]
print(l1)

l3=[12,34,56,78,89]
print(l3[1:4])

l4=[99,88,77,66,55,44,33,22,11,"program","line","tuple",5.6,7.8,44.5]
for i in l4:
    print(i,end=" ")

l5=[99,88,77,66,55,44,33,22,11]
print(l5)
print(len(l5))
print(sorted(l5))
print(sum(l5))
print(max(l5))
print(min(l5))

l4=[99,88,77,66,55,44,33,22,11,"program","line","tuple",5.6,33,66,11,88,7.8,44.5]
del l4[1]
print(l4)

l4=[99,88,77,66,55,44,33,22,11,"program","line","tuple",5.6,33,66,11,88,7.8,44.5]
l4.append("data")
print(l4)
l4.insert(3,111)
print(l4)
l4.remove(22)
print(l4)
l4.pop()
print(l4)

l5=[99,88,77,66,55,44,33,22,11,99,44,33,77]
print(l5)
print(l5.index(77))

l5=[99,88,77,66,55,44,33,22,11,99,44,33,77,33,33]
print(l5)
print(l5.count(33))

l5=[99,88,77,66,55,44,33,22,11,99,44,33,77,33,33]
print(l5)
l5.clear()
print(l5)