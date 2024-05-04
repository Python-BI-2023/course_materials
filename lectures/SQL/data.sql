-- SELECT, FROM, LIMIT

SELECT *
FROM users;

SELECT name,
       sex
FROM users;

SELECT name AS user_name,
       sex
FROM users;

select name,
       price / 1.20
from products;

select name,
       round(price / 1.20)
from products;

select name,
       round(price / 1.20) AS price_without_tax
from products;

select *
from products;

select distinct id
from products;

select count(distinct id)
from products;

select count(*)
from products;

select count(*) as total
from products;

select distinct type
from products;

select count(distinct type)
from products;

select *
from purchase;

select *
from purchase
limit 2;

-- WHERE, ORDER BY

select *
from products
where price > 2000;

select *
from products
where price > 2000
  AND type = 'tech';

select *
from products
order by price; -- asc

select *
from products
order by price desc;

select *
from products
where price > 2000
  AND type = 'tech'
order by price desc;

-- GROUP BY, HAVING

select ???? -- Ошибка!
from products
group by type;

select * -- Ошибка!
from products
group by type;

select type
from products
group by type;

select price, -- Ошибка
       type
from products
group by type;

select sum(price),
       count(id),
       string_agg(name, ', '),
       type
from products
group by type;

select sum(price),
       count(id),
       string_agg(name, ', '),
       type
from products
where price < 8000
group by type;

select sum(price),
       count(id),
       string_agg(name, ', '),
       type
from products
where price < 10000
group by type
having count(id) > 1;


-- JOIN

select *
from purchase
         join products -- INNER
              on products.id = purchase.product_id;

select *
from purchase AS l
         join products AS r -- INNER
              on r.id = l.product_id;

select *
from purchase
         left join products on products.id = purchase.product_id;

select *
from purchase
         right join products on products.id = purchase.product_id;

select *
from products
         left join purchase on products.id = purchase.product_id;

select *
from purchase
         full join products on products.id = purchase.product_id;


select pu.user_id,
       pu.product_id,
       pr.name as product,
       u.name  as user_name
from purchase pu
         full join products pr on pr.id = pu.product_id
         full join users u on u.id = pu.user_id;

-- Subqueries

select *
from products
where price >= (select avg(price)
                from products);


select users.name,
       products.name,
       products.price
from purchase
         inner join users on purchase.user_id = users.id
         inner join products on purchase.product_id = products.id;

select users.name,
       products.name,
       products.price
from purchase
         inner join users on purchase.user_id = users.id
         inner join (select *
                     from products
                     where price > 10000) as products on purchase.product_id = products.id;








