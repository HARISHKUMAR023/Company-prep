## 1- Remove The Word That are Palindrome in given Sentence :

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

## 2-Write a program to get the output:
### Input and Output
``` bash
input1 = "a1b10"
output1 = expand_string(input1)
print(output1)  # Output: abbbbbbbbb
```
``` bash
input2 = "b3c6d15"
output2 = expand_string(input2)
print(output2)  # Output: bbbccccccddddddddddddddd
```

``` python 
def expand_string(s):
    expanded_str = ""
    i = 0
    
    while i < len(s):
        # Extract the character
        char = s[i]
        i += 1
        
        # Extract the number
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
            
        # Convert the number to an integer
        num = int(num_str)
        
        # Append the character 'num' times to the result
        expanded_str += char * num
    
    return expanded_str
```


## 3-Write a program to get the output:


``` python 
a = "ZohoCorporation"
for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            print(a[i], end="")
        elif (len(a) - 1) - i == j:
            print(a[::-1][i], end="")
        else:
            print(" ", end="")
    print("")

```
### Input and Output
``` bash 
Z             n
 o           o 
  h         i  
   o       t   
    C     a    
     o   r     
      r o      
       p       
      r o      
     o   r     
    C     a    
   o       t   
  h         i  
 o           o 
Z             n
```
