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

def main():
    fd = open("readers.txt", "w")
    fd.write(str(register()))
    fd.close()


if __name__ == '__main__':
    main()