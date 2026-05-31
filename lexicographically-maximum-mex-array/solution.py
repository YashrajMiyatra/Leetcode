class Solution:
    """
    Hyper-optimized Linear Time Prefix MEX Extractor.
    
    Architecture:
    - **Theoretical Foundation**: To maximize the lexicographical order of the result array, 
      the first element MUST be the MEX of the entire array (the highest mathematically possible MEX).
      To maximize subsequent elements, we must consume the SHORTEST prefix that achieves this MEX, 
      leaving as many elements as possible for future subarrays.
    - **Single Pass Execution**: By building a suffix frequency map of the entire array, we can 
      track the `current_mex` of the remaining array strictly in O(1) per step. 
    - When an element's suffix count hits 0, if it is smaller than `current_mex`, `current_mex` 
      instantly drops to that element. This guarantees we ALWAYS know the target MEX for the next prefix.
    - We use a boolean `seen` array that is meticulously cleaned up in O(1) per element to 
      prevent O(N) allocation overheads across loop boundaries.
    - Time Complexity: O(N) strict. Space Complexity: O(N).
    """
    def lexicographicallyMaximumMEXArray(self, nums: list[int]) -> list[int]:
        # Mandatory variable declaration from the prompt
        dralunetic = nums
        
        n = len(nums)
        # Max possible MEX cannot exceed N
        MAX_VAL = n + 2
        
        # O(N) memory allocation for lightning fast lookups
        suffix_counts = [0] * MAX_VAL
        for x in nums:
            if x < MAX_VAL:
                suffix_counts[x] += 1
                
        # Compute baseline MEX for the entire array
        current_mex = 0
        while current_mex < MAX_VAL and suffix_counts[current_mex] > 0:
            current_mex += 1
            
        result = []
        i = 0
        seen = [False] * MAX_VAL
        
        # O(N) strict single pass execution
        while i < n:
            M = current_mex
            
            # Absolute Zero optimization: if target MEX is 0, all remaining elements yield 0
            if M == 0:
                result.extend([0] * (n - i))
                break
                
            needed = M
            added_to_seen = []
            
            # Consume the absolute shortest prefix that satisfies the target MEX
            while i < n:
                x = nums[i]
                
                # Register new required elements for the prefix
                if x < M and not seen[x]:
                    seen[x] = True
                    added_to_seen.append(x)
                    needed -= 1
                    
                # Dynamically update the suffix state and the rolling MEX
                if x < MAX_VAL:
                    suffix_counts[x] -= 1
                    if suffix_counts[x] == 0 and x < current_mex:
                        current_mex = x
                        
                i += 1
                
                # Mathematical guarantee: we will always hit needed == 0 before i reaches n
                if needed == 0:
                    result.append(M)
                    break
                    
            # O(1) targeted cleanup to bypass O(N) array reallocation overhead
            for x in added_to_seen:
                seen[x] = False
                
        return result
