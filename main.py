import search

from search import Contact as c

choice = ''

while choice != 'exit':

    choice = input('Enter your choice (Press exit to quit the process) : ')

    if choice == 'add':
        name1 = input("Enter the contact's name : ")
        phone_no = input("Enter the phone number : ")
        c.add(name1,phone_no)

    elif choice == 'delete':
        name2 = input("Enter the name of person to be deleted from contacts : ")
        c.delete(name2)

    elif choice == 'view':
        join = c.view()
        print('Phone List : ',join)

    elif choice == 'edit':
        s = input('Do you want to edit the contact name or through phone number : ')
        if s == 'name':
            b = input('Enter the phone number : ')
            d = input('Enter the name where it needs to be edited : ')
            c.edit1(d,b)
        elif s == 'phone number':
            b1 = input('Enter the name : ')
            d1 = input('Enter the phone number where it needs to be edited : ')
            c.edit2(d1,b1)

    elif choice == 'search':
        s = input('Do you want to search the contact by name or through phone number : ')
        if s == 'name':
            t = input("Enter the name : ")
            c.search1(t)
        elif s == 'phone number':
            t = input("Enter the phone number : ")
            c.search2(t)
        else:
            print('Invalid search .')

    elif choice == 'exit':
        print('Thank You!')
        break

    else:
        print('Sorry , Invalid choice .')