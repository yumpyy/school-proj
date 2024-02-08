import mysql.connector as m
import datetime as dt

HOST = "localhost"
USER = "beep"
PASSWORD = "beep"
DATABASE = "school"

def chatUpload(query, response):
    
    con = m.connect(host=HOST, user=USER, passwd=PASSWORD, database=DATABASE)

    if not con.is_connected():
        print("Error in connection, Try Again.")
        exit() 

    cursor = con.cursor()

    timestamp = dt.datetime.now()

    queryCommand = 'INSERT INTO convo VALUES ("User : ", "{}", "{}")'.format(query, timestamp)
    responseCommand = 'INSERT INTO convo VALUES ("AI : ", "{}", "{}")'.format(response, timestamp)
    cursor.execute(queryCommand)
    cursor.execute(responseCommand)

    con.commit()
    con.close()
