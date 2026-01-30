

from collections import Counter # this line a library for counting elements. it's 
                                # always best to place it at the beginning of the code to 
                                # protect the processor from overload, because evry time, which leads to
                                # processor overload.

def check_ip():
    i=0
    num=int(input("Enter the number that expresses the number of elrments in list\n"))
    
    ip_list=[] # empty list 
    
    for i in range(num):
        
        ip=input(f"enter IP address number {i+1}\n")
        
        ip_list.append(ip)

        print(" ")
        
        print(f"remainder of the number is {num-(i+1)}")
    
    print(" ")
    
    iteration=Counter(ip_list) # the counter function used to count elements in list.
    
    print(f"number of elements is {iteration}")
    
    print(" ")
    
    print(f"the most frequently occurring element is {iteration.most_common(1)[0]}")

    most_iteration=iteration.most_common(1)[0]  # This line means enter the variable in which the elements were arranged.
                                                # And do the following:
                                                # I only need one of the most frequently used elements.
                                                # Secondly, I want the value of this element.
                                                               

    count=most_iteration[1]   # This means that this variable,
                              # which contains a list, has a list containing two elements, 
                              # the first of which is number 0 and the second is number 1. 
                              # The same variable, and position number 1 contains the number of IP addresses,
                              # where position number 0 contains the address.
                             
                            
    print(" ")
    
    if count>=5:
    
        print ("tring hacker")
    
    else:
    
        print("Dont wory evry thing is nuture. ")



check_ip()