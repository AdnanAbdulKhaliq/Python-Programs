import csv
from time import localtime 

file = open('ParkingFee/ParkingData.csv', 'r', newline='\n')

Data=[]
Read=csv.reader(file)
for row in Read:
    Data.append(row)
Data=Data[1:]
file.close()

HourlyFee = 20

def Entry():
    
    VehicleNo = input('Enter 4-digit vehicle number: ')
    InTime= input('Enter Entrance Time(format: hour minute) or Enter "0" for current time: ')       #Current time to be entered in 24-hour format
    if InTime == '0':
        InTime = f'{localtime().tm_hour} {localtime().tm_min}'
        
    file = open('ParkingFee/ParkingData.csv', 'a')
    w=csv.writer(file)
    Row=[VehicleNo, InTime, '', '', '']
    w.writerow(Row)
    Data.append(Row)
    file.close()
    
    return 0
    
def Exit():
    
    VehicleNo = input('Enter Vehicle No: ')
                
    for i in Data:
        if i[0] == VehicleNo:
            InTime = i[1]
            break
    else:
        print('Vehicle Not Found\n\n')
        return 0
    
    OutTime= input('Enter Exit Time(format: hour minute) or Enter "0" for current time: ')          #Current time to be entered in 24-hour format
    if OutTime == '0':
        OutTime = f'{localtime().tm_hour} {localtime().tm_min}'

    Out=OutTime.split()
    In=InTime.split()
    hours = int(Out[0]) - int(In[0])
    if (int(Out[1])<int(In[1])):
        hours -= 1

    Fee = hours * HourlyFee

    for i in Data:
        if i[0] == VehicleNo:
            i[2] = OutTime
            i[3] = hours
            i[4] = Fee
    
    print(f'\n\nNumber of hours: {hours}\nAmount to be paid: Rs.{Fee}\n\n\n')
    return 0

def Display():
    print(['Vehicle Number', 'In Time', 'Exit Time', 'Hours stayed', 'Fee'])
    for i in Data:
        print(i)
    print('\n\n')
    
    
while True:
    choice = input('1. Vehicle Entrance\n2. Vehicle Exit\n3. Change Parking Fee\n4. View Data\n5. Clear Data\n6. Save and Exit\n\nEnter choice: ')
    
    if choice == '1':
        Entry()
        
    elif choice == '2':
        Exit()
    
    elif choice == '3':
        HourlyFee = int(input('Enter new hourly fee: '))
        
    elif choice == '4':
        Display()
    
    elif choice == '5':
        file = open('ParkingFee/ParkingData.csv', 'w')
        w=csv.writer(file)
        w.writerow(['Vehicle Number', 'In Time', 'Exit Time', 'Hours stayed', 'Fee'])
        file.close()
        Data=[]
    
    elif choice == '6':
        file = open('ParkingFee/ParkingData.csv', 'w')
        w=csv.writer(file)
        w.writerow(['Vehicle Number', 'In Time', 'Exit Time', 'Hours stayed', 'Fee'])
        w.writerows(Data)
        file.close()
        break       
    
    else:
        print('Invalid Input')