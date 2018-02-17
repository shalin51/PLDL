
"contact list"
Contact_list=[
    {"name":"Rashmi","number":"8797989821","email":"rr@gmail.com"},
    {"name":"Saria","number":"9897989821","email":"ss@gmail.com"},
    {"name": "shalin", "number": "5214521452", "email": "shalin@gmail.com"},
    {"name":"patel","number":"9659874632","email":"patel@gmail.com"},
    {"name":"megha","number":"9853200147","email":"megha@gmail.com"},
]

prompt="""Choose operation by entering number:
press a to display contact by name
press b to display contact by number
press c to edit contact by name
press any character to exit 
"""

'function to display contact by name'
def contactByName():
    name=input("Enter name to find contact: ")
    for contact in Contact_list:
        if(contact.get('name')==name):
            print("{name:",contact.get('name'),", number:",contact.get('number'),", email:",contact.get('email'),"}")

'function to display contact by number'
def contactByNumber():
    number = input("Enter number to find contact: ")
    for contact in Contact_list:
        if (contact.get('number') == number):
            print("{name:", contact.get('name'), ", number:", contact.get('number'), ", email:", contact.get('email'),
                  "}")

'function to edit contact by name'
def editByName():
    name = input("Enter name to find contact: ")
    for contact in Contact_list:
        if (contact.get('name') == name):
            number=input("Enter new number: ")
            contact['number']=number
            print("Updated contact is {name:", contact.get('name'), ", number:", contact.get('number'), ", email:", contact.get('email'),
                  "}")

"dictionary for operation"
operationDic={
    "a":contactByName,
    "b":contactByNumber,
    "c":editByName,
}


while(1==1):
    userInput=input(prompt)
    if userInput in ["a","b","c"]:
       operationDic[userInput]()
    else:
        break

        

