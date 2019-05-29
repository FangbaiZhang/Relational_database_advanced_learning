# Relational_database_advanced_learning
# 关系型数据进阶系统学习

- 第一部分：MySQL-基本使用
- 第二部分：MySQL-Shell命令脚本
- 第三部分：MySQL-数据库查询


# 第一部分：MySQL-基本使用

# 1. 关系型数据库核心元素

- 数据行(记录)
- 数据列(字段)
- 数据表(数据行的集合)
- 数据库(数据表的集合)    

### RDBMS(Relational Database Management System)
- 所谓的关系型数据库RDBMS，是建立在关系模型基础上的数据库，
- 借助于集合代数等数学概念和方法来处理数据库中的数据

### 关系型数据库的主要产品：
- oracle：在以前的大型项目中使用,银行,电信等项目
- mysql：web时代使用最广泛的关系型数据库
- ms sql server：在微软的项目中使用
- sqlite：轻量级数据库，主要应用在移动平台

- 数据库排名[https://db-engines.com/en/ranking]

# 2. SQL(Structured Query Language) 结构化查询语言
- SQL是结构化查询语言，是一种用来操作RDBMS的数据库语言，当前关系型数据库都支持使用SQL语言进行操作,
- 也就是说可以通过 SQL 操作 oracle,sql server,mysql,sqlite 等等所有的关系型的数据库

- SQL语句主要分为：
    DQL：数据查询语言，用于对数据进行查询，如select
    DML：数据操作语言，对数据进行增加、修改、删除，如insert、udpate、delete
    TPL：事务处理语言，对事务进行处理，包括begin transaction、commit、rollback
    DCL：数据控制语言，进行授权与权限回收，如grant、revoke
    DDL：数据定义语言，进行数据库、表的管理等，如create、drop
    CCL：指针控制语言，通过控制指针完成表的操作，如declare cursor
    对于web程序员来讲，重点是数据的crud（增删改查），必须熟练编写DQL、DML，能够编写DDL完成数据库、表的操作，
    其它语言如TPL、DCL、CCL了解即可
    SQL 是一门特殊的语言,专门用来操作关系数据库
    不区分大小写

# 3. MySQL
- MySQL是一个关系型数据库管理系统,关联数据库将数据保存在不同的表中，
- 而不是将所有数据放在一个大仓库内，这样就增加了速度和提高了灵活性

- 特点:
    使用C和C++编写，并使用了多种编译器进行测试，保证源代码的可移植性
    支持多种操作系统，如Linux、Windows、AIX、FreeBSD、HP-UX、MacOS、NovellNetware、OpenBSD、OS/2 Wrap、Solaris等
    为多种编程语言提供了API，如C、C++、Python、Java、Perl、PHP、Eiffel、Ruby等
    支持多线程，充分利用CPU资源
    优化的SQL查询算法，有效地提高查询速度
    提供多语言支持，常见的编码如GB2312、BIG5、UTF8
    提供TCP/IP、ODBC和JDBC等多种数据库连接途径
    提供用于管理、检查、优化数据库操作的管理工具
    大型的数据库。可以处理拥有上千万条记录的大型数据库
    MySQL软件采用了双授权政策，它分为社区版和商业版，由于其体积小、速度快、总体拥有成本低，尤其是开放源码这一特点，
    一般中小型网站的开发都选择MySQL作为网站数据库
    MySQL使用标准的SQL数据语言形式
    Mysql是可以定制的，采用了GPL协议，你可以修改源码来开发自己的Mysql系统
    在线DDL更改功能,复制全局事务标识,复制无崩溃从机,复制多线程从机

# 4. 数据完整性
- 一个数据库就是一个完整的业务单元，可以包含多张表，数据被存储在表中
- 在表中为了更加准确的存储数据，保证数据的正确有效，可以在创建表的时候，为表添加一些强制性的验证，包括数据字段的类型、约束

- 数据类型

    可以通过查看帮助文档查阅所有支持的数据类型
    使用数据类型的原则是：够用就行，尽量使用取值范围小的，而不用大的，这样可以更多的节省存储空间
    常用数据类型如下：
        整数：int，bit
        小数：decimal
        字符串：varchar,char
        日期时间: date, time, datetime
        枚举类型(enum)
    特别说明的类型如下：
        decimal表示浮点数，如decimal(5,2)表示共存5位数，小数占2位
        char表示固定长度的字符串，如char(3)，如果填充'ab'时会补一个空格为'ab '
        varchar表示可变长度的字符串，如varchar(3)，填充'ab'时就会存储'ab'
        字符串text表示存储大文本，当字符大于4000时推荐使用
        对于图片、音频、视频等文件，不存储在数据库中，而是上传到某个服务器上，然后在表中存储这个文件的保存路径
    更全的数据类型可以参考[http://blog.csdn.net/anxpp/article/details/51284106]

- 约束

    主键primary key：物理上存储的顺序
    非空not null：此字段不允许填写空值
    惟一unique：此字段的值不允许重复
    默认default：当不填写此值时会使用默认值，如果填写时以填写为准
    外键foreign key：对关系字段进行约束，当为关系字段填写值时，会到关联的表中查询此值是否存在，
    如果存在则填写成功，如果不存在则填写失败并抛出异常，
    外键是另外一个表中的主键
    说明：虽然外键约束可以保证数据的有效性，但是在进行数据的crud（增加、修改、删除、查询）时，
    都会降低数据库的性能，所以不推荐使用，那么数据的有效性怎么保证呢？答：可以在逻辑层进行控制


# 第二部分：MySQL-Shell命令脚本

# 5. MySQL数据库的命令行脚本
- MySQL的安装：参考Python爬虫开发和项目实战pdf中的注释和QQ浏览器中数据库中的MySQL里面有安装收藏
- Navicat：参考我的博客和QQ浏览器中数据库中的Navicat里面有收藏

- MySQL启动方式：
    - 方式1：打开CMD窗口执行：mysql -u root -p 然后输入MySQL的密码00----56
    - 方式2：开始菜单里面有一个MySQL 8.0 Command Line Client打开即可

- MySQL shell命令：
    - SQL语句不区分大小写，语句可以多行写，最终结尾是分号‘；’
    - 有了分号，按下enter才会执行
    
## 5.1. 数据库操作
- 连接数据库：
    mysql -u root -p  接着输入密码
    mysql -u root -p密码  
- 退出数据库：
    exit\quit\ctrl+d
- 退出当前输入状态：
    \c
- 查看版本：
    select version();
- 显示当前时间：
    select now();
- 显示所有数据库：(注意后面分号要写)
    show databases;
- 使用数据库
    use 数据库名;
- 查看当前使用的数据库
    select database();
- 创建数据库
    create database 数据库名 charset=utf8;
    例：
    create database python charset=utf8;
- 显示数据库是怎么创建的：
    show create database python;
- 删除数据库
    drop database 数据库名;
    例：
    drop database python;


## 5.2. 数据表操作

- 查看当前数据库中所有表
    show tables;
- 查看表结构
    desc 表名;
- 创建表
    auto_increment表示自动增长   
    CREATE TABLE table_name(
    column1 datatype contrai,
    column2 datatype,
    column3 datatype,
    .....
    columnN datatype,
    PRIMARY KEY(one or more columns)
    );
    
    例：创建班级表
    create table classes(
        id int unsigned auto_increment primary key not null,
        name varchar(10)
    );
    
    例：创建学生表
    create table students(
        id int unsigned primary key auto_increment not null,
        name varchar(20) default '',
        age tinyint unsigned default 0,
        height decimal(5,2),
        gender enum('男','女','人妖','保密'),
        cls_id int unsigned default 0
    )
- 修改表-添加字段
    alter table 表名 add 列名 类型;
    例：
    alter table students add birthday datetime;
- 修改表-修改字段：重命名版
    alter table 表名 change 原名 新名 类型及约束;
    例：
    alter table students change birthday birth datetime not null;
- 修改表-修改字段：不重命名版
    alter table 表名 modify 列名 类型及约束;
    例：
    alter table students modify birth date not null;
- 修改表-删除字段
    alter table 表名 drop 列名;
    例：
    alter table students drop birthday;
- 删除表
    drop table 表名;
    例：
    drop table students;
- 查看表的创建语句
    show create table 表名;
    例：
    show create table classes;
-  查看表中具体内容
    select * from students;


## 5.3. 增删改查(curd)

curd的解释: 代表创建（Create）、更新（Update）、读取（Retrieve）和删除（Delete）
        
### 5.3.1. 查询基本使用

- 查询所有列
    select * from 表名;
    例：
    select * from classes;
- 查询指定列
    可以使用as为列或表指定别名
    select 列1,列2,... from 表名;
    例：
    select id,name from classes;

### 5.3.2. 增加

- 格式:INSERT [INTO] tb_name [(col_name,...)] {VALUES | VALUE} ({expr | DEFAULT},...),(...),...
- 说明：主键列是自动增长，但是在全列插入时需要占位，通常使用0或者 default 或者 null 来占位，插入成功后以实际数据为准
- 全列插入：值的顺序与表中字段的顺序对应
    insert into 表名 values(...)
    例：
    insert into students values(0,’郭靖‘,1,'蒙古','2016-1-2');

- 部分列插入：值的顺序与给出的列顺序对应
    insert into 表名(列1,...) values(值1,...)
    例：
    insert into students(name,hometown,birthday) values('黄蓉','桃花岛','2016-3-2');

- 上面的语句一次可以向表中插入一行数据，还可以一次性插入多行数据，这样可以减少与数据库的通信
- 全列多行插入：值的顺序与给出的列顺序对应
    insert into 表名 values(...),(...)...;
    例：
    insert into classes values(0,'python1'),(0,'python2');
    insert into 表名(列1,...) values(值1,...),(值1,...)...;
    例：
    insert into students(name) values('杨康'),('杨过'),('小龙女');

### 5.3.3. 修改删除

- 修改
- 格式: UPDATE tbname SET col1={expr1|DEFAULT} [,col2={expr2|default}]...[where 条件判断]
    update 表名 set 列1=值1,列2=值2... where 条件
    例：
    update students set gender=0,hometown='北京' where id=5;

- 删除
- DELETE FROM tbname [where 条件判断]
    真正的删除：
    delete from 表名 where 条件
    例：
    delete from students where id=5;
    
    实际使用逻辑删除：
    逻辑删除，本质就是修改操作
    update students set isdelete=1 where id=1;
    delete from students; 删除students这个数据表

- 逻辑删除常规操作
    - 先添加is_delete一列，作为标记列（默认值为0）：删除的标记为1，未删除的标记为0，
    - mysql> alter table students add is_delete bit default 0;
    - mysql> select * from students;
    +----+------+------+--------+--------+--------+---------------------+-----------+
    | id | name | age  | height | gender | cls_id | birthday            | is_delete |
    +----+------+------+--------+--------+--------+---------------------+-----------+
    |  1 | 老王 |   18 | 188.80 | 男     |      0 | 0000-00-00 00:00:00 |           |
    |  2 | 小李 |   20 | 180.00 | 男     |      1 | 1990-01-01 00:00:00 |           |
    |  3 | 小李 |   35 | 180.00 | 女     |      1 | 1990-01-01 00:00:00 |           |
    +----+------+------+--------+--------+--------+---------------------+-----------+
    - 上面查看已经添加了一列，然后执行逻辑删除：
    - mysql> update students set is_delete=1 where id=2;
    - mysql> select * from students;
    +----+------+------+--------+--------+--------+---------------------+-----------+
    | id | name | age  | height | gender | cls_id | birthday            | is_delete |
    +----+------+------+--------+--------+--------+---------------------+-----------+
    |  1 | 老王 |   18 | 188.80 | 男     |      0 | 0000-00-00 00:00:00 |           |
    |  2 | 小李 |   20 | 180.00 | 男     |      1 | 1990-01-01 00:00:00 |          |
    |  3 | 小李 |   35 | 180.00 | 女     |      1 | 1990-01-01 00:00:00 |           |
    +----+------+------+--------+--------+--------+---------------------+-----------+
    - 逻辑删除后，数据有了一个特殊标记
    - 查看未注销的：select * from students where is_delete=0;
    - 查看已经注销的：select * from students where is_delete=1;
    
    
# 第三部分：MySQL-数据库查询

# 6. MySQL查询
- 创建数据库和数据表

-- 创建数据库
create database python_test_1 charset=utf8;

-- 使用数据库
use python_test_1;

-- 创建students表，注意最后一行不需要逗号：
create table students(
    id int unsigned primary key auto_increment not null, 
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit default 0
);

- 前面第一个单词是字段名（每列的名称），后面的都是约束
    - 例如id行：
    id:字段名，int:数据的类型，unsigned：无符号范围(从0开始，没有负数），
    primary key:主键，auto_increment：自动增长，not null：不能为空，
    - name varchar(20)的字符个数为20可变，default ''默认值为空
    - age tinyint极小值，unsigned无负数，范围0-255，default 0默认为0
    - height decimal(5, 2)身高的值有五位，小数点后面两位
    - gender enum枚举，'男','女','中性','保密'可以用数字1,2,3,4替代，默认值为保密
    - is_delete bit default 0, is_delete 默认值是0，bit只能存储一个比特，值只能是0或者1

-- 创建classes表
create table classes (
    id int unsigned auto_increment primary key not null,
    name varchar(30) not null
);


-- 插入数据

-- 向students表中插入数据
-- 主键都是0，自动增长
insert into students values
(0,'小明',18,180.00,2,1,0),
(0,'小月月',18,180.00,2,2,1),
(0,'彭于晏',29,185.00,1,1,0),
(0,'刘德华',59,175.00,1,2,1),
(0,'黄蓉',38,160.00,2,1,0),
(0,'凤姐',28,150.00,4,2,1),
(0,'王祖贤',18,172.00,2,1,1),
(0,'周杰伦',36,NULL,1,1,0),
(0,'程坤',27,181.00,1,2,0),
(0,'刘亦菲',25,166.00,2,2,0),
(0,'金星',33,162.00,3,3,1),
(0,'静香',12,180.00,2,4,0),
(0,'郭靖',12,170.00,1,4,0),
(0,'周杰',34,176.00,2,5,0);

-- 向classes表中插入数据
insert into classes values (0, "python_01期"), (0, "python_02期");

## 6.1. 基本查询

- 查询所有字段
    select * from 表名;
    例：
    select * from students;

- 查询指定字段
    select 列1,列2,... from 表名;
    例:
    select name from students;

- 使用 as 给字段起别名
    select id as 序号, name as 名字, gender as 性别 from students;

- 可以通过 as 给表起别名
    -- 如果是单表查询 可以省略表明
    select id, name, gender from students;
    -- 表名.字段名
    select students.id,students.name,students.gender from students;
    -- 可以通过 as 给表起别名 (多个表可以使用别名)
    select s.id,s.name,s.gender from students as s;

- 消除重复行
    在select后面列前使用distinct可以消除重复的行，后面重复的就不会显示出来
    select distinct 列1,... from 表名;
    例：
    select distinct gender from students;


## 6.1. 条件查询
- 详细案例参考html文件15.2

- 使用where子句对表中的数据筛选，结果为true的行会出现在结果集中
- 语法如下：
    select * from 表名 where 条件;
    例：
    select * from students where id=1;

- where后面支持多种运算符，进行条件的处理
    比较运算符
    逻辑运算符
    模糊查询
    范围查询
    空判断
    
- 比较运算符
    等于: =
    大于: >
    大于等于: >=
    小于: <
    小于等于: <=
    不等于: != 或 <>

    
- 逻辑运算符
    and  and的左边和右边单独作为一个条件整体
    or
    not
    
- 模糊查询
    like
    %表示任意多个任意字符
    _表示一个任意字符
    
    rlike  正则查询
    select name from students where name rlike "^周.*";

- 范围查询
    in表示在一个非连续的范围内
    查询编号是1或3或8的学生
    select * from students where id in(1,3,8);
    between ... and ...表示在一个连续的范围内
    select * from students where id between 3 and 8;
    not in不在非连续范围内

- 空判断
    注意：null与''是不同的
    判空is null
    判非空is not null

- 优先级
    优先级由高到低的顺序为：小括号，not，比较运算符，逻辑运算符
    and比or先运算，如果同时出现并希望先算or，需要结合()使用

## 6.2. 排序
- 详细案例参考html文件15.3

语法：

select * from 表名 order by 列1 asc|desc [,列2 asc|desc,...]

说明：
将行数据按照列1进行排序，如果某些行列1的值相同时，则按照列2排序，以此类推
默认按照列值从小到大排列（asc）
asc从小到大排列，即升序
desc从大到小排序，即降序

例1：查询未删除男生信息，按学号降序
select * from students where gender=1 and is_delete=0 order by id desc;

例2：查询未删除学生信息，按名称升序
select * from students where is_delete=0 order by name;

例3：显示所有的学生信息，先按照年龄从大-->小排序，当年龄相同时 按照身高从高-->矮排序
select * from students  order by age desc, height desc;


## 6.3. 聚合函数
- 详细案例参考html文件15.4

聚合函数
为了快速得到统计数据，经常会用到如下5个聚合函数

总数
count(*)表示计算总行数，括号中写星与列名，结果是相同的
例1：查询学生总数
select count(*) from students;

最大值
max(列)表示求此列的最大值
例2：查询女生的编号最大值
select max(id) from students where gender=2;

最小值
min(列)表示求此列的最小值
例3：查询未删除的学生最小编号
select min(id) from students where is_delete=0;

求和
sum(列)表示求此列的和
例4：查询男生的总年龄
select sum(age) from students where gender=1;
-- 平均年龄
select sum(age)/count(*) from students where gender=1;

平均值
avg(列)表示求此列的平均值
例5：查询未删除女生的编号的平均值
select avg(id) from students where is_delete=0 and gender=2;
例6：查询未删除女生的年龄的平均值，以下两种方式结果一样：
select avg(age) from students where is_delete=0 and gender=2;
select sum(age)/count(*) from students where is_delete=0 and gender=2;

保留小数位数: 1位小数
select round(avg(age), 1) from students where is_delete=0 and gender=2;


## 6.4. 分组
- 详细案例参考html文件15.5

- 分组：group by
    group by的含义:将查询结果按照1个或多个字段进行分组，字段值相同的为一组
    group by可用于单个字段分组，也可用于多个字段分组
    group by单独使用时，只显示出每组的第一条记录, 所以group by单独使用时的实际意义不大
    
- group by + group_concat()
    group_concat(字段名)可以作为一个输出字段来使用，括号里面的内容组合为一个字段
    表示分组之后，根据分组结果，使用group_concat()来放置每一组的某字段的值的集合
    性别进行分组，显示每个分组下所有的姓名：
    mysql> select gender, group_concat(name) from students group by gender;
    +--------+------------------------------------------+
    | gender | group_concat(name)                       |
    +--------+------------------------------------------+
    | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖           |
    | 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰 |
    | 中性   | 金星                                     |
    | 保密   | 凤姐                                     |
    +--------+------------------------------------------+
    4 rows in set (0.00 sec)
    
- group by + 集合函数
    通过group_concat()的启发，我们既然可以统计出每个分组的某字段的值的集合，
    那么我们也可以通过集合函数来对这个值的集合做一些操作
    里面也可以传入字符串
    
    - 统计每个性别所有的年龄：
    mysql> select gender, group_concat(age) from students group by gender;
    +--------+----------------------+
    | gender | group_concat(age)    |
    +--------+----------------------+
    | 男     | 29,59,36,27,12       |
    | 女     | 18,18,38,18,25,12,34 |
    | 中性   | 33                   |
    | 保密   | 28                   |
    +--------+----------------------+
    4 rows in set (0.00 sec)
    
    传入字符串下划线_和空格
    mysql> select gender, group_concat(name, "_", age, " ", id) from students where gender=1 group by gender;
    +--------+----------------------------------------------------------+
    | gender | group_concat(name, "_", age, " ", id)                    |
    +--------+----------------------------------------------------------+
    | 男     | 彭于晏_29 3,刘德华_59 4,周杰伦_36 8,程坤_27 9,郭靖_12 13 |
    +--------+----------------------------------------------------------+
    1 row in set (0.00 sec)
        
    - 统计每个分组的平均年龄：
    mysql> select gender, avg(age) from students group by gender;
    +--------+----------+
    | gender | avg(age) |
    +--------+----------+
    | 女     |  23.2857 |
    | 男     |  32.6000 |
    | 保密   |  28.0000 |
    | 中性   |  33.0000 |
    +--------+----------+
    4 rows in set (0.00 sec)
    
    - 分别统计性别为男/女的人的个数
    select gender, count(*) from students group by gender;

- group by + having
    having 条件表达式：用来分组查询后指定一些条件来输出查询结果
    having作用和where一样，但having只能用于group by
    统计出性别里面人数大于2人的分组：
    select gender,count(*) from students group by gender having count(*)>2;
    +--------+----------+
    | gender | count(*) |
    +--------+----------+
    | 女     |        7 |
    | 男     |        5 |
    +--------+----------+
    2 rows in set (0.00 sec)
    
    select后面的都是要显示的列内容，性别进行分组，显示里面人数大于2的分组，并显示每个分组里面的名称和平均年龄
    mysql> select gender, group_concat(name), avg(age) from students group by gender having count(*)>2;
    +--------+------------------------------------------+----------+
    | gender | group_concat(name)                       | avg(age) |
    +--------+------------------------------------------+----------+
    | 男     | 彭于晏,刘德华,周杰伦,程坤,郭靖           |  32.6000 |
    | 女     | 小明,小月月,黄蓉,王祖贤,刘亦菲,静香,周杰 |  23.2857 |
    +--------+------------------------------------------+----------+
        
- group by + with rollup
    with rollup的作用是：在最后新增一行，来记录当前列里所有记录的总和
    select gender,count(*) from students group by gender with rollup;
    +--------+----------+
    | gender | count(*) |
    +--------+----------+
    | 男     |        5 |
    | 女     |        7 |
    | 中性   |        1 |
    | 保密   |        1 |
    | NULL   |       14 |
    +--------+----------+
    
## 6.5. 分页
- 详细案例参考html文件15.6
- limit必须放在最后

- 获取部分行
    当数据量过大时，在一页中查看数据是一件非常麻烦的事情
    语法：select * from 表名 limit count
    说明：查询到的数据，只显示前面count条数据
    语法: select * from 表名 limit start,count
    说明: 显示从start开始，获取的count条数据
    
    mysql> select * from students limit 0,3;
    +----+--------+------+--------+--------+--------+-----------+
    | id | name   | age  | height | gender | cls_id | is_delete |
    +----+--------+------+--------+--------+--------+-----------+
    |  1 | 小明   |   18 | 180.00 | 女     |      1 |           |
    |  2 | 小月月 |   18 | 180.00 | 女     |      2 |          |
    |  3 | 彭于晏 |   29 | 185.00 | 男     |      1 |           |
    +----+--------+------+--------+--------+--------+-----------+

- 分页
    已知：每页显示m条数据，当前显示第n页
    求总页数：此段逻辑后面会在python中实现
        查询总条数p1
        使用p1除以m得到p2
        如果整除则p2为总数页
        如果不整除则p2+1为总页数
    求第n页的数据：n代表第几页，m代表每页显示的数据
    select * from students where is_delete=0 limit (n-1)*m,m
    - SQL查询时候要计算出：(n-1)*m,m的具体数字值
    
- 顺序：where --- order by --- limit


## 6.6. 连接查询
- 详细案例参考html文件15.7
当查询结果的列来源于多张表时，需要将多张表连接成一个大的数据集，再选择合适的列返回
mysql支持三种类型的连接查询，分别为：

- 内连接查询：查询的结果为两个表匹配到的数据,取交集
- 右连接查询：查询的结果为两个表匹配到的数据，右表特有的数据，对于左表中不存在的数据使用null填充，右边要全显示
- 左连接查询：查询的结果为两个表匹配到的数据，左表特有的数据，对于右表中不存在的数据使用null填充，左边要全显示

- 语法
    select * from 表1 inner或left或right join 表2 on 表1.列 = 表2.列
    
- 例1：使用内连接查询班级表与学生表
    select * from students inner join classes on students.cls_id = classes.id;
    mysql> select * from students inner join classes on students.cls_id=classes.id;
    +----+--------+------+--------+--------+--------+-----------+----+-------------+
    | id | name   | age  | height | gender | cls_id | is_delete | id | name        |
    +----+--------+------+--------+--------+--------+-----------+----+-------------+
    |  1 | 小明   |   18 | 180.00 | 女     |      1 |           |  1 | python_01期 |
    |  2 | 小月月 |   18 | 180.00 | 女     |      2 |          |  2 | python_02期 |
    |  3 | 彭于晏 |   29 | 185.00 | 男     |      1 |           |  1 | python_01期 |
    |  4 | 刘德华 |   59 | 175.00 | 男     |      2 |          |  2 | python_02期 |
    |  5 | 黄蓉   |   38 | 160.00 | 女     |      1 |           |  1 | python_01期 |
    |  6 | 凤姐   |   28 | 150.00 | 保密   |      2 |          |  2 | python_02期 |
    |  7 | 王祖贤 |   18 | 172.00 | 女     |      1 |          |  1 | python_01期 |
    |  8 | 周杰伦 |   36 |   NULL | 男     |      1 |           |  1 | python_01期 |
    |  9 | 程坤   |   27 | 181.00 | 男     |      2 |           |  2 | python_02期 |
    | 10 | 刘亦菲 |   25 | 166.00 | 女     |      2 |           |  2 | python_02期 |
    | 11 | 金星   |   33 | 162.00 | 中性   |      3 |          |  3 | python_03期 |
    | 12 | 静香   |   12 | 180.00 | 女     |      4 |           |  4 | python_04期 |
    | 13 | 郭靖   |   12 | 170.00 | 男     |      4 |           |  4 | python_04期 |
    +----+--------+------+--------+--------+--------+-----------+----+-------------+

    上面取出了所有的students.cls_id=classes.id相同的列然后，进行连接
    我们也可以只取出学生的名称和班级名称
    mysql> select students.id, students.name, classes.name from students inner join classes on students.cls_id=classes.id;
    +----+--------+-------------+
    | id | name   | name        |
    +----+--------+-------------+
    |  1 | 小明   | python_01期 |
    |  2 | 小月月 | python_02期 |
    |  3 | 彭于晏 | python_01期 |
    |  4 | 刘德华 | python_02期 |
    |  5 | 黄蓉   | python_01期 |
    |  6 | 凤姐   | python_02期 |
    |  7 | 王祖贤 | python_01期 |
    |  8 | 周杰伦 | python_01期 |
    |  9 | 程坤   | python_02期 |
    | 10 | 刘亦菲 | python_02期 |
    | 11 | 金星   | python_03期 |
    | 12 | 静香   | python_04期 |
    | 13 | 郭靖   | python_04期 |
    +----+--------+-------------+
    - 重命名简化写法
    mysql> select s.id, s.name, c.name from students as s inner join classes as c on s.cls_id=c.id;
    - 按班级和id排序连续显示 
    mysql> select c.name, s.id, s.name from students as s inner join classes as c on s.cls_id=c.id order by c.name, s.id; 
    +-------------+----+--------+
    | name        | id | name   |
    +-------------+----+--------+
    | python_01期 |  1 | 小明   |
    | python_01期 |  3 | 彭于晏 |
    | python_01期 |  5 | 黄蓉   |
    | python_01期 |  7 | 王祖贤 |
    | python_01期 |  8 | 周杰伦 |
    | python_02期 |  2 | 小月月 |
    | python_02期 |  4 | 刘德华 |
    | python_02期 |  6 | 凤姐   |
    | python_02期 |  9 | 程坤   |
    | python_02期 | 10 | 刘亦菲 |
    | python_03期 | 11 | 金星   |
    | python_04期 | 12 | 静香   |
    | python_04期 | 13 | 郭靖   |
    +-------------+----+--------+

- 例2：使用左连接查询班级表与学生表，学生表为基准，班级表没有的就是Null        
    select s.id, s.name, c.name from students as s left join classes as c on s.cls_id=c.id;
    +----+--------+-------------+
    | id | name   | name        |
    +----+--------+-------------+
    |  1 | 小明   | python_01期 |
    |  2 | 小月月 | python_02期 |
    |  3 | 彭于晏 | python_01期 |
    |  4 | 刘德华 | python_02期 |
    |  5 | 黄蓉   | python_01期 |
    |  6 | 凤姐   | python_02期 |
    |  7 | 王祖贤 | python_01期 |
    |  8 | 周杰伦 | python_01期 |
    |  9 | 程坤   | python_02期 |
    | 10 | 刘亦菲 | python_02期 |
    | 11 | 金星   | python_03期 |
    | 12 | 静香   | python_04期 |
    | 13 | 郭靖   | python_04期 |
    | 14 | 周杰   | NULL        |
    +----+--------+-------------+
- 左连接两个数据表交换一下位置，就变成了右连接
- select s.id, s.name, c.name from classes as c left join students as s on s.cls_id=c.id; 
   
- 例3：使用右连接查询班级表与学生表, 班级表为基准，学生表多的学生直接删除
    select s.id, s.name, c.name from students as s right join classes as c on s.cls_id=c.id;

- 交集结果中取出特定的值使用having，推荐使用
    select s.id, s.name, c.name from students as s left join classes as c on s.cls_id=c.id having c.name is null;
- 原数据表中取结果使用where,但是该处的交集也可用where取出结果
    select s.id, s.name, c.name from students as s left join classes as c on s.cls_id=c.id where c.name is null;
    
## 6.7. 自关联
- 详细案例参考html文件15.8

- 设计省信息的表结构provinces
    id
    ptitle
- 设计市信息的表结构citys
    id
    ctitle
    proid
- citys表的proid表示城市所属的省，对应着provinces表的id值

- 定义表areas，结构如下
        id
        atitle
        pid
说明:
    因为省没有所属的省份，所以可以填写为null
    城市所属的省份pid，填写省所对应的编号id
    这就是自关联，表中的某一列，关联了这个表中的另外一列，但是它们的业务逻辑含义是不一样的，城市信息的pid引用的是省信息的id
    在这个表中，结构不变，可以添加区县、乡镇街道、村社区等信息

- 先创建一个表：
    create table booktest_areainfo(
        aid int primary key,
        atitle varchar(20),
        pid int
    );
    
    表结构如下：
    mysql> desc booktest_areainfo;
    +--------+-------------+------+-----+---------+-------+
    | Field  | Type        | Null | Key | Default | Extra |
    +--------+-------------+------+-----+---------+-------+
    | aid    | int(11)     | NO   | PRI | NULL    |       |
    | atitle | varchar(20) | YES  |     | NULL    |       |
    | pid    | int(11)     | YES  |     | NULL    |       |
    +--------+-------------+------+-----+---------+-------+
    
    切换sql数据文件所在的目录下，打开CMD窗口，然后打开mysql服务,使用以上表所在的数据库
    从sql文件中导入数据
    source areas.sql;
    
    - 查询一共有多少个省
    select count(*) from areas where pid is null;
    select count(*) from booktest_areainfo where pid is null;
    
    - 例1：查询省的名称为“山西省”的所有城市
    select city.* from areas as city
    inner join areas as province on city.pid=province.aid
    where province.atitle='山西省';
    
    - 例2：查询市的名称为“广州市”的所有区县
    select dis.* from areas as dis
    inner join areas as city on city.aid=dis.pid
    where city.atitle='广州市';

## 6.8. 自关联
- 详细案例参考html文件15.9

- 子查询：在一个 select 语句中,嵌入了另外一个 select 语句, 那么被嵌入的 select 语句称之为子查询语句

- 子查询分类
    标量子查询: 子查询返回的结果是一个数据(一行一列)
    列子查询: 返回的结果是一列(一列多行)
    行子查询: 返回的结果是一行(一行多列)
    
- 标量子查询
    查询班级学生平均年龄
    查询大于平均年龄的学生
    查询班级学生的平均身高
    select * from students where age > (select avg(age) from students);

- 列级子查询
    查询还有学生在班的所有班级名字
        找出学生表中所有的班级 id
        找出班级表中对应的名字
    select name from classes where id in (select cls_id from students);

- 行级子查询
    需求: 查找班级年龄最大,身高最高的学生
    行元素: 将多个字段合成一个行元素,在行级子查询中会使用到行元素
    select * from students where (height,age) = (select max(height),max(age) from students);

- 子查询中特定关键字使用
    in 范围
        格式: 主查询 where 条件 in (列子查询)
        

## 6.9. 查询总结，执行顺序
- 详细案例参考html文件15.9

- 查询总结
- 查询的完整格式 ^_^ 不要被吓到 其实很简单 ! _ !
SELECT select_expr [,select_expr,...] [      
      FROM tb_name
      [WHERE 条件判断]
      [GROUP BY {col_name | postion} [ASC | DESC], ...] 
      [HAVING WHERE 条件判断]
      [ORDER BY {col_name|expr|postion} [ASC | DESC], ...]
      [ LIMIT {[offset,]rowcount | row_count OFFSET offset}]
]

- 完整的select语句
    select distinct *
    from 表名
    where ....
    group by ... having ...
    order by ...
    limit start,count

    执行顺序为：
        from 表名
        where ....
        group by ...
        select distinct *
        having ...
        order by ...
        limit start,count
    实际使用中，只是语句中某些部分的组合，而不是全部

## 6.10. 数据库设计模式
- 详细案例参考html文件14.6





