import pymysql

class DaoMem:
    def __init__(self):
        self.conn = pymysql.connect(
        user="root",
        password="python",
        host="localhost",
        port=3304,
        database="python"
        )
        
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def selectList(self):
        sql = """
        select * from mem
        """
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
    
    def selectOne(self,m_id):
        sql = f"""
        select * from mem where m_id={m_id}
        """  
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list[0]
    
    def insert(self, m_id, m_nm, tel, address):
        sql = f"""
        insert into mem values({m_id}, {m_nm}, {tel}, {address})
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
        
    def update(self, m_nm, tel, address, m_id):
        sql = f"""
        update mem set m_nm = {m_nm}, tel = {tel}, address = {address} where m_id = {m_id}
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt

    def delete(self, m_id):
        sql = f"""
        delete from mem where m_id = {m_id}
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    dm = DaoMem()
    #emp = de.insert('3', '3', '3', '3')
    #emp = de.update('6', '6', '6', '3')
    mem = dm.delete('3')
    print(mem)
    