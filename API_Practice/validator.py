from lxml import etree


def validate(xml_path: str, xsd_path: str) -> bool:
    ## Providing path of xsd and providing knowledge
    xml_schema_doc = etree.parse(xsd_path)
    xml_schema = etree.XMLSchema(xml_schema_doc)
    xml_doc = etree.parse(xml_path)
    final_result = xml_schema.validate(xml_doc)
    return final_result






