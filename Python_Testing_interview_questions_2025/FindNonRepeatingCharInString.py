Input_str = "nxtwawvnxeve"
Non_Rpeating_Chars=[]
for char in Input_str:
    count = Input_str.count(char)
    if count <= 1:
        Non_Rpeating_Chars.append(char)
print(Non_Rpeating_Chars[0])

def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char
    return None

print(first_non_repeating_char("nxtwave"))