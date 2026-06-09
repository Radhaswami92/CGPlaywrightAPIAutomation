nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
indexex=[]
for i in range(0, len(nums)):
    for j in range(len(nums)-1, i, -1):
        if nums[i] == nums[j]:
            del nums[j]


print(nums)
# for index in indexex:
#     nums.remove(num[])

def find_dup_lis(arr):
    unique_ele= []
    for items in arr:
        if items not in unique_ele:
            unique_ele.append(items)
    return unique_ele
print(find_dup_lis(nums))