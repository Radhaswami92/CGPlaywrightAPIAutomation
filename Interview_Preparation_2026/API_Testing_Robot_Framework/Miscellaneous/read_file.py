with open(r"C:\Users\JIBISWAS\PycharmProjects\FirstAutomationSetting\Interview_Preparation_2026\API_Testing_Robot_Framework\Resources\Libraries\Read_write_text_file.txt", "r") as file_read:

    for lines in file_read:
        lines = lines.rstrip("\n")

        line_h = lines.split("    ")

        print(line_h)
