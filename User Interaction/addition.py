contact_dictionary = {}

def add(contact_dictionary):

    addition_desire = input('Is there a contact to add? Yes/No ').lower()

    if addition_desire == 'yes':
        
        phone_number = input('Input contact\'s phone number: ')
        contact_name = input('Input conact\'s name: ')
        contact_email = input('Input contact\'s email: ')
        contact_notes = input('Input any notes, comments, or additional information.\n If none, input NA: ')
        
        new_contact = {
            'contact name' : contact_name,
            'contact email' : contact_email,
            'contact notes' : contact_notes
            }
        
        contact_dictionary[phone_number] = new_contact

        print('Contact has been added\n')
    else:
        print('Returning to Main Menu.')

