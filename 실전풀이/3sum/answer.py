# def threeSum(nums):
#         nums.sort()
#         n,res=len(nums),[]
#         for i in range(n-2):
#             if i and nums[i-1]==nums[i]:
#                 print('continue: ', i)
#                 continue
#             for j in range(i+1,n-1):
#                 x=nums[i]+nums[j]
#                 if -x in nums[j+1:]:
#                     res.append([nums[i],nums[j],-x])
#         return res

class Solution:
     def threeSum(self, nums: List[int]) -> List[List[int]]:
         nums.sort()
         n,hash,res=len(nums),{},[]
         for i in range(n-1):
             if i and nums[i]==nums[i-1]: continue
             for j in range(i+1,n):
                 x=nums[j]
                 c=hash.get(x)
                 if c:
                     res.append(c+[x])
                     del hash[x]
                 elif i+1<j and nums[j-1]==x:
                     continue
                 else:
                     hash[-(nums[i]+nums[j])]=[nums[i],nums[j]]
             hash.clear()
         return res

print(threeSum([-1,0,1,2,-1,-4]))