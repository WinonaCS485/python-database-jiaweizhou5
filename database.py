import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='cl8355ps',
                             password='Kabi666',
                             db='cl8355ps_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        
        # Get user input
        name = input("Please enter the last name to search: ")
        
        # Select students that have entered last name
        sql = "SELECT * from Student WHERE StudentLastName = '" + name + "' "
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        for result in cursor:
            print (result)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

finally:
    connection.close()
