lst=['a', 1, 'b', 2, 'c', 3]
keys=[lst[i] for i in range(len(lst)) if i%2==0]
values=[lst[i] for i in range(len(lst)) if i%2!=0]
print(dict(zip(keys,values)))
