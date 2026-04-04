class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char

        for i in range(len(newS)):
            if newS[i].lower() != newS[len(newS)-1-i].lower():
                return False

        return True