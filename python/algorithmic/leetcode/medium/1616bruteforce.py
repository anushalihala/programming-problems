class Solution:
    def isPalindrome(self, s):
        length = len(s)
        for i in range(0, int(length/2)):
            if s[i] != s[length-1-i]:
                return False
        return True

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.checkPalindromeFormationHelper(a,b) or self.checkPalindromeFormationHelper(b,a)

    def checkPalindromeFormationHelper(self, a: str, b: str) -> bool:
        length = len(a)
        for i in range(0,length):
            if self.isPalindrome(a[:i]+b[i:]):
                print(i, a[:i]+b[i:])
                return True

        return False

if __name__ == '__main__':
    # a="pvhmupgqeltozftlmfjjde"
    # b="yjgpzbezspnnpszebzmhvp"
    a="aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd"
    b="uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"
    ans = Solution().checkPalindromeFormation(a,b)
    print(ans)
    # print(Solution().palindromicIndex("baelss"))