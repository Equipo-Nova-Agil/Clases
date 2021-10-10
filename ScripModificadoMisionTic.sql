-- Crear tabla rol
CREATE TABLE misiontic.rol (
	id_rol INT auto_increment NOT NULL,
	rol_usuario varchar(20) NOT NULL,
	CONSTRAINT id_rol_pk PRIMARY KEY (id_rol)
	
)
AUTO_INCREMENT=1;

-- crear tabla estados

CREATE TABLE `estado` (
  `id_estado` int NOT NULL AUTO_INCREMENT,
  `estado` varchar(30) NOT NULL,
  PRIMARY KEY (`id_estado`)
) 
AUTO_INCREMENT=1;

-- Como queda la tabla usuarios 
CREATE TABLE `usuarios` (
  `id_usuarios` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `apellido` varchar(45) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `edad` int DEFAULT NULL,
  `genero` varchar(1) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `correo` varchar(100) NOT NULL,
  `telefono` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `fecha_registro` date NOT NULL,
  `tipo` varchar(45) NOT NULL,
  `direccion` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `password` varchar(45) NOT NULL,
  `id_rol` int NOT NULL,
  `id_estado` int NOT NULL,
  PRIMARY KEY (`id_usuarios`),
  KEY `usuarios_FK` (`id_rol`),
  KEY `usuarios_FK_1` (`id_estado`),
  CONSTRAINT `usuarios_FK` FOREIGN KEY (`id_rol`) REFERENCES `rol` (`id_rol`),
  CONSTRAINT `usuarios_FK_1` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`)
) 
ENGINE=InnoDB 
AUTO_INCREMENT=1;

-- Insertar datos
INSERT INTO misiontic.rol
(rol_usuario)
VALUES('Administrador');

INSERT INTO misiontic.rol
(rol_usuario)
VALUES('Vendedor');

-- tabla estado
INSERT INTO misiontic.estado
(estado)
VALUES('Autorizado');

INSERT INTO misiontic.estado
(estado)
VALUES('Pendiente');

INSERT INTO misiontic.estado
(estado)
VALUES('No autorizado');

-- tabla usuarios
insert into misiontic.usuarios (nombre, apellido, edad, genero,correo, 
telefono, fecha_registro, tipo, direccion, password, id_rol, id_estado)
values ('Camilo', 'Lopez', 20, 'M','camilo@gmail.com','263277443', '2021-09-29',  'rol', 'calle 30',  'camilo1233', 2, 1);
------------

select * from usuarios;
-----------------------
delete from usuarios where id_usuarios =2;


