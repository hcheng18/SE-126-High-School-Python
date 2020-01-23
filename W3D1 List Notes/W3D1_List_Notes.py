#Week 3 Day 1: Importing Data from a File

#List can hold multiple points and data to store them to "memory" so they can be used later in our program.

import csv
import turtle

total_records = 0


  total_salaries = 0


#CREATE EMPTY LISTS -- Processor needs to know that they're lists and not variables
#Create a list for each field within the file (also err on the side of the longest record)



name = []
age = []
salary = []



print("{0:.10}\t{1:.10}\t      {2.10}".format("NAME", "AGE", "SALARY"))









#STEP 2: CONNNECT TO THE FILE LOCATION
#right-click the text/csv file in folder view --> "Properties" to find the file b   v  location
#these file locations are cAsE sEnSiTiVe & space/special character sensitive so DOUBLE CHECK THEM!
#flip all '\' to '/'
with open("C:/Users/008007270/Downloads/example.csv") as csvfile:


    #notice ':' everything must be INDENTED now (until we're ready to "close" the file)

    #STEP 3: ALLOW THE FILE TO BE READ BY OUR PROGRAM
    file = csv.reader(csvfile)
    #now the file we have connected is known in the program as 'file'
    #file has several records, each record has several fields

    #below is a FOR loop
    #for loops are loops -- continually repeated sequence of code
    #they continue NOT based on a CONDITION but on a RANGE
    #range: '0 - 10', 'a - f'
    
    #STEP 4: ACTUALLY READ/PROCESS THE FILE DATA, ONE RECORD AT A TIME
    total_records = 0
    for rec in file:


        #notice the ':' everything in the for loop must be INDENTED
        #RANGE: for each record in the file, do the following
        #rec is a variable that is initialized the the for loop range
        #           on line 35
        
        total_records += 1
        #SHORTHAND VERSION of: total_records = total_records + 1
        print(rec[0])
                    #print entire record of file. we are seeing this as a LIST
                    #lists can hold multiple points of data at once
                    #in order to specify a data point over another, we need to know its POSITION IN THE LIST

        #print only the names in the file -- specify position of data in lit
            

            

        #add all salaries to total_salary -- REMEMBER: all data entering a Python program is treated as a STRING unless cast otherwise
        
        total_salaries += int(rec[2])

        #STORE FIELD DATA INTO LISTS
        name.append(rec[0]) #append (add) value stored in rec[0] into the list 'name'
        age.append(rec[1])
        salary.append(float(rec[2])) #<------- casting salary value as float for easier numeric processing later
        extra.append("x") #can be stored value or constant value

        print(rec)
        
        #add field width to ensure columns stay aligned
        print("{0:.10}\t{1:.10}\t${2:10}".format(rec[0], rec[1], int(rec[2])))

#closing file ---- disconnecing from file path
#we can disconnect because all file data is now stored into LISTS
#"process list" = FOR LOOP

for index in range(0, total_records): #index will start at 0 and run as many times as the value stored in 'records'-- index will grow by +1 each time through the for loop

    print("INDEX:", index, "\t {0} {1} {2}".format(name[index], age[index], salary[index]))


#process the lists to calcculate total_salary

for index in range(0, total_recourds):

    total_salaries += salary[index]
#print final values: total records processed and total salary of all employees in file
print("TOTAL RECORDS:", total_records)
print("TOTAL SALARY: ${0:.2f}".format(total_salaries))