class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        count_map = dict()
        n = len(s)
        j,ret = 0,0
        for i in xrange(n):
            count_map[s[i]] = count_map.get(s[i], 0) + 1
            while count_map[s[i]] > 1:
                count_map[s[j]] -= 1
                j += 1
            ret = max(ret, i - j +1)
            print i, j, ret
        return ret

#Time complexity : O(2n) = O(n)O(2n)=O(n). In the worst case each character will be visited twice by ii and jj.
#Space complexity : O(min(m, n))O(min(m,n)). Same as the previous approach. We need O(k)O(k) space for the sliding window, where kk is the size of t#he Set. The size of the Set is upper bounded by the size of the string nn and the size of the charset/alphabet mm.

        #Optimized Solution
        n = len(s)
        ans = 0
        mp = {}
        i = 0
        for j in xrange(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
        return ans

"""
Time complexity : O(n) Index jj will iterate n times.
Space complexity (HashMap) : O(min(m, n)). Same as the previous approach.
"""