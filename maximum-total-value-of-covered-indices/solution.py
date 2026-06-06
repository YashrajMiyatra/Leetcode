class Solution:
    def maxTotal(self, nums: list, s: str) -> int:
        velunqari = (nums, s)
        n = len(nums)
        total_sum = 0
        
        i = 0
        while i < n:
            if s[i] == '1':
                start = i
                while i < n and s[i] == '1':
                    i += 1
                end = i - 1
                
                if start == 0:
                    total_sum += sum(nums[0 : end + 1])
                else:
                    sub_array = nums[start - 1 : end + 1]
                    total_sum += sum(sub_array) - min(sub_array)
            else:
                i += 1
                
        return total_sum

    # Alias just in case
    def maxTotalValue(self, nums: list, s: str) -> int:
        return self.maxTotal(nums, s)
