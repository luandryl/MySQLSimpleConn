-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema TESTE
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema TESTE
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `TESTE` DEFAULT CHARACTER SET latin1 ;
USE `TESTE` ;

-- -----------------------------------------------------
-- Table `TESTE`.`Curso`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TESTE`.`Curso` (
  `crCod` INT(11) NOT NULL COMMENT '',
  `crNome` VARCHAR(50) NULL DEFAULT NULL COMMENT '',
  `crMensalidade` DECIMAL(6,2) NULL DEFAULT NULL COMMENT '',
  `crCodCoordenador` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`crCod`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `TESTE`.`Aluno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TESTE`.`Aluno` (
  `aluCodigo` INT(11) NOT NULL COMMENT '',
  `aluNome` VARCHAR(50) NOT NULL COMMENT '',
  `codCurso` INT(11) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`aluCodigo`)  COMMENT '',
  INDEX `FK_Curso` (`codCurso` ASC)  COMMENT '',
  CONSTRAINT `FK_Curso`
    FOREIGN KEY (`codCurso`)
    REFERENCES `TESTE`.`Curso` (`crCod`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `TESTE`.`Disciplina`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TESTE`.`Disciplina` (
  `dCod` INT(11) NOT NULL COMMENT '',
  `dNome` VARCHAR(50) NOT NULL COMMENT '',
  `qtdAulaSemana` INT(11) NOT NULL COMMENT '',
  PRIMARY KEY (`dCod`)  COMMENT '')
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `TESTE`.`MATRICULA`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TESTE`.`MATRICULA` (
  `aluCod` INT(11) NOT NULL COMMENT '',
  `dCod` INT(11) NOT NULL COMMENT '',
  `mAno` INT(11) NOT NULL COMMENT '',
  `mMedia` DECIMAL(4,2) NULL DEFAULT NULL COMMENT '',
  `mFreq` DECIMAL(5,2) NULL DEFAULT NULL COMMENT '',
  PRIMARY KEY (`mAno`, `aluCod`, `dCod`)  COMMENT '',
  INDEX `fk_Aluno` (`aluCod` ASC)  COMMENT '',
  INDEX `fk_Disc` (`dCod` ASC)  COMMENT '',
  CONSTRAINT `fk_Aluno`
    FOREIGN KEY (`aluCod`)
    REFERENCES `TESTE`.`Aluno` (`aluCodigo`),
  CONSTRAINT `fk_Disc`
    FOREIGN KEY (`dCod`)
    REFERENCES `TESTE`.`Disciplina` (`dCod`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
