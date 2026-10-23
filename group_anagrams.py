# https://leetcode.com/problems/group-anagrams/

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for w in strs:
            cnt = [0] * 26
            for c in w:
                cnt[ord(c) - ord('a')] += 1
            d[tuple(cnt)].append(w)
        return list(d.values())


# ключ в словаре - частоты букв (у анаграмм одинаковые), tuple потому что list не хешируется
# O(n*k), n - кол-во слов, k - длина слова
# можно было sorted(w) как ключ, но это O(n*k*logk)

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
