print('hello world')
l1 = [4,2,45,6,7,3,6,8,0,1,6,7,9,7,5]

l2=sorted(l1) # sorted function returns new list of any iterable obj in sorted keys

print('sorted list : ',l2)
print('original list : ',l1)

l1.sort()
print('original list : ',l1)

# sorting in descending order

l3 = sorted(l1,reverse=True)

print('sorted list in desc : ',l3)

t1 = (4,2,45,6,7,3,6,8,0,1,6,7,9,7,5)

