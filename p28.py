"""
Given a single string s, the task is to check if it is a palindrome sentence or not.
A palindrome sentence is a sequence of characters, such as word, phrase, or series of symbols that reads the same backward as
forward after converting all uppercase letters to lowercase and removing all non-alphanumeric characters (including spaces and punctuation).
"""
class Solution:
    def isPalinSent(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Convert to lowercase
        s = s.lower()
        # Filter out non-alphanumeric characters
        filtered_chars = [ch for ch in s if ch.isalnum()]
        
        # Check if filtered list is the same forwards and backwards
        return filtered_chars == filtered_chars[::-1]
