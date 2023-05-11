use mydb;

select * from users;
INSERT INTO `mydb`.`users`
( first_name, last_name, email)
VALUES
( 'steve', 'martin',  's.martin@hulu.com' ),
( 'eddie', 'murphy',  'e.murphy@nbc.com' ),
( 'richard', 'pryor', 'r.pryor@gmail.com' )
;

INSERT INTO `mydb`.`users`
( first_name, last_name, email)
VALUES
( 'bud', 'abbott',   'b.abbott@otr.com' ),
( 'george', 'burns', 'g.burns@nbc.com' ),
( 'lou', 'costello', 'l.costello@aol.com' )
;

SELECT * FROM users;

SELECT * FROM users WHERE email = 'b.abbott@otr.com';

UPDATE `mydb`.`users` SET `last_name` = 'Pancakes'
WHERE `id` = 3;

DELETE FROM `mydb`.`users`  WHERE id = 2;

SELECT first_name, last_name FROM users ORDER BY first_name;
SELECT first_name, last_name FROM users ORDER BY first_name DESC;


