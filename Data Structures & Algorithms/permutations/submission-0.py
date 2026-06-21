class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def dfs():
            if len(sol) == n:
                res.append(sol[:])

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    dfs()
                    sol.pop()

        dfs()
        return res