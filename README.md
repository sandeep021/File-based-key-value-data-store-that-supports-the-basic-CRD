# File-based-key-value-data-store-that-supports-the-basic-CRD

## Tasks
Build a file-based key-value data store that supports the basic CRD (create, read, and delete) operations. This data store is meant to be used as a local storage for one single process on one laptop. The data store must be exposed as a library to clients that can instantiate a class and work with the data store,
* The data store will support the following functional requirements.
1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.
2 A new key-value pair can be added to data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON obiect - capped at 16KB. 
3. If Create is invoked for an existing key, an appropriate error must be returned. A Read operation on a key can be performed by providing the key, and receiving the
4. value in response, as a JSON object.
5. A Delete operation can be performed by providing the key. 
6. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of     seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations. 
7. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits.
* The data store will also support the following non-functional requirements.
1. The size of the file storing data must never exceed 1GB 
2. More than one client process cannot be allowed to use the same file as a data store at any given time. 
3. A client process is allowed to access the data store using multiple threads, if it desires to The data store must therefore be thread-safe.
4. The client will bear as little memory costs as possible to use this data store, while deriving maximum performance with respect to response times for accessing the data store

## Requirements
 ```
 Python3.5 and above
 ```
 ## Run
 ``` 
     python index.py
     create("sandeep",25)
     create("index",70,3600)
     read("index")
     delete("index")
 ```
 
## Syntax
```  
  create(key_name,value,timeout_value) #for creating key value pair
  read(key_name) #for read operation
  delete(key_name) #for delete operation
  update(key_name,new_value) ##for update operation
  
  ```

## Demo
   ![Screenshot (162)](https://user-images.githubusercontent.com/41124504/103173944-319a2280-4884-11eb-9e41-5b6d323c2f09.png)




 
 
