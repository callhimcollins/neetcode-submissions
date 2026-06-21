class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_digit = ''.join(str(x) for x in digits)
        add_one = int(str_digit) + 1
        return [int(x) for x in str(add_one)]