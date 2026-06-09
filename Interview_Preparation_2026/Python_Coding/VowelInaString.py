given_str= "Hello World"
vowel = "aeiou"
vowel_in_a_str =""
count_of_vowel_in_a_string=0
for ele in given_str:
    if ele in vowel:

        if ele not in vowel_in_a_str:
            count_of_vowel_in_a_string += 1
            vowel_in_a_str +=ele
print(vowel_in_a_str)
print(count_of_vowel_in_a_string)

def dd(*arg):
    a= 0
    for nos in arg:
        a = a + 1 + nos
    return a
print(dd(2,3,4,5))
