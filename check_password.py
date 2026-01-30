                           #< check password >#

password=input("enter your password\n")

lenght=len(password) # The "len" function was used to counter lenght of password

has_digit=any(char.isdigit() for char in password) # this line checks if there are any number in the password

has_upper=any(char.isupper() for char in password)  # this line checks for the 
                                                   # presence of at least one capital letter 

has_lower=any(char.islower() for char in password) # this line checks for the 
                                                   # presence of at least one small letter

if lenght >= 8 and has_lower and has_digit and has_upper:
    print(" your password is storng ")
else:
    print("please enter password agine, your password must contion 8 letters, " \
    "\n including at least one number, at least one uppercase letter, and lowercase letter.")