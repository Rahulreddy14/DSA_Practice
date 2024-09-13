def jumpGame(nums):
    farthest = 0
    for i in range(len(nums)):
        if i > farthest:
            return False
        farthest = max(farthest, i + nums[i])

    return True 


result = jumpGame([2,3,1,1,4])
print(result)