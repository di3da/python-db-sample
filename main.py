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
    print("Книге присвоен номер ", a.id)

def checkbook():
    print("Введите условие, чтобы вывести все книги, к которым оно применимо:")
    condition = input()
    models.Book.select(condition)
#здесь нужно обратиться к хранилищу по полученному номеру читателя 
#    print(Book(bookname, bookgenre))

def debtcheck():
#обращаемся ко всем книгам в хранилище
#условием выводим в список fio, dob и adress каждого владельца книги, у которой истек срок
    pass


def main():
    print("Введите команду (addbook, register, debtcheck, checkbook):")
    message = input()
    if message == "addbook":
        addbook()
    elif message == "register":
        register()
    elif message == "checkbook":
        checkbook()
    elif message == "debtcheck":
        debtcheck()
    else:
        main()


if __name__ == '__main__':
    main()