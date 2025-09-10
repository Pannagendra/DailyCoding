"""
On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

    There are n languages numbered 1 through n,
    languages[i] is the set of languages the i​​​​​​th​​​​ user knows, and
    friendships[i] = [u​​​​​​i​​​, v​​​​​​i] denotes a friendship between the users u​​​​​​​​​​​i​​​​​ and vi.

You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.
Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z. 
"""
class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        cncon = set()
        for friendship in friendships:
            mp = {}
            conm = False
            for lan in languages[friendship[0] - 1]:
                mp[lan] = 1
            for lan in languages[friendship[1] - 1]:
                if lan in mp:
                    conm = True
                    break
            if not conm:
                cncon.add(friendship[0] - 1)
                cncon.add(friendship[1] - 1)

        max_cnt = 0
        cnt = [0] * (n + 1)
        for friendship in cncon:
            for lan in languages[friendship]:
                cnt[lan] += 1
                max_cnt = max(max_cnt, cnt[lan])

        return len(cncon) - max_cnt
