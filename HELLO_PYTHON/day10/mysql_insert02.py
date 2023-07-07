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
e_id = "3"
e_name = "3"
gen = "3"
addr = "3"

sql = f"""insert into emp (e_id, e_name, gen, addr)
                                    values('{e_id}', '{e_name}', '{gen}', '{addr}');"""
cnt = curs.execute(sql)
print("cnt", cnt)

conn.commit()

curs.close()
conn.close()
