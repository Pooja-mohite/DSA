class Solution(object):
    def letterCombinations(self, digits):
        
        phone = {
            "2": "abc",
            "3": "def",
            "4":"ghi",
            "5":"jkl",
            "6": "mno",
            "7" : "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = [""]
        for digit in digits:
            new_result = []
            for combination in result:
                for ch in phone[digit]:
                    new_result.append(combination+ch)
            result = new_result
        return result
        
        