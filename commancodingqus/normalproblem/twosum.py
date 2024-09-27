nums = [2, 7, 11, 15]
target = 9
ans=[]
for i in range(len(nums)):
    if target -nums[i] in nums[i+1:len(nums)]:
        for j in range(len(nums)):
            if target-nums[i] == nums[j]:
                ans.append(i)
                ans.append(j)
                break
print(ans)
                