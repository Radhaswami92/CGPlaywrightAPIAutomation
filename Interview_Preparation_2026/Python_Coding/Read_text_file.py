import string
with open("Test_Text_file.txt", "r", encoding="utf-8") as file_read:
    for line in file_read:
        line = line.rstrip()
        #print(line)
        fields = line.split('\t')
        print(fields)
