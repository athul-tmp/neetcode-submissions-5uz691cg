class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            S = str(sorted(str(s)))
            if S not in d:
                d[S] = [s]
            else: 
                d[S].append(s)


        ans = []
        for k,v in d.items():
            ans.append(v)

        return ans