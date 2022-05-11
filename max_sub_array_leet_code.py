#Input: [-2,1,-3,4,-1,2,1,-5,4],
#devide array with sub array 1. [-2 ], 2. [-2 1], 3.[-2 ,1,-3]..
#calculate sub_array's element's sum
# compair to get largest..
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution:
    def maxSubArray(nums):
        maxSub = nums[0]
        curSum = 0

        for i in nums:
            if curSum < 0:
                curSum = 0
            curSum += i
            maxSub = max(maxSub, curSum)

        return maxSub

    num = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(num))
