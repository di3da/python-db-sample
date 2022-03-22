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

    SQL_SELECTBYID = '''
        SELECT * from books WHERE id = {};
    '''
    SQL_SELECTBYNAME = '''
        SELECT * from books WHERE name = {};
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
    

    def __repr__(self):
        rep =  '\nКнига ' + str(self.id) + '\nНазвание - ' + str(self.name) + '\nАвтор - ' + str(self.author) + '\nЖанр - ' + str(self.genre) + '\nДата печати - ' + str(self.publish_date) + '\nСостояниe - ' + str(self.state) + '\n______________ ' 
        return rep

    def __str__(self) -> str:
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

    @staticmethod
    def delete(condition):
        cursor = CONNECTION.cursor()
        cursor.execute(Book.SQL_DELETE.format(condition))
        CONNECTION.commit()


    @staticmethod
    def selectbyid(condition):
        cursor = CONNECTION.cursor()
        cursor.execute(Book.SQL_SELECTBYID.format(condition))

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
    
    @staticmethod
    def selectbyname(condition):
        cursor = CONNECTION.cursor()
        cursor.execute(Book.SQL_SELECTBYNAME.format(condition))

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

    SQL_SELECTBYID = '''
        SELECT * from readers WHERE id = {};
    '''
    SQL_SELECTBYNAME = '''
        SELECT * from readers WHERE name = {};
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
        # присвоить библиотечную карточку

    def __repr__(self):
        rep = '\n______________ ' + '\nЧитатель ' + str(self.id) + '\nФИО - ' + str(self.fio) + '\nДата рождения - ' + str(self.dob) + '\nПол - ' + str(self.gender) + '\nАдрес - ' + str(self.adress) + '\nНомер телефона - ' + str(self.phonenumber)
        return rep
        
        
    
    def delete(self):
        cursor = CONNECTION.cursor()
        cursor.execute(self.SQL_DELETE.format(
            self.id
        ))


    @staticmethod
    def selectbyid(condition):
        cursor = CONNECTION.cursor()
        cursor.execute(Reader.SQL_SELECTBYID.format(condition))
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

    @staticmethod
    def selectbyname(condition):
        cursor = CONNECTION.cursor()
        cursor.execute(Reader.SQL_SELECTBYNAME.format(condition))
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

    SQL_CREATE = '''
        CREATE TABLE records (
            id INTEGER PRIMARY KEY,
            reader_id TEXT NOT NULL,
            book_id TEXT NOT NULL,
            date_issued DATE NOT NULL,
            date_due DATE NOT NULL
        );
    '''

    SQL_INSERT = ''' 
        INSERT INTO records (
            reader_id,
            book_id,
            date_issued,
            date_due
        )
        VALUES(
            "{}",
            "{}",
            "{}",
            "{}"
        ); 
    '''

    SQL_SELECTBYREADER = '''
        SELECT * from records WHERE reader_id = {};
    '''
    SQL_SELECTBYBOOK = '''
        SELECT * from records WHERE book_id = {};
    '''
    SQL_SELECTBYRECORD = '''
        SELECT * from records WHERE id = {};
    '''

    SQL_DEBTCHECK = '''
        SELECT * from records WHERE date_due < DATE('now');
    '''

    SQL_DELETE = '''
        DELETE * from records WHERE book_id = {};
    '''


    def __init__(self, reader_id, book_id, date_issued, date_due):
        cursor = CONNECTION.cursor()
        self.id = None
        self.reader_id = reader_id
        self.book_id = book_id
        self.date_issued = date_issued
        self.date_due = date_due
        try:
            cursor.execute(self.SQL_CREATE)
        except Exception:
            pass

    def save(self):
        cursor = CONNECTION.cursor()
        cursor.execute(self.SQL_INSERT.format(
            self.reader_id,
            self.book_id,
            self.date_issued,
            self.date_due
        ))
        CONNECTION.commit()
        self.id = cursor.lastrowid



    def __repr__(self):
        rep =  '\nКарточка ' + str(self.id) + '\nЧитатель - ' + str(self.reader_id) + '\nКнига - ' + str(self.book_id) + '\nДата выдачи книги ' + str(self.date_issued) + '\nДата возврата книги - ' + str(self.date_due) + '\n______________ ' 
        return rep

    @staticmethod
    def selectbyreader(condition):
        cursor = CONNECTION.cursor()
        cursor.execute(LibraryRecord.SQL_SELECTBYREADER.format(condition))
        result = []
        for row in cursor.fetchall():
            idx = row[0]
            reader_id = row[1]
            book_id = row[2]
            date_issued = row[3]
            date_due = row[4]
            record = LibraryRecord(reader_id, book_id, date_issued, date_due)
            record.id = idx
            result.append(record)
        return result

    @staticmethod
    def selectbybook(condition):
        cursor = CONNECTION.cursor()
        cursor.execute(LibraryRecord.SQL_SELECTBYBOOK.format(condition))
        result = []
        for row in cursor.fetchall():
            idx = row[0]
            reader_id = row[1]
            book_id = row[2]
            date_issued = row[3]
            date_due = row[4]
            record = LibraryRecord(reader_id, book_id, date_issued, date_due)
            cursor.execute(Reader.SQL_SELECTBYID.format(reader_id))
            for roww in cursor.fetchall():
                idx = roww[0]
                name = roww[1]
                dob = roww[2]
                gender = roww[3]
                adress = roww[4]
                phonenumber = roww[5]
                reader = Reader(name, dob, gender, adress, phonenumber)
                reader.id = idx
                result.append(reader)
            record.id = idx
            result.append(record)
        return result

    @staticmethod
    def selectbyrecord(condition):
        cursor = CONNECTION.cursor()
        
        cursor.execute(LibraryRecord.SQL_SELECTBYRECORD.format(condition))
        result = []
    
        for row in cursor.fetchall():
            
            idx = row[0]
            reader_id = row[1]
            book_id = row[2]
            date_issued = row[3]
            date_due = row[4]
            record = LibraryRecord(reader_id, book_id, date_issued, date_due)
            cursor.execute(Reader.SQL_SELECTBYID.format(reader_id))
            for roww in cursor.fetchall():
                idx = roww[0]
                name = roww[1]
                dob = roww[2]
                gender = roww[3]
                adress = roww[4]
                phonenumber = roww[5]
                reader = Reader(name, dob, gender, adress, phonenumber)
                reader.id = idx
                result.append(reader)
            record.id = idx
            result.append(record)
        
        return result

    def debtcheck():
        cursor = CONNECTION.cursor()
        cursor.execute(LibraryRecord.SQL_DEBTCHECK)
        result = []
        for row in cursor.fetchall():
            
            idx = row[0]
            reader_id = row[1]
            book_id = row[2]
            date_issued = row[3]
            date_due = row[4]
            record = LibraryRecord(reader_id, book_id, date_issued, date_due)
            cursor.execute(Reader.SQL_SELECTBYID.format(reader_id))
            for roww in cursor.fetchall():
                idx = roww[0]
                name = roww[1]
                dob = roww[2]
                gender = roww[3]
                adress = roww[4]
                phonenumber = roww[5]
                reader = Reader(name, dob, gender, adress, phonenumber)
                reader.id = idx
                result.append(reader)
            record.id = idx
            result.append(record)
        return result


import sqlite3

create_dicks_command = '''
    CREATE TABLE dicks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        size INTEGER NOT NULL
    );
'''
