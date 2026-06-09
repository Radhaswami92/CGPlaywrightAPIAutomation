

try:
    with open("rsv.txt", "r") as file_open:
        c = file_open.read
        print(c)
except Exception as e:
    print(f"{e} adjah")

finally:
    print("abcdef")