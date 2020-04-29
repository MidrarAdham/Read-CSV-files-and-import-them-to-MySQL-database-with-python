#import libraries:

import csv
import MySQLdb

#Enter Credentials:

#Connect to MySQL:

mydb = MySQLdb.connect(
        host = "localhost",
        user = "root",
        password = "1111",
        database = "LOAD_PROFILES"
        #auth_plugin = "mysql_native_password"
)
#Initilize cursor:

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS Household1")

#The following command will bring all databases:

mycursor.execute("SHOW DATABASES;")

#To print databases, let python go through all databases and print them

for db in mycursor:
    print(db)

#Create Tables:

# In my case, I used DATETIME instead of Timestamp because timestamp uses DST which causes issues when iterating through summer and winter timestamp.

sql = " CREATE TABLE Household1(sx DATETIME NOT NULL, Vehicle1 INT NOT NULL)"
mycursor.execute("SHOW TABLES")

mycursor.execute(sql)

# In the next block of commands, we will read CSV files and copy its contents into "Household1" table created above.
    # This command asks for which csv file is desired. REMEMBER to put .csv after the file name. EX.file_name.csv

fname=input('file name: ')
    # If no file is specified, "converted0.csv will be chosen by default"
if len(fname) < 1 : fname="converted0.csv"
with open(fname) as csv_file:
    # Read csv file and make sure it is csv. If it is not, use , to seperate data in the file
    csv_reader = csv.reader(csv_file, delimiter=',')
    # Skip Headers
    next(csv_reader)
    # Iterate through the file
    for row in csv_reader:
        # Print each row (NOT RECOMMENDED for PSU Power lab load profiles files because they're huge)
        print(row)
        #res = row[0].split();
        sx = row[0];
        Vehicle1 =row[1]
        # THIS is the format for using MySQL commands with Python.
        data = mycursor.execute('''INSERT INTO Household1 VALUES (%s, %s)''',row)
        #mycursor.execute("data,row")
        mycursor.execute("select * from Household1")
        row = mycursor.fetchall()


mycursor.execute("select * from Household1")
f = mycursor.fetchall()
print(f)
mydb.commit()
# IF YOU USE TERMINAL IN LINUX MACHINE IN THE POWER LAB PSU TO RUN THIS FILE, REMEMBER TO USE "Python3" command.
