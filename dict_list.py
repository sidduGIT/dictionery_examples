dict1={'abc':1,'def':2,'ghi':3,'jkl':4}
lst=['abc','ghi']
print(dict((k,v) for k,v in dict1.items() if k in lst))
print(dict((k,v) for k,v in dict1.items() if k not in lst))
