# -*- coding:utf-8 -*-
# date: 2019-06-03

# 首先打开数据库，打开jing_dong数据库
# 创建一个用于测试的表：create table test_index(title varchar(10));


from pymysql import connect

def main():
    # 创建Connection连接
    conn = connect(
        host='localhost', port=3306, database='jing_dong',
        user='root', password='00116656', charset='utf8'
    )
    # 获得Cursor对象，该对象用于执行sql语句
    cursor = conn.cursor()
    # 插入10万次数据
    for i in range(100000):
        cursor.execute("insert into test_index values('ha-%d')" % i)
    # 提交数据
    conn.commit()

if __name__ == '__main__':
    main()
