keys=['a','b','c','d']
values=[10,20,30,40]
dict1={k:v for k,v in zip(keys,values)}
print(dict1)

lst=[1,2,3,4,5,6,7]
print({i:i**2 for i in lst})
dict1={i:i**3 for i in lst}
print(dict1)

str1='atharv'
print({i.upper():i*3 for i in str1})

dict1={'A': 'aaa', 'T': 'ttt', 'H': 'hhh', 'R': 'rrr', 'V': 'vvv'}
keys=list(dict1.keys())
values=list(dict1.values())
print({v:k for k,v in zip (keys,values)})
