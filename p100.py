"""
Given a board of dimensions n × m that needs to be cut into n*m squares. The cost of making a cut along a horizontal or vertical edge is provided in two arrays:

    x[]: Cutting costs along the vertical edges (length-wise).
    y[]: Cutting costs along the horizontal edges (width-wise).

Find the minimum total cost required to cut the board into squares optimally.
"""
class Solution:
    def minCost(self, n, m, x, y):
        # Sort x and y in descending order
        x.sort(reverse=True)
        y.sort(reverse=True)
        
        # Initialize pointers, results, and pieces counts
        i = 0
        j = 0
        horizontal_pieces = 1
        vertical_pieces = 1
        total_cost = 0
        
        # Greedily make cuts along the most expensive remaining edge
        while i < len(x) and j < len(y):
            if x[i] >= y[j]:
                total_cost += x[i] * horizontal_pieces
                vertical_pieces += 1
                i += 1
            else:
                total_cost += y[j] * vertical_pieces
                horizontal_pieces += 1
                j += 1
        
        # Finish remaining vertical cuts
        while i < len(x):
            total_cost += x[i] * horizontal_pieces
            i += 1
        
        # Finish remaining horizontal cuts
        while j < len(y):
            total_cost += y[j] * vertical_pieces
            j += 1
        
        return total_cost
