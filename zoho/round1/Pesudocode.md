
### 1 - Output of The following code 

``` c++
#include <stdio.h>

enum Status { SUCCESS, FAILURE };

enum Status checkStatus(int value) {
    return (value % 2 == 0) ? SUCCESS : FAILURE;
}

int main() {
    int num = 3;
    enum Status result = checkStatus(num);
    printf("%d\n", result);
    return 0;
}


```
### Output 
``` bash
1
```

### 2 - Output of The following code 

``` c++
#include <stdio.h>

int main() {
    int a[5] = {5, 1, 15, 20, 25}; // Corrected the closing brace
    int i, j, m;

    i = ++a[1]; // Pre-increment: a[1] becomes 2, i = 2
    j = a[1]++; // Post-increment: j = 2, a[1] becomes 3
    m = a[i++]; // i is used as index (2), then i is incremented: m = a[2] (15), i becomes 3

    printf("%d, %d, %d", i, j, m);

    return 0;
}


```
### Output 
``` bash
3, 2, 15
```
### 3 - Output of The following code 

``` c++
#include <stdio.h>

static int i;       // First declaration of static variable i (initialized to 0).
static int i = 25;  // Error: Re-declaration of static variable i. This is not allowed.
static int i;       // Error: Re-declaration of static variable i. This is not allowed.

void func() {
    printf("%d", i);
    return;
}

int main() {
    static int i;  // Local static variable i (initialized to 0).
    printf("%d", i);
    func();
    return 0;
}


```
### Output 
``` bash
Compilation failed due to following error(s).main.cpp:3:12: error: redefinition of ‘int i’
    3 | static int i = 25;
      |            ^
main.cpp:2:12: note: ‘int i’ previously declared here
    2 | static int i ;
      |            ^
main.cpp:4:12: error: redefinition of ‘int i’
    4 | static int i;
      |            ^
main.cpp:2:12: note: ‘int i’ previously declared here
    2 | static int i ;
      |            ^
```

### 4 - Output of The following code 

``` c++
#include <stdio.h>
int main(){
    int x =3;
    if (x==2);
    x=0;
    if (x==3) x++;
    else x+=2;
    printf("%d", x);
    return 0;
}


```
### Output 
``` bash
2
```

### 5 - Output of The following code 

``` c++
#include <stdio.h>
void func(char str[], int len){
    for ( int i =0; i<len/2; i++){
        char temp = str[i];
        str[i] = str[len-1-i];
        str[len-1-i]= temp;
    }
}
int main(){
  char str[] = "ZohoCorporation";
  int len=7;
  func(str,len);
  printf("%s\n", str);
  return 0;
}

```
### Output 
``` bash
roCohoZporation
```

### 6 - Output of The following code 

``` java
int a , b;
	for ( a=6 , b =4 ; a <=24;a = a+6){
    if (a % b ==0)
    break;
}
System.out.println(a);

```
### Output 
``` bash
12
```

### 7 - Output of The following code 

``` c++
#include <iostream>

int q(int x , int y){
    x = x * y ;
    return x < 50 ? (x) : (q(2,3));
}

int main()
{
    int result ;
    result = q(20,4);
    printf("%d\n" , result );
    
    

    return 0;
}
```
### Output 
``` bash
6
```
### 8 - Output of The following code 

``` c++
int main()
{
    char str[]={'z','i','o','s','a','u','b'};
    int indices[10]={4,3,6,1,0,2,5};
    char a , b;
    int i = 5;
    i = indices[i];
    b = str[i];
    i = i - indices[i];
    i = indices[4]+1;
    a=str[i];
   
    printf("%c %c" , a,b );      
    return 0;
}
```
### Output 
``` bash
i o

```
### 9 - Output of The following code 

``` c++

int main()
{
    char a[]={'a','o','o','k','u','b'};
    int index[10]={1,2,3,3,2,4,5};
    char i,j,k ,l;
    int n = 5;
    l = a[index[n]];
    n= index[n];
    k = a[n-1];
    n= n+index[n];
    i=a[n-1];
    n=index[1]-1;
    j=a[n];
    
   
    printf("%c %c %c %c" ,i,j,k,l );
    
    

    return 0;
}
```
### Output 
``` bash
b o k u

```
### 10 - Output of The following code 

``` java

 public int zoho(String[] args) {
        int nums[] = {1, 2, 3, 1, 1, 1};
        int ans = 0;

        for (int i = 0; i < nums.length; i++) { 
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] == nums[j]) 
                    ans++;
            }
        }

        return ans;
    }
```
### Output 
``` bash
6
```
### 11 - Output of The following code 

``` java

public String zoho(String[] strs) {
    if (strs.length == 0) 
        return "";  // Return an empty string if the array is empty
    
    String temp = strs[0];  // Start with the first string as the initial prefix
    
    for (int i = 1; i < strs.length; i++) {  // Loop through the other strings
        while (strs[i].indexOf(temp) != 0) {  // Check if the current string starts with `temp`
            temp = temp.substring(0, temp.length() - 1);  // Shorten `temp` if it doesn't match
            if (temp.isEmpty()) 
                return "";  // If `temp` is empty, no common prefix exists
        }
    }
    
    return temp;  // Return the longest common prefix found
}

```
### Input
``` bash
Input: ["flower", "flow", "flight"]
```
### Output 
``` bash
 "fl"
```
### 12 - Output of The following code 

``` java

class Solution {
    public int[] zoho(int[] nums) {
        int[] ans = new int[2 * nums.length];  // Create a new array with double the length
        
        for (int i = 0; i < nums.length; i++) {
            ans[i] = ans[i + nums.length] = nums[i];  // Copy each element to two positions
        }
        
        return ans;  // Return the concatenated array
    }
}


```
### Input
``` bash
Input:[1, 2, 1]
```
### Output 
``` bash
[1, 2, 1, 1, 2, 1]
```

