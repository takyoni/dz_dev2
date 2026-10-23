# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in pairs:
                if not stack or stack[-1] != pairs[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0


# O(n) - один проход по строке, push/pop за O(1)
# стек потому что закрывающая скобка относится к последней открытой, это LIFO

print(Solution().isValid("()"))      # True
print(Solution().isValid("()[]{}"))  # True
print(Solution().isValid("(]"))      # False
print(Solution().isValid("([])"))    # True
print(Solution().isValid("([)]"))    # False
