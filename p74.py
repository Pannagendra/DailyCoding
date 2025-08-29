"""
Given two strings s and p. Find the smallest substring in s consisting of all the characters (including duplicates) of the string p. Return empty string in case no such substring is present.
If there are multiple such substring of the same length found, return the one with the least starting index.

Examples:

Input: s = "timetopractice", p = "toc"
Output: "toprac"
Explanation: "toprac" is the smallest substring in which "toc" can be found.

Sliding Window Approach

Character Counts: Use a dictionary/counter for p to know the required count for each character.

Expand Window: Use two pointers, move the right one to include enough characters to meet the required frequencies.

Shrink Window: Move the left pointer to make the window as small as possible while still containing all characters from p.

Track Minimum: Remember the smallest window observed that fits the requirements and its starting index.

Return Result: If no such window found, return ""; else return the substring.

"""

class Solution:
    def smallestWindow(self, s, p):
        from collections import Counter
        need = Counter(p)
        window = {}
        required = len(need)
        formed = 0
        l = 0
        res = (float('inf'), None, None)  # window length, left, right
        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                formed += 1
        
            # Try to contract window from left if all characters are present
            while l <= r and formed == required:
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
            
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
                
        if res[0] == float('inf'):
            return ""
        return s[res[1]:res[2]+1]
