class Solution:
    def valid_number(self, s):
        try:
            float(s)
            return True
        except:
            return False


s = Solution()
print(s.valid_number("0"))  # True
print(s.valid_number(" 0.1 "))  # True
print(s.valid_number("abc"))  # False
print(s.valid_number("1 a"))  # False
print(s.valid_number("2e10"))  # True
print(s.valid_number(" -90e3   "))  # True
print(s.valid_number(" 1e"))  # False
print(s.valid_number("e3"))  # False
print(s.valid_number(" 6e-1"))  # True
print(s.valid_number(" 99e2.5 "))  # False
print(s.valid_number("53.5e93"))  # True
print(s.valid_number(" --6 "))  # False
print(s.valid_number("-+3"))  # False
print(s.valid_number("95a54e53"))  # False
