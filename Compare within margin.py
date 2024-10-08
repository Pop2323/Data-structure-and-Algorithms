def close_compare(a, b, margin=0):
    if abs(a - b) <= margin:
        return 0
    elif a < b:
        return -1
    else:
        return 1
    
# 2nd solution
    # return 0 if abs(a - b) <= margin else -1 if a < b else 1


print(close_compare(4, 5))         # -1)
print(close_compare(5, 5))         # 0
print(close_compare(6, 5))         # 1
print(close_compare(2, 5, 3))      # 0
print(close_compare(5, 5, 3))      # 0
print(close_compare(8, 5, 3))      # 0
print(close_compare(8.1, 5, 3))    # 1
print(close_compare(1.99, 5, 3))   # -1