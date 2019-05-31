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
        '''显示所有品牌分类'''
        sql = "select name from goods_brands;"
        self.execute_sql(sql)

    def add_brands(self):
        '''增加商品品牌'''
        item_name = input("输入新商品品牌的名称：")
        sql = """insert into goods_brands(name) values('%s')""" % item_name
        self.cursor.execute(sql)
        # 执行提交上面sql语句的结果到数据库
        self.conn.commit()

    def get_info_by_name(self):
        '''查询商品的信息'''
        find_name = input("请输入要查询的商品的名字：")
        sql = """select * from goods where name='%s';""" % find_name
        print("-------------->%s<--------------" % sql)
        self.execute_sql(sql)

    # 静态方法，类内部调用，不需要传入参数
    @staticmethod
    def print_menu():
        print("--------京东--------")
        print("1: 所有的商品")
        print("2: 所有的商品分类")
        print("3: 所有的商品品牌分类")
        print("4: 添加一个商品品牌分类")
        print("5: 根据名字查询商品的信息")
        return input("请输入功能所对应的序号: ")

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
            elif num == "4":
                # 添加一个商品分类
                self.add_brands()
            elif num == "5":
                # 查询商品的信息
                self.get_info_by_name()
            else:
                print("输入序号有误，请重新输入")

def main():
    # 1.创建一个京东商城对象
    jd = JD()

    # 2.调用这个对象的run方法，让其运行
    jd.run()

if __name__ == '__main__':
    main()

# sql注入问题：
# 上面查询商品的sql语句如下：
# sql = """select * from goods where name='%s';""" % find_name
# name后面是一个双单引号''
# 如果我们输入的商品名字是，请输入要查询的商品的名字：' or 1=1 or '
# 结果就是：select * from goods where name='' or 1=1 or '';
# 由于使用的是or只要满足一个即可，1=1满足，这样就会查询出所有的商品