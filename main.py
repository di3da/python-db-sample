import models
import sqlite3

models.CONNECTION = sqlite3.connect('library.db')


def register():
    print("Введите ФИО читателя без сокращений:")
    fio = input()
    print("Введите дату рождения читателя в формате dd.mm.yyyy:")
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
    print("Введите условие, чтобы вывести все книги, к которым оно применимо:")
    condition = input()
    print(models.Book.select(condition))
    main()

def checkreader():
    print("Введите 'id = x' читателя:")
    condition = input()
    print(models.Reader.select(condition))
    main()

def checkrecord():
    print("Введите 'id = x' для доступа по номеру карточки:")
    condition = input()
    print(models.LibraryRecord.select(condition))
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