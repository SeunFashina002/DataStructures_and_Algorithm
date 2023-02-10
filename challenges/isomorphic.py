class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        iso_map = {}
        for s1, t1 in zip(s,t):
            if s1 not in iso_map:
                iso_map[s1] = t1
            elif iso_map[s1] != t1:
                return False
        return len(set(iso_map.values())) == len(iso_map.values())

sol = Solution()
print(sol.isIsomorphic('add', 'egg'))
