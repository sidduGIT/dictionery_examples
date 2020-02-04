dict1={'a':1,'b':-2,'c':3,'d':-4,'e':5}
values=[i for i in dict1.values() if i>0]
keys=list(dict1.keys())
print(dict(zip(keys,values)))

print(dict((k,v) for k,v in dict1.items() if v>0))

print(dict(filter(lambda x:x[1]>0,dict1.items())))
