a = "Jitaditya"
#{Reverse with string split}
#aytidatiJ
print(a[::-1])

#atdtJ
print(a[::-2])

#idy
print(a[1::3])

#tadity
print(a[2:8:])

b = "Automation test Engineer Jitaditya am I Hi Hello"
# Hello Hi I am Jitaditya engineer test automation
splited_str_array_list = b.split(" ")
Rvrsd = splited_str_array_list[::-1]
exp_sentnce = " ".join(Rvrsd)
print(exp_sentnce)

c = "I am Jaspreet"
#a ap

print(c[2:-4:2])
print(c[2:10:2])


