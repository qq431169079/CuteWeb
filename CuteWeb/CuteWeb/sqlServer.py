# encoding:utf-8
import pymssql
from time import *
##将sqlserver 封装成mysql的样子

class Mysql:
    def __init__(self,server,user,password,database):
        """server,user,password,database"""
        self.server=str(server).strip()
        self.user=str(user).strip()
        self.password=str(password).strip()
        self.database=str(database).strip()
        self.conn = None
        self.cur=None

    def __GetConnect(self):
        """
        得到连接的返回信息
        :返回：conm.cursor()
        """
        if not self.conn is None:
            self.cur.close()
            self.conn.close()
            sleep(0.05)
        try:
            self.conn=pymssql.connect(host=self.server,user=self.user,password=self.password,database=self.database,charset='utf8')
            self.cur=self.conn.cursor()
        except Exception,e:
            print e.message


    def Disconnect(self):
        try:
            if not self.conn is None:
                self.cur.close()
                self.conn.close()
        except Exception, e:
            print e.message



    def deleteTable(self,tableName):
        """
        删除表
        :param tableName:
        :return:
        """
        self.__GetConnect()
        try:
            self.cur.execute("delete  from %s" % tableName)
        except Exception,e:
            print e.message
        self.conn.commit()
        self.__Disconnect()

    def ExecQuery(self,sql):
        """
        执行查询语句，返回的是一个包含tuple的list,list记录行，tuple为每行记录的字段
         ms = MSSQL(host="localhost",user="sa",pwd="123456",db="PythonWeiboStatistics")
                resList = ms.ExecQuery("SELECT id,NickName FROM WeiBoUser")
                for (id,NickName) in resList:
                    print str(id),NickName
        """
        self.__GetConnect()
        self.cur.execute(sql)
        resList=self.cur.fetchall()
        self.Disconnect()
        return resList

    def ExecNonQuery(self,sql):
        """
        执行非查询语句
        调用示例：
            cur = self.__GetConnect()
            cur.execute(sql)
            self.conn.commit()
            self.conn.close()
        """
        self.__GetConnect()
        self.cur.execute(sql)
        self.conn.commit()
        self.Disconnect()

    def ExecmanysNonQuery(self,sql,list1):
        """
        插入sql语句集，一次执行多个sql查询语句
        :param sqllist:
        :return:
        """
        self.__GetConnect()
        try:
            for i in list1:
                #print i,type(i),len(i)
                self.cur.execute(sql%i)
            self.conn.commit()
        except Exception, e:
            print "数据已经存在", e.message
            print "异常",sql,i
            print sql%i

    def ExecmanyNonQuery(self,sql,list1):
        """
        插入sql语句集，一次执行多个sql非查询语句
        :param sqllist:
        :return:
        """
        self.__GetConnect()
        self.cur.execute(sql%list1)

        self.conn.commit()
        self.Disconnect()

