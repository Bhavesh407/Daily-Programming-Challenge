def find_zero_sum_subarrays(arr):
    sum_map = {}
    zero_sum_subarrays = []

    cum_sum = 0
    
    for index in range(len(arr)):
        cum_sum += arr[index]

        if cum_sum == 0:
            zero_sum_subarrays.append((0, index))

        if cum_sum in sum_map:
            for start_index in sum_map[cum_sum]:
                zero_sum_subarrays.append((start_index + 1, index))
        
        if cum_sum not in sum_map:
            sum_map[cum_sum] = []
        sum_map[cum_sum].append(index)
    
    return zero_sum_subarrays


arr = [1,2,-3,3,-1,2]
result = find_zero_sum_subarrays(arr)
print("Subarrays with zero sum:", result)
