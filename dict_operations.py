lst1=['a','b','c','d','e','f']
lst2=[1,2,3,4,5,6]
print(dict(zip(lst1,lst2)))
dict1=dict(zip(lst1,lst2))
for k,v in dict1.items():
    print(k,v)

print(dict1.keys())
print(dict1.values())

dict1['g']=7
dict1['h']=8
print(dict1)

print(len(dict1))

for v in dict1.values():
    print(v)

for k in dict1.keys():
    print(k)

del dict1['b']
del dict1['f']
print(dict1)

dict1['b']=2
dict1['f']=6
print(dict1)

print(dict(siddu=100,atharv=200,suraj=300,sumit=400))
dict2={}
print(dict2)
dict2['siddu']=4
dict2['santu']=5
dict2['shivu']=1
dict2['jagu']=3
dict2['shaila']=2
print(dict2)

print(dict2.pop('siddu'))
print(dict2.pop('santu'))
print(dict2)

print('shivu' in dict2)
print('siddu' in dict2)

dict1={'a': 1, 'c': 3, 'd': 4, 'e': 5, 'g': 7, 'h': 8, 'b': 2, 'f': 6}

for k,v in sorted(dict1.items()):
    print(k,v)

for k in sorted(dict1):
    print(k,dict1[k])

dict1={'a':1,'b':2}
dict2={'c':3,'d':4}
dict3={'e':5,'f':6}
dict1.update(dict2)
print(dict1)
dict1.update(dict3)
print(dict1)

dict1={'a': 5, 'b': 2, 'c': 3, 'd': 1, 'e': 6, 'f': 4}
print(dict1)
for k in sorted(dict1.items(),key=lambda x:x[1]):
    print(k)

dict1={'a': 5, 'b': 2, 'c': 3, 'd': 1, 'e': 6, 'f': 4}
print(dict1)
for k in sorted(dict1.items(),key=lambda x:x[0]):
    print(k)

print(dict(sorted(dict1.items(),key=lambda x:x[0])))
print(dict(sorted(dict1.items(),key=lambda x:x[1])))



#print(dict(sorted(dict1.items(),key=)))
