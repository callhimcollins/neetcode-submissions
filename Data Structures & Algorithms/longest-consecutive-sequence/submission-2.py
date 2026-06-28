class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest_seq = 0
        for num in sett:
            if num-1 not in sett:
                length_seq = 1
                next_num = num + 1
                while next_num in sett:
                    length_seq += 1
                    next_num += 1
                longest_seq = max(longest_seq, length_seq)
        
        return longest_seq
        

