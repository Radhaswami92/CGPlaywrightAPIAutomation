Input_str = "The fox jumps over the lazy dog"

splt_str = Input_str.split(" ")

max_char_len_char = splt_str[0]
for i in range(1, len(splt_str)):
    if len(splt_str[i]) > len(max_char_len_char):
        max_char_len_char = splt_str[i]

print(max_char_len_char)