def max_sequence(arr):
    max_sum = 0
    current_sum = 0
    for n in arr:
        current_sum = max(n, current_sum + n)
        max_sum = max(max_sum, current_sum)
    return max_sum


print(max_sequence([]))                                                                           # 0
print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))                                              # 6
print(max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]))                                         # 0
print(max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]))          # 155