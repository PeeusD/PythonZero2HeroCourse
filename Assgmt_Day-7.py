'''Day 7 Assignment -
PDBC --> Python DB- Connection--> Updates required values using UPDATE and WHERE clause and select * (all table) data and print it.'''

from mysql import connector as sql          

# Creating Connection to the mysql database
database = sql.connect(host = 'localhost', user = 'root', passwd = 'mysecretpass4589', database = 'empdetails')


#Creating DB object
cur = database.cursor()
 # Updating the records using WHERE clause
cur.execute("update employee set emp_sal = 5000 where emp_id = 10") 

# Retrieving all data in  table   
cur.execute("select * from employee")        

for i in cur:
    print(i)

# Closing connection and committing to DB
cur.close()
database.commit()      
