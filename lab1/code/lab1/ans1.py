
'take input form the user'
password=input("Enter password");

'declare variables'
hasNumber=False
hasUpperCase=False
haslowerCase=False
hasSpecial=False
inRange=True if len(password)>5 and len(password)<17 else False

'loop to set all variable according to condition'
if inRange:
    for w in password:
        if w.isupper():
            hasUpperCase=True
        if w.islower():
            haslowerCase=True
        if w.isnumeric():
            hasNumber=True
        if w in "[$@!*]":
            hasSpecial=True
else:
    print("Pasword must be in length of 6 to 16")

'validate all the condition is true'
if hasSpecial and hasNumber and hasUpperCase and haslowerCase:
    print("You chose write password")
else:
    print("Password is not matching with criteria")
