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




## 4 -Write a program to get the output:


``` python 
zohost = {
    "zo": "zoho",
    "a": "and",
    "in": "invoice",
    "bk": "books",
    "exp": "expense",
    "io": "inventory",
    "chek": "checkout",
    "pa": "payroll",
    "com": "commerce",
    "py": "payments",
    "bg": "billing"  
}

a = "zobgachek"
ans = []
key = ""

for i in a:
    key += i
    if key in zohost:
        ans.append(zohost[key])
        key = ""
if key:
    ans.append(key)

print(" ".join(ans))

```
### Input and Output
``` bash 
zoho billing and checkout
```

### Question -5:

Given an array, the distance between two array values is the number of indices between them. Find the minimum distance between any pair of equal elements in the array. If no such value exists, return `-1`.

### Example:

- **Input:** `[1, 2, 3, 4, 10]`
- **Output:** `-1`

### Explanation:

Since there are no repeating elements in the array, there is no distance to calculate. Therefore, the output is `-1`.

### Code:

```python
arr = [1, 2, 3, 4, 10]
my = {}
mini = len(arr) + 1  # Start with a value larger than the array length

for i, nums in enumerate(arr):
    if nums in my: 
        m = i - my[nums]
        mini = min(m, mini)
        
    my[nums] = i  # Store the index of the current number

# Check if a valid minimum distance was found
if mini == len(arr) + 1:
    print(-1)
else:
    print(mini)  # Output will be -1 since there are no pairs

