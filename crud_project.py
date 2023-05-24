import sqlite3

conn = sqlite3.connect(r'C:\Users\hp\Desktop\Programming\Python\DBMS\projectfile.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS School(ItemId INTEGER PRIMARY KEY NOT NULL, Name TEXT, Age INTEGER, Programme TEXT, GPA REAL)''')

def input_data():
    ans = input("To enter data enter [y] else enter [n]")

    while ans == 'y':
        nom = input("Enter the name: \n")
        age = input("Enter the age: \n")
        prog = input("Enter the programme: \n")
        gpa = float(input("Enter the GPA: \n"))
        cur.execute('''INSERT INTO School(Name, Age, Programme, GPA)
                VALUES(?, ?, ?, ?)''',
                (nom, age, prog, gpa))
        conn.commit()
        ans = input("Do you want to more enter data\n Please enter [y]/ [n]")

    else:
        start()
        
def show_values():
    res = cur.execute('''SELECT * FROM School''')
    for i in res:
        print(i)
    start()
        
def update_values():
    column = input("What do you want to update: \n")
    descr = input("Enter the new value: \n")
    nom = input("Who does this affect? ")
    
    cur.execute(f'''UPDATE School
                SET {column} = ?
                WHERE Name == ?''',
                (descr, nom))
    conn.commit()
    start()
    
def delete():
    ans = input('Whose record do you want to delete: ')
    cur.execute('''DELETE FROM School WHERE Name == ?''', (ans))
    start()
    conn.commit()

def start():    
    task = input('What would you like to do: \na. input data\nb. show values\nc. update values\nd. delete values\ne. exit\n Please enter the letter for the task you want to complete.')
    if task == 'a':
        input_data()
    elif task == 'b':
        show_values()
    elif task == 'c':
        update_values()
    elif task == 'd':
        delete()
    elif task == 'e':
        exit()
    
start()    
    
conn.commit()
conn.close()