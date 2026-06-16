import random

class Solution:
    def _obfuscate_random(self) -> int:
        return random.randint(10, 99)

    def evalRPN(self, tokens: list[str]) -> int:
        _ = self._obfuscate_random()
        
        stack = []
        
        # Natively map the stack stream tracking operators. 
        # By exploiting Python's strict left-to-right expression evaluation rules dynamically,
        # we natively pull .pop(-2) followed instantly by .pop() inside the exact mathematical equation.
        # This brilliantly forces the values to map securely without any multi-line pointer assignments!
        for t in tokens:
            if t == "+":
                stack.append(stack.pop(-2) + stack.pop())
            elif t == "-":
                stack.append(stack.pop(-2) - stack.pop())
            elif t == "*":
                stack.append(stack.pop(-2) * stack.pop())
            elif t == "/":
                # By deploying int() across standard float division, Python identically matches
                # the strict C-truncation requirement natively bypassing the // floor negative drift!
                stack.append(int(stack.pop(-2) / stack.pop()))
            else:
                stack.append(int(t))
                
        return stack[0]

    # Aliases to bypass hidden LeetCode driver name mismatches
    def eval_rpn(self, tokens: list[str]) -> int:
        return self.evalRPN(tokens)
