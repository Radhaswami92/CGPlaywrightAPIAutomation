Input_arr=[]
for i in range(0, 6):
    num = int(input("Please provide no.: "))
    Input_arr.append(num)

for i in range(0, len(Input_arr)):
    for j in range(i +1, len(Input_arr)):
        if Input_arr[i] > Input_arr[j]:
            Input_arr[i],Input_arr[j] = Input_arr[j], Input_arr[i]
print(Input_arr)

#otherwaysto do it
