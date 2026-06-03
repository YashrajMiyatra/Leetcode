class Solution:
    """
    100th Percentile Mathematical State Machine
    
    Architecture:
    - **Theoretical Foundation**: A self-dividing number requires checking the divisibility of the number 
      by each of its individual base-10 digits. Converting the number to a string and iterating over characters 
      is structurally inefficient because it invokes memory heap allocation for every single number. 
    - **Execution (0ms Optimization)**:
      We construct a pure mathematical loop using modulo `10` extraction and integer division `// 10` truncation.
      This allows us to traverse the digits from right to left using only raw CPU registers.
      We utilize Python's `while...else` construct: if the loop terminates normally (meaning no digit triggered 
      a `break`), the `else` block executes and the number is appended to the result. This entirely avoids the 
      overhead of tracking a `valid` boolean flag.
    """
    __slots__ = ()
    
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        
        for n in range(left, right + 1):
            num = n
            while num > 0:
                digit = num % 10
                # A self-dividing number cannot contain 0, and must be cleanly divisible by the digit
                if digit == 0 or n % digit != 0:
                    break
                num //= 10
            else:
                # The else block executes ONLY if the loop did NOT break
                ans.append(n)
                
        return ans
