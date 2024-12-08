import mysql.connector

select_query="SELECT*FROM sps_vendors"

try:
    conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="", database="testing")
    curs = conn.cursor()
    curs.execute(select_query)
    for row in curs:
        print(row[0],row[1],row[2],row[3],row[4],row[5])
    conn.close()
except:
    print("Connection unsuccessfull or someting went wrong in sql query")
