##Example
##Li = [1,2,3,2,2,1,3,3,4,0]
##Expected Output:{1: 2, 2: 3, 3: 2, 4: 2, 5: 1}

# Numbers = []
# frequency = {}
# for i in range(0, 10):
#     num = input("Please provide the nos.: ")
#     Numbers.append(num)
#
# for num in Numbers:
#     count = Numbers.count(num)
#     if num not in frequency:
#         frequency[num] = count
# print(frequency)

### same code if it is for a string
## Need to compress a string
##GivenString:aaaabbcccddfg
##ExpectedOutput:a4b2c3d2fg


stra = "aaaabbcccddfg"
finalstr = ""
for char in stra:
    count = stra.count(char)
    if count == 1:
        count = str("")
    if char not in finalstr:
        finalstr = finalstr + char + str(count)
print(finalstr)




