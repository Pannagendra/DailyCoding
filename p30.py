"""
Given a string s in Roman number format, your task is to convert it to an integer. Various symbols and their values are given below.
Note: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
"""
class Solution:
    def romanToDecimal(self, s):
      roman_values= { 'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
      total =0
      prev_values =0
      for char in reversed(s):
        value = roman_values[char]
        if val>= prev_value:
          total+=value
        else:
          total-=value
        prev_val =value
      return total
