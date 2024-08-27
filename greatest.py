numbers = [1,2,55,66,46,231,-9,-4,0,2]

greatest = numbers[0]
smallest = numbers[0]
for i in numbers:
    if i >= greatest:
        greatest = i
    if i <=smallest:
        smallest = i

print(greatest)

print(smallest)



