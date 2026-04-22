---------CUSTOMER TABLE---------

create table customers(
customer_id    int ,
name    varchar(20),
city    varchar(20),
age     int,
gender   varchar(10)
);


select * from customers;

------- phase 2------
--------- detecting duplicate rows --------

select customer_id, count(*)
from customers
group by customer_id
having count(*)>1;


select count(distinct customer_id)
from customers;


-------- identify missing values ---------

select 
COUNT(*) FILTER (WHERE customer_id IS NULL) AS id_null,
COUNT(*) FILTER (WHERE name IS NULL) AS name_null,
COUNT(*) FILTER (WHERE age IS NULL) AS age_null,
COUNT(*) FILTER (WHERE city IS NULL) AS city_null
FROM customers;

--------- detect invalid numeric enteries------
SELECT count(*) 
FROM customers
WHERE age < 0 OR age > 100;

--------- creating clean sql table-------
select distinct city from customers;

select count(*)
from customers
where city is null or city ='NAN';


CREATE VIEW clean_customer AS
SELECT 
    customer_id,
    name,
    age,
    CASE 
        WHEN city IS NULL OR city = 'NAN' THEN 'UNKNOWN'
        ELSE city
    END AS city
FROM customers;

SELECT * FROM clean_customer limit 60;


------- ORDER TABLE----------------

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    product_id INT,
    qty INT,
    selling_price int,
    order_date DATE
);

SELECT* FROM ORDERS;

--------DETECT DUPLICATE ROWS---------

select order_id, count(*)
from orders
group by order_id
having count(*)>1;


select count(distinct order_id)
from orders;
------------- identify missing values------
select 
COUNT(*) FILTER (WHERE order_id IS NULL) AS orderid_null,
COUNT(*) FILTER (WHERE customer_id IS NULL) AS customerid_null,
COUNT(*) FILTER (WHERE product_id IS NULL) AS productid_null,
COUNT(*) FILTER (WHERE qty IS NULL) AS qty_null,
COUNT(*) FILTER (WHERE selling_price IS NULL) AS sellingprice_null,
COUNT(*) FILTER (WHERE order_date IS NULL) AS orderdate_null
FROM orders;

------------ detect invalid numeric enteries-------------
---- qty validation-----
select count(*)
from orders
where qty<1;

------- outliers check------
--high qty
select count (*)
from orders
where qty>100;

-- high price---
select count (*)
from orders
where selling_price>100000;


-----creating clean table /view----
--- qty=1 where qty is less than 1-----
CREATE VIEW clean_orders AS
SELECT 
    order_id,
    customer_id,
    product_id,
    CASE 
        WHEN qty < 1 THEN 1
        ELSE qty
    END AS qty,
    selling_price,
    order_date
FROM orders;

select * from orders limit 50;

-------- PRODUCT TABLE------------
CREATE TABLE products (
    product_id INT,
    category TEXT,
    brand TEXT,
    cost_price INT
);

SELECT * FROM products;

--------------DETECT DUPLICATE ROWS---------
select product_id, count(*)
from products
group by product_id
having count(*)>1;


select count(distinct product_id)
from products;

-------- identify missing values------
------------- identify missing values------
select 
COUNT(*) FILTER (WHERE product_id IS NULL) AS productid_null,
COUNT(*) FILTER (WHERE category IS NULL) AS category_null,
COUNT(*) FILTER (WHERE brand IS NULL) AS brand_null,
COUNT(*) FILTER (WHERE cost_price IS NULL) AS costprice_null
FROM products;

-------- identifying spelling mistakes -------

select distinct category from products;

select count(*)
from products
where category='Eletronics';

----- cost price validation----
select count(*)
from products 
where cost_price is null or cost_price<=0;
