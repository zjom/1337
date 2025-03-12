# https://leetcode.com/problems/top-k-frequent-words/description/
from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counter = Counter(words)

        buckets:list[list[str]] = [[] for _ in range(len(words))]
        for word, count in counter.items():
            buckets[count].append(word)

        retv:list[str] = []
        for i in range(len(buckets)-1,-1,-1):
            bucket = buckets[i]
            bucket.sort()
            for word in bucket:
                if len(retv) == k:
                    return retv
                retv.append(word)

        return retv
