class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []

        def rec(cur_sum, potential, index):
            if cur_sum > target:
                return
            elif cur_sum == target:
                ans.append(potential[:])
                return
            
            for i in range(index, len(candidates)):
                num = candidates[i]
                if num == candidates[i - 1] and i > index:
                    continue
                potential.append(num)
                rec(cur_sum + num, potential, i + 1)
                potential.pop()

        
        candidates.sort()    
        rec(0, [], 0)

        return ans