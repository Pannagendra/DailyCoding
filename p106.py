"""
You are given an array of strings arr[] that represents a valid arithmetic expression written in Reverse Polish Notation (Postfix Notation). 
Your task is to evaluate the expression and return an integer representing its value.

Note: A postfix expression is of the form operand1 operand2 operator (e.g., "a b +"). 
And the division operation between two integers always computes the floor value, i.e floor(5 / 3) = 1 and floor(-5 / 3) = -2.
It is guaranteed that the result of the expression and all intermediate calculations will fit in a 32-bit signed integer.
"""
class Solution:
    def evaluatePostfix(self, arr):
        stack = []

        for token in arr:
            if token.lstrip("-").isdigit():
                stack.append(int(token))
            else:
                # Additional check for sufficient stack size
                if len(stack) < 2:
                    return 0  # or raise error/message
                b = stack.pop()
                a = stack.pop()
                
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(a // b)
                elif token == '^':
                    stack.append(pow(a, b))
                else:
                    # Unknown operator, optionally handle gracefully
                    return 0  # or raise error/message
        return stack[0] if stack else 0
