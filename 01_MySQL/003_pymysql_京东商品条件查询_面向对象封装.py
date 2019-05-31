# -*- coding:utf-8 -*-
# date: 2019-05-30

# 使用pymysql连接数据库
# 条件查询

from pymysql import *

class JD(object):
    def __init__(self):
        # 创建Connection连接
        self.conn = connect(
            host='localhost', port=3306, database='jing_dong',
            user='root', password='00116656', charset='utf8'
        )
        # 获得Cursor对象，该对象用于执行sql语句
        self.cursor = self.conn.cursor()

    def __del__(self):
        # 关闭Cursor对象
        self.cursor.close()
        # 关闭Connection对象
        self.conn.close()
        print("-----查询完成,数据库连接已关闭-----")

    def execute_sql(self, sql):
        # 执行sql语句的方法
        # 执行sql语句,读取出sql语句选择的table中的数据
        self.cursor.execute(sql)
        # 取出上面已经选择的数据
        for temp in self.cursor.fetchall():
            print(temp)

    def show_all_items(self):
        '''显示所有的商品'''
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        '''显示所有商品分类'''
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        '''显示所有商品分类'''
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    # 静态方法，类内部调用，不需要传入参数
    @staticmethod
    def print_menu():
        print("--------京东--------")
        print("1: 所有的商品")
        print("2: 所有的商品分类")
        print("3: 所有的商品品牌分类")
        return input("请输入功能所对应的序号(1或着2或者3): ")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                # 查询所有的商品
                self.show_all_items()
            elif num == "2":
                # 查询所有的商品分类
                self.show_cates()
            elif num == "3":
                # 查询所有的商品品牌分类
                self.show_brands()
            else:
                print("输入序号有误，请重新输入")

def main():
    # 1.创建一个京东商城对象
    jd = JD()

    # 2.调用这个对象的run方法，让其运行
    jd.run()

if __name__ == '__main__':
    main()