"""
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        i = 0
        while i < len(s)-1:
            i += 1
            if s[i] == "[":
                l.append(i)
            elif s[i] == "]":
                j = l.pop()          
                try:
                    try:
                        num = int(s[j-3:j]) # 3 digit
                        prefix = s[:j-3]
                    except:
                        num = int(s[j-2:j]) # 2 digit
                        prefix = s[:j-2]
                except:
                    num = int(s[j-1]) # 1 digit
                    try:
                        prefix = s[:j-1] 
                    except:
                        prefix = ""                
                try:
                    suffix = s[i+1:]
                except:
                    suffix = ""
                s = prefix + num * s[j+1:i] + suffix
                i -= 3
        
        return s

"""
Runtime: 20 ms, faster than 43.14% of Python online submissions for Decode String.
Memory Usage: 13.6 MB, less than 54.92% of Python online submissions for Decode String.
"""


### reference code

def stacky(s):
    """
    When we hit an open bracket, we know we have parsed k for the contents of the bracket, so 
    push (current_string, k) to the stack, so we can pop them on closing bracket to duplicate
    the enclosed string k times.
    """
    stack = []
    current_string = ""
    k = 0
    
    for char in s:
        if char == "[":
            # Just finished parsing this k, save current string and k for when we pop
            stack.append((current_string, k))
            # Reset current_string and k for this new frame
            current_string = ""
            k = 0
        elif char == "]":
            # We have completed this frame, get the last current_string and k from when the frame 
            # opened, which is the k we need to duplicate the current current_string by
            last_string, last_k = stack.pop(-1)
            current_string = last_string + last_k * current_string
        elif char.isdigit():
            k = k * 10 + int(char) # Great Idea
        else:
            current_string += char
    
    return current_string