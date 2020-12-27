import threading
import time

#It is the dictionary in which we store data
dictionary = {}

#for create operation
def create(key, value, timeout=0):
    if key in dictionary:
        print("error: key alreday present duplicate keys not allowed")#error message
    else :
        if(key.isalpha()):
            if len(dictionary)<(1024*1020*1024) and value<=(16*1024*1024):#checking the file size(less than 1GB and Jasonobject value less than 16KB is allowed)
                if timeout==0:
                    value_list=[value,timeout]
                else:
                    value_list=[value,time.time()+timeout]
                if len(key)<=32: #checking for input key_name capped at 32chars
                    dictionary[key]=value_list
                    print("success! key-value added")
            else:
                print("error: Memory limit exceeded")#error message
        else:
            print("error: Invalind key_name, only string key_names are allowed")#error message


#for read operation
def read(key):
    if key not in dictionary :
        print("error: given key does not exist in database. Please enter a valid key!") #error message
    else:
        value_found=dictionary[key]
        if value_found[1]!=0:
            if time.time()<value_found[1]: #comparing the current time with expiry time
                stri=str(key)+":"+str(value_found[0]) #JSON Object i.e.,"key_name:value"
                print(stri)
            else:
                print("error: time-to-live of",key,"has expired") #error message
        else:
            stri=str(key)+":"+str(value_found[0])
            print(stri)

#for delete operation

def delete(key):
    if key not in dictionary:
        print("error: given key does not exist in database. Please enter a valid key") #error message
    else:
        value_found=dictionary[key]
        if value_found[1]!=0:#checking for time-out
            if time.time()<value_found[1]: #comparing the current time with expiry time
                del dictionary[key]
                print("success! key is deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message
        else:
            del dictionary[key]
            print("success! key is deleted")

# I have made another function to update the values of a key-value pair

#for update operation 
def update(key,value):
    value_found=dictionary[key]
    if value_found[1]!=0:
        if time.time()<value_found[1]:
            if key not in dictionary:
                print("error: given key does not exist in database. Please enter a valid key") #error message
            else:
                new_value=[]
                new_value.append(value)
                new_value.append(value_found[1])
                dictionary[key]=new_value
                print("success! key-value updated")

        else:
            print("error: time-to-live of",key,"has expired") #error message
    else:
        if key not in dictionary:
            print("error: given key does not exist in database. Please enter a valid key") #error message
        else:
            new_value=[]
            new_value.append(value)
            new_value.append(value_found[1])
            dictionary[key]=new_value
            print("success! key-value updated")

#ways to use threading

#template to use thread.

#thread1=Thread(target=(create or read or delete),args=(key,value,timeout)) 
#thread1.start()
#thread1.sleep(time)

"""create("sandeep",25)
time.sleep(1)
create("index",70,3600)
read("index")
delete("index")
thread2= threading.Thread(target=read, args=("src", )) #as per the operation
thread2.start()
time.sleep(1)
print("abcde")
print(dictionary)
print(thread2);
"""
#and so on upto n

create("sandeep",25)
create("index",70,3600)
read("index")
delete("index")