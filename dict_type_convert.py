dict1={'1':['2','3','4'],'5':['6','7','8'],'9':['10','11']}
res={}
for k,v in dict1.items():
    res[int(k)]=[int(i) for i in v]

print(res)

print({int(k):[int(i) for i in v]for k,v in dict1.items()})

lst=[{'a':'1','b':'2'},{'c':'3','d':'4'}]
res=[]
for i in lst:
    res.append({k:int(v) for k,v in i.items()})
print(res)

print([{k:int(v)} for i in lst for k,v in i.items()])
