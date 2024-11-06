def export(contact_dictionary):
    exportable_contact = '\n'.join(
        f"Phone: {phone}\n    Name: {details['contact name']}, Email: {details['contact email']}, Notes: {details['contact notes']}"
        for phone, details in contact_dictionary.items()
    )
    try:
        with open('Contacts.txt', 'x') as file:
            file.write(exportable_contact)
        print('File created and saved.')
    except FileExistsError:
        with open('Contacts.txt', 'w') as file:
            file.write(exportable_contact)
        print('Contacts.txt already exists. File updated.')