def display_contacts(contact_dictionary):
    for contact in contact_dictionary:
            print(contact)
            for details in contact_dictionary[contact]:
                  print(f'    {details} : {contact_dictionary[contact][details]}')
    print('')