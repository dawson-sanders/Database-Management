#================================================================
# Name: Dawson Sanders
# Date: 2/13/23
# Description: This is the DB class that holds all variables and functions 
#              to perform operations on a csv file
#================================================================
import csv
import os.path
import json

class DB:
    isOpen = False

    # Default Constructor
    def __init__(self):
        self.filestream = None
        self.numRecords = 0
        self.numOverflow = 0
        self.dataFilePtr = None
        self.record_size = 91    # This is the number of bits that a single record line has 


    # Create Database
    def createDB(self, filename):
        if filename == "Fortune500":
            # Generate File Names
            csv_filename = filename + ".csv"
            data_filename = filename + ".data"
            config_filename = filename + ".config"

            # Read the CSV file and write into data files
            with open(csv_filename, "r") as csv_file:
                data_list = list(csv.DictReader(csv_file, fieldnames = ('NAME', 'RANK', 'CITY', 'STATE', 'ZIP', 'EMPLOYEES')))
                self.numRecords = len(data_list)

            # Write Formatting files with spaces so each field is fixed length, i.e. ID field has a fixed length of 10
            def writeRecord(filestream, dict):
                filestream.write("{:40.40}".format(dict["NAME"]))
                filestream.write("{:5.5}".format(dict["RANK"]))
                filestream.write("{:20.20}".format(dict["CITY"]))
                filestream.write("{:5.5}".format(dict["STATE"]))
                filestream.write("{:10.10}".format(dict["ZIP"]))
                filestream.write("{:10.10}".format(dict["EMPLOYEES"]))
                filestream.write("\n")
            
            # Write data file 
            with open(data_filename, "w") as data_outfile:
                for dict in data_list:
                    writeRecord(data_outfile, dict)
            print("Database was successfully created!")
            print("Input File: " + csv_filename + " \n" + "Output files: " + config_filename + ", " + data_filename)
            DB.isOpen = False
            
            # Write config file
            with open(config_filename, "w") as config_outfile:
                config_outfile.write(
                    "{\"numRecords\": \"" 
                    + str(self.numRecords)
                    + "\", \"name size\": \"40\",\""
                    + "rank size\": \"5\",\""
                    + "city size\" :\"20\",\""
                    + "state size\" :\"5\",\""
                    + "zip size\" :\"10\",\""
                    + "employees size\" :\"10\"} \n")
        else:
            print("Invalid filename please try again.")


    # Open database method that reads the database
    def openDB(self, userDatabaseName):
        if userDatabaseName == "Fortune500":
            self.dataFilePtr = userDatabaseName
            data_filename = userDatabaseName + ".data"
            config_filename = userDatabaseName +".config"
            if not os.path.isfile(data_filename):
                print("ERROR: " + data_filename + " not found, please create DataBase first.")
            elif not DB.isOpen:
                # 1. read numRecords from config file
                self.config_file = open(config_filename, 'r')
                jsonData = json.load(self.config_file)
                numR = jsonData['numRecords']
                self.numRecords = int(numR)

                # 2. opens the data file in read/write mode
                self.data_file = open(data_filename, 'r+')

                # 3. updates values in any other instance variables
                DB.isOpen = True
                print("Database " + userDatabaseName + " is successfully opened")
                print("Database contains " + str(numR) + " records")
                return DB.isOpen
            else:
                print("ERROR: Another database is opened, please select option 3 to close it first")
        else:
            print("Invalid prefix of database. Please try again.")


    # Helper method to help binary search method
    def findRecord(self, recordNum):
        self.flag = False
        name = rank = city = state = zip = employees = "None"

        if recordNum >= 0 and recordNum < self.numRecords:
            self.data_file.seek(0, 0)
            self.data_file.seek(recordNum * self.record_size)
            recLine = self.data_file.readline().rstrip('\n')
            self.flag = True
        
        if self.flag:
            name = recLine[0:40].strip()
            rank = recLine[40:45]
            city = recLine[45:65]
            state = recLine[65:70]
            zip = recLine[70:80]
            employees = recLine[80:90]

        self.record = dict(
            {
                "NAME": name,
                "RANK": rank,
                "CITY": city,
                "STATE": state,
                "ZIP": zip,
                "EMPLOYEES": employees
            }
        )


    # Binary search by the name 
    def binarySearch (self, recordName):
        low = 0
        high = self.numRecords - 1
        self.found = False

        while high >= low:
            self.middle = (low + high) // 2
            self.findRecord(self.middle)
            mid_name = self.record["NAME"]
            
            if mid_name == recordName:
                self.found = True
                break
            elif mid_name > recordName:
                high = self.middle - 1
            elif mid_name < recordName:
                low = self.middle + 1

        
    # Display record method
    def displayRecord(self):
        if DB.isOpen:
            recordName = input("Enter the record name to search for: ")
            self.binarySearch(recordName)

            if self.found == True:
                print(
                        "NAME: " + self.record["NAME"].replace("_"," ") + 
                        "\t RANK: " + self.record["RANK"] + 
                        "\t CITY: " + self.record["CITY"] + 
                        "\t STATE: " + self.record["STATE"] + 
                        "\t ZIP: " + self.record["ZIP"] + 
                        "\t EMPLOYEES: " + str(self.record["EMPLOYEES"])
                )
            else:
                print("Error: Record not found please try again.")

        else:
            print("ERROR: Cannot find opened database. Please select option 1 to create a database or option 2 to open a database.")
    

    # Helper method to update/delete record by rewriting the record
    def writeRecord2(self, dict, recordNum):
        filestream = open("Fortune500.data", "r+")
        filestream.seek(recordNum * self.record_size, 0)
        filestream.write("{:40.40}".format(dict["NAME"]))
        filestream.write("{:5.5}".format(dict["RANK"]))
        filestream.write("{:20.20}".format(dict["CITY"]))
        filestream.write("{:5.5}".format(dict["STATE"]))
        filestream.write("{:10.10}".format(dict["ZIP"]))
        filestream.write("{:10.10}".format(dict["EMPLOYEES"]))
        filestream.write("\n")
        filestream.close()


    # Update record method which allows users to update the number of employees
    def updateRecord(self):
        if DB.isOpen:
            recordName = input("Enter the record name to update: ") 
            self.binarySearch(recordName)
            if self.record["NAME"] == "None":
                print("ERROR: Record name not found. Please try again.")
            else:
                updateEmployees = input("Enter the new number of employees: ")
                print("Success! Record has updated to " + updateEmployees + " employees!")
                self.record["EMPLOYEES"] = updateEmployees
                self.writeRecord2(self.record, self.middle)

                print(
                    "NAME: " + self.record["NAME"].replace("_"," ") + 
                    "\t RANK: " + self.record["RANK"] + 
                    "\t CITY: " + self.record["CITY"] + 
                    "\t STATE: " + self.record["STATE"] + 
                    "\t ZIP: " + self.record["ZIP"] + 
                    "\t EMPLOYEES: " + str(self.record["EMPLOYEES"])
                )
        else:
            print("ERROR: Cannot find opened database. Please select option 1 to create a database or option 2 to open a database.")


    # Create record method
    def createReport(self, recordNum):
        if DB.isOpen:
            self.flag = False
            name = rank = city = state = zip = employees = "None"
            if recordNum >= 0 and recordNum < self.numRecords:
                self.data_file.seek(0, 0)
                self.data_file.seek(recordNum * self.record_size)
                recLine = self.data_file.readline().rstrip('\n')
                self.flag = True
            else:
                print("ERROR: Input is out of record range, please enter number from 0 to " + str(self.numRecords - 1))
        
            if self.flag:
                name = recLine[0:40]
                rank = recLine[40:45]
                city = recLine[45:65]
                state = recLine[65:70]
                zip = recLine[70:80]
                employees = recLine[80:90]

                self.record = dict(
                    {
                        "NAME": name,
                        "RANK": rank,
                        "CITY": city,
                        "STATE": state,
                        "ZIP": zip,
                        "EMPLOYEES": employees
                    }
                )

            print(
                    "NAME: " + self.record["NAME"].replace("_"," ") + 
                    "\t RANK: " + self.record["RANK"] + 
                    "\t CITY: " + self.record["CITY"] + 
                    "\t STATE: " + self.record["STATE"] + 
                    "\t ZIP: " + self.record["ZIP"] + 
                    "\t EMPLOYEES: " + str(self.record["EMPLOYEES"])
            )
        else:
            print("ERROR: Cannot find opened database. Please select option 1 to create a new database and then option 2 to open a database.")


    # Delete record method
    def deleteRecord(self):
        if DB.isOpen:
            recordName = input("Enter the record name to delete: ")
            self.binarySearch(recordName)

            if self.record["NAME"] == "None":
                print("ERROR: Record name not found. Please try again.")
            else:
                print("Record content deleted successfully!")
                self.record["NAME"] = "None"
                self.record["RANK"] = "0"
                self.record["CITY"] = "NONE"
                self.record["STATE"] = "NA"
                self.record["ZIP"] = "0"
                self.record["EMPLOYEES"] = "0"
                self.writeRecord2(self.record, self.middle)

                print(
                    "NAME: " + self.record["NAME"].replace("_"," ") + 
                    "\t RANK: " + self.record["RANK"] + 
                    "\t CITY: " + self.record["CITY"] + 
                    "\t STATE: " + self.record["STATE"] + 
                    "\t ZIP: " + self.record["ZIP"] + 
                    "\t EMPLOYEES: " + str(self.record["EMPLOYEES"])
                )
        else:
            print("ERROR: Cannot find opened database. Please select option 1 to create a database or option 2 to open a database.")


    # Close database method
    def closeDB(self):
        if DB.isOpen:
            self.numRecords = 0
            self.filestream = None
            self.data_file.close()
            self.config_file.close()
            self.dataFilePtr = None
            DB.isOpen = False
            print("Current database successfully closed")
            return DB.isOpen
        else:
            print("ERROR: No opened database. Please select option 2 to open a database.")