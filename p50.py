"""
You are given an array citations[], where each element citations[i] represents the number of citations received by the ith paper of a researcher. 
You have to calculate the researcher’s H-index.
The H-index is defined as the maximum value H, such that the researcher has published at least H papers, 
and all those papers have citation value greater than or equal to H.
"""
class Soluetion(object):
  def reasercher(self,citations):
    h = 0
    citations.sort(reverse=True)
    for i,c in enumerate(citations):
      if c>= i+1:
        h=i+1
      else:
        break
    return h
