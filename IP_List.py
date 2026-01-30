list_ip=["129.168.1.1","10.0.0.1","127.16.0.1","129.168.1.1","10.0.0.1"] #IP list 

list2=set(list_ip) # the set function was used to delete duplicate items in list_ip

list3=list(list2) # the list function was used to convert the elements placed ( list2 )  into a list,
                  # not just a collection of elementes 


list3.sort() # the sort function was used to sort elements 

print(list3) 
