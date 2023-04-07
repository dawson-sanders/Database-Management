#================================================================
# Name: Dawson Sanders
# Date: 2/13/23
# Description: This is the main file where the user interface is.
#              The UI will allow users to test the Database.py file
#================================================================
from DB import DB

def printMenu():
    print("=================================================================")
    print("                         DataBase Menu                           ")
    print("=================================================================")
    print("1) Create a New Database")
    print("2) Open Database")
    print("3) Close Database")
    print("4) Read/Display Record")
    print("5) Update Record")
    print("6) Create Report")
    print("7) Delete Record")
    print("8) Quit") 

printMenu()
sample = DB()
choice = input("Choose from the options above (enter integer): ")

while choice != '8':
    if (choice == '1'):
        print("=================================================================")
        print("                        Create New Databse                       ")
        print("=================================================================")
        filename = input("Please type in the prefix of a .csv file: ")
        sample.createDB(filename)
        printMenu()
        choice = input("Choose from the options above (enter integer): ")
    elif (choice == '2'):
        print("=================================================================")
        print("                           Open Databse                          ")
        print("=================================================================")
        userDatabaseName = input("Please type in the prefix of a database to open: ")
        sample.openDB(userDatabaseName)
        printMenu()
        choice = input("Choose from the options above (enter integer): ")
    elif (choice == '3'):
        print("=================================================================")
        print("                           Close Databse                         ")
        print("=================================================================")
        sample.closeDB()
        printMenu()
        choice = input("Choose from the options above (enter integer): ")
    elif (choice == '4'):
        print("=================================================================")
        print("                        Read/Display Record                      ")
        print("=================================================================")
        sample.displayRecord()
        printMenu()
        choice = input("Choose from the options above (enter integer): ")
    elif (choice == '5'):
        print("=================================================================")
        print("                           Update Record                         ")
        print("=================================================================")
        sample.updateRecord()
        printMenu()
        choice = input("Choose from the options above (enter integer): ")
    elif (choice == '6'):
        print("=================================================================")
        print("                           Create Report                         ")
        print("=================================================================")
        sample.createReport(0)
        sample.createReport(1)
        sample.createReport(2)
        sample.createReport(3)
        sample.createReport(4)
        sample.createReport(5)
        sample.createReport(6)
        sample.createReport(7)
        sample.createReport(8)
        sample.createReport(9)
        printMenu()
        choice = input("Choose from the options above (enter integer): ")
    elif (choice == '7'):
        print("=================================================================")
        print("                            Delete Record                        ")
        print("=================================================================")
        sample.deleteRecord()
        printMenu()
        choice = input("Choose from the options above (enter integer): ")
    else:
        print("Invalid input, please select choice from the list")
        printMenu()
        choice = input("Choose from the options above (enter integer): ")
if DB.isOpen:
    print("You left the database opened!")
    print("Closing database automatically...")
    sample.closeDB()
print("Quitting...")


