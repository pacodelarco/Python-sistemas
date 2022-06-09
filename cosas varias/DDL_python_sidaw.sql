use pruebacompeticion;

CREATE TABLE `competicion` (
  `id` int NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `numeroPremios` int DEFAULT NULL,
  `numeroPilotos` int DEFAULT NULL,
  PRIMARY KEY (`id`)
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `equipo` (
  `nombre` varchar(40) NOT NULL,
  `empleados` int DEFAULT NULL,
  `presupuesto` decimal(2,0) DEFAULT NULL,
  `piloto_id` int DEFAULT NULL,
  `fabricante_id` int DEFAULT NULL,
  `competicion_id` int DEFAULT NULL,
  PRIMARY KEY (`nombre`),
  UNIQUE KEY `nombre_UNIQUE` (`nombre`),
  KEY `equipo_piloto_idx` (`piloto_id`),
  KEY `equipo_fabricante_idx` (`fabricante_id`),
  KEY `equipo_competicion_idx` (`competicion_id`),
  CONSTRAINT `equipo_competicion` FOREIGN KEY (`competicion_id`) REFERENCES `competicion` (`id`),
  CONSTRAINT `equipo_fabricante` FOREIGN KEY (`fabricante_id`) REFERENCES `fabricante` (`id`),
  CONSTRAINT `equipo_piloto` FOREIGN KEY (`piloto_id`) REFERENCES `piloto` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `fabricante` (
  `id` int NOT NULL,
  `nombre` varchar(40) NOT NULL,
  `numeroMotos` int DEFAULT NULL,
  `cilindrada` int DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `piloto` (
  `id` int NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `dorsal` int DEFAULT NULL,
  `equipo_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;