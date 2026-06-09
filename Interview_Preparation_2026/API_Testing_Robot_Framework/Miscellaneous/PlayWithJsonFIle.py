
import json

with open (r"C:\Users\JIBISWAS\PycharmProjects\FirstAutomationSetting\Interview_Preparation_2026\API_Testing_Robot_Framework\Resources\Libraries\complex.json") as file_read:
    data = json.load(file_read)
    print(data.keys())
    my_json_val = data["milestones"]["phase_1"]["tasks"][0]["history"][1]["timestamp"]
    if my_json_val == "2024-05-23T17:00:00Z":
        print("Data validation successful")
    else:
        print("Data validation failed")