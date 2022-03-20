import models
import sqlite3

models.CONNECTION = sqlite3.connect('library.db')


def register():
    print("Введите ФИО читателя без сокращений:")
    fio = input()
    print("Введите дату рождения читателя в формате yyyy-mm-dd:")
    dob = input()
    print("Введите пол читателя:")
    gender = input()
    print("Введите адрес читателя:")
    adress = input()
    print("Введите телефонный номер читателя:")
    phonenumber = input()
    a = models.Reader(fio, dob, gender, adress, phonenumber)
    a.save()
    print("Читателю присвоен номер ", a.id)
    main()

def addbook():
    print("Введите название книги:")
    bookname = input()
    print("Введите автора книги:")
    bookauthor = input()
    print("Введите дату печати издания:")
    pubdate = input()
    print("Введите жанр книги:")
    bookgenre = input()
    print("Введите состояние книги:")
    bookstate = input()
    a = models.Book(
        bookname, 
        bookauthor, 
        pubdate, 
        bookgenre, 
        bookstate)
    a.save()
    print("Книге присвоен номер", a.id)
    main()

def checkbook():
    print("Выберите условие, по которому нужно найти книгу (name, id):")
    if input() == "id":
        print("Введите номер книги:")
        id = input()
        print(models.Book.selectbyid(id))
        main()
    elif input() == "name":
        print("Введите название книги:")
        name = input()
        print(models.Book.selectbyname(name))
        main()
    else:
        print("Найти книгу можно только по имени или номеру:")
        main()

def checkreader():
    print("Введите условие, по которому нужно найти читателя(name, id):")
    if input() == "id":
        print("Введите номер читателя:")
        id = input()
        print(models.Reader.selectbyid(id))
        main()
    elif input() == "name":
        print("Введите полное ФИО читателя без сокращений:")
        name = input()
        print(models.Book.selectbyname(name))
        main()
    else:
        print("Найти читателя можно только по имени или номеру:")
        main()
    main()

def checkrecord():
    print("Введите условие, по которому нужно найти карточку(reader, book, id):")
    if input() == "id":
        print("Введите номер карточки:")
        id = input()
        print(models.LibraryRecord.selectbyrecord(id))
        main()
    if input() == "reader":
        print("Введите номер читателя:")
        reader_id = input()
        print(models.LibraryRecord.selectbyreader(reader_id))
    if input() == "book":
        print("Введите полное ФИО читателя без сокращений:")
        book = input()
        print(models.LibraryRecord.selectbybook(book))
    main()

def takebook():
    print("Введите id читателя:")
    reader_id = int(input())
    print("Введите id книги:")
    book_id = int(input())
    print("Введите сегодняшнюю дату:")
    date_issued = input()
    print("Введите дату, до которой необходимо вернуть книгу:")
    date_due = input()
    a = models.LibraryRecord(reader_id, book_id, date_issued, date_due)
    a.save()
    print("Номер карточки -", a.id)
    main()

def returnbook():
    print("Введите номер возвращаемой книги:")
    a = input()
    models.LibraryRecord.SQL_DELETE.format(a)
    print("Книга возвращена, запись удалена:")
    main()
    
def debtcheck():
    print(models.LibraryRecord.debtcheck())
    main()

def delbook():
    print("Введите 'id = x' книги:")
    condition = input()
    models.Book.SQL_DELETE.format(condition)
    #не удаляется
    main()

def main():
    print("Введите команду (addbook, register, debtcheck, checkbook, checkreader, checkrecord, takebook, returnbook):")
    message = input()
    if message == "addbook":
        addbook()
    elif message == "register":
        register()
    elif message == "checkbook":
        checkbook()
    elif message == "debtcheck":
        debtcheck()
    elif message == "takebook":
        takebook()
    elif message == "checkreader":
        checkreader()
    elif message == "checkrecord":
        checkrecord()
    elif message == "returnbook":
        returnbook()
    elif message == "delbook":
        delbook()
    elif message == "exit":
        exit()
    else:
        main()
if __name__ == '__main__':
    main()