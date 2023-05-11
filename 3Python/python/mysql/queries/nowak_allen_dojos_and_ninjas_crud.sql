-- SELECT * FROM dojos_and_ninjas_schema.dojos;
-- SELECT * FROM dojos_and_ninjas_schema.ninjas;

-- Or remove the need to constantly restate the schema
use dojos_and_ninjas_schema;



-- Seed some other dojos
INSERT INTO dojos (name) VALUES
('bellingham'), ('puyallup'), ('olympia'), ('poulsbo'), ('bonnie lake'), ('spokane');



-- create 3 new dojos
INSERT INTO dojos (name) 
VALUES ('Orlando'), ('Miami'), ('Tallahassee');



-- delete the 3 dojos just created
delete from dojos order by id desc limit 3;



-- create 3 more dojos
INSERT INTO dojos (name) 
VALUES ('Reno'), ('Paris'), ('London');

-- select * from dojos;
-- select * from ninjas;






-- Seed some ninjas
INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
VALUES 
('bruce',  'lee', 84, 1),
('chuck', 'norris', 77, 2),
('jean claude', 'van damme', 66, 3),
('jackie', 'chan', 65, 1)
;

-- select * from dojos;
-- select * from ninjas;



-- create 3 ninjas in the 3rd most recent dojo
set @third_from_last = (SELECT * from (
	select id from dojos order by id desc limit 3
) as trio order by id limit 1);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
VALUES 
('leonardo',  'da Vinci', 14, @third_from_last),
('donatello', 'bardi', 16, @third_from_last),
('michelangelo', 'simoni', 15, @third_from_last)
;
-- select * from dojos;
-- select * from ninjas;



-- create 3 ninjas in the 2nd most recent dojo
-- no guarantee that id's are still in sequence
set @second_from_last = (SELECT * from (
	select id from dojos order by id desc limit 2
) as SCND order by id limit 1);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
VALUES 
('matt', 'murdoch', 30, @second_from_last),
('stick', 'hand', 70, @second_from_last),
('stone', 'hand', 110, @second_from_last)
;



-- create 3 ninjas in the most recent dojo
-- no guarantee that id's are still in sequence
set @last = (select id from dojos as final order by id desc limit 1);

INSERT INTO ninjas (first_name, last_name, age, dojo_id) 
VALUES 
('raphael', 'da urbino', 14, @last),
('shredder', 'rat', 30, @last),
('splinter', 'rat', 22, @last)
;

-- select * from dojos;
-- select * from ninjas;



-- Retrieve all the ninjas from the first dojo
select * from ninjas
join dojos on ninjas.dojo_id = dojos.id
where dojo_id = @third_from_last;


-- Retrieve all the ninjas from the last dojo
select * from ninjas
join dojos on ninjas.dojo_id = dojos.id
where dojo_id = (select id from dojos order by id desc limit 1);


-- Use a JOIN to retrieve the ninja with id 6 as well as the data from its dojo. Be sure to do this in one query using a join statement.

select * from ninjas
join dojos on ninjas.dojo_id = dojos.id
where ninjas.id = 6;



-- Retrieve the last ninja's dojo
select dojo_id from ninjas order by id desc limit 1;



