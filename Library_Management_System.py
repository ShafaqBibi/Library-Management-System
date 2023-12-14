
print("\nWelcom To The Book World\n")

Books = []

def addBook():
    bookName = input("Enter book name you want to add: ")
    if bookName in Books:
        print("\nAlready Exist") 
    else:
        Books.append(bookName)
        print("\nBook: " + bookName + " Successfully added!")


def remBook():
    bookName = input("Enter book name you want to remove: ")
    if bookName in Books:
        Books.remove(bookName)
        print("\nBook: " + bookName + " successfully removed!")
    else:
        print("\nNot Exist")

def retBook():
    if not Books:
        print("Library is empty... You can add books in library")
    else:
        print("Available Books: ")
        for b in Books:
            print(b)
            

while True:
    ques = input("Want to Remove, Add or Check any book? (R/A/C): ")
    if ques.lower() == 'r':
        remBook()
    elif ques.lower() == 'a':
        addBook()
    elif ques.lower() == 'c':
        retBook()
    else:
        print("Invalid input!")

    ask = input("Want to exit? (y/n): ")
    if ask.lower() == 'y':
        break

    
