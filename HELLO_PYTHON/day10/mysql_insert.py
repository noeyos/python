import pymysql
 
conn = pymysql.connect(
                        host='localhost', 
                        user='root', 
                        password='python',
                        db='python', 
                        port=3304, 
                        charset='utf8'
                        )
 
curs = conn.cursor(pymysql.cursors.DictCursor) #Dictionary Cursor (like json)

my_tup = (5,5,5,5)

sql = """insert into emp (e_id, e_name, gen, addr)
                                    values(%s,%s,%s,%s);"""
curs.execute(sql, my_tup)

conn.commit()
conn.close()
