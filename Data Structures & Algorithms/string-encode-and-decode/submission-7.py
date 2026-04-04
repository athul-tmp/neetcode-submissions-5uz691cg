class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        output = ""
        sizes = []
        for string in strs:
            sizes.append(len(string))

        for size in sizes:
            output += str(size)
            output += ","

        output += "#"

        for string in strs:
            output += string
        return output

    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        output = []
        sizes = []
        newS = ""
        num = ""

        for i in range(len(s)):
            if s[i] == "#":
                newS = s[i+1::]
                break
            elif s[i] == ",":
                sizes.append(int(num))
                num = ""
                continue
            else:
                num += s[i]
        
        for size in sizes:
            word = ""
            for i in range(size):
                word += newS[i]
            output.append(word)
            newS = newS[size::]

        return output


        

