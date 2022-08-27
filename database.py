import mysql.connector                  #mysql connector are imported
from mysql.connector import errorcode

try:
   cm_connection = mysql.connector.connect(user="spulukuri",password="S4567",host="127.0.0.1",port="3306",database="teaproject")
    #above code is connection to the database which is content of user,password,host,port,database
except mysql.connector.Error as e:
   if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:   #error message for the connection code
      print("credentials is Invalid")
   elif e.errno == errorcode.ER_BAD_DB_ERROR:
      print("no database")
   else:
      print("can't: connect", e)

else:


   my_cursor = cm_connection.cursor()
   task = 1                               #declere a veriable
   while (task != 0):                     # declere a while loop for user interface

      print ("==============================================")
      print("0. Exit")
      print ("1. Press 2 for showing Data")
      print("2.  Press 3 for inserted Data")
      print("3.  Press 4 for updated Data")
      print("4.  Press 5 for  delete Data")
      print("==============================================")
      task = int(input("Enter your choice : "))      #declere task veriable for choose user input

      if (task==2) :                                 #declere a if condition for perform a task
         select_query = ("SELECT customer_id, customer_name,customer_address,phone_number FROM customer_details") # query for shows data
         my_cursor.execute(select_query)           #execute the query
         for row in my_cursor.fetchall():          #fatch the query
            print("{}   {} {} {} ".format(row[0], row[1], row[2], row[3]))    #declere the rows of table.
      elif (task==3) :                                                        #else if condition
         id = input("Enter customer id ")                                     #takes user input
         name = input("Enter customer name: ")
         address = input("Enter customer address ")
         phone = input("Enter phone no ")


         customer_query = ("INSERT INTO customer_details "
                           "(customer_id,customer_name,customer_address,phone_number)"          #insert query
                           "VALUES (%s, %s, %s, %s)")

         customer_data = (id,name,address,phone)                             #takes user input into a veriable
         try:
            customer_cursor = cm_connection.cursor()                        #connection cursor
            customer_cursor.execute(customer_query, customer_data)
            cm_connection.commit()
            print("customer are added successfully")
            customer_cursor.close()
         except mysql.connector.Error as e:                                  #except
          print("customer not added")
          print("Error: {}".format(e))



      elif (task==4) :                                                     #elif condition
         customer_id = input("Enter customer_id for Update")
         column = input("Enter item to update (customer_id, customer_name, customer_address, phone_number) ")
         prompt = "Enter new value for {} ".format(column)
         value = input(prompt)

         customer_query = ("UPDATE customer_details "
                     "SET " + column + " =  %s "
                                       "WHERE customer_id = %s")
         customer_data = (value, customer_id)
         try:
           customer_cursor = cm_connection.cursor()
           customer_cursor.execute(customer_query, customer_data)
           cm_connection.commit()
           print("Updated customer")
           customer_cursor.close()
         except mysql.connector.Error as e:
           print("customer not updated")
           print("Error: {}".format(e))



      elif (task==5):                                               #elif condition for delete
          customer_id = input("Enter customer id to delete ")        #takes id for delete

          customer_query = ("DELETE FROM customer_details "        #delete query       
                        "WHERE customer_id = %s")
          customer_data = (customer_id,)
          try:
            customer_cursor = cm_connection.cursor()            #connection cursor
            customer_cursor.execute(customer_query, customer_data)       #execute the query
            cm_connection.commit()
            print("Deleted customer")                    #print result
            customer_cursor.close()
          except mysql.connector.Error as e:
           print(" customer not updated")
           print("Error: {}".format(e))
           print("Sucess connection")
   cm_connection.close()

