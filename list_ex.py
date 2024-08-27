"""
1. Sum of all numbers in the list
2. Sum of all odd positions numbers in the list
3. Sum of all even positions numbers in the list
4. Sum of all odd numbers in the list
5. Sum of all even numbers in the list
"""

def sum_of_list(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i

    return sum

def sum_of_odd_pos(numbers):
    sum_of_odd = 0

    for i in range(0,len(numbers)):
        if i % 2 !=0:
            sum_of_odd = sum_of_odd + numbers[i]
    return sum_of_odd

numbers = [1,2,3,4,8,9,5,7]

sum = sum_of_list(numbers)
print(sum)