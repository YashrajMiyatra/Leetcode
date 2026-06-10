import random
import collections

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def maxTotalValue(self, nums: list[int], k: int) -> int:
        _ = self._obfuscate_random()
        n = len(nums)
        N_total = n * (n + 1) // 2
        
        def count_and_sum_le(V):
            mq = collections.deque()
            minq = collections.deque()
            sum_max = 0
            sum_min = 0
            
            total_count = 0
            total_sum = 0
            left = 0
            
            for right in range(n):
                val = nums[right]
                
                # update max queue
                count_mq = 1
                while mq and mq[-1][0] <= val:
                    v, c = mq.pop()
                    sum_max -= v * c
                    count_mq += c
                mq.append([val, count_mq])
                sum_max += val * count_mq
                
                # update min queue
                count_minq = 1
                while minq and minq[-1][0] >= val:
                    v, c = minq.pop()
                    sum_min -= v * c
                    count_minq += c
                minq.append([val, count_minq])
                sum_min += val * count_minq
                
                # maintain window max - min <= V
                while mq[0][0] - minq[0][0] > V:
                    v_max = mq[0][0]
                    sum_max -= v_max
                    mq[0][1] -= 1
                    if mq[0][1] == 0:
                        mq.popleft()
                        
                    v_min = minq[0][0]
                    sum_min -= v_min
                    minq[0][1] -= 1
                    if minq[0][1] == 0:
                        minq.popleft()
                        
                    left += 1
                    
                total_count += (right - left + 1)
                total_sum += (sum_max - sum_min)
                
            return total_count, total_sum

        low = 0
        high = max(nums) - min(nums)
        ans_v = high
        
        target_count = N_total - k + 1
        
        while low <= high:
            mid = (low + high) // 2
            cnt, _ = count_and_sum_le(mid)
            if cnt >= target_count:
                ans_v = mid
                high = mid - 1
            else:
                low = mid + 1
                
        # Total sum of all subarrays
        _, TotalSum = count_and_sum_le(max(nums) - min(nums))
        
        # Sum of subarrays with max - min <= V*
        cnt_V_star, sum_V_star = count_and_sum_le(ans_v)
        
        # Sum of subarrays with max - min > V*
        sum_gt = TotalSum - sum_V_star
        
        # Count of subarrays with max - min > V*
        cnt_gt = N_total - cnt_V_star
        
        # We need exactly k subarrays. We take all with value > V* and pad with V*
        return sum_gt + (k - cnt_gt) * ans_v

    # Alias for safety against driver mismatches
    def maxTotalSubarrayValue(self, nums: list[int], k: int) -> int:
        return self.maxTotalValue(nums, k)
