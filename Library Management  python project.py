# library class and its methods....
class Library:
    def __init__(self,booklist,name):
        self.booksList = bookslist
        self.name = name
        self.lendDict = []
    def displayBooks(self):
        print(f"we have following books in our library :{self.name}")
        for book in self.booksList:
            print(book)
    def lendBook(self,book,user):
        if book in bookList:
            
            if book not in self.lendDict.keys():
                self.lenDict.update({book:user})
                print("book has been lended. Database update.")
            else:
                print(f"Book is alredy being used by {self.lendDict[book]}")
        else:
            print("Sorry! we don't have this book in library")
    def addBook(self,book):
        if book in bookList:
            print("book alredy exist")
        else:
            self.bookList.append(book)
            bookDatabase = open(databaseName,'a')
            bookDatabase.write('\n')
            bookDatabase.write(book)
            print('Book added')
    def returnBook(self,book):
        if book in self.lendDict.keys():
            self.lendDict.pop(book)
            print("Book returned successfully")
        else:
            print("the book does not exist in the Book Lending Database")
 # main function - Accepting User Input
def main():
    while(True):
        print(f"welcome to the {library.name} library")
        choice ='''
                1. Display Books
                2. Lend a Book
                3. Add a Book
                4. Return a Book'''
        print(choice)
        userInput = input("press Q to quite and C to continue: ")
        if userInput =='C':
            userInput = int(input("select an option to continuue:"))
            if userChoice == 1:
                library.displayBooks()
            elif userChoice == 2:
                book = input("Enter the name of the book you want to lend:")
                user=input("enter the name of the user: ")
                library.lendBook(book,user)
            elif userChoice == 3:
                book = input("Enter the name of the book you want to add:")
                library.addBook(book)
            elif userChoice == 4:
                book = input("Enter the name of the book you want to return:")
                library.returnBook(book)
            else:
                print("Please chose a valid option")
        elif userInput == 'Q':
            break
        else:
            print("enter the valid option")
    if __name__=='__main__':
    bookList=[]
    databaseName=input("Enter the name of the database file with extension:")
    bookDatabase = open(databaseName,'r')
    for book in bookDatabase:
        booksList.append(book)
        library = Library(booksList,'pythonX')
        main()
      
                                
            
            
            
            
            
