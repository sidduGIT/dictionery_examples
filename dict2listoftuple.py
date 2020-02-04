dict1={ 'Geeks': 10, 'for': 12, 'Geek': 31 }
print([(k,v) for k,v in dict1.items()])

print(list(zip(dict1.keys(),dict1.values())))
