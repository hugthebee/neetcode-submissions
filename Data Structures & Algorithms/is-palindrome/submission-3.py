class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum()).lower()

        length = len(clean)

        i = 0
        j = length - 1
        print(clean)
        while i<j:
            if clean[i] != clean[j]:
                return False
            
            i+=1
            j-=1

        return True