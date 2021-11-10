```py
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recursion - backtracking?
        # tutorial by GeeksToGeeks
        a = []
        
        def pm(n, a, l, r):
            if (l == r):
                a.append(n[:])
            else:
                for i in range(l, r+1):
                    #swap
                    n[l], n[i] = n[i], n[l]
                    #recursion
                    pm(n, a, l+1, r)
                    #swap back
                    n[l], n[i] = n[i], n[l]
        
        pm(nums, a, 0, len(nums)-1)
        return a
```
![demonstration of algorithm](https://media.geeksforgeeks.org/wp-content/cdn-uploads/NewPermutation.gif)
