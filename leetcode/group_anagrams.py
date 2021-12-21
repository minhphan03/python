class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # algorithm by towardsdatascience
        
        # construct a map
        items={}
        
        for s in strs:
            key = "".join(sorted(s))
            if key not in items:
                items[key]=[]
            
            items[key].append(s)
        
        return[[x for x in items[key]] for key in items.keys()]
        
        
        
