class Solution:
    def reverseVowels(self, s: str):
        all_vowels = []
        string_with_reversed_vowels = ""

        for i in s:
            if i in "oeiuaOEIUA":
                all_vowels.append(i)

        for i in s:
            if i in "oeiuaOEIUA":
                string_with_reversed_vowels += all_vowels.pop()
            else:
                string_with_reversed_vowels += i
        return string_with_reversed_vowels


s = Solution()
print(s.reverseVowels("hello"))  # holle
print(s.reverseVowels("leetcode"))  # leotcede
print(s.reverseVowels("aA"))  # Aa
