import pymysql

conn = pymysql.connect(
                        host='localhost', 
                        user='root', 
                        password='python',
                        db='python', 
                        port=3304, 
                        charset='utf8'
                        )
 
curs = conn.cursor()
# cursor => java의 statement

sql = "UPDATE emp SET e_name=%s, gen=%s, addr=%s WHERE e_id=%s"
cnt = curs.execute(sql, ("6", "6", "6", "3"))
print("cnt", cnt)

conn.commit()

curs.close()
conn.close()
