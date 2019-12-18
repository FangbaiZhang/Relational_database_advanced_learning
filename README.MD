# Relational_database_advanced_learning
# 关系型数据进阶系统学习

- 第一部分：MySQL-基本使用
- 第二部分：MySQL-Shell命令脚本
- 第三部分：MySQL-数据库查询
- 第四部分：MySQL模拟操作京东商品数据库
- 第五部分：MySQL与Python交互
- 第六部分: MySQL高级


- MySQL安装参考以下博文：
MySQL8.0.16安装---安装MySQL注意事项
https://blog.csdn.net/u011318077/article/details/90754766
MySQL基础知识---MySQL详细安装步骤
https://www.cnblogs.com/ayyl/p/5978418.html

- 我电脑安装时候使用的默认安装文件夹
- 电脑中MySQL安装安装位置：
C:\Program Files\MySQL

- 用于存储数据的文件夹位于Data下面，可以打开发现每个数据库database都是一个独立的文件夹：
C:\ProgramData\MySQL\MySQL Server 8.0\Data

- MySQL图形化管理工具
Navicat12中文版安装及破解（安装在H盘）
https://blog.csdn.net/u011318077/article/details/90519874


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
        整数：int, bit
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

- mysql字段约束
    约束	              名称
    primary key	      主键
    unique key	      唯一约束
    not null	      非空约束
    default	          默认值
    auto_increment	  自增长约束
    comment	          注释
    foreign key	      外键约束

    主键primary key：物理上存储的顺序，
        主键约束 = 唯一性约束 + 非空约束，
        是一张表的代表性字段，一张表只能有一个主键，
    　　主键可以是一个字段，也可以是多个字段（联合主键，复合主键），
        整形主键字段可以使用auto_increment（自动增长）修饰，
    非空not null：此字段不允许填写空值
    唯一unique：此字段的值不允许重复
    默认default：当不填写此值时会使用默认值，如果填写时以填写为准，（当增加数据时没有插⼊值时，会自动插⼊默认值；）
    注释(comment)：表、列都可以设置注释(comment),注释就是对表、列的意思的进行解释
    外键foreign key：对关系字段进行约束，当为关系字段填写值时，会到关联的表中查询此值是否存在，
        如果存在则填写成功，如果不存在则填写失败并抛出异常，
        外键是另外一个表中的主键
        说明：虽然外键约束可以保证数据的有效性，但是在进行数据的crud（增加、修改、删除、查询）时，
        都会降低数据库的性能，所以不推荐使用，那么数据的有效性怎么保证呢？答：可以在逻辑层进行控制
        
    补充约束：
    unsigned 是MYSQL自定义的类型，非标准SQL。用途是起到约束数值的作用，可以增加数值范围（相当于把负数那部分加到正数上）。
    整型的每一种都分有无符号（unsigned）和有符号（signed）两种类型（float和double总是带符号的），
    在默认情况下声明的整型变量都是有符号的类型（char有点特别），
    如果需声明无符号类型的话就需要在类型前加上unsigned。
    无符号版本和有符号版本的区别就是无符号类型能保存2倍于有符号类型的正整数数据，
    比如16位系统中一个int能存储的数据的范围为-32768~32767，而unsigned能存储的数据范围则是0~65535。

# 第二部分：MySQL-Shell命令脚本

# 5. MySQL数据库的命令行脚本
- MySQL的安装：参考Python爬虫开发和项目实战pdf中的注释和QQ浏览器中数据库中的MySQL里面有安装步骤收藏(详细步骤pdf已保存到本地)
- Navicat：参考我的博客和QQ浏览器中数据库中的Navicat里面有收藏

- MySQL启动方式：
    - 方式1：打开CMD窗口执行：mysql -u root -p 然后输入MySQL的密码00----56(安装过程默认用户就是root，密码是安装时候设置的)
    - 方式2：开始菜单里面有一个MySQL 8.0 Command Line Client打开即可

- MySQL shell命令：
    - SQL语句不区分大小写，语句可以多行写，最终结尾是分号;
    - 有了分号，按下enter才会执行
    
## 5.1. 数据库常用操作
- 连接数据库：
    mysql -u root -p  接着输入密码
    mysql -u root -p密码  
- 退出数据库：
    exit\quit\ctrl+d
- 退出当前输入状态(有时候输入错误)：
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
- 导入外部的sql数据文件
    - 先切换到要导入数据的数据库
    use stock_db
    - 导入数据
    source sql文件的路径  
    （注意你的文件路径要是复制过来的，windows下要将"\"全部换成“/”）
    mysql> source D:/stock_db.sql    


## 5.2. 数据表操作

- 查看当前数据库中所有表
    show tables;
- 查看表结构
    desc 表名;
- 创建表

    表名 字段名(数据列的名称) 定义每一个字段(该字段的各种约束)
    注意：创建时候，表名和字段名可以使用反引号。
          创建 MySql 的表时，表名和字段名外面的符号 ` 不是单引号，而是英文输入法状态下的反单引号，
          也就是键盘左上角 esc 按键下面的那一个 ~ 按键。反引号是为了区分 MySql 关键字与普通字符而引入的符号，一般的，表名与字段名都使用反引号。
    
    CREATE TABLE table_name(
        column1 datatype constraint(约束),
        column2 datatype,
        column3 datatype,
        .....
        columnN datatype,
        PRIMARY KEY(one or more columns)
    );
    
    标准写法(MySQL不区分大小写)：
    CREATE TABLE IF NOT EXISTS runoob_tbl(
        runoob_id INT UNSIGNED AUTO_INCREMENT,
        runoob_title VARCHAR(100) NOT NULL,
        runoob_author VARCHAR(40) NOT NULL,
        submission_date DATE,
        PRIMARY KEY (runoob_id)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    解析：
        如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL， 在操作数据库时如果输入该字段的数据为NULL ，就会报错。
        AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1。
        PRIMARY KEY关键字用于定义列为主键。 您可以使用多列来定义主键，列间以逗号分隔。
        ENGINE 设置存储引擎，CHARSET 设置编码。
    
    实例：创建班级表
    create table classes(
        id int unsigned auto_increment primary key not null,   # auto_increment表示自动增长  
        name varchar(10)
    );
    
    实例：创建学生表
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
    
- 修改表-修改字段：不重命名版，修改birth的类型
    alter table 表名 modify 列名 类型及约束;
    例：
    alter table students modify birth date not null;
    
- 修改表-删除字段(删除一列)
    alter table 表名 drop 列名;
    例：
    alter table students drop birthday;
    
- 删除表
    drop table 表名;
    例：
    drop table students;
    
    删除数据表的另外一种方法：
    delete from students;  删除students这个数据表
    
- 查看表的创建语句
    show create table 表名;
    例：
    show create table classes;
    
-  查看表中具体内容
    select * from students;


## 5.3. 增删改查(curd)(针对行的操作)

curd的解释: 代表创建（Create）、更新（Update）、读取（Retrieve）和删除（Delete）
        
### 5.3.1. 查询基本使用

- 查询所有列的内容(查询整个表的内容)
    select * from 表名;
    例：
    select * from classes;
- 查询指定列的内容
    可以使用as为列或表指定别名
    select 列1,列2,... from 表名;
    例：
    select id,name from classes;

### 5.3.2. 增加

- 格式:INSERT [INTO] tb_name [(col_name,...)] {VALUES | VALUE} ({expr | DEFAULT},...),(...),...
- 说明：主键列是自动增长，但是在全列插入时需要占位，通常使用0或者 default 或者 null 来占位，插入成功后以实际数据为准
- 全列插入：值的顺序与表中字段的顺序对应，只需要写值
    insert into 表名 values(...)
    例：
    insert into students values(0,'郭靖',1,'蒙古','2016-1-2');

- 部分列插入：值的顺序与给出的列顺序对应，需要写列的名称和对应的值
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

- 将分组结果写入到goods_cates数据表
    insert into goods_cates (name) select cate_name from goods group by cate_name;

### 5.3.3. 修改删除

- 修改
- 格式: UPDATE tbname SET col1={expr1|DEFAULT} [,col2={expr2|default}]...[where 条件判断]
    update 表名 set 列1=值1,列2=值2... where 条件;
    例：
    update students set gender=0,hometown='北京' where id=5;

- 删除行
- DELETE FROM table_name [where 条件判断]
    真正的删除：
    delete from 表名 where 条件
    例：
    delete from students where id=5;
    
    实际使用逻辑删除，只是修改了isdelete的值：
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
    id:字段名，int:数据的类型，整数，unsigned：无符号范围(从0开始，没有负数，本来是负数的部分加到正数上去），
    primary key:主键，auto_increment：自动增长，not null：不能为空，
    - name varchar(20)的字符个数为20可变，default ''默认值为空
    - age tinyint极小值，unsigned无负数，范围0-255，default 0默认为0
    - height decimal(5, 2)身高的值有五位，小数点后面两位
    - gender enum枚举，'男','女','中性','保密' 可以用数字1,2,3,4替代，默认值为保密(没有给值，就是默认值保密)
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
    select name,age from students;

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
    
    select * from students where id=1 or id=3 or id=8;
    
- 模糊查询
    like
    %表示任意多个任意字符
    _表示一个任意字符
    
    rlike  正则查询  比如查询姓周的学生
    select name from students where name rlike "^周.*";

- 范围查询

    in表示在一个非连续的范围内(类似于或)
    查询编号是1或3或8的学生
    select * from students where id in(1,3,8);
    select * from students where id=1 or id=3 or id=8;  两个结果相同
    
    between ... and ...表示在一个连续的范围内
    select * from students where id between 3 and 8;   查询结果是3到8之间的学生
    
    not in不在非连续范围内
    select * from students where id not in (3,8,10);   除了3,8,10以外的学生
    select * from students where id!=3 and id!=8 and id!=10; 

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
默认按照列值从小到大排列（asc,可以不用写）
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
count(*)表示计算总行数，括号中写星或列名，结果是相同的
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
    当数据量过大时，在一页中查看所有的数据是一件非常麻烦的事情
    
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

- 语法，on后面是查询的条件
    select * from 表1 inner或left或right join 表2 on 表1.列 = 表2.列
    
- 例1：使用内连接查询班级表与学生表
    学生表中的cls_id即班级，根据学生表中的cls_id和班级表中的id查询数据
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
    
    我们也可以只取出部分数据，比如只需要学生的名称和班级名称
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
    - 重命名简化写法，将学生表重命名为s，班级表重命名为c
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

- 例2：使用左连接查询班级表与学生表，学生表为基准，班级表没有的就是Null，周杰的班级编号是5,班级表中没有5       
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
- 左连接两个数据表在left join左右交换一下位置，就变成了右连接
- select s.id, s.name, c.name from classes as c left join students as s on s.cls_id=c.id; 
   
- 例3：使用右连接查询班级表与学生表, 以班级表为基准，学生表没有的就为空，但是该数据库，学生比班级多，因此多的学生表多的学生直接删除
    select s.id, s.name, c.name from students as s right join classes as c on s.cls_id=c.id;
    +------+--------+-------------+
    | id   | name   | name        |
    +------+--------+-------------+
    |    1 | 小明   | python_01期 |
    |    2 | 小月月 | python_02期 |
    |    3 | 彭于晏 | python_01期 |
    |    4 | 刘德华 | python_02期 |
    |    5 | 黄蓉   | python_01期 |
    |    6 | 凤姐   | python_02期 |
    |    7 | 王祖贤 | python_01期 |
    |    8 | 周杰伦 | python_01期 |
    |    9 | 程坤   | python_02期 |
    |   10 | 刘亦菲 | python_02期 |
    |   11 | 金星   | python_03期 |
    |   12 | 静香   | python_04期 |
    |   13 | 郭靖   | python_04期 |
    +------+--------+-------------+


- 交集结果中取出特定的值使用having，推荐使用
    select s.id, s.name, c.name from students as s left join classes as c on s.cls_id=c.id having c.name is null;
    取出班级名称为空的学生
    +----+------+------+
    | id | name | name |
    +----+------+------+
    | 14 | 周杰 | NULL |
    +----+------+------+

- 原数据表中取结果使用where,但是该处的交集也可以使用where取出结果
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


# 第四部分：MySQL模拟操作京东商品数据库

# 7. MySQL模拟操作京东商品数据库

## 7.1. 准备数据
- 详细案例参考html文件16.1
    -- 创建 "京东" 数据库
    create database jing_dong charset=utf8;
    
    -- 使用 "京东" 数据库
    use jing_dong;
    
    -- 创建一个商品goods数据表
    create table goods(
        id int unsigned primary key auto_increment not null,
        name varchar(150) not null,
        cate_name varchar(40) not null,
        brand_name varchar(40) not null,
        price decimal(10,3) not null default 0,
        is_show bit not null default 1,
        is_saleoff bit not null default 0
    );
    
    查看数据库 数据表 常用命令：
    show databases;        显示所有数据库
    select database();     显示当前数据库信息
    show tables;           显示所有数据表
    desc goods;            显示当前数据表的字段信息
    select * from goods;   显示当前数据表
    
- 查看数据库
    mysql> select * from goods;
    +----+---------------------------------+---------------+------------+-----------+---------+------------+
    | id | name                            | cate_name     | brand_name | price     | is_show | is_saleoff |
    +----+---------------------------------+---------------+------------+-----------+---------+------------+
    |  1 | r510vc 15.6英寸笔记本           | 笔记本        | 华硕       |  3399.000 |        |            |
    |  2 | y400n 14.0英寸笔记本电脑        | 笔记本        | 联想       |  4999.000 |        |            |
    |  3 | g150th 15.6英寸游戏本           | 游戏本        | 雷神       |  8499.000 |        |            |
    |  4 | x550cc 15.6英寸笔记本           | 笔记本        | 华硕       |  2799.000 |        |            |
    |  5 | x240 超极本                     | 超级本        | 联想       |  4880.000 |        |            |
    |  6 | u330p 13.3英寸超极本            | 超级本        | 联想       |  4299.000 |        |            |
    |  7 | svp13226scb 触控超极本          | 超级本        | 索尼       |  7999.000 |        |            |
    |  8 | ipad mini 7.9英寸平板电脑       | 平板电脑      | 苹果       |  1998.000 |        |            |
    |  9 | ipad air 9.7英寸平板电脑        | 平板电脑      | 苹果       |  3388.000 |        |            |
    | 10 | ipad mini 配备 retina 显示屏    | 平板电脑      | 苹果       |  2788.000 |        |            |
    | 11 | ideacentre c340 20英寸一体电脑  | 台式机        | 联想       |  3499.000 |        |            |
    | 12 | vostro 3800-r1206 台式电脑      | 台式机        | 戴尔       |  2899.000 |        |            |
    | 13 | imac me086ch/a 21.5英寸一体电脑 | 台式机        | 苹果       |  9188.000 |        |            |
    | 14 | at7-7414lp 台式电脑 linux ）    | 台式机        | 宏碁       |  3699.000 |        |            |
    | 15 | z220sff f4f06pa工作站           | 服务器/工作站 | 惠普       |  4288.000 |        |            |
    | 16 | poweredge ii服务器              | 服务器/工作站 | 戴尔       |  5388.000 |        |            |
    | 17 | mac pro专业级台式电脑           | 服务器/工作站 | 苹果       | 28888.000 |        |            |
    | 18 | hmz-t3w 头戴显示设备            | 笔记本配件    | 索尼       |  6999.000 |        |            |
    | 19 | 商务双肩背包                    | 笔记本配件    | 索尼       |    99.000 |        |            |
    | 20 | x3250 m4机架式服务器            | 服务器/工作站 | ibm        |  6888.000 |        |            |
    | 21 | 商务双肩背包                    | 笔记本配件    | 索尼       |    99.000 |        |            |
    +----+---------------------------------+---------------+------------+-----------+---------+------------+
    21 rows in set (0.00 sec)
   
## 7.2 SQL演练
- 详细案例参考html文件16.2
- 所有商品的平均价格
    mysql> select round(avg(price),2) from goods;
    +---------------------+
    | round(avg(price),2) |
    +---------------------+
    |             5570.57 |
    +---------------------+
    1 row in set (0.00 sec)
    
- 商品进行分类，显示分类后的平均价格
    mysql>  select cate_name,round(avg(price),1) from goods group by cate_name;
    +---------------+---------------------+
    | cate_name     | round(avg(price),1) |
    +---------------+---------------------+
    | 笔记本        |              3732.3 |
    | 游戏本        |              8499.0 |
    | 超级本        |              5726.0 |
    | 平板电脑      |              2724.7 |
    | 台式机        |              4821.3 |
    | 服务器/工作站 |             11363.0 |
    | 笔记本配件    |              2399.0 |
    +---------------+---------------------+
    7 rows in set (0.00 sec)
    
- 查询每种类型的商品中 最贵、最便宜、平均价、数量
    select cate_name,max(price),min(price),avg(price),count(*) from goods group by cate_name;


- 查询所有价格大于平均价格的商品，并且按价格降序排序
    select id,name,price from goods 
    where price > (select round(avg(price),2) as avg_price from goods) 
    order by price desc;
    
    +----+---------------------------------+-----------+
    | id | name                            | price     |
    +----+---------------------------------+-----------+
    | 17 | mac pro专业级台式电脑           | 28888.000 |
    | 13 | imac me086ch/a 21.5英寸一体电脑 |  9188.000 |
    |  3 | g150th 15.6英寸游戏本           |  8499.000 |
    |  7 | svp13226scb 触控超极本          |  7999.000 |
    | 18 | hmz-t3w 头戴显示设备            |  6999.000 |
    | 20 | x3250 m4机架式服务器            |  6888.000 |
    +----+---------------------------------+-----------+
    6 rows in set (0.00 sec)


### 连接查询

- 查询出每个分类中最贵商品的价格
    mysql> select cate_name,max(price) from goods group by cate_name;
    +---------------+------------+
    | cate_name     | max(price) |
    +---------------+------------+
    | 笔记本        |   4999.000 |
    | 游戏本        |   8499.000 |
    | 超级本        |   7999.000 |
    | 平板电脑      |   3388.000 |
    | 台式机        |   9188.000 |
    | 服务器/工作站 |  28888.000 |
    | 笔记本配件    |   6999.000 |
    +---------------+------------+ 
- 上面查出了每个分类中最贵的价格，现在要查询每种类型中最贵的电脑信息 
- 我们可以使用连接查询，可以将上面的表as作为一个表，然后和原始商品表进行连接查询


- 使用子查询创建一个新表
    mysql> select * from (select cate_name,max(price) as max_price from goods group by cate_name) as g_new;
    +---------------+-----------+
    | cate_name     | max_price |
    +---------------+-----------+
    | 笔记本        |  4999.000 |
    | 游戏本        |  8499.000 |
    | 超级本        |  7999.000 |
    | 平板电脑      |  3388.000 |
    | 台式机        |  9188.000 |
    | 服务器/工作站 | 28888.000 |
    | 笔记本配件    |  6999.000 |
    +---------------+-----------+

- 先创建一个新表，包含类别名称和最高价，并以此新表为基准，得到一个新表           
    mysql> 
    select * from (select cate_name,max(price) as max_price from goods group by cate_name) as g_new
    left join goods as g
    on g_new.cate_name=g.cate_name and g_new.max_price=g.price;
    +---------------+-----------+------+---------------------------------+---------------+------------+-----------+---------+------------+
    | cate_name     | max_price | id   | name                            | cate_name     | brand_name | price     | is_show | is_saleoff |
    +---------------+-----------+------+---------------------------------+---------------+------------+-----------+---------+------------+
    | 笔记本        |  4999.000 |    2 | y400n 14.0英寸笔记本电脑        | 笔记本        | 联想       |  4999.000 |        |            |
    | 游戏本        |  8499.000 |    3 | g150th 15.6英寸游戏本           | 游戏本        | 雷神       |  8499.000 |        |            |
    | 超级本        |  7999.000 |    7 | svp13226scb 触控超极本          | 超级本        | 索尼       |  7999.000 |        |            |
    | 平板电脑      |  3388.000 |    9 | ipad air 9.7英寸平板电脑        | 平板电脑      | 苹果       |  3388.000 |        |            |
    | 台式机        |  9188.000 |   13 | imac me086ch/a 21.5英寸一体电脑 | 台式机        | 苹果       |  9188.000 |        |            |
    | 服务器/工作站 | 28888.000 |   17 | mac pro专业级台式电脑           | 服务器/工作站 | 苹果       | 28888.000 |        |            |
    | 笔记本配件    |  6999.000 |   18 | hmz-t3w 头戴显示设备            | 笔记本配件    | 索尼       |  6999.000 |        |            |
    +---------------+-----------+------+---------------------------------+---------------+------------+-----------+---------+------------+
    7 rows in set (0.00 sec)
    
## 7.2.1 拆表创建表
- 详细案例参考html文件16.2 

- 将查询结果写入一个新表
- 创建商品分类表
    create table if not exists goods_cates(
        id int unsigned primary key auto_increment,
        name varchar(40) not null
    );

- 查询goods表中商品的种类
    select cate_name from goods group by cate_name;

- 将分组结果写入到goods_cates数据表
    insert into goods_cates (name) select cate_name from goods group by cate_name;

- 同步表数据
    通过goods_cates数据表来更新goods表，将goods表类别名设置为分类表的id（cate_name外键是分类表的主键id）
    update goods as g inner join goods_cates as c on g.cate_name=c.name set g.cate_name=c.id;
 
    
- 通过create...select来创建数据表并且同时写入记录,一步到位
    -- select brand_name from goods group by brand_name;
    -- 在创建数据表的时候一起插入数据
    -- 注意: 需要对brand_name 用as起别名，否则name字段就没有值
    create table goods_brands (
        id int unsigned primary key auto_increment,
        name varchar(40) not null) select brand_name as name from goods group by brand_name;

- 同步数据
    通过goods_brands数据表来更新goods数据表
    update goods as g inner join goods_brands as b on g.brand_name=b.name set g.brand_name=b.id;

- 修改表结构
    将goods标注的分类和品牌字符类型修改和分类表和品牌表中id的数据类型一致
    查看 goods 的数据表结构,会发现 cate_name 和 brand_name对应的类型为 varchar 但是存储的都是数字
    通过alter table语句修改表结构
    alter table goods  
    change cate_name cate_id int unsigned not null,
    change brand_name brand_id int unsigned not null;
    
    mysql> desc goods;
    +------------+------------------+------+-----+---------+----------------+
    | Field      | Type             | Null | Key | Default | Extra          |
    +------------+------------------+------+-----+---------+----------------+
    | id         | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
    | name       | varchar(150)     | NO   |     | NULL    |                |
    | cate_id    | int(10) unsigned | NO   |     | NULL    |                |
    | brand_id   | int(10) unsigned | NO   |     | NULL    |                |
    | price      | decimal(10,3)    | NO   |     | 0.000   |                |
    | is_show    | bit(1)           | NO   |     | b'1'    |                |
    | is_saleoff | bit(1)           | NO   |     | b'0'    |                |
    +------------+------------------+------+-----+---------+----------------+
    7 rows in set (0.01 sec)


# 第五部分：MySQL与Python交互
## 8.1 创建连接
- 详细案例参考html文件16.4

- 引入模块
    在py文件中引入pymysql模块
    from pymysql import *

- Connection 对象
    用于建立与数据库的连接
    创建对象：调用connect()方法
    
    conn=connect(参数列表)
    参数host：连接的mysql主机，如果本地就使用'localhost'
    参数port：连接的mysql主机的端口，默认(安装软件时候默认的端口)是3306
    参数database：数据库的名称
    参数user：数据库的用户名
    参数password：数据库的密码
    参数charset：通信采用的编码方式，推荐使用utf8

- 对象的方法
    close()关闭连接
    commit()提交
    cursor()返回Cursor对象，用于执行sql语句并获得结果

- Cursor对象
    用于执行sql语句，使用频度最高的语句为select、insert、update、delete
    获取Cursor对象：调用Connection对象的cursor()方法
    cs1=conn.cursor()

- 对象的方法
    close()关闭
    execute(operation [, parameters ])执行语句，返回受影响的行数，主要用于执行insert、update、delete语句，也可以执行create、alter、drop等语句
    fetchone()执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
    fetchall()执行查询时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回

- 对象的属性
    rowcount只读属性，表示最近一次execute()执行后受影响的行数
    connection获得当前连接对象

- 参考01_MySQL案例：
    002/003/004
    


## 8.2 参数化
- 参数化
    sql语句的参数化，可以有效防止sql注入
    注意：此处不同于python的字符串格式化，全部使用%s占位
    
- 参考01_MySQL案例：
    005/006


# 第六部分: MySQL高级
- 详细资料参考html文件17

## 9.1 视图

- 1. 问题
    对于复杂的查询，往往是有多个数据表进行关联查询而得到，如果数据库因为需求等原因发生了改变，
    为了保证查询出来的数据与之前相同，则需要在多个地方进行修改，维护起来非常麻烦
    解决办法：定义视图
    
- 2. 视图是什么
    通俗的讲，视图就是一条SELECT语句执行后返回的结果集，该条查询语句的结果保存为一张表，就是视图。
    所以我们在创建视图的时候，主要的工作就落在创建这条SQL查询语句上。
    视图是对若干张基本表的引用，一张虚表，查询语句执行的结果，
    不存储具体的数据（基本表数据发生了改变，视图也会跟着改变）；
    方便操作，特别是查询操作，减少复杂的SQL语句，增强可读性；
    
- 3. 定义视图
    建议以v_开头
    create view 视图名称 as select语句;
    
- 4. 查看视图
    查看表会将所有的视图也列出来
    show tables;
    
- 5. 使用视图
    视图的用途就是查询
    select * from v_stu_score;
    
- 6. 删除视图
    drop view 视图名称;
    例：
    drop view v_stu_sco;
    
- 8. 视图的作用
    提高了重用性，就像一个函数
    对数据库重构，却不影响程序的运行
    提高了安全性能，可以对不同的用户
    让数据更加清晰

- 实例：
- 提取出京东商品数据库三张表的所有信息
mysql> select * from goods as g left join goods_cates as c on g.cate_id=c.id left join goods_brands as b on g.brand_id=b.id;
+----+---------------------------------+---------+----------+-----------+---------+------------+------+---------------+------+------+
| id | name                            | cate_id | brand_id | price     | is_show | is_saleoff | id   | name          | id   | name |
+----+---------------------------------+---------+----------+-----------+---------+------------+------+---------------+------+------+
|  1 | r510vc 15.6英寸笔记本           |       1 |        1 |  3399.000 |        |            |    1 | 笔记本        |    1 | 华硕 |
|  2 | y400n 14.0英寸笔记本电脑        |       1 |        2 |  4999.000 |        |            |    1 | 笔记本        |    2 | 联想 |
|  4 | x550cc 15.6英寸笔记本           |       1 |        1 |  2799.000 |        |            |    1 | 笔记本        |    1 | 华硕 |
|  3 | g150th 15.6英寸游戏本           |       2 |        3 |  8499.000 |        |            |    2 | 游戏本        |    3 | 雷神 |
|  5 | x240 超极本                     |       3 |        2 |  4880.000 |        |            |    3 | 超级本        |    2 | 联想 |
|  6 | u330p 13.3英寸超极本            |       3 |        2 |  4299.000 |        |            |    3 | 超级本        |    2 | 联想 |
|  7 | svp13226scb 触控超极本          |       3 |        4 |  7999.000 |        |            |    3 | 超级本        |    4 | 索尼 |
|  8 | ipad mini 7.9英寸平板电脑       |       4 |        5 |  1998.000 |        |            |    4 | 平板电脑      |    5 | 苹果 |
|  9 | ipad air 9.7英寸平板电脑        |       4 |        5 |  3388.000 |        |            |    4 | 平板电脑      |    5 | 苹果 |
| 10 | ipad mini 配备 retina 显示屏    |       4 |        5 |  2788.000 |        |            |    4 | 平板电脑      |    5 | 苹果 |
| 11 | ideacentre c340 20英寸一体电脑  |       5 |        2 |  3499.000 |        |            |    5 | 台式机        |    2 | 联想 |
| 12 | vostro 3800-r1206 台式电脑      |       5 |        6 |  2899.000 |        |            |    5 | 台式机        |    6 | 戴尔 |
| 13 | imac me086ch/a 21.5英寸一体电脑 |       5 |        5 |  9188.000 |        |            |    5 | 台式机        |    5 | 苹果 |
| 14 | at7-7414lp 台式电脑 linux ）    |       5 |        7 |  3699.000 |        |            |    5 | 台式机        |    7 | 宏碁 |
| 15 | z220sff f4f06pa工作站           |       6 |        8 |  4288.000 |        |            |    6 | 服务器/工作站 |    8 | 惠普 |
| 16 | poweredge ii服务器              |       6 |        6 |  5388.000 |        |            |    6 | 服务器/工作站 |    6 | 戴尔 |
| 17 | mac pro专业级台式电脑           |       6 |        5 | 28888.000 |        |            |    6 | 服务器/工作站 |    5 | 苹果 |
| 20 | x3250 m4机架式服务器            |       6 |        9 |  6888.000 |        |            |    6 | 服务器/工作站 |    9 | ibm  |
| 18 | hmz-t3w 头戴显示设备            |       7 |        4 |  6999.000 |        |            |    7 | 笔记本配件    |    4 | 索尼 |
| 19 | 商务双肩背包                    |       7 |        4 |    99.000 |        |            |    7 | 笔记本配件    |    4 | 索尼 |
| 21 | 商务双肩背包                    |       7 |        4 |    99.000 |        |            |    7 | 笔记本配件    |    4 | 索尼 |
+----+---------------------------------+---------+----------+-----------+---------+------------+------+---------------+------+------+
21 rows in set (0.03 sec)

- 提取出京东商品数据库三张表的部分信息
mysql> select g.*, c.name as cate_name, b.name as brand_name from goods as g left join goods_cates as c on g.cate_id=c.id left join goods_brands as b on g.brand_id=b.id;
+----+---------------------------------+---------+----------+-----------+---------+------------+---------------+------------+
| id | name                            | cate_id | brand_id | price     | is_show | is_saleoff | cate_name     | brand_name |
+----+---------------------------------+---------+----------+-----------+---------+------------+---------------+------------+
|  1 | r510vc 15.6英寸笔记本           |       1 |        1 |  3399.000 |        |            | 笔记本        | 华硕       |
|  2 | y400n 14.0英寸笔记本电脑        |       1 |        2 |  4999.000 |        |            | 笔记本        | 联想       |
|  3 | g150th 15.6英寸游戏本           |       2 |        3 |  8499.000 |        |            | 游戏本        | 雷神       |
|  4 | x550cc 15.6英寸笔记本           |       1 |        1 |  2799.000 |        |            | 笔记本        | 华硕       |
|  5 | x240 超极本                     |       3 |        2 |  4880.000 |        |            | 超级本        | 联想       |
|  6 | u330p 13.3英寸超极本            |       3 |        2 |  4299.000 |        |            | 超级本        | 联想       |
|  7 | svp13226scb 触控超极本          |       3 |        4 |  7999.000 |        |            | 超级本        | 索尼       |
|  8 | ipad mini 7.9英寸平板电脑       |       4 |        5 |  1998.000 |        |            | 平板电脑      | 苹果       |
|  9 | ipad air 9.7英寸平板电脑        |       4 |        5 |  3388.000 |        |            | 平板电脑      | 苹果       |
| 10 | ipad mini 配备 retina 显示屏    |       4 |        5 |  2788.000 |        |            | 平板电脑      | 苹果       |
| 11 | ideacentre c340 20英寸一体电脑  |       5 |        2 |  3499.000 |        |            | 台式机        | 联想       |
| 12 | vostro 3800-r1206 台式电脑      |       5 |        6 |  2899.000 |        |            | 台式机        | 戴尔       |
| 13 | imac me086ch/a 21.5英寸一体电脑 |       5 |        5 |  9188.000 |        |            | 台式机        | 苹果       |
| 14 | at7-7414lp 台式电脑 linux ）    |       5 |        7 |  3699.000 |        |            | 台式机        | 宏碁       |
| 15 | z220sff f4f06pa工作站           |       6 |        8 |  4288.000 |        |            | 服务器/工作站 | 惠普       |
| 16 | poweredge ii服务器              |       6 |        6 |  5388.000 |        |            | 服务器/工作站 | 戴尔       |
| 17 | mac pro专业级台式电脑           |       6 |        5 | 28888.000 |        |            | 服务器/工作站 | 苹果       |
| 18 | hmz-t3w 头戴显示设备            |       7 |        4 |  6999.000 |        |            | 笔记本配件    | 索尼       |
| 19 | 商务双肩背包                    |       7 |        4 |    99.000 |        |            | 笔记本配件    | 索尼       |
| 20 | x3250 m4机架式服务器            |       6 |        9 |  6888.000 |        |            | 服务器/工作站 | ibm        |
| 21 | 商务双肩背包                    |       7 |        4 |    99.000 |        |            | 笔记本配件    | 索尼       |
+----+---------------------------------+---------+----------+-----------+---------+------------+---------------+------------+
21 rows in set (0.00 sec)

- 将上面查询的结果作为一张虚拟的表，这就是视图
mysql> create view v_goods_info as select g.*, c.name as cate_name, b.name as brand_name from goods as g left join goods_cates as c on g.cate_id=c.id left join goods_brands as b on g.brand_id=b.id;
Query OK, 0 rows affected (0.02 sec)

mysql> show tables
    -> ;
+---------------------+
| Tables_in_jing_dong |
+---------------------+
| goods               |
| goods_brands        |
| goods_cates         |
| v_goods_info        |
+---------------------+
4 rows in set (0.00 sec)


- 插入一条数据，再次查看视图，已经自动更新
mysql> insert into goods values(0,'笔记本包','7','5','109',default,default);
Query OK, 1 row affected (0.01 sec)
mysql> select * from v_goods_info;
+----+---------------------------------+---------+----------+-----------+---------+------------+---------------+------------+
| id | name                            | cate_id | brand_id | price     | is_show | is_saleoff | cate_name     | brand_name |
+----+---------------------------------+---------+----------+-----------+---------+------------+---------------+------------+
|  1 | r510vc 15.6英寸笔记本           |       1 |        1 |  3399.000 |        |            | 笔记本        | 华硕       |
|  2 | y400n 14.0英寸笔记本电脑        |       1 |        2 |  4999.000 |        |            | 笔记本        | 联想       |
|  3 | g150th 15.6英寸游戏本           |       2 |        3 |  8499.000 |        |            | 游戏本        | 雷神       |
|  4 | x550cc 15.6英寸笔记本           |       1 |        1 |  2799.000 |        |            | 笔记本        | 华硕       |
|  5 | x240 超极本                     |       3 |        2 |  4880.000 |        |            | 超级本        | 联想       |
|  6 | u330p 13.3英寸超极本            |       3 |        2 |  4299.000 |        |            | 超级本        | 联想       |
|  7 | svp13226scb 触控超极本          |       3 |        4 |  7999.000 |        |            | 超级本        | 索尼       |
|  8 | ipad mini 7.9英寸平板电脑       |       4 |        5 |  1998.000 |        |            | 平板电脑      | 苹果       |
|  9 | ipad air 9.7英寸平板电脑        |       4 |        5 |  3388.000 |        |            | 平板电脑      | 苹果       |
| 10 | ipad mini 配备 retina 显示屏    |       4 |        5 |  2788.000 |        |            | 平板电脑      | 苹果       |
| 11 | ideacentre c340 20英寸一体电脑  |       5 |        2 |  3499.000 |        |            | 台式机        | 联想       |
| 12 | vostro 3800-r1206 台式电脑      |       5 |        6 |  2899.000 |        |            | 台式机        | 戴尔       |
| 13 | imac me086ch/a 21.5英寸一体电脑 |       5 |        5 |  9188.000 |        |            | 台式机        | 苹果       |
| 14 | at7-7414lp 台式电脑 linux ）    |       5 |        7 |  3699.000 |        |            | 台式机        | 宏碁       |
| 15 | z220sff f4f06pa工作站           |       6 |        8 |  4288.000 |        |            | 服务器/工作站 | 惠普       |
| 16 | poweredge ii服务器              |       6 |        6 |  5388.000 |        |            | 服务器/工作站 | 戴尔       |
| 17 | mac pro专业级台式电脑           |       6 |        5 | 28888.000 |        |            | 服务器/工作站 | 苹果       |
| 18 | hmz-t3w 头戴显示设备            |       7 |        4 |  6999.000 |        |            | 笔记本配件    | 索尼       |
| 19 | 商务双肩背包                    |       7 |        4 |    99.000 |        |            | 笔记本配件    | 索尼       |
| 20 | x3250 m4机架式服务器            |       6 |        9 |  6888.000 |        |            | 服务器/工作站 | ibm        |
| 21 | 商务双肩背包                    |       7 |        4 |    99.000 |        |            | 笔记本配件    | 索尼       |
| 22 | 笔记本包                        |       7 |        5 |   109.000 |        |            | 笔记本配件    | 苹果       |
+----+---------------------------------+---------+----------+-----------+---------+------------+---------------+------------+

## 9.2 事务

- 所谓事务,它是一个操作序列，这些操作要么都执行，要么都不执行，它是一个不可分割的工作单位。
    例如，银行转帐工作：从一个帐号扣款并使另一个帐号增款，
    这两个操作要么都执行，要么都不执行。所以，应该把他们看成一个事务。
    事务是数据库维护数据一致性的单位，在每个事务结束时，都能保持数据一致性

- 事务四大特性(简称ACID)
    原子性(Atomicity)
    一致性(Consistency)
    隔离性(Isolation)
    持久性(Durability)

- 下面举一个银行应用是解释事务必要性的一个经典例子。假如一个银行的数据库有两张表：支票表（checking）和储蓄表（savings）。
    现在要从用户Jane的支票账户转移200美元到她的储蓄账户，那么至少需要三个步骤：
    1. 检查支票账户的余额高于或者等于200美元。
    2. 从支票账户余额中减去200美元。
    3. 在储蓄帐户余额中增加200美元。

上述三个步骤的操作必须打包在一个事务中，任何一个步骤失败，则必须回滚所有的步骤。

- 一个很好的事务处理系统，必须具备这些标准特性：

    原子性（atomicity）
    一个事务必须被视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，
    要么全部失败回滚，对于一个事务来说，不可能只执行其中的一部分操作，这就是事务的原子性

    一致性（consistency）
    数据库总是从一个一致性的状态转换到另一个一致性的状态。
    （在前面的例子中，一致性确保了，即使在执行第三、四条语句之间时系统崩溃，
    支票账户中也不会损失200美元，因为事务最终没有提交，所以事务中所做的修改也不会保存到数据库中。）

    隔离性（isolation）
    通常来说，一个事务所做的修改在最终提交以前，对其他事务是不可见的。
    （在前面的例子中，当执行完第三条语句、第四条语句还未开始时，此时有另外的一个账户汇总程序开始运行，
    则其看到支票帐户的余额并没有被减去200美元。）

    持久性（durability）
    一旦事务提交，则其所做的修改会永久保存到数据库。（此时即使系统崩溃，修改的数据也不会丢失。）

- 事务命令
    表的引擎类型必须是innodb类型才可以使用事务，这是mysql表的默认引擎
    查看表的创建语句，show create table goods;
    可以看到engine=innodb    

- 开启事务，命令如下：
    开启事务后执行修改命令，变更会维护到本地缓存中，而不维护到物理表中
    begin;
    或者
    start transaction;

- 提交事务，命令如下
    将缓存中的数据变更维护到物理表中
    commit;

- 回滚事务，命令如下
    注意：在提交前回滚，提交后就不能回滚了，只能删除数据了

    放弃缓存中变更的数据
    rollback;
    注意：
    修改数据的命令会自动的触发事务，包括insert、update、delete
    而在SQL语句中有手动开启事务的原因是：可以进行多次数据的修改，如果成功一起成功，否则一起会滚到之前的数据

## 9.3 索引

- 索引是什么
    索引是一种特殊的文件(InnoDB数据表上的索引是表空间的一个组成部分)，
    它们包含着对数据表里所有记录的引用指针。
    更通俗的说，数据库索引好比是一本书前面的目录，能加快数据库的查询速度

- 索引目的
    索引的目的在于提高查询效率，可以类比字典，如果要查“mysql”这个单词，
    我们肯定需要定位到m字母，然后从下往下找到y字母，再找到剩下的sql。
    如果没有索引，那么你可能需要把所有单词看一遍才能找到你想要的，

- 索引原理
    数据库也是一样，但显然要复杂许多，因为不仅面临着等值查询，
    还有范围查询(>、<、between、in)、模糊查询(like)、并集查询(or)等等。
    数据库应该选择怎么样的方式来应对所有的问题呢？
    我们回想字典的例子，能不能把数据分成段，然后分段查询呢？
    最简单的如果1000条数据，1到100分成第一段，101到200分成第二段，
    201到300分成第三段……这样查第250条数据，只要找第三段就可以了，
    一下子去除了90%的无效数据。
    
- 索引使用
    - 查看索引
    show index from 表名;
    
    - 创建索引
    如果指定字段是字符串，需要指定长度，建议长度与定义字段时的长度一致
    字段类型如果不是字符串，可以不填写长度部分
    create index 索引名称 on 表名(字段名称(长度))

    - 删除索引：
    drop index 索引名称 on 表名;
    
    
- 索引查询时间对比
    - 开启运行时间监测：
    set profiling=1;
    - 查找第1万条数据ha-99999
    select * from test_index where title='ha-99999';
    - 查看执行的时间：
    show profiles;
    
    - 为表title_index的title这一列创建索引：
    create index title_index on test_index(title(10));
    - 执行查询语句：
    select * from test_index where title='ha-99999';
    - 再次查看执行的时间
    show profiles;
    
    mysql> show profiles;
    +----------+------------+---------------------------------------------------+
    | Query_ID | Duration   | Query                                             |
    +----------+------------+---------------------------------------------------+
    |        1 | 0.07055400 | select * from test_index where title='ha-99999'   |
    |        2 | 0.58853000 | create index title_index on test_index(title(10)) |
    |        3 | 0.01141550 | show index from test_index                        |
    |        4 | 0.00039400 | select * from test_index where title='ha-99999'   |
    +----------+------------+---------------------------------------------------+
    4 rows in set, 1 warning (0.00 sec)
    - 明显可以看见，创建索引后，再次查询，时间明显缩短

- 参考案例007

- 注意
    要注意的是，建立太多的索引将会影响更新和插入的速度，
    因为它需要同样更新每个索引文件。对于一个经常需要更新和插入的表格，
    就没有必要为一个很少使用的where字句单独建立索引了，
    对于比较小的表，排序的开销不会很大，也没有必要建立另外的索引。
    建立索引会占用磁盘空间
    
    表的主键就相当于主键
    表中存在外键也相当于主键
    因此，通过主键搜索速度最快，其它字段速度就会慢一些


## 9.4 账户管理
- 参考index文件17.4

- 账户管理
    在生产环境下操作数据库时，绝对不可以使用root账户连接，而是创建特定的账户，授予这个账户特定的操作权限，然后连接进行操作，主要的操作就是数据的crud
    MySQL账户体系：根据账户所具有的权限的不同，MySQL的账户可以分为以下几种
        服务实例级账号：，启动了一个mysqld，即为一个数据库实例；如果某用户如root,拥有服务实例级分配的权限，那么该账号就可以删除所有的数据库、连同这些库中的表
        数据库级别账号：对特定数据库执行增删改查的所有操作
        数据表级别账号：对特定表执行增删改查等所有操作
        字段级别的权限：对某些表的特定字段进行操作
        存储程序级别的账号：对存储程序进行增删改查的操作
    账户的操作主要包括创建账户、删除账户、修改密码、授权权限等

- 注意：
    进行账户操作时，需要使用root账户登录，这个账户拥有最高的实例级权限
    通常都使用数据库级操作权限


## 9.5 MySQL主从
- 参考index文件17.5

- 主从同步的定义
    主从同步使得数据可以从一个数据库服务器复制到其他服务器上，在复制数据时，
    一个服务器充当主服务器（master），其余的服务器充当从服务器（slave）。
    因为复制是异步进行的，所以从服务器不需要一直连接着主服务器，
    从服务器甚至可以通过拨号断断续续地连接主服务器。
    通过配置文件，可以指定复制所有的数据库，某个数据库，甚至是某个数据库上的某个表。
    
     MongoDB副本集和MySQL主从区别：
     - MongoDB是在同一个服务器(一台机器)，同时复制备份多个数据库
     - MySQL复制备份数据是在多个服务器（多台机器)，复制备份多个数据库
     - MongoDB复制备份是同步的，MySQL复制备份可以是异步的，也可以主从同步
     - MongoDB读写在指定的某一个数据库作为主数据库
     - MySQL一般主服务器写，从服务器读，读写分离
    
- 使用主从同步的好处：(读写分离，数据备份，负载均衡)
    - 通过增加从服务器来提高数据库的性能，在主服务器上执行写入和更新，在从服务器上向外提供读功能，
        可以动态地调整从服务器的数量，从而调整整个数据库的性能。
    - 提高数据安全，因为数据已复制到从服务器，从服务器可以终止复制进程，
        所以，可以在从服务器上备份而不破坏主服务器相应数据
    - 在主服务器上生成实时数据，而在从服务器上分析这些数据，从而提高主服务器的性能

- 配置主从同步的基本步骤
    有很多种配置主从同步的方法，可以总结为如下的步骤：
    1. 在主服务器上，必须开启二进制日志机制和配置一个独立的ID
    2. 在每一个从服务器上，配置一个唯一的ID，创建一个用来专门复制主服务器数据的账号
    3. 在开始复制进程前，在主服务器上记录二进制文件的位置信息
    4. 如果在开始复制之前，数据库中已经有数据，就必须先创建一个数据快照（可以使用mysqldump导出数据库，或者直接复制数据文件）
    5. 配置从服务器要连接的主服务器的IP地址和登陆授权，二进制日志文件名和位置




    
    
    