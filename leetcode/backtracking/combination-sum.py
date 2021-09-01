class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        solution = set()

        def combinedSum(block, candidates, target, solutions):
            if sum(block) == target:
                new_copy = []
                new_copy.extend(sorted(block))
                solutions.add(tuple(new_copy))
            elif sum(block) > target:
                return
            for num in candidates:
                block.append(num)
                combinedSum(block, candidates, target, solutions)
                block.pop()
        combinedSum([],candidates,target,solution)
        return [list(x) for x in solution]
