def find_duplicate(nums):

    a = nums[0]
    b = nums[0]

    while True:
        a = nums[a]  
        b = nums[nums[b]]    
        if a == b:
            break

    a = nums[0] 
    while a != b:
        a = nums[a]  
        b = nums[b]         

    return b  

nums = [3, 1, 3, 4, 2]
duplicate = find_duplicate(nums)
print(f"The duplicate number is: {duplicate}")
