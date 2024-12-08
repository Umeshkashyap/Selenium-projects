import mysql.connector


insert_query="insert INTO sps_vendors VALUES(6,'ramesh','abcd','2020-09-15 17:33:58','','')"
update_query="UPDATE sps_vendors SET vendor_name='UMESH kumar kashyap' where vendor_id=3"
delete_query="delete from sps_vendors where vendor_id=3"


try:
    conn=mysql.connector.connect(host="localhost", port=3306, user="root", passwd="",database="testing")
    curs=conn.cursor()
    curs.execute(insert_query)
    curs.execute(update_query)
    curs.execute(delete_query)
    conn.commit()
    conn.close()
except:
    print("Connection unsuccessfull or someting went wrong in sql query")
    