class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist = []
        i = 0
        while i < len(strs):
            list = []
            j = i+1
            while j < len(strs):
                if i != len(strs):
                    if sorted(strs[i]) == sorted(strs[j]):
                        list.append(strs[j])
                        strs.pop(j)
                        j -= 1
                j += 1

            list.append(strs[i])
            sublist.append(list)
            i += 1

        return sublist