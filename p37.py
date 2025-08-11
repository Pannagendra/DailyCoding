"""
Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.

You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.


Step-by-step plan

    Extract powers

        For each set bit in n (binary representation), append 2^bit_position to the array.

        Sort ascending (though from bit scanning from LSB to MSB already gives ascending order).

    Prefix product for fast range queries

        Precompute prefix[i] = product of powers[0..i] mod M.

        For query [l, r]:

            If l == 0: answer = prefix[r]

            Else: answer = (prefix[r] * inv(prefix[l-1])) % M

                Here inv is modular inverse (use pow(x, M-2, M) since M is prime).

    Modulo

        M = 10^9 + 7

"""

class Solution(object):
  def productQueries(self,n,queries):
    MOD = 10**9+7
    exps =[]
    bit=0
    temp=n
    while temp:
      if temp & 1:
        exps.append(1 << bit)
      bit+=1
      temp>>1
    prefix = [0] * len(exps)
    prefix[0] = exps[0] % MOD
    for i in range(1,len(exps)):
      prefix[i] = (prefix[i-1] + exps[i] ) % MOD
    res=[]
    for l,r in enumerate(queries):
      if l==0:
        res.append(prefix[r])
      else:
        res.append((prefix[r] * pow(prefix[l-1], MOD-2, MOD)) % MOD) #res.append(prefix[r]*pow((prefix[i-1] + exps[i] ) % MOD))
    return res


    
