class Solution:
    # Solution 1.
    # def detectCapitalUse(self, word):
    #     if word.islower():
    #         return True
    #     elif word.istitle():
    #         return True
    #     elif word.isupper():
    #         return True
    #     else:
    #         return False

    # Solution 2.
    def detectCapitalUse(self, word):
        return (word.isupper() or word.islower() or word.istitle())


s = Solution()
print(s.detectCapitalUse("USA"))  # True
print(s.detectCapitalUse("leetcode"))  # True
print(s.detectCapitalUse("Google"))  # True
print(s.detectCapitalUse("FlaG"))  # False
