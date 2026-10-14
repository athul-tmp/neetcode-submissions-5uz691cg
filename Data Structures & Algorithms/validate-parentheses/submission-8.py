class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")" : "(" , "]" : "[" , "}" : "{"}
        
        stack = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False
        
