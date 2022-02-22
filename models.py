class Book():
    def __init__(self, 
            idx, 
            bookname, 
            bookauthor, 
            pubdate, 
            bookgenre, 
            bookstate
        ):
        self.id = int(idx)
        self.name = str(bookname)
        self.author = str(bookauthor)
        self.publish_date = str(pubdate)
        self.genre = str(bookgenre)
        self.state = str(bookstate)
    
class Reader():
    def __init__(self, idr, name, dob, gender, adress, phonenumber): 
        self.id = int(idr)
        self.fio = str(name)
        self.dob = str(dob)
        self.gender = str(gender)
        self.adress = str(adress)
        self.phonenumber = str(phonenumber)
    
class LibraryRecord():
    def __init__(self, idx, reader, book, date_issued, date_due):
        self.id = idx
        self.reader_id = reader.id
        self.book_id = book.id
        self.date_issued = date_issued
        self.date_due = date_due



