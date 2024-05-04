-- Сколько стоят джинсы и ноутбук?
select sum(price)
from products
where name = 'jeans'
   or name = 'laptop';


-- Какой самый дешевый товар среди одежды?
select name as most_cheapest_cloth,
       price
from products
where type = 'cloth'
order by price asc
limit 1;

--
--

-- Какая минимальная цена в товарах одежды и техники?
select type,
       min(price)
from products
group by type;

--
--

-- Какие товары не были куплены?
select products.id   as id,
       products.name as name
from products
         left join purchase on products.id = purchase.product_id
where purchase.product_id is null;


-- Какие товары купила Полина и сколько она заплатила?
select users.name                      as name,
       string_agg(products.name, ', ') as products,
       sum(price)
from purchase
         join products on purchase.product_id = products.id
         join users on users.id = purchase.user_id
where users.name = 'Polina'
group by users.name;
