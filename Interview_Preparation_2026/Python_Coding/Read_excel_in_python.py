import pandas as pd

df = pd.read_excel(r"C:\Users\JIBISWAS\Downloads\Interview_API_Automation.xlsx", sheet_name="Microsoft")

df_dict = df.to_dict(orient="list")

# print(df_dict)
# # print(list(df_dict.keys()))
# print(len(df_dict[(list(df.keys())[0])]))
# print(len(df_dict))
max_range = 0
for key in df_dict.keys():
    li = df_dict[key]
    if len(li) > max_range:
        max_range = len(li)

for i in range (0, max_range):
    str =""
    for j in range (0, len(df_dict.keys())):
        key_val = list(df_dict.keys())[j]
        #print(key_val)
        li = df_dict[key_val]
        val = li[i]
        #print(li)
        str += f"{key_val} : {val}"
        # str += list(df_dict.keys())[j][i]
    print(str)
    str =""
    print("\n")


