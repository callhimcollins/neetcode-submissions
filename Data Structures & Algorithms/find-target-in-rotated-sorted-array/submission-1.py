class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        smallest = r

        l, r = 0, n-1
        while l <= r:
            mid = (l + r) // 2
            realmid = (mid + smallest) % n
            if nums[realmid] == target:
                return realmid
            elif nums[realmid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1