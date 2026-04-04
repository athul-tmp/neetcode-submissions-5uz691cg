class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""
        for s in strs:
            res += s
            res += "-"

        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        word = ""
        for char in s:
            if char != "-":
                word += char
            else:
                res.append(word)
                word = ""

        return res

        