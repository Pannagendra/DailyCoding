"""
Given a row-wise sorted matrix mat[][] of size n*m, where the number of rows and columns is always odd. Return the median of the matrix.
"""
class Solution:
    def median(self, mat):
    	# code here 
    	import bisect
    	n,m = len(mat), len(mat[0])
    	min_val = min(row[0] for row in mat)
    	max_val = max(row[-1] for row in mat )
    	
    	desired = (n*m+1)//2
    	
    	while min_val < max_val:
    	    mid = (min_val+max_val) //2
    	    
    	    count =0
    	    for row in mat:
    	        count+= bisect.bisect_right(row,mid)
    	    if count<desired:
    	        min_val =mid+1
    	    else:
    	        max_val =mid
    	return min_val
