class Solution:
    def toGoatLatin(self, S):
        arr = S.strip().split()
        for i in range(0, len(arr)):
            if arr[i][0] in "aeoiuAEOIU":
                arr[i] = arr[i] + "ma"
            elif arr[i][0] not in "aeoiuAEOIU":
                arr[i] = arr[i][1:] + arr[i][0] + "ma"
            arr[i] = arr[i] + "a" * (i + 1)
        return " ".join(arr)


s = Solution()
seq = "I speak Goat Latin"
print(s.toGoatLatin(seq))  # "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
