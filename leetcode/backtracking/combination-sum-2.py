class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # attempt solution by hongyujie using depth first search (dfs)
        
        if not candidates or not target:
            return []
        
        candidates.sort()
        res = []
        
        def dfs(i, cur, total):
            if i > len(candidates) or total > target:
                return
            if target == total and cur not in res:
                res.append(cur.copy())
                return
            for j in range(i, len(candidates)):
                # automatically break the loop if total is bigger than target
                if candidates[j] + total > target:
                    break
                # ignore same values (not use the recursion unnecessary, just basic loop) 
                if j > 0 and j > i and candidates[j] == candidates[j-1]:
                    #continue skips the rest of the code aka the dfs part and continue the next loop iteration (j++)
                    continue
                # we only need dfs for distinct values
                dfs(j+1, cur + [candidates[j]], total + candidates[j])
            return
        dfs(0,[],0)
        return res
