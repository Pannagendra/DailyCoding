"""
There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

Given a string text of words separated by a single space (no leading or trailing spaces) and a 
string brokenLetters of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.
"""
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)   # for O(1) lookup
        words = text.split()
        count = 0
        
        for w in words:
            if not any(ch in broken for ch in w):
                count += 1
        
        return count
