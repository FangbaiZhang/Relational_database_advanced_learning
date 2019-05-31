# -*- coding:utf-8 -*-
# date: 2019-05-30

# 使用pymysql连接数据库
# 对数据库进行增删改

from pymysql import *


def main():
    # 创建Connection连接
    conn = connect(
        host='localhost', port=3306, database='jing_dong',
        user='root', password='00116656', charset='utf8'
    )
    # 获得Cursor对象，该对象用于执行sql语句
    cs1 = conn.cursor()
    # 执行sql语句，读取出sql语句选择的table中的数据
    # 返回结果是数据的行数
    print(cs1.execute('select * from goods;'))
    print('*' * 100)

    # 取出的数据是以元组的形式
    # 取出1行数据,取过的就不会再取
    print(cs1.fetchone())
    print('*' * 100)
    print(cs1.fetchone())
    print('*' * 100)

    # 取出多行数据,传入取出的行数
    print(cs1.fetchmany(3))
    print('*' * 100)

    # 取出所有的数据
    print(cs1.fetchall())
    print('*' * 100)

    # 关闭Cursor对象
    cs1.close()
    # 关闭Connection对象
    conn.close()
    print("MySQL数据库连接已关闭")

if __name__ == '__main__':
    main()
