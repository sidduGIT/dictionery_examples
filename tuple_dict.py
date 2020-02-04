#tuple to dict

t1=('A','B','C','D')
t2=(1,2,3,None)
print(dict(zip(t1,t2)))

print({t1[i]:t2[i] for i in range(len(t1))})

lst=[('A',1),('B',2),('C',3),('D',4),('E',5),('F',6)]
print('orig',lst)
print('modified',{lst[i][0]:[lst[i][1]] for i in range(len(lst))})

