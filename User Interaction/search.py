def search(contact_dictionary):
    contact_search = input('Input the phone number for the contact to be found:\n')
    if contact_search in contact_dictionary:
        query = contact_dictionary[contact_search]
        for contact, info in query.items():
            print(f'    {contact}: {info}')
    else:
        print('This contact does not exist.\n')