
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Usuarios` (
  `ID_usuario` VARCHAR(45) GENERATED ALWAYS AS () VIRTUAL,
  `Nombre_usuario` VARCHAR(145) NOT NULL,
  `Correo_usuario` VARCHAR(255) NOT NULL,
  `Edad_usuario` INT NOT NULL,
  `Fecha_registro` DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Direccion_usuario` VARCHAR(90) NULL,
  `Tipo_usuario` VARCHAR(45) NOT NULL,
  `Genero` VARCHAR(45) BINARY NOT NULL,
  `Telefono_usuario` VARCHAR(10) NOT NULL,
  `Contraseña_usuario` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`ID_usuario`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Correo_usuario_UNIQUE` ON `mydb`.`Usuarios` (`Correo_usuario` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `mydb`.`Tiendas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Tiendas` (
  `ID_tienda` VARCHAR(45) NOT NULL,
  `Nombre_tienda` VARCHAR(90) NOT NULL,
  `Direccion_tienda` VARCHAR(90) NOT NULL,
  `Correo_tienda` VARCHAR(250) NOT NULL,
  `Telefono_tienda` VARCHAR(10) NOT NULL,
  `Responsable_tienda` VARCHAR(90) NOT NULL,
  `Contraseña_tienda` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`ID_tienda`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `Nombre_tienda_UNIQUE` ON `mydb`.`Tiendas` (`Nombre_tienda` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `mydb`.`Productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Productos` (
  `ID_producto` VARCHAR(45) NOT NULL,
  `ID_tienda` VARCHAR(45) NOT NULL,
  `Nombre_producto` VARCHAR(90) NOT NULL,
  `Precio` FLOAT NOT NULL,
  `Seccion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID_producto`),
  CONSTRAINT `ID_tienda`
    FOREIGN KEY (`ID_tienda`)
    REFERENCES `mydb`.`Tiendas` (`ID_tienda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `ID_tienda_idx` ON `mydb`.`Productos` (`ID_tienda` ASC) VISIBLE;


-- -----------------------------------------------------
-- Table `mydb`.`Historial_ventas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Historial_ventas` (
  `ID_venta` INT NOT NULL AUTO_INCREMENT,
  `ID_usuario` VARCHAR(45) NOT NULL,
  `ID_tienda` VARCHAR(45) NOT NULL,
  `ID_producto` VARCHAR(90) NOT NULL,
  `Precio_producto` FLOAT NOT NULL,
  `Cantidad` INT NOT NULL,
  PRIMARY KEY (`ID_venta`),
  CONSTRAINT `Usuario`
    FOREIGN KEY (`ID_usuario`)
    REFERENCES `mydb`.`Usuarios` (`ID_usuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Productos`
    FOREIGN KEY (`ID_producto`)
    REFERENCES `mydb`.`Productos` (`ID_producto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `Tiendas`
    FOREIGN KEY (`ID_tienda`)
    REFERENCES `mydb`.`Tiendas` (`ID_tienda`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `Usuario_idx` ON `mydb`.`Historial_ventas` (`ID_usuario` ASC) VISIBLE;

CREATE INDEX `Productos_idx` ON `mydb`.`Historial_ventas` (`ID_producto` ASC) VISIBLE;

CREATE INDEX `Tiendas_idx` ON `mydb`.`Historial_ventas` (`ID_tienda` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
