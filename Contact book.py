import sqlite3
conn=sqlite3.connect('contact_book.db')
cursor=conn.cursor()

cursor.execute('''create table if not exists contacts(
               id integer primary key,
               name text not null,
               number integer unique,
               email text not null,
               address text not null
               )''')

def list_all_conatcts():
    cursor.execute('select * from contacts')
    for row in cursor.fetchall():
        print(row)

def add_conatct(name,number,email,address):
    cursor.execute('insert into contacts(name,number,email,address) values(?,?,?,?)',(name,number,email,address))
    conn.commit()
    print("Contact added successfully.")

def update_conatct(name,number,email,address,id_input):
    cursor.execute('update contacts set name=?, number=?, email=?, address=? where id=?'(name,number,email,address,id_input))
    conn.commit()
    print("Contact updated successfully.")

def delete_conatct(id_input):
    cursor.execute('delete from contacts where id=(?)',(id_input,))
    conn.commit()
    print("Contact deleted successfully.")

def main():
    while True:
        print('Manage contact details of people')
        print('choose 1 to list all contacts')
        print('choose 2 to add a contact')
        print('choose 3 to update a contact')
        print('choose 4 to delete a contact')
        print('choose 5 to exit')
        choice=input('Enter your choice: ')

        if choice=='1':
            list_all_conatcts()

        elif choice=='2':
            name=input('Enter name: ')
            number=int(input('Enter number: '))
            email=input('Enter email: ')
            address=input('Enter address: ')
            add_conatct(name,number,email,address)

        elif choice=='3':
            id_input=int(input('Enter the video id to be updated: '))
            name=input('Enter name: ')
            number=int(input('Enter number: '))
            email=input('Enter email: ')
            address=input('Enter address: ')
            update_conatct(id_input,name,number,email,address)

        elif choice=='4':
            id_input=int(input('Enter the video id to be deleted: '))
            delete_conatct(id_input)

        else:
            break

    conn.close()

if __name__=='__main__':
    main()


