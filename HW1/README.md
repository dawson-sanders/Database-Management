# HW1 File Management System

## Description
This is a CLI program that can manipulate data from a csv file. The csv file contains information regarding all of the Fortune 500 companies such as name, rank, city, state, zip, and number of employees. The goal of this program is to let users mainpulate this data how they want.

## User Options
- Create a New Database: This option allows users to type in the name Fortune500 and create the database as well as output two files. The two outputted files are called Fortune500.config and Fortune500.data. The Fortune500.config contains JSON formatted data about the number of records and sizes of each record. The Fortune500.data file contains all the csv inormation in a data file format. The data file is what will be manipulated when users choose options such as update record, delete record, etc. 
- Open Database: This option allows users to open the newly created database using the name Fortune500. After opening the database users can start to mainpulate its contents.
- Close Database: This option allows users to have the option to close out of the database before quitting the program if they so choose. If the user does not close out of the database before quitting, then the database will be closed automatically. 
- Read/Dispaly Record: This options gives the users a chance to display any record that is in the database by typing in the name of the company. Note that all of the company names are all CAPS in the data files, so the user input for the name of a company should be in all CAPS.
- Update Record: This option allows users to update the number of employees in the database.
- Create Report: This option allows the user to print out the first 10 records in the database.
- Delete Record: This option allows users to delete a record from the database. Note that the record is not totally deleted from the .data file, rarther the records name, rank, city, etc are all changed to 0 or NONE.
- Quit: This option allows users to quit the program.

## User Instructions to run program
- Download/Clone all files from this repository 
- Open the command line and navigate to the correct directory where this repository ended up
- Once at the correct directory type in the command "python3 -B TestDB.py" this will start the program
- Once the program is started users need to use option 1 first and then option 2 second. After the first two options are successful the user can use any other option in any order
