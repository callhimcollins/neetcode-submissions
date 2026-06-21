class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_nums = [0] * n
        r_nums = [0] * n

        l_val = 1
        r_val = 1

        i = 0
        while i < n:
            j = -i - 1
            l_nums[i] = l_val
            r_nums[j] = r_val
            
            l_val *= nums[i]
            r_val *= nums[j]



            i += 1
        
        return [l * r for l, r in zip(l_nums, r_nums)]