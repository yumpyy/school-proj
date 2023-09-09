import mysql.connector as m
import datetime as dt

DATABASE = "test2"


def chatUpload(query, response):
    
    con = m.connect(host="localhost", user="anupam", passwd="anupam", database=DATABASE)

    if not con.is_connected():
        print("Error in connection, Try Again.")
        exit() 

    cursor = con.cursor()

    timestamp = dt.datetime.now()

# query = "weather today"
# response = "feels like 34 deg celcius"

# chatHistory = f"{query}\n{response}\n\n"
    queryCommand = 'INSERT INTO convo VALUES ("User : ", "{}", "{}")'.format(query, timestamp)
    responseCommand = 'INSERT INTO convo VALUES ("AI : ", "{}", "{}")'.format(response, timestamp)
    cursor.execute(queryCommand)
    cursor.execute(responseCommand)

    con.commit()
    con.close()

def chatLoad():
    
    con = m.connect(host="localhost", user="anupam", passwd="anupam", database=DATABASE)

    if not con.is_connected():
        print("Error in connection, Try Again.")
        exit() 

    cursor = con.cursor()

    
    loadQuery = f"SELECT * FROM convo ORDER BY Time DESC LIMIT 1"
    cursor.execute(loadQuery)

    chatHistory = str(cursor.fetchall())
    # chatHistory = []
    # for row in rows:
    #     chatHistory.append(row)
    print(chatHistory)

    return chatHistory
