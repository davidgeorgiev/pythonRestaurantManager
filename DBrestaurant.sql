DROP DATABASE IF EXISTS `DBrestaurant`;
CREATE DATABASE `DBrestaurant`;

CREATE TABLE `DBrestaurant`.`customers` (
	`customerID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`firstName` VARCHAR(55) NOT NULL,
	`middleName` VARCHAR(55) NOT NULL,
	`lastName` VARCHAR(55) NOT NULL,
	`email` VARCHAR(55) NULL, 
	`phone` VARCHAR(20) NOT NULL, 
	`address` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`customerID`)
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;

CREATE TABLE `DBrestaurant`.`tables` (
	`tableID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`chairsNumber` INT UNSIGNED NOT NULL,
	`ifSmoking` VARCHAR(20) NOT NULL,
	PRIMARY KEY (`tableID`)
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8;

INSERT INTO `DBrestaurant`.`customers` (`firstName`,`middleName`,`lastName`,`email`,`phone`,`address`)
VALUES ("David", "Luchezarov", "Georgiev", "davidpiano@abv.bg", "0893514113", "Sofia");
INSERT INTO `DBrestaurant`.`customers` (`firstName`,`middleName`,`lastName`,`email`,`phone`,`address`)
VALUES ("David2", "Luchezarov2", "Georgiev2", "davidpiano@abv.bg2", "08935141132", "Sofia2");
