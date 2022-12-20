import view
import model
import xml_creator

def phone_book():
    menu = 0
    while menu != 4:
        menu = view.choose_main_menu()
        if menu == 1:
            view_type = view.choose_view_menu()
            if view_type in (1,2):
                phone_list = model.get_phone_list()
                if view_type == 1:
                    view.print_phone_book(phone_list)
                elif view_type == 2:  
                    xml_creator.create_xml(phone_list)
                    view.print_message('Файл создан')
        elif menu == 2:
            surname = view.input_surname_for_search() 
            filtered_phone_list = model.filter_by_surname(model.get_phone_list(),surname) 
            view.print_phone_book(filtered_phone_list)
        elif menu == 3:
            new_entry = view.input_new_entry() 
            model.add_new_entry(new_entry) 


phone_book()