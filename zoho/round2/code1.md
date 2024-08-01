## Remove The Word That are Palindrome in given Sentence :

``` python 
s="Malayalam is my mother tongue"

world=[]
def convetlist(s):
    w=""
    for i in s:
        
        if i != " ":
            w+=i.lower()
        else:
            world.append(w)
            w=""
    world.append(w)

  
def palilromecheker(world):
    ans=[]
    
    for n in world:
     left=0
     right=len(n)-1
     while left < right:
        if n[left] != n[right]:
            ans.append(n)
            break
        
        left+=1
        right -= 1
    print(' '.join(ans))

convetlist(s)    
palilromecheker(world)
    
```
## Output The above code 
``` bash
is my mother tongue
```