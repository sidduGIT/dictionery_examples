str1='After beating the eggs Dana read the next step Add mix and eggs then add flour and sugar'
dict1={}
words=str1.split()
for word in words:
    word=word.lower()
    if word not in dict1:
        dict1[word]=1
    else:
        dict1[word]+=1
print(dict1)
