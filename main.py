import sqlite3

db = sqlite3.connect('phone.db')

choice = ''

cur = db.cursor()
cur.execute('create table if not exists' + ' phone(name text , ph_no text)')
while choice != 'exit':

    choice = input('Enter your choice (Press exit to quit the process) : ')

    db.commit()

    if choice == 'add':
        name1 = input("Enter the contact's name : ")
        phone_no = input("Enter the phone number : ")
        cur.execute('insert into phone values(?,?)',(name1,ph_no))

    elif choice == 'delete':
        name2 = input("Enter the name of person to be deleted from contacts : ")
        cur.execute('delete from phone where name = (?)',(name2))

    elif choice == 'view':
        cur.execute('select * from phone')
        cts = cur.fetchall()
        print('Phone List : ',cts)

    elif choice == 'edit':
        s = input('Do you want to edit the contact name or through phone number : ')
        if s == 'name':
            b = input('Enter the phone number : ')
            d = input('Enter the name where it needs to be edited : ')
            cur.execute('update phone set name = (?) where ph_no = (?)',(d,b))
        elif s == 'phone number':
            b1 = input('Enter the name : ')
            d1 = input('Enter the phone number where it needs to be edited : ')
            cur.execute('update phone set ph_no = (?) where name = (?)', (d1, b1))

    elif choice == 'search':
        s = input('Do you want to search the contact by name or through phone number : ')
        if s == 'name':
            cur.execute('select * from phone where name == (?)',(s))
        elif s == 'phone number':
            cur.execute('select * from phone where ph_no == (?)', (s))
        else:
            print('Invalid search .')

    elif choice == 'exit':
        print('Thank You!')
        break

    else:
        print('Sorry , Invalid choice .')