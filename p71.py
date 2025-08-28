"""
Given a binary array arr[] containing only 0s and 1s and an integer k, you are allowed to flip at most k 0s to 1s. 
Find the maximum number of consecutive 1's that can be obtained in the array after performing the operation at most k times.


"""
class Soultion(object):
  def maxOnes(self,arr,k):
    left =0 
    max_length=0
    zero_count=0
    for right in range(len(arr)):
      if arr[right] == 0:
        zero_count += 1

      while zero_count > k:
        zero_count-=1
      left+=1

      max_length = max(max_length, right -left+1)
    return max_length
