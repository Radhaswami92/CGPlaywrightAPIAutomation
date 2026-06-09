nums = [10, 5, 8, 20, 3]

largest = float('-inf')
second_largest = float('-inf')
print(largest)
for num in nums:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num
print(second_largest)
