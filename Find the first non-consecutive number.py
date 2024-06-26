def first_non_consecutive(arr):
    for i in range(1, len(arr)):
        if arr[i] - arr[i - 1] != 1:
            return arr[i]
    return None





print(first_non_consecutive([1,2,3,4,6,7,8]))             # 6
print(first_non_consecutive([1,2,3,4,5,6,7,8]))           # None
print(first_non_consecutive([4,6,7,8,9,11]))              # 6
print(first_non_consecutive([4,5,6,7,8,9,11]))            # 11
print(first_non_consecutive([31,32]))                     # None
print(first_non_consecutive([-3,-2,0,1]))                 # 0
print(first_non_consecutive([-5,-4,-3,-1]))               # -1