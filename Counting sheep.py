def count_sheeps(sheep):
# 1st solution
    return sheep.count(True)

# 2nd solution
    # count = 0
    # for i in sheep:
    #     if i == True:
    #         count += 1
    # return count




print(count_sheeps([True,  True,  True,  False,
                  True,  True,  True,  True ,
                  True,  False, True,  False,
                  True,  False, False, True ,
                  True,  True,  True,  True ,
                  False, False, True,  True ]))