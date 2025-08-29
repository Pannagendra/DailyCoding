"""
Alice and Bob are playing a turn-based game on a field, with two lanes of flowers between them. 
There are x flowers in the first lane between Alice and Bob, and y flowers in the second lane between them.

The game proceeds as follows:

    Alice takes the first turn.
    In each turn, a player must choose either one of the lane and pick one flower from that side.
    At the end of the turn, if there are no flowers left at all, the current player captures their opponent and wins the game.

Given two integers, n and m, the task is to compute the number of possible pairs (x, y) that satisfy the conditions:

    Alice must win the game according to the described rules.
    The number of flowers x in the first lane must be in the range [1,n].
    The number of flowers y in the second lane must be in the range [1,m].

Return the number of possible pairs (x, y) that satisfy the conditions mentioned in the statement.



Explanation

    There are n×mn×m total pairs (x,y)(x,y).

Half of these pairs have x+yx+y odd, and half have x+yx+y even, because:

    For each value of xx, half of the yy values will make x+yx+y odd and half will make it even (except possibly one extra in case both nn and mm are odd, but integer division automatically handles this).

        For example, fixing xx as odd, yy must be even for x+yx+y to be odd, and vice versa.

    Thus, the total number of winning pairs for Alice is simply the floor division of the total pairs by 2:

Alice’s winning pairs=m*n//2

    This matches the more explicit formula derived previously, but is simpler because it condenses all cases (even and odd counts) into one succinct expression.

Relation to Previous Formula

    The more general formula was:
        x_odd = (n + 1) // 2
        x_even = n // 2
        y_odd = (m + 1) // 2
        y_even = m // 2
        return x_odd * y_even + x_even * y_odd

    For any integer n,m this always simplifies mathematically to (m×n)//2 using integer properties.

"""
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m * n) // 2
