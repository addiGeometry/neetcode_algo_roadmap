"""
Problem: longest consecutive sequence in an Array
"""
from typing import List
from collections import defaultdict

def longest_consecutive(nums: List[int]) -> int:
    """
    Find the longest consecutive sequence wihthin the array
    :param nums: input array
    :return: length of the sequence
    """
    nums, max_len = set(nums), 0
    for num in nums:
        if num-1 in nums:
            continue
        current = 1
        while num+1 in nums:
            current += 1
            num += 1
        if current > max_len:
            max_len = current
    return max_len


def mycoolbutnotgeniussolution(nums: List[int]) -> int:
    """
    Find the longest consecutive sequence wihthin the array
    :param nums: input array
    :return: length of the sequence
    """
    sequences, max_l = defaultdict(list), 0
    for num in nums:
        if num in sequences:
            continue
        #check left neighbor
        print("--------------------")
        print(f"Handling number {num}")
        sequences[num] = [num]
        left = num-1
        right = num+1 
        if  left in sequences:
            print(f"left neighbor in {left}")
            print(f"left neighbor contained: {sequences[left]}")
            print(f"num contained: {sequences[num]}")
            sequences[left] += sequences[num]
            sequences[num] = sequences[left]
            print(f"now: {sequences[num]}")
            while left-1 in sequences:
                sequences[left-1] = sequences[num]
                left -= 1
        #check right
        if right in sequences:
            print(f"right neighbor in {right}")
            print(f"right neighbor contained: {sequences[right]}")
            print(f"num contained: {sequences[num]}")
            sequences[num] += sequences[right]
            sequences[right] = sequences[num]
            print(f"now: {sequences[num]}")
            while right+1 in sequences:
                sequences[right+1] = sequences[num]
                right += 1
        newlen = len(sequences[num])
        if newlen > max_l:
            max_l = newlen
    return max_l