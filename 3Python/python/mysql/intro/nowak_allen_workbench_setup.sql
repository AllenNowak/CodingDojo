-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema names
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema names
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `names` DEFAULT CHARACTER SET utf8 ;
USE `names` ;

-- -----------------------------------------------------
-- Table `names`.`names`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `names`.`names` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


-- -----------------------------------------------------
-- Schema Created after this executes
-- Inserting more than one Ninja in a single statement
-- -----------------------------------------------------
use names;
insert into names (name) values ('anna'), ('brandy'),('cara'),('daniel'),('eve'),('freddy'),('greg');
SELECT * FROM names.names;


-- -----------------------------------------------------
-- Updating
-- -----------------------------------------------------
use names;
SET SQL_SAFE_UPDATES = 0;
UPDATE names SET name = 'Amy' WHERE id = 1;
UPDATE names SET name = 'Connor' WHERE name = 'cara';
UPDATE names SET name = 'Paddy' WHERE name LIKE ('%y');


-- -----------------------------------------------------
-- Deleting all the Paddy's
-- -----------------------------------------------------
use names;
SET SQL_SAFE_UPDATES = 0;
delete from names where name = 'Paddy';
SELECT * FROM names.names;
