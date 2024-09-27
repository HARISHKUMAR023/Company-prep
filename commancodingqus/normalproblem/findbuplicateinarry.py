a=[1,2,2,2,3,4,5,5]
ans=[]
for i in set(a):
    if a.count(i) > 1:
        ans.append(i)
print(ans)