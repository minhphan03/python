class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #attempt solution by mguthrie45
        
        lett = {"2":["a","b","c"],
               "3":["d","e","f"],
               "4":["g","h","i"],
               "5":["j","k","l"],
               "6":["m","n","o"],
               "7":["p","q","r","s"],
               "8":["t","u","v"],
               "9":["w","x","y","z"]}
        
        result=[]
        
        def backtrack(digits, combo, idx):
            #prevent to go pass the digit limit
            if len(combo)==len(digits):
                if len(combo) != 0:
                    #join the letters in the combo together
                    result.append(''.join(combo[::]))
                return
            
            dig = digits[idx]
            
            for char in lett[dig]:
                combo.append(char)
                backtrack(digits, combo, idx+1)
                combo.pop()
        
        backtrack(digits, [], 0)
        
        return result
                
