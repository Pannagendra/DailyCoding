"""
You are given an array arr[] of size n, where arr[i] represents the number of soldiers in the i-th troop. You are also given an integer k. 
A troop is considered "lucky" if its number of soldiers is a multiple of k. 
Find the minimum total number of soldiers to add across all troops so that at least ⌈n / 2⌉ troops become lucky.
"""
def Soultion(object):
  def minSoldiers(self,arr,k):
    n = len(arr)
    costs=[]
    need=(n+1)//2
    for soldiers in arr:
      if soldier %k ==0:
        costs.append(0)
      else:
        costs.append(k-(soldier%k))
    costs.sort()
  return(sum(costs[:need]))
      
