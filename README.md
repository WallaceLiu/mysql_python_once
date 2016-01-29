# mysql_python_once
http://wallaceliu.github.io/mysql_python_once/

# 项目背景
最近做个项目，需要进行试驾分析，所谓“试驾”，是指顾客在 4S 店指定人员的陪同下，沿着指定的路线驾驶车辆，从而了解这款汽车的行驶性能和操控性能。通常，无论是车厂（制造商），还是4S店（经销商），对车辆的试驾都比较感兴趣。从车厂的角度，不仅仅可以知道某辆车是否受欢迎，还可以监控4S店对车辆的使用的情况（车厂肯定不愿意原本是用来卖钱的车被私用）。

所以，试驾分析，是利用车载设备，比如 OBD、车机，或是其他能监控车辆的设备，我们采用 OBD，发送给软件平台一系列车辆实时状态消息，如GPS定位、百公里耗油、报警等，平台根据这些消息，以及4S店设置的电子围栏，进行试驾分析，包括试驾开始时间、试驾结束时间、试驾持续时间、行驶里程、油耗、平均速度、最大速度等。

试驾分析算法，虽然有一定难度（核心算法1000多行），但跟测试这个算法相比，简直容易得不了。OBD 由另一个公司生产，他们只给了我们文档，来说明OBD消息二进制流的格式，由我们自己解析，再进行试驾分析。事实上，这个项目我的工作，要完成两个程序：消息解析服务和试驾分析服务，2个月完成，一共将近3.8万行代码，但是前期没有任何测试手段进行软件测试，直到3个月后公司安排实车测试~

但问题来了，如果每次想测试软件和算法，都要用实车，这成本太高了，尤其是时间成本。程序员的时间很宝贵的。唯一的办法是，另写一个程序，能够模拟OBD发送消息，相当于把之前实车的数据“回放”一遍。不仅如此，最好能自定义几个命令，来控制消息的发送以及电子围栏和相关时间的设置，比如，
* “send”表示发送指定消息；
* “wait”表示等待指定时间后再发送一下一个消息；
* “set”表示设置电子围栏，或采集时间，或报备时间，即试驾分析只在采集时间内、报备时间外进行。
* “echo”表示显示信息。

示例：

`send 5830

wait 1

send 5841

wait 1

echo 将发送报警...

send 5842

……`

事实也是这么做的。我用 Python 写了一个程序，并利用 [nestordeharo/mysql-python-class](https://github.com/nestordeharo/mysql-python-class) 库访问 MySQL，可意外来了，时不时地程序会报错，MySQL 拒绝我的连接请求，有时一星期没事，有时完全无法使用。虽然我也知道，这个程序访问数据库太频繁，效率太低，但只是作为内部测试工具，没必要写的太好~后来实在受不了了，严重影响测试进度，就弃用上面的库，自己写个简单的 Python 库，它只访问一次数据库。

***

# 功能简介
该 Python 库只访问一次 MySQL 数据库。

***

# API
假设，有个表 t1，它有四个字段：id、name、age、loc。
## * open(self)
打开数据库。

## * close(self)
关闭数据库。

## * select(self, table, where=None, *args, **kwargs)
若查找ID为1的用户：

`SELECT id,name FROM t1 WHERE id='1'`

可以这样调用该方法：

`select('t1', 'id = %s ', 'id', 'name', id='1')`

## * insert(self, table, *args, **kwargs)
若想插入一条记录：

`INSERT INTO t1(id, name, age, loc) VALUES(2,'person2', '20', '北京')`

可以这样调用该方法：

`insert('t1', id='2', name='person2', age='20')`

## * update(self, table, where=None, *args, **kwargs)
若想更新一条记录：

`UPDATE t1 SET name='p2' WHERE id='2'`

可以这样调用该方法：

`update('t1', 'id = %s ', '2', name='p2')`

## * delete(self, table, where=None, *args)
若想删除ID为2的记录：

`DELETE FROM t1 where id='2'`

可以这样调用该方法：

`delete('t1', ' id = %s ', '2')`

## * select_advanced(self, sql, *args)
若想查找北京地区的成年人：

`SELECT id,name,age FROM t1 WHERE age>18 and loc='北京'`

可以这样调用该方法：

`select_advanced('SELECT id,name FROM t1 WHERE age > %s AND loc = %s', ('age', '18'),('loc','北京'))`

