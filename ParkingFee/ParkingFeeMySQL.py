import mysql.connector as sql
from time import localtime

MyDB = sql.connect(host='localhost', user='root', password='modern', database='Test')
MyCursor = MyDB.cursor()

#Creating database in case it doesn't exist
try:
    MyCursor.execute('Create Database Test;')
    MyCursor.execute('Create Table Vehicles (VehicleID CHAR(4), InTime CHAR(5), ExitTime CHAR(5)), HoursStayed INT, Fee INT;')
except:
    pass

HourlyFee = 20

def Entry():
    VehicleNo = input('Enter 4-digit vehicle number: ')
    InTime= input('Enter Entrance Time(format: hour minute) or Enter "0" for current time: ')       #Time to be entered in 24-hour format
    
    if InTime == '0':
        InTime = f'{localtime().tm_hour} {localtime().tm_min}'          #Use current time
    
    sql = 'Insert Into Vehicles (VehicleID, InTime) Values(%s, %s);'
    val = (VehicleNo, InTime)

    MyCursor.execute(sql, val)
    MyDB.commit()
    print('Record appended!\n')
    
def Exit(VehicleNo):
    
    MyCursor.execute(f'Select InTime from Vehicles where VehicleID = {VehicleNo};')
    
    try: 
        InTime = MyCursor.fetchall()[0][0]
        print(InTime)           #Fetching Data in case it exists
    except:
        print('No such Vehicle found')
        return 0
    OutTime= input('Enter Exit Time(format: hour minute) or Enter "0" for current time: ')          #Time to be entered in 24-hour format
    
    if OutTime == '0':
        OutTime = f'{localtime().tm_hour} {localtime().tm_min}'         #Use current time
    
    Out = OutTime.split()
    In = InTime.split()
    hours = int(Out[0]) - int(In[0])        #Calculating hours stayed
    
    if (int(Out[1])<int(In[1])):
        hours -= 1
    
    Fee = hours * HourlyFee                 #Calculating Total Fees
    
    sql = 'UPDATE Vehicles SET ExitTime = %s, HoursStayed = %s, Fee = %s WHERE VehicleID = %s;'
    val = (OutTime, hours, Fee, VehicleNo)
    
    MyCursor.execute(sql, val)
    MyDB.commit()
    
    return hours, Fee

def Display():
    
    MyCursor.execute('SELECT * FROM Vehicles;')         #Fetching all the data
    results = MyCursor.fetchall()
    
    if results:
        print('VehicleID, InTime, ExitTime, HoursStayed, Fee')
        for i in results:
            print(i)
        print('\n')
        
    else:
        print("No data found.\n")

    
while True:
    choice = input('1. Vehicle Entrance\n2. Vehicle Exit\n3. Change Parking Fee\n4. View Data\n5. Clear Data\n6. Exit\n\nEnter choice: ')
    
    if choice == '1':
        Entry()
        
    elif choice == '2':
        VehicleNo = input('Enter VehicleNo: ')
        hours, Fee = Exit(VehicleNo)
        print('Hours stayed: ', hours, '; Amount to be paid: ', Fee, '\n')
    
    elif choice == '3':
        HourlyFee = int(input('Enter new hourly fee: '))
        
    elif choice == '4':
        Display()
    
    elif choice == '5':
        MyCursor.execute('DELETE FROM Vehicles;')
        MyDB.commit()
        print('Cleared successfully!')
    
    elif choice == '6':
        break
    
    else:
        print('Invalid Input')