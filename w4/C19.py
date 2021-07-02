"""
17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        # Reference Dictionary
        ref = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        # Output
        self.res = []

        if len(digits)<1:
            return self.res

        # Helper function that appends next digit combinations
        def partsum(query):
            # If first digit
            if not self.res:
                for letter in ref[query]:
                    self.res.append(letter)
            # Second or later digits
            else:
                # Number of original elements in the res array
                n = len(self.res)
                for i in range(n):
                    # Take out the first n elements (original elements)
                    tmp = self.res.pop(0)
                    for letter in ref[query]:
                        # Append all combinations
                        self.res.append(tmp+letter)

        for num in digits:
            partsum(num)

        return self.res

"""
Runtime: 16 ms, faster than 76.62% of Python online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.4 MB, less than 66.60% of Python online submissions for Letter Combinations of a Phone Number.
"""