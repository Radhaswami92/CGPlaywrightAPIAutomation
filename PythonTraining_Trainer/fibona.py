while True:
    number = int(input("Please enter the number "))

    num1 = 0
    num2 = 1
    count = 0

    if number <= 0:
        print("Please enter a positive integer")
    elif number == 1:
        print("Fibonacci sequence upto",number,":")
        print(num1)

    else:
        print("Fibonacci sequence:")

    while count < number:
         print(num1)
         nth = num1 + num2
         num1 = num2
         num2 = nth
         count += 1
    choice = str(input("Do you want to continue ? "))
    if choice == "Yes":
        continue
    else:
        break
    if number % 2 == 0:
        print("The number is even")
    elif number < 1:
        print("Number is neither odd or even")
    else:
        print("The number is odd")





