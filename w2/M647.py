"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.


1 <= s.length <= 1000
s consists of lowercase English letters.
"""

# 남의 풀이인데, 아주 잘해서 이거로 업로드
class Solution:
    def countSubstrings(self, s):
        def count_palindrome(s, left, right):
            count = 0
            while 0 <= left and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        ans = 0
        for i in range(len(s)):
            # 홀수
            ans += count_palindrome(s, i, i)
            # 짝수
            ans += count_palindrome(s, i, i+1)
        return ans

"""
Runtime: 120 ms, faster than 89.08% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 14.2 MB, less than 86.21% of Python3 online submissions for Palindromic Substrings.
"""