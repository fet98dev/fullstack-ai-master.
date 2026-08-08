CREATE DATABASE IF NOT EXISTS sistema_peliculas;
USE sistema_peliculas;
CREATE TABLE usuarios (
	id INT AUTO_INCREMENT PRIMARY KEY ,
    nombre VARCHAR(100) NOT NULL,
    email  VARCHAR(100) NOT NULL
);
CREATE TABLE peliculas (
	id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    year YEAR NOT NULL
    
);

INSERT INTO usuarios (nombre,email) VALUES
('Carlos','carlos@gmail.com'),
('Maria','maria@gmail.com'),
('Juan','juan@gmail.com'),
('Gerardo','gerardo@gmail.com');

INSERT INTO peliculas (titulo,year) VALUES
('Titanic', 1998),
('Interestelar', 2014),
('Mario Bros', 2024);

SELECT * FROM usuarios;
SELECT * FROM peliculas;


