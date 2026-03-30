class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for s in strs:
            sortedstr = "".join(sorted(s))
            if sortedstr in ans:
                ans[sortedstr].append(s)
            else:
                ans[sortedstr] = [s]

        return list(ans.values())