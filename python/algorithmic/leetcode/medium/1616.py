# 1616. Split Two Strings to Make Palindrome
# https://leetcode.com/problems/split-two-strings-to-make-palindrome/

class Solution:
    def isPalindrome(self, s):
        length = len(s)
        for i in range(0, int(length/2)):
            if s[i] != s[length-1-i]:
                return False
        return True

    def palindromicIndex(self, s):
        length = len(s)
        index = 0
        for i in range(0, int(length / 2)):
            if s[i] != s[length - 1 - i]:
                index = i + 1
        return index

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        indexA = self.palindromicIndex(a)
        if indexA == 0:
            return True
        indexB = self.palindromicIndex(b)
        if indexB == 0:
            return True

        i = self.checkPalindromeFormationHelper(a,b)
        if indexA<=i or indexB<=i:
            return True
        i = self.checkPalindromeFormationHelper(b,a)
        if indexA<=i or indexB<=i:
            return True
        return False

    def checkPalindromeFormationHelper(self, a: str, b: str) -> bool:
        length = len(a)
        b_rev = list(reversed(b))
        for i in range(0,length):
            if a[i] != b_rev[i]:
                break
        return i

if __name__ == '__main__':
    # a="pvhmupgqeltozftlmfjjde"
    # b="yjgpzbezspnnpszebzmhvp"
    a="aejbaalflrmkswrydwdkdwdyrwskmrlfqizjezd"
    b="uvebspqckawkhbrtlqwblfwzfptanhiglaabjea"
    ans = Solution().checkPalindromeFormation(a,b)
    print(ans)
    # print(Solution().palindromicIndex("baelss"))