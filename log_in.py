user="abdullah hossam"

name=input("Enter your name please\n").lower()

pass_word=20112007 # Access PIN 

success=3 # Number of attepeds allowed 

i=1 # counter

while success !=0:
    number_of_attemped=int(input(f"Enter your password , you have {success} attepts .\n")) 
    # Enter the number of attmped

    if number_of_attemped == pass_word and name==user :
        print(f"Welcom for you {name}")
        break
    else:
        print ("try again, {success} attempts remaining.")
        success-=1


    