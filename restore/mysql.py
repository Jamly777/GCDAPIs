import pymysql

class MySql():
    def __init__(self,ip,name,password,database):
        self.ip=ip
        self.name=name
        self.password=password
        self.database=database

    def do_work(func):
        def conn(self,string):
            conn=pymysql.connect(host=self.ip,user=self.name,password=self.password,
                                 database=self.database)
            cursor=conn.cursor()
            cursor.execute(func(self,string))
            res=cursor.fetchall()
            conn.commit()
            cursor.close()
            conn.close()
            return res
        return conn

    @do_work
    def sql(self,string):
        return string


if __name__ == '__main__':
    test=MySql('122.51.168.67','root','IRVing777!','Django_Book')
    print(test.sql('select * from Book_book'))