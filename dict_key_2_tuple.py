dict1={'abc':1,'def':2,'ghi':3}
print({tuple(k):v for k,v in dict1.items()})

dict1={('a','b','c'):1,('d','e','f'):2,('g','h','i'):3}
dict1[('x','y','z')]=26
print({''.join(k):v for k,v in dict1.items()})
