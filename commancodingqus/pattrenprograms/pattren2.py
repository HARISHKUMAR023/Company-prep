n=5
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end="")
    for l in range(i):
        print("*" , end="")
    print()
#output
#*****
# ****
#  ***
#   **
#    *