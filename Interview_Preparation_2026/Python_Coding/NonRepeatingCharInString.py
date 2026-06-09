Input_str = "nxtwawvnxeve"
non_rep_chars = []

for char in Input_str:
    if Input_str.count(char) < 2:
        if char not in non_rep_chars:
            non_rep_chars.append(char)
print(non_rep_chars)
