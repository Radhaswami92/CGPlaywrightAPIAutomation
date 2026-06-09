import xml.etree.ElementTree as ET



#with open (r"C:/Users/JIBISWAS/PycharmProjects/FirstAutomationSetting/Interview_Preparation_2026/API_Testing_Robot_Framework/Resources/Libraries/complex.xml") as file_read_xml:
    # a=file_read_xml.read()
    # print(a)
xm_path=r"C:/Users/JIBISWAS/PycharmProjects/FirstAutomationSetting/Interview_Preparation_2026/API_Testing_Robot_Framework/Resources/Libraries/complex.xml"

tree = ET.parse(xm_path)
root = tree.getroot()
text_cust_id = root.find('.//customer/id')
print(text_cust_id)


