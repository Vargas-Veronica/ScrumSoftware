CREATE SCHEMA IF NOT EXISTS `tuStockOnline` DEFAULT CHARACTER SET utf8 ;
USE `tuStockOnline` ;

-- Create Table User
CREATE TABLE IF NOT EXISTS `tuStockOnline`.`USER` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `NAME` VARCHAR(45) NOT NULL,
  `EMAIL` VARCHAR(45) NOT NULL,
  `PASSWORD` VARCHAR(45) NOT NULL,
  UNIQUE INDEX `EMAIL_UNIQUE` (`EMAIL` ASC) VISIBLE,
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB;



-- Create Table Role
CREATE TABLE IF NOT EXISTS `tuStockOnline`.`ROLE` (
  `ID` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE,
  UNIQUE INDEX `name_UNIQUE` (`name` ASC) VISIBLE)
ENGINE = InnoDB;


-- Create Table User_has_Role
CREATE TABLE IF NOT EXISTS `tuStockOnline`.`USER_has_ROLE` (
  `USER_ID` INT NOT NULL,
  `ROLE_ID` INT NOT NULL,
  PRIMARY KEY (`USER_ID`, `ROLE_ID`),
  INDEX `fk_USER_has_ROLE_ROLE1_idx` (`ROLE_ID` ASC) VISIBLE,
  INDEX `fk_USER_has_ROLE_USER1_idx` (`USER_ID` ASC) VISIBLE,
  CONSTRAINT `fk_USER_has_ROLE_USER1`
    FOREIGN KEY (`USER_ID`)
    REFERENCES `tuStockOnline`.`USER` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_USER_has_ROLE_ROLE1`
    FOREIGN KEY (`ROLE_ID`)
    REFERENCES `tuStockOnline`.`ROLE` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

 CREATE TABLE IF NOT EXISTS `tuStockOnline`.`PRODUCTOS`(  
  `ID_Producto` INT NOT NULL AUTO_INCREMENT,
  `codigo` INT NOT NULL, 
  `nombre` VARCHAR(45) NOT NULL,
  `marca` VARCHAR(45) NOT NULL,
  `categoria` VARCHAR(45) NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `precioDeVenta` DOUBLE NOT NULL,
  `cantidadPorBulto` INT NOT NULL,
  `fechaDeVencimiento` DATE NOT NULL,

  UNIQUE INDEX `ID_UNIQUE` (`ID_Producto` ASC) VISIBLE,
  PRIMARY KEY (`ID_Producto`))
ENGINE = InnoDB;

 CREATE TABLE IF NOT EXISTS `tuStockOnline`.`STOCK`(  
  `ID_stock` INT NOT NULL AUTO_INCREMENT,
  `ID_Producto` INT NOT NULL, 
  `codigo` INT NOT NULL, 
  `producto` VARCHAR(45) NOT NULL,
  `stockMinimo` INT NOT NULL, 
  `stockMaximo` INT NOT NULL, 
  `stockActual` INT NOT NULL, 
  `cantidadDeVentas` INT NOT NULL,
  UNIQUE INDEX `ID_UNIQUE` (`ID_stock` ASC) VISIBLE,
  PRIMARY KEY (`ID_stock`))
ENGINE = InnoDB;

-- Inserts user
INSERT INTO user (name, email, password) VALUES ('Rosemary Southey', 'rsouthey0@delicious.com', 'TP6Rj129');
INSERT INTO user (name, email, password) VALUES ('Monty Ert', 'mert1@vkontakte.ru', 'gZfx5q58X');
INSERT INTO user (name, email, password) VALUES ('Ilene Aronovich', 'iaronovich2@twitpic.com', 'WPUnBqLG0U');
INSERT INTO user (name, email, password) VALUES ('Bethanne Halfacree', 'bhalfacree3@mit.edu', 'TFsvwAjeMmo');
INSERT INTO user (name, email, password) VALUES ('Jocelin Larmuth', 'jlarmuth4@indiegogo.com', 'jaQGKCS');

-- Insert Roles
INSERT INTO role (name) VALUES ('admin'), ('user');

-- Set Roles
INSERT INTO user_has_role (USER_ID, ROLE_ID)
VALUES (1, 2),
       (2, 2),
       (3, 1),
       (4, 1),
       (5, 2);
        
       
 -- Inserts productos
INSERT INTO productos (codigo, nombre, marca, categoria, descripcion, precioDeVenta, cantidadPorBulto, fechaDEVencimiento) VALUES ( 1, 'mate', 'Marolio', 'Almacen', 'paquete', 200, 12 ,'12/12/25');
INSERT INTO productos (codigo, nombre, marca, categoria, descripcion, precioDeVenta, cantidadPorBulto, fechaDEVencimiento) VALUES ( 2, 'cafe', 'Marolio', 'Almacen', 'paquete', 900, 6 ,'12/12/25');
INSERT INTO productos (codigo, nombre, marca, categoria, descripcion, precioDeVenta, cantidadPorBulto, fechaDEVencimiento) VALUES ( 3, 'harina', 'Marolio', 'Almacen', 'paquete', 200, 12 ,'12/12/25');
INSERT INTO productos (codigo, nombre, marca, categoria, descripcion, precioDeVenta, cantidadPorBulto, fechaDEVencimiento) VALUES ( 4, 'palmitos', 'Marolio', 'Almacen', 'paquete', 300, 12 ,'12/12/25');
INSERT INTO productos (codigo, nombre, marca, categoria, descripcion, precioDeVenta, cantidadPorBulto, fechaDEVencimiento) VALUES ( 5, 'yerba', 'Marolio', 'Almacen', 'paquete', 500, 12 ,'12/12/25');
 
 
-- Inserts stock
INSERT INTO user (producto, stockMinimo, stockMaximo, stockActual, cantidadDeVentas) VALUES ('mermelada', 200, 800, 500, 100);
INSERT INTO user (producto, stockMinimo, stockMaximo, stockActual, cantidadDeVentas) VALUES ('cacao', 300, 200, 500, 300);
INSERT INTO user (producto, stockMinimo, stockMaximo, stockActual, cantidadDeVentas) VALUES ('picadillo', 300, 300, 500, 400);
INSERT INTO user (producto, stockMinimo, stockMaximo, stockActual, cantidadDeVentas) VALUES ('pate', 100, 800, 400, 500);
INSERT INTO user (producto, stockMinimo, stockMaximo, stockActual, cantidadDeVentas) VALUES ('caballa', 100, 800, 500, 600);


-- Select All From User
SELECT * FROM user;
-- Select only name and email from user
SELECT name, email FROM user;
-- Join with role
SELECT us.id, us.name, us.email, r.name FROM user us
    JOIN user_has_role uhr on us.ID = uhr.USER_ID
    JOIN role r on uhr.ROLE_ID = r.ID;

-- Update
UPDATE user SET name = 'Irene Aronovich' WHERE id = 3;