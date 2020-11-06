class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if stack and s[i] != stack[-1] and s[i].lower() == stack[-1].lower():
                stack.pop(-1)
            else:
                stack.append(s[i])

        return ''.join(stack)


Solution().makeGood('abBAcC')