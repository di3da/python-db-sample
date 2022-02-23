from models import Reader
from models import Book


def register():
    print("Введите номер читателя в 4-значном формате:")
    id = input()
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
    a = Reader(id, fio, dob, gender, adress, phonenumber)
    return a

def addbook():
    print("Введите номер книги в 4-значном формате:")
    id = input()
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
    a = Book(id, bookname, bookauthor, pubdate, bookgenre, bookstate)
    
    return a

def checkbook():
    print("Введите номер билета читателя:")
    id = input()
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