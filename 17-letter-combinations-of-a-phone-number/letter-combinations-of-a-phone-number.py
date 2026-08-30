class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # numbers = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        # letters = []
        # for digit in digits:
        #     letters.append(numbers[digit])
        # combi_len = len(digits)
        # result = []

        # def combinationsLetters(combi_len,letters,idx,result,combi):
        #     if len(combi)==combi_len:
        #         result.append("".join(combi))
        #         return 
        #     for letter in letters[idx]:
        #         combi.append(letter)
        #         combinationsLetters(combi_len,letters,idx+1,result,combi)
        #         combi.pop()
        
        # combinationsLetters(combi_len,letters,0,result,[])
        # return result

        a = {"1":"",
          "2":"abc",
          "3":"def",
          "4":"ghi",
          "5":"jkl",
          "6":"mno",
          "7":"pqrs",
          "8":"tuv",
          "9":"wxyz"}
        
        result = [""]  

        for i in digits:
            result = [x+y for x in result for y in a[i]]

        return result    