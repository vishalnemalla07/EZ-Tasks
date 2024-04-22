def find_second_largest(nums):
    if len(nums) < 2:
        return "List must contain at least two distinct integers"
    
    largest = nums[0]
    second_largest = float('-inf')
    
    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    
    return second_largest

input_list = [3, 5, 7, 2, 8, 5, 9]
print(find_second_largest(input_list))
