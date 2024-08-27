"""
Q. Find the second smallest/largest number from a list
"""

def second_smallest(numbers):
    sm = 0
    ssm = 0
    for i in numbers:
        if i <= sm:
            sm, ssm = i, sm
        elif i < ssm:
            ssm = i
    return ssm

numbers = [1,1,2,2,33,34,5,6,6,-1,-1,0,-3,-3]
numbers_list = list()

print(second_smallest(numbers))