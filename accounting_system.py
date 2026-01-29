#                             <<  ACCOUNTING SYSTEM  >>

print("Dear user ,this application is an accounting system that" \
"\n calculates your expenses ,income, and net profit." \
"\n income is expressed as a negative value ,and income as a positive value." )

transactions=[]  #empty list

sum=0
sub=0
net=0
i=1
print(" ")

print("Enter your transactions,noting that when expressing expenditure,"
    "\nplease enter negative values. Also,Keep in mind that "
    "\n the program will stop if a value equals zero in entered \n ")

while True:# loop of infinty 
    value= float(input(f"Enter {i} : trasaction\n"))
    if value==0:
        break
    elif value==int or float:
        transactions.append(value)
        i=i+1
    else:
        print("please only enter numbers")

for i in transactions:
    if i > 0 :
        sum+=i
    else:
        sub+=i

net=sub+sum
print(" ")

print(f"your total income is : {sum}")

print(" ")

print(f"total expenses is : {sub}")

print(" ")

print(f"net profit is : {net}")
        
