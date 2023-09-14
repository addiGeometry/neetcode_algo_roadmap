from typing import List
from collections import defaultdict

def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = count.get(n, 0) + 1
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res



"""    freq = defaultdict(int)
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    sorted_list = sorted(list(freq.items()), key=lambda x: x[1], reverse=True)

    return [sorted_list.pop(0)[0] for k in range(0,k)] #Only the second element of the tuple in the sorted list of occurences"""
        