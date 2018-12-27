# -*- coding: utf-8 -*-
# @Time    : 2018/12/27 15:35
# @Author  : ZouJunLin
"""
连接配置文件的数据库
"""
import ConfigParser,sys,os


class InfoAPI:
    def __init__(self,path):

        self.cf=ConfigParser.ConfigParser()
        self.cf.read(path+"./config.ini")

    def GetStockDatabase(self):
        """分别返回server,user,password,dbname"""
        temp=self.cf.get("db","stock").split(",")
        return temp[0],temp[1],temp[2],temp[3]

# if __name__=='__main__':
#     print InfoAPI().GetStockDatabase()