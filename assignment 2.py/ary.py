import array as arr

b=arr.array("i",[11,22,33,44,55,66,77])
for i in range(0,7):
     print(b[i],end=" ")
print()
b.insert(7,88)
for i in (b):
     print(i,end=" ")
print()
b.append(111)
for i in (b):
    print(i,end=" ")
print()
b.remove(44)
for i in (b):
    print(i,end="-")
print()
b.pop()
for i in (b):
    print(i,end=" ")
print()
b.reverse()
for i in (b):
    print(i,end=" ")