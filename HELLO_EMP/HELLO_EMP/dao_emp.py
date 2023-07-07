import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(
        user="root",
        password="python",
        host="127.0.0.1",
        port=3304,
        database="python"
        )
        
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = """
        select * from emp
        """
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def selectOne(self,e_id):
        sql = f"""
        select e_id, e_name, gen, addr from emp where e_id='{e_id}'
        """  
        self.curs.execute(sql)
        
        res = self.curs.fetchone()
        return res
    
    def insert(self, e_id, e_name, gen, addr):
        sql = f"""
        insert into emp values('{e_id}', '{e_name}', '{gen}', '{addr}')
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
        
    def update(self, e_name, gen, addr, e_id):
        sql = f"""
        update emp set e_name = '{e_name}', gen = '{gen}', addr = '{addr}' where e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt

    def delete(self, e_id):
        sql = f"""
        delete from emp where e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()

        
if __name__ == '__main__':
    de = DaoEmp()
    #emp = de.insert('3', '3', '3', '3')
    #emp = de.update('6', '6', '6', '3')
    emp = de.delete('3')
    print(emp)
    