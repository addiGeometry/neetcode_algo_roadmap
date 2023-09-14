from collections import defaultdict
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    """anagram_groups = {}
    for word in strs:
        print(word)
        ana_key = tuple(sorted(set(word)))
        if not ana_key in anagram_groups:
            anagram_groups[ana_key] = []
        anagram_groups[ana_key].append(word)
    return list(anagram_groups.values())"""
    res = defaultdict(list)

    for s in strs:
        count = 0 * [26]
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)

    return res.values()