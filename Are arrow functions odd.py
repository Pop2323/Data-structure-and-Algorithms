odds = lambda arr: [x for x in arr if x % 2 != 0]

print(odds([]))                      # []
print(odds([2,4,6]))                 # []
print(odds([1,3,5]))                 # [1,3,5]
print(odds([1, 2, 3, 4, 5, 6]))      # [1, 3, 5]