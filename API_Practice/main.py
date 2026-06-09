from API_Practice.validator import validate
from robot.api.deco import library, keyword


@library
class main:
    #def __init__(self):

    @keyword
    def validate_xml_response(self):
        if validate("C:/Users/JIBISWAS/PycharmProjects/FirstAutomationSetting/API_Practice/XML/get_res.xml", "C:/Users/JIBISWAS/PycharmProjects/FirstAutomationSetting/API_Practice/XML/schema.xsd"):
            print('Valid! :)')
        else:
            print('Not valid! :(')
















