import re

"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    res = ""
    for i in strs:
        res += f"{len(i)}#{i}"
    return res

"""
@param: str: A string
@return: decodes a single string to a list of strings
"""
def decode(string):
    res, i = [], 0
    while i < len(string):
        j = i
        while string[j] != "#":
            j += 1
        length = int(string[i:j])
        print(f"length: {length}")
        res.append(string[j + 1: j + 1 + length])
        print(f"new res: {res}")
        i = j + 1 + length
        print(f"j was: {j} and so i is: {i}") 
    return res