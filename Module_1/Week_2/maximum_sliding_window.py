def max_kernel(num_list, k):
    result = []
    i = 0
    j = k
    while i < len(num_list) and j < len(num_list) + 1:
        result.append(max(num_list[i:j]))
        i += 1
        j += 1

    return result