
CREATE DATABASE IF NOT EXISTS PROYECTO_MySQL;
USE PROYECTO_MYSQL;


-- 1. Creamos la tabla Libros primero, 
#ya que no depende de ninguna otra
CREATE TABLE  Libros (
	id INT PRIMARY KEY,
	titulo VARCHAR (150) NOT NULL,
	autor VARCHAR(200) NOT NULL,
	anio_publicacion INT,
	disponible BOOLEAN DEFAULT TRUE
);


#Creamos la tabla usuarios(tampoco depende de otra)
CREATE TABLE Usuarios (
    id INT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL
);


#-- 3. Creamos la tabla Préstamos al final porque necesita que 
#Libros y Usuarios ya existan.
CREATE TABLE Prestamos (
	id INT PRIMARY KEY,
	libro_id INT,
	usuario_id INT,
	fecha_prestamo DATE NOT NULL,
	fecha_devolucion DATE,
	FOREIGN KEY (libro_id) REFERENCES Libros(id),
	FOREIGN KEY (usuario_id) REFERENCES Usuarios(id)
);



#INSERTAR LOS 5 LIBROS, CADA UNO CON LO QUE SE LE PIDE.
INSERT INTO Libros (id, titulo, autor, anio_publicacion, disponible)
VALUES
	(1, 'Don Quijote de la Mancha', 'Miguel de cervantes', 1605, TRUE),
	(2, 'El senor de los anillos', 'J.R.R Tolkien', 1954, FALSE),
	(3, 'Romeo y Julieta', 'William Shakespeare', 1597, FALSE),
    (4, 'Orgullo y prejuicio', 'Jane Austen', 1813, TRUE),
    (5, 'Harry Potter y la piedra filosofal', 'J.K Rowling', 1997, TRUE);




#INSERTAR LOS 3 USUARIOS
INSERT INTO Usuarios (id, nombre, email)
VALUES
	(1, ' Laura Gomez', 'laura.g@email.com'),
    (2, 'Pedro Sanchez', 'pedro.s@email.com' ),
    (3, 'Maria Lopez', 'maria.l@email.com');


#INSERTAR LOS 2 PRESTAMOS ACTIVOS.
INSERT INTO Prestamos (id, libro_id, usuario_id, fecha_prestamo, fecha_devolucion)
VALUES
	(1, 2, 1, '2026-09-01', NULL),
    (2, 3, 2, '2026-09-05', NULL);

#####CONSULTAS OBLIGATORIAS########
#1.- LIBROS DISPONIBLES (SOLO LOS NO PRESTADOS)
#Mostrar una lista de los libros que actualmente se pueden prestar a los usuarios.
SELECT * FROM Libros
WHERE disponible = TRUE;

#2.- PRESTAMOS ACTIVOS (MOSTRAR LIBRO + USUARIO + FECHA)
#Generar un informe que le diga al biblioticario que libros estan fuera, quien los tiene y 
#en que fecha se los llevaron.
SELECT 
    Libros.titulo AS libro, 
    Usuarios.nombre AS usuario, 
    Prestamos.fecha_prestamo
FROM Prestamos
INNER JOIN Libros ON Prestamos.libro_id = Libros.id
INNER JOIN Usuarios ON Prestamos.usuario_id = Usuarios.id
WHERE Prestamos.fecha_devolucion IS NULL;

#3.- DIAS TRANSCURRIDOS DESDE EL PRESTAMO (USAR DATEDIFF).
#Objetivo calcular exactamente cuantos dias han pasado desde que el usuario se llevo el libro 
#hasta el dia de hoy, para saber si hay retrasos.

SELECT 
	Prestamos.id AS prestamos_id,
    Libros.titulo AS libro,
    Usuarios.nombre AS usuario,
    Prestamos.fecha_prestamo,
    DATEDIFF(CURRENT_DATE, Prestamos.fecha_prestamo) AS dias_transcurridos
FROM Prestamos
INNER JOIN Libros ON Prestamos.libro_id = Libros.id
INNER JOIN Usuarios ON Prestamos.usuario_id = Usuarios.id
WHERE Prestamos.fecha_devolucion IS NULL;


########QUE HACE EL QUE########
#CURRENT_DATE; Detecta automaticamente la fecha exacta del dia de hoy en el sistema.

#DATEDIFF(fecha_reciente, Prestamos.fecha_prestamo); Es una funcion matematica de fechas 
#Resta dos fechas y devuelve el resultado en numero entero de dias. 
#Al hacer; DATEDIFF(fecha_reciente, Prestamos.fecha_prestamo) le decimos;
#Resta la fecha de hoy menos la fecha en que se presto el libro.

#AS dias_transcurridos: le da un nombre claro a la columna calculada 
#para que no salga la formula en al tabla de resultados



 



    
    
    





