
contact_dictionary = {}

import addition
import delete
import display
import edit
import exitProgram
import export
import importing
import search

def menu():

    print('Welcome to the interactive contact management program!\n')
    
    while True:
        try:
            print(
        '1. Add a new contact\n2. Edit an existing contact\n3. Delete a contact\n4. Search for a contact\n5. Display all contacts\n6. Export contacts to a text file\n7. Quit\n'
        )
            menu_selection = input('Please make a selection from the menu: ')
        except ValueError:
            print('Input just the number for the menu action you would like to select.\n For example: To add a new contzct input "1"')
        else:
            if menu_selection == '1':
                addition.add(contact_dictionary)
                #done
            elif menu_selection == '2':
                edit.edit(contact_dictionary)
                #done
            elif menu_selection == '3':
                delete.delete(contact_dictionary)
                #done
            elif menu_selection == '4':
                search.search(contact_dictionary)
            elif menu_selection == '5':
                display.display_contacts(contact_dictionary)
                #done
            elif menu_selection == '6':
                export.export(contact_dictionary)
            #elif menu_selection == '7':
            #    importing.import_file(contact_dictionary)
            elif menu_selection == '7':
                exitProgram.exit_program(contact_dictionary)
                break
                #done
            else:
                print('This is not a valid selection. Please try again.\n')

menu()
