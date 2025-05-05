class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        count_map = defaultdict(int)
        count_map[0] = 1
        odd_count = 0
        result = 0
        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            result += count_map[odd_count - k]
            count_map[odd_count] += 1
        return result
#the time complexity is O(n) and the space complexity is O(n)