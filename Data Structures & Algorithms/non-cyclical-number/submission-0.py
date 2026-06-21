class Solution:
    def isHappy(self, n: int, seen=None) -> bool:
        if seen is None:
            seen = set()
            
        if n == 1:
            return True

        if n in seen:
            return False
        
        seen.add(n)
        next_n = sum(int(x) ** 2 for x in str(n))
        return self.isHappy(next_n, seen)