class Solution:
    # sort and binary search
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        
        for i, n in enumerate(nums):
            # skip to next iter if this elem equal to the last
            if i > 0 and n == nums[i-1]:
                continue
            
            # left right pointers
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum == 0:
                    output.append([n, nums[l], nums[r]])
                    # update the pointer
                    l += 1
                    while nums[l-1] == nums[l] and l<r:
                        l+=1
                elif threeSum >0:
                    r-=1
                elif threeSum <0:
                    l+=1
        return output