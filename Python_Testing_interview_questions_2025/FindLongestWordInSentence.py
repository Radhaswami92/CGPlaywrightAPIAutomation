Input_str = "The fox jumps over the lazy dog"

Input_str = Input_str.split(" ")

Longst_word_len=0
Longest_word = ""
for words in Input_str:
    if len(words) > Longst_word_len:
        Longst_word_len= len(words)
        Longest_word = words
print(Longest_word)



##### other ways to do it .
Input_str_2 = "The fox jumps over the lazy dog execute and"
Input_str_2 = Input_str_2.split(" ")

print(max(Input_str_2, key=len))




