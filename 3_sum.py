def threeSum(nums):
    ans = []
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                print(i,j,k)

                if  nums[i]+nums[j]+nums[k] == 0:
                    ans.append([nums[i],nums[j],nums[k]])
    
    # print(ans_set)
    return ans

nums = [0,0,0]

print(threeSum(nums))
print([0,1] , [1,0])


