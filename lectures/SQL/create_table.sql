-- DROP TABLE purchase;
-- DROP TABLE users;
-- DROP TABLE products;

CREATE TABLE users
(
    id   SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    sex  VARCHAR(50)
);

CREATE TABLE products
(
    id    SERIAL PRIMARY KEY,
    name  TEXT NOT NULL,
    type  TEXT NOT NULL,
    price NUMERIC(6)
);

CREATE TABLE purchase
(
    id         SERIAL PRIMARY KEY,
    user_id    INT,
    product_id INT,

    FOREIGN KEY (user_id) REFERENCES users (id)
    -- Специально не делаем внешний ключ на product_id, чтоб была ошибка
);

INSERT INTO users (name, sex)
VALUES ('Ann', 'female'),
       ('Andrew', 'male'),
       ('Misha', 'male'),
       ('Polina', 'female');

INSERT INTO products (name, type, price)
VALUES ('laptop', 'tech', 150000.0),
       ('phone 1', 'tech', 7000.0),
       ('phone 2', 'tech', 15000.0),
       ('tablet', 'tech', 20000.0),
       ('jeans', 'cloth', 2000.0),
       ('sweatshirt', 'cloth', 2800.0),
       ('jacket', 'cloth', 3900.0);

INSERT INTO purchase (user_id, product_id)
VALUES (1, 1),
       (3, 2),
       (2, 1),
       (4, 1),
       (4, 2),
       (2, 1),
       (1, 4),
       (1, 42142), -- Типо ошибка
       (1, 12331); -- Типо ошибка
