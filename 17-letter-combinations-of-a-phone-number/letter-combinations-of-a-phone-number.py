class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        letters = []
        for digit in digits:
            letters.append(numbers[digit])
        result = []

        def combinationsLetters(digits,letters,idx,result,combi):
            if len(combi)==len(digits):
                result.append("".join(combi))
                return 
            for letter in letters[idx]:
                combi.append(letter)
                combinationsLetters(digits,letters,idx+1,result,combi)
                combi.pop()
        
        combinationsLetters(digits,letters,0,result,[])
        return result