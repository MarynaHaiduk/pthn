class Solution:
    def reverseOnlyLetters(self, S):
        letters = []
        reversed_string = ""

        for i in S:
            if i.isalpha():
                letters.append(i)
        for i in S:
            if i.isalpha():
                reversed_string += letters.pop()
            else:
                reversed_string += i
        return reversed_string


# Tests
s = Solution()
print(s.reverseOnlyLetters("ab-cd"))  # dc-ba
print(s.reverseOnlyLetters("a-bC-dEf-ghIj"))  # j-Ih-gfE-dCba
print(s.reverseOnlyLetters("Test1ng-Leet=code-Q!"))  # Qedo1ct-eeLg=ntse-T!
