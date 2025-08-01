"""
You are given an array of strings arr[], where each arr[i] consists of lowercase english alphabets. You need to find the number of balanced strings in arr[] which can be formed by concatinating one or more contiguous strings of arr[].
A balanced string contains the equal number of vowels and consonants. 
"""
class Solution:
    def countBalanced(self, arr):
        vowels = set('aeiou')
        n = len(arr)
        
        # Build prefix sums for (vowel_count - consonant_count)
        diff_count = [0] * (n + 1)  # diff_count[i] = diff for arr[0:i]
        for i in range(n):
            v, c = 0, 0
            for ch in arr[i]:
                if ch in vowels:
                    v += 1
                else:
                    c += 1
            diff_count[i+1] = diff_count[i] + (v - c)
        
        # Use hashmap to count the frequency of each prefix diff seen so far
        freq = {}
        result = 0
        for d in diff_count:
            if d in freq:
                result += freq[d]
            # increment freq for this diff
            freq[d] = freq.get(d, 0) + 1
        return result
