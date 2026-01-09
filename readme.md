# 后端作业
## 后端作业一
在 fastapi 中实现 chinook 数据库中 `employee` 和 `customer` 表的增删改查接口，为查询接口完成限流，10秒限3次

## 后端作业二
1. 查询不在美国境内的客户的姓名，客户id和国家。
```sql
SELECT
	customer.customer_id AS "客户ID",
	customer.first_name || ' ' || customer.last_name AS "姓名",
	customer.country AS "国家"
FROM customer
WHERE customer.country != 'USA'
```
2. 统计不同的国家有多少个顾客。
```sql
SELECT
	customer.country AS "国家",
	COUNT(customer.customer_id) AS "顾客数量"
 FROM customer
 GROUP BY customer.country;
```
3. 2021年和2025年分别有多少张发票？这两年的发票额分别是多少？
```sql
SELECT
	EXTRACT(YEAR FROM invoice.invoice_date) AS "年份",
	COUNT(invoice.invoice_id) AS "发票数量",
  SUM(invoice.total) AS "总销售额"
FROM invoice
WHERE EXTRACT(YEAR FROM invoice.invoice_date) IN (2021, 2025)
GROUP BY "年份"
- 这个库里2010和2011没有数据
```
4. 哪位员工的顾客总数最少。
```sql
SELECT 
    e.employee_id AS "员工编号",
    e.first_name || ' ' || e.last_name AS "员工姓名",
    e.title AS "职位",
    count(c.customer_id) AS "顾客总数"
FROM employee e
LEFT JOIN customer c ON e.employee_id = c.support_rep_id
GROUP BY e.employee_id, e.first_name, e.last_name, e.title
ORDER BY "顾客总数" ASC
LIMIT 1;
```
5. 查询每个播放列表中曲目的总数。
```sql
SELECT 
    p.playlist_id AS "播放列表编号",
    p.name AS "播放列表名称",
    COUNT(pt.track_id) AS "曲目总数"
FROM playlist p
JOIN playlist_track pt ON p.playlist_id = pt.playlist_id
GROUP BY p.playlist_id, p.name
```
6. 查询不同歌单中每种流派有多少歌曲.
```sql
SELECT 
    p.playlist_id AS "歌单编号",
    p.name AS "歌单名称",
    g.name AS "流派名称",
    COUNT(t.track_id) AS "歌曲数量"
FROM playlist p
JOIN playlist_track pt ON p.playlist_id = pt.playlist_id
JOIN track t ON pt.track_id = t.track_id
JOIN genre g ON t.genre_id = g.genre_id
GROUP BY p.playlist_id, p.name, g.genre_id, g.name
ORDER BY p.playlist_id ASC, "歌曲数量" DESC;
```

## 后端作业三
### 1. 常见数据库建模中常见ER（实体关系）类型

- 一对一
- 一对多
- 多对多

### 2. 一对多和多对多在建模关系上的特点

- 一对多：无需中间表，一方必须有主键关联多方的外键
- 多对多：需要引入中间表

### 3. 网络编程异常

• Timeout: ⽹络请求超时
• Connection refuse : 此端⼝没有服务绑定(bind)
• Connection reset : 连接被重置, ⽹络连接被 RST包重置(⾮正常关闭)

### 4. 服务报错 connection refuse

该端口未绑定(bind)服务

### 5. C/C++、java、Python在方法调用参数的时候是传值还是传引用

- C/C++：普通的是传值，指针是传引用
- java：基本数据类型传值，引用数据类型传引用
- python：一切皆对象，传参传递引用的副本

### 6. 网络编程中连接池的作用

复用已经创建的网络链接