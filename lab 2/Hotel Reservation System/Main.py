
#create class Room
class Room(object):
    def __init__(self,number,roomType,price):
        self.number=number
        self.roomType=roomType
        self.price=price

#create a class named Hotel
class Hotel(object):
    #Static Properties declaration
    totalRooms = 76
    soldRooms = 51
    availableRooms = 22
    roomForMaintenance = 3
    counterBalance=401

    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.houseKeepers={}
        self.fdEmployee = {}
        self.rooms=list()

    #method to register housekeepr
    def registerHouseKeep(self,houseKeeper):
        self.houseKeepers[houseKeeper.name]=houseKeeper
        print(houseKeeper.name, " is added as a Housekeeper")

    #method to register FrontDesk Employee
    def registerFrontDeskEmployee(self, fdEmployee):
        self.fdEmployee[fdEmployee.name]=fdEmployee
        print(fdEmployee.name, " is added as a front desk employee")

    #method to get Status of motel
    def getStatus(self):
        print("----------------Hotel",self.name ,"Status------------------")
        print("Total rooms: ",Hotel.totalRooms)
        print("Sold rooms: ", Hotel.soldRooms)
        print("Available rooms: ", Hotel.availableRooms)
        print("Rooms under maintenance: ", Hotel.roomForMaintenance)
        print("------------------------------------------------------------")

     #method to register room
    def registerRooms(self,room):
        self.rooms.append(room)

#create a class named Person
class Person:
    def __init__(self,name,age,phNo):
        self.name=name
        self.age=age
        self.phNo=phNo
#creare class named Customer which inherits Person
class Customer(Person):
    def __init__(self,name,age,phNo):
        super().__init__(name,age,phNo)

#creare class named House Keeper which inherits Person
class HouseKeeper(Person):
    def __init__(self,name,age,phNo):
        super().__init__(name,age,phNo)
        self.roomsAssigned=0

    def assignRooms(self,roomsAssigned):
        self.roomsAssigned=roomsAssigned

#creare class Front Desk employee which inherits Person
class FrontDeskEmployee(Person):
    def __init__(self,name,age,phNo):
        super().__init__(name, age, phNo)
        self.selectedRoomNumber=0
        self.salary=10000

    # method to open shift
    def openShift(self):
        print("------------------------------------------------------------")
        print("Shift opened by ",self.name)

    # method to register Customer
    def registerCustomer(self):
        print("-----------------------Take Customer Details---------------")
        name=input("Customer Name")
        age=input("Customer Age")
        phNo=input("Customer Phone Number")
        customer=Customer(name,age,phNo)
        print("Customer ",customer.name ," registered successfully")

    #
    def calculateCounterBalance(self):
        print("Counter balance is ",Hotel.counterBalance)

    def askForRoom(self,hotel):
         print("-----------------------Take Room Requirement---------------")
         roomType=input("What kind of room required? ")
         price= int(input("Price? "))
         rooms=list()

         #get rooms that matches requirement
         for room in hotel.rooms:
             if room.price==price or room.roomType==roomType :
                rooms.append(room)
         print("Available rooms are")
         for room in rooms:
             print("Room Number: ",room.number," Room type: ",room.roomType," Price: ",room.price)

    def bookRoom(self):
        selectedRoomNumber=int(input("Which room you want to book? "))

        #book room by selected customer
        for room in hotel.rooms:
            if room.number == selectedRoomNumber:
                print("Congrats!!!!")
                print("You booked Room Number ",room.number," Room Type ",room.roomType," Price ",room.price)
                Hotel.availableRooms= Hotel.soldRooms- 1
                Hotel.soldRooms= Hotel.soldRooms+1
                Hotel.counterBalance = Hotel.counterBalance+room.price
                break

    def closeShift(self):
        print("Shift Closed")

#Hotel Registartion and Setup
hotel=Hotel("Quality Inn","5100 Cherry St,kcmo, 64109")
hotel.getStatus()

room1=Room(101,"Double bed",70)
hotel.registerRooms(room1)
room2=Room(201,"Queen bed",50)
hotel.registerRooms(room2)
room3=Room(301,"King bed",60)
hotel.registerRooms(room3)
room4=Room(102,"King bed",60)
hotel.registerRooms(room4)
room5=Room(103,"Double bed",70)
hotel.registerRooms(room5)
room6=Room(202,"Queen bed",50)
hotel.registerRooms(room6)

houseKeep1=HouseKeeper("Bharat","21","8512541236")
houseKeep1.roomsAssigned=15

houseKeep2=HouseKeeper("Raju","35","9856325412")
houseKeep2.roomsAssigned=32

hotel.registerHouseKeep(houseKeep1)
hotel.registerHouseKeep(houseKeep2)


fdEmplyee1=FrontDeskEmployee("Vinita","30","8163288464")
fdEmplyee2=FrontDeskEmployee("Jinal","26","8511318649")

hotel.registerFrontDeskEmployee(fdEmplyee1)
hotel.registerFrontDeskEmployee(fdEmplyee2)

#Shift oper
fdEmplyee1.openShift()
#callculate Balance
fdEmplyee1.calculateCounterBalance()

# get customer info and register customer
fdEmplyee1.registerCustomer()

#Adsk for room and book room
fdEmplyee1.askForRoom(hotel)
fdEmplyee1.bookRoom()
fdEmplyee1.calculateCounterBalance()

#show hotel status
hotel.getStatus()
