given_str= "Hello World"
vowel = "aeiou"
matching_ele=[]
count = 0
for char in given_str:
    if char in vowel:
        matching_ele.append(char)
        count = count + 1
print(count)