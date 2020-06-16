import sqlite3

db = sqlite3.connect('phone.db')

cur = db.cursor()
cur.execute('create table if not exists' + ' phone(name text , ph_no text)')

class Contact:
    
    def __init__(self,name,call):
        self.name = name
        self.call = call
        pass
    
    def add(name,call):
        cur.execute('insert into phone values(?,?)', (name, call))
        db.commit()
        pass
    
    def delete(name):
        cur.execute('delete from phone where name = (?)', (name))
        db.commit()
        pass
    
    def view():
        cur.execute('select * from phone')
        cts = cur.fetchall()
        db.commit()
        return cts
    
    def edit1(name,call):
        cur.execute('update phone set name = (?) where ph_no = (?)', (name, call))
        db.commit()
        pass
    
    def edit2(name,call):
        cur.execute('update phone set ph_no = (?) where name = (?)', (call, name))
        db.commit()
        pass
    
    def search1(names):
        cur.execute("SELECT * FROM phone WHERE name = ?",(names,))
        row1 = cur.fetchall()
        for i in row1:
            print(i)
        pass
    
    def search2(calls):
        cur.execute("SELECT * FROM phone WHERE ph_no = ?",(calls,))
        row1 = cur.fetchall()
        for i in row1:
            print(i)
        pass