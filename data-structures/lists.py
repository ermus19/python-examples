a = ['a', 'b', 'c', 'd']

print("This is a list", a)
print("It is", len(a), "elements length.")
print("Let's check if element 'd' is in the list:", 'd' in a)
print("This should be the maximun value of the list", max(a))
print("This should be the minnimun value of the list", min(a))

print("This is a list, item by item: ", end=' ')

for item in a:
    print(item, end=' ')

print("\r\nThis is the first element of the list: ", a[0])

a.remove('b')

print("This is the list after removing the 'b' ", a)

del a[0]

print("This is the list after removing the first element", a)