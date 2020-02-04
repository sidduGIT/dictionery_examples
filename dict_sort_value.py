dict1={'a':'siddu','b':'atharv','c':'renuka'}
print(dict(sorted([(k,v) for k,v in dict1.items()],key=lambda i:i[1])))
