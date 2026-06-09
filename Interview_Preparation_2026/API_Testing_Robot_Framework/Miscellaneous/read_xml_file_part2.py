

import xml.etree.cElementTree as et

xml_obj = et.parse(r"C:\Users\JIBISWAS\PycharmProjects\FirstAutomationSetting\Interview_Preparation_2026\API_Testing_Robot_Framework\Resources\Libraries\complex.xml")
d = xml_obj.getroot()



desired_text = d.findtext(".//order/orderSummary/totalAmount")

elemets = d.findall()

print(desired_text)
assert  desired_text == "1418.97"
