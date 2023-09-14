from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in reversed(range(len(nums))):
        res[i] *= postfix
        postfix *= nums[i]

    return res
    
    
    
    
    
    
    
    
    
    
    
    
    
""" 
it was a grind
res = [1] * len(nums)
lastpre = 1
lastpost = 1
for i in range(len(nums)-1):
    inverse = len(nums) - 1 - i
    lastpre = nums[i] * lastpre
    res[i+1] = lastpre * res[i+1]
    lastpost = nums[inverse] * lastpost
    res[inverse - 1] = lastpost * res[inverse - 1]
return res """