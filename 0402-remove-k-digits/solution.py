class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            # Maintain a monotonic increasing stack
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        # If we still have digits to remove, remove them from the end (since stack is sorted ascending)
        if k > 0:
            stack = stack[:-k]
            
        # Join the stack and strip leading zeros
        result = "".join(stack).lstrip('0')
        
        return result if result else "0"
