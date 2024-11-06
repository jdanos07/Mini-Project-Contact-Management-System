import display
def delete(contact_dictionary):
    display.display_contacts(contact_dictionary)
    confirm_delete = input('Is there a contact that requires deletion? Yes/No ').lower()
    if confirm_delete == 'yes':
        selection = input ('Input the phone number for the desired contact: ')
        if selection in contact_dictionary:
            del contact_dictionary[selection]
        else:
            print('Contact does not exist.')
    else:
        print('Returning to Main Menu.')
        
