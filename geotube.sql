-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema geotube
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema geotube
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `geotube` DEFAULT CHARACTER SET utf8 ;
USE `geotube` ;

-- -----------------------------------------------------
-- Table `geotube`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `geotube`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL,
  `email` VARCHAR(255) NULL,
  `pw_hash` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `geotube`.`credentials`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `geotube`.`credentials` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `fb_id` VARCHAR(255) NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_credentials_users_idx` (`user_id` ASC),
  CONSTRAINT `fk_credentials_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `geotube`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `geotube`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `geotube`.`favorites` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `description` VARCHAR(255) NULL,
  `url` LONGTEXT NULL,
  `created_at` DATETIME NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_search_favs_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_search_favs_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `geotube`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
