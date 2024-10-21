numbers = {11,22,33,44,55,66,70,80,99}
numbers1 = {10,20,30,40,50,60,70,80,90}

numbers.add(110)

print(numbers)

x = numbers.copy()
print(x)

z = numbers.difference(numbers1)
print(z)

numbers.difference_update(numbers1)
print(numbers)

numbers.discard("33")
print(numbers)

n1={1,2,3}
n2={2,3,6}
w=n1.intersection(n2)
print(w)

n1.intersection_update(n2)

print(n1)


a = n1.union(n2)

print(a)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)

print(z)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

z = x.issuperset(y)

print(z)

fruits = {"apple", "banana", "cherry"}

fruits.pop()

print(fruits)

fruits.remove("banana")

print(fruits)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

x.update(y)

print(x)

mylist = ['adarsh', 'ganesh', 'sahil']
x = frozenset(mylist)

