CREATE TABLE orders
( order_id     NUMBER     NOT NULL,
  order_date   DATE           NULL,
  total_amount NUMBER     NOT NULL);

INSERT INTO 
 orders (order_id, order_date, total_amount)
VALUES 
 (1, '2023-07-15', 50.99),
 (2, '2023-07-16', 75.5),
 (3, '2023-07-17', 30.25);
COMMIT;

SELECT *
FROM orders;

CREATE TABLE customers
( customer_id NUMBER NOT NULL,
  name     VARCHAR(20)     NOT NULL,
  email   VARCHAR(100)           NULL,
  phone VARCHAR(20)     NOT NULL);

INSERT INTO
 customers(customer_id, name, email, phone)
VALUES
 (1, '허균', 'hong.gildong@example.com', '010-1234-5678'),
 (2, '김영희', 'kim.younghee@example.com', '010-9876-5432'),
 (3, '이철수', 'lee.cheolsu@example.com', '010-5555-4444');
COMMIT;



SELECT *
FROM customers;

DELETE FROM orders
WHERE order_id = 3;

UPDATE
 customers
SET
 name = '홍길동'
WHERE
 customer_id = 1;