from lib2to3.pgen2.pgen import generate_grammar


CONNECTION = None

class Book():
    SQL_CREATE = '''
        CREATE TABLE books (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            pubdate DATE NOT NULL,
            genre TEXT NOT NULL,
            state TEXT NOT NULL
        );
    '''

    SQL_INSERT = ''' 
        INSERT INTO books (
            name,
            author,
            pubdate,
            genre,
            state
        )
        VALUES(
            "{}",
            "{}",
            "{}",
            "{}",
            "{}"
        ) 
    '''

    SQL_UPDATE = '''
    
    '''

    SQL_DELETE = '''
        DELETE * from books WHERE {};
    '''

    SQL_SELECT = '''
        SELECT * from books WHERE {};
    '''

    def __init__(self, 
            bookname, 
            bookauthor, 
            pubdate, 
            bookgenre, 
            bookstate
        ):

        # Проверить есть ли такая таблица в базе
        cursor = CONNECTION.cursor()

        self.id = None
        self.name = bookname
        self.author = bookauthor
        self.publish_date = pubdate
        self.genre = bookgenre
        self.state = bookstate
        try:
            cursor.execute(self.SQL_CREATE)
        except Exception:
            pass

        

    def save(self):
        cursor = CONNECTION.cursor()
        # Создать или обновить в базе
        cursor.execute(self.SQL_INSERT.format(
            self.name,
            self.author,
            self.publish_date,
            self.genre,
            self.state
        ))
        CONNECTION.commit()
        # присвоить айди из базы
        self.id = cursor.lastrowid

    def delete(self):
        cursor = CONNECTION.cursor()
        cursor.execute(self.SQL_DELETE.format(
            self.id
        ))


    @staticmethod
    def select(condition):
        cursor = CONNECTION.cursor()
        cursor.execute(Book.SQL_SELECT.format(condition))

        result = []
        for row in cursor.fetchall():
            idx = row[0]
            name = row[1]
            author = row[2]
            pubdate = row[3]
            genre = row[4]
            state = row[5]
            book = Book(name, author, pubdate, genre, state)
            book.id = idx
            result.append(book)

        return result
        # получить по условию
    
class Reader():
    SQL_CREATE = '''
        CREATE TABLE readers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            dob DATE NOT NULL,
            gender TEXT NOT NULL,
            adress TEXT NOT NULL,
            phonenumber TEXT NOT NULL
        );
    '''

    SQL_INSERT = ''' 
        INSERT INTO readers (
            name,
            dob,
            gender,
            adress,
            phonenumber
        )
        VALUES(
            "{}",
            "{}",
            "{}",
            "{}",
            "{}"
        ) 
    '''

    SQL_SELECT = '''
        SELECT * from readers WHERE {};
    '''
    SQL_DELETE = '''
        DELETE * from readers WHERE {};
    '''

    def __init__(self, name, dob, gender, adress, phonenumber): 
        self.id = None
        self.fio = name
        self.dob = dob
        self.gender = gender
        self.adress = adress
        self.phonenumber = phonenumber
        cursor = CONNECTION.cursor()
        try:
            cursor.execute(self.SQL_CREATE)
        except Exception:
            pass


    def save(self):
        cursor = CONNECTION.cursor()
        # Создать или обновить в базе
        cursor.execute(self.SQL_INSERT.format(
            self.fio,
            self.dob,
            self.gender,
            self.adress,
            self.phonenumber
        ))
        CONNECTION.commit()
        # присвоить айди из базы
        self.id = cursor.lastrowid
    
    def delete(self):
        cursor = CONNECTION.cursor()
        cursor.execute(self.SQL_DELETE.format(
            self.id
        ))

    

    @staticmethod
    def select(condition):
        cursor = CONNECTION.cursor()
        cursor.execute(Reader.SQL_SELECT.format(condition))
        result = []
        for row in cursor.fetchall():
            idx = row[0]
            name = row[1]
            dob = row[2]
            gender = row[3]
            adress = row[4]
            phonenumber = row[5]
            reader = Reader(name, dob, gender, adress, phonenumber)
            reader.id = idx
            result.append(reader)
        return result





    
class LibraryRecord():
    def __init__(self, idx, reader, book, date_issued, date_due):
        self.id = idx
        self.reader_id = reader.id
        self.book_id = book.id
        self.date_issued = date_issued
        self.date_due = date_due


import sqlite3

create_dicks_command = '''
    CREATE TABLE dicks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        size INTEGER NOT NULL
    );
'''

# class Person:
#     def __init__(self, name, size) -> None:
#         self.id = None
#         self.name = name
#         self.size = size

# connection = sqlite3.connect('library.db')
# cursor = connection.cursor()

# cursor.execute("SELECT * from dicks WHERE id = 1;")
# for row in cursor.fetchall():
#     print(row)

# Book.select()

# cursor.execute(create_dicks_command)
# cursor.execute('INSERT INTO dicks(name, size) VALUES ("Artem", 100);')
# cursor.execute('INSERT INTO dicks(name, size) VALUES ("Nikita", 50);')
# cursor.execute('UPDATE dicks SET size = 150 WHERE id IN (1,2,3,4)')
# cursor.execute('DELETE FROM dicks WHERE id = 2')
# connection.commit()