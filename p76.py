"""
A celebrity is a person who is known to all but does not know anyone at a party. 
A party is being organized by some people. 
A square matrix mat[][] of size n*n is used to represent people at the party such that if an element of row i and column j 
is set to 1 it means ith person knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.

The celebrity problem is based on the condition that the celebrity is someone known by everyone else at the party but who does not know anyone themselves.
Key Points of the Problem:

    A celebrity is known by all other people.

    The celebrity knows no one at the party.

    The problem is represented by an n x n matrix where element mat[i][j] = 1 means person i knows person j.

Algorithm and Logic:

    Candidate Selection (Elimination Phase):

        Start by assuming the first person (index 0) is a celebrity candidate.

        Compare the candidate with each person i from 1 to n-1.

        If the candidate knows i (mat[candidate][i] == 1), then the candidate cannot be the celebrity, so update the candidate to i.

        If the candidate does not know i, continue checking with next i.

        By the end of this loop, we get a single candidate who might be a celebrity.

    Verification Phase:

        Verify the candidate by checking two conditions for every other person i:

            Candidate should not know i — mat[candidate][i] must be 0 for all i != candidate.

            Everyone else should know the candidate — mat[i][candidate] must be 1 for all i != candidate.

        If either condition fails for any i, return -1 indicating there is no celebrity.

    Return:

        If the candidate passes verification, return their index.

Why it works efficiently:

    Every time you find that candidate knows someone, candidate is eliminated, so by the end only one candidate remains.

    Verification is done with a linear scan to confirm the candidate truly satisfies celebrity criteria.

    Time complexity is O(n)O(n) because each person is checked only a constant number of times.

    Space complexity is O(1)O(1) since no extra data structures are required.

This method cleverly reduces the problem from a naive O(n2)O(n2) approach to a linear O(n)O(n) solution by systematic elimination and verification.


"""


class Solution:
    def celebrity(self, mat):
        n = len(mat)
        # Step 1: Find candidate
        candidate = 0
        for i in range(1, n):
            if mat[candidate][i] == 1:  # candidate knows i, eliminate candidate
                candidate = i
        # Step 2: Verify candidate
        for i in range(n):
            if i != candidate:
                # Candidate should not know i and i should know candidate
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1
        return candidate
