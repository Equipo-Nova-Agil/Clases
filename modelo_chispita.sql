CREATE DATABASE `misiontic`;

CREATE TABLE `misiontic`.`rol` (
	id_rol INT auto_increment NOT NULL,
	rol_usuario varchar(20) NOT NULL,
	CONSTRAINT id_rol_pk PRIMARY KEY (id_rol)
)
AUTO_INCREMENT=1;

-- crear tabla estados

CREATE TABLE `misiontic`.`estado` (
  `id_estado` int NOT NULL AUTO_INCREMENT,
  `estado` varchar(30) NOT NULL,
  PRIMARY KEY (`id_estado`)
)
AUTO_INCREMENT=1;

-- Como queda la tabla usuarios
CREATE TABLE `misiontic`.`usuarios` (
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


CREATE TABLE `misiontic`.`tiendas` (
  `id_tienda` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(45) NOT NULL,
  `direccion` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `telefono` varchar(20) NOT NULL,
  `responsable` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL,
  PRIMARY KEY (`id_tienda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE `misiontic`.`productos` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `id_tienda` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `precio` double NOT NULL,
  `seccion` varchar(45) NOT NULL,
  PRIMARY KEY (`id_producto`),
  KEY `id_tienda_idx` (`id_tienda`),
  CONSTRAINT `id_tienda` FOREIGN KEY (`id_tienda`) REFERENCES `tiendas` (`id_tienda`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


CREATE TABLE `misiontic`.`ventas` (
  `id_venta` int NOT NULL AUTO_INCREMENT,
  `id_usuario` int NOT NULL,
  `id_producto` int NOT NULL,
  `cantidad` int NOT NULL,
  `precio` double NOT NULL,
  PRIMARY KEY (`id_venta`),
  KEY `id_usuario_idx` (`id_usuario`),
  KEY `id_producto_idx` (`id_producto`),
  CONSTRAINT `id_producto` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`),
  CONSTRAINT `id_usuario` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuarios`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;




