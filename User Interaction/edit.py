import display

def edit(contact_dictionary):
    display.display_contacts(contact_dictionary)
    edit_selection = input('Select a contact to edit. \n NOTE: Only one edit can be made at a time: ')
    if edit_selection in contact_dictionary:
        contact_edit = contact_dictionary[edit_selection]

        value_edit = input('Edit "Name", "Email", or "Notes": ').lower()
        if value_edit == 'name':
            edit_name = input('Input the updated name: ')
            contact_edit['contact name'] = edit_name
        elif value_edit == 'email':
            edit_email = input('Input the updated email: ')
            contact_edit['contact email'] = edit_email
        elif value_edit == 'notes':
            note_edit = input('Input notes.\n Note this new information will erase any notes currently\n associated with the contact: ')
            contact_edit['contact notes'] = note_edit
        else:
            "If you are trying to change the phone number:\n Create a new contact\n Delete the incorrect contact "
    else:
        print('This contact is not in the system.')