# Write a function to find the first non-repeating character in a given string.
# If all characters repeat, return a special value like None or -1.


def onrep(arr):
  my={}
  for i in arr:
      my[i]=my.get(i,0)+1
#   print(my)
  for j , k in my.items():
      if k == 1:
          return j
  return -1
print(onrep("aabb"))