class library :
    def __init__(self,books) :
        self.books = books

    def avilableBooks(self) :
        print("the list of the books are : ")
        for book in self.books :
            print(" *",book)
        
    def borrowBook(self,bookName) :
        if bookName in self.books :
            print(f"You have been issued {bookName} \nPlease keep it safe and return within 30 days")
            self.books.remove(bookName)

        else :
            print("sorry, this book has alrady been issued to someone else or not avilable. \nPlease wait untill the book is returned or to donet by someone!! ")

    def returnBook(self,bookName) :
        self.books.append(bookName)
        print("Thanks for return/donet this book!")

class student :
    def requestBook(self) :
        book = input("Enter the book name you want to borrow : ")
        return book

    def returnBook(self) :
        book = input("Enter the book name you want to return/donet : ")
        return book

centralLibrary = library(["DMS","python notes","Evs","cengle"])
smith = student()

while (True) :
    welcomeMsg ='''***** Welcome to the central library *****
    1.list of books
    2.borrow the book
    3.return/donet the book
    4.exit the library
    '''
    print(welcomeMsg)

    a = int(input("Enter your choice : "))


    if a==1 :
            centralLibrary.avilableBooks()
    elif a==2 :
            centralLibrary.borrowBook(smith.requestBook())
    elif a==3 :
            centralLibrary.returnBook(smith.returnBook())
    elif a==4 :
            print("Thank for using central library \nWe are out of the library \nHave a great day ahead!")
            exit()
    else:
            print("invalid input comand")

    

    

