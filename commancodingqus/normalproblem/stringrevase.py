def rev(str):
    ans=""
    l=len(str)-1
    while len(ans) < len(str):
        ans+=str[l]
        l-=1
    return ans
print(rev("harish"))