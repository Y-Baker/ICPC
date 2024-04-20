class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split(' ')[::-1]
        return ' '.join(filter(lambda x: x != '', arr))


s = Solution()
print(s.reverseWords("the sky is blue")) # "blue is sky the"
