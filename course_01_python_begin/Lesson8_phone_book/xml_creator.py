def create_xml(phone_list):
    xml = '<xml>\n'

    for entry in phone_list:
        surname, name, phone, description = entry
        xml += f'    <surname>{surname}</surname>\n'
        xml += f'    <name>{name}</name>\n'
        xml += f'    <phone>{phone}</phone>\n'
    xml += '</xml>'

    with open('phone_book.xml', 'w') as file:
        file.write(xml)

