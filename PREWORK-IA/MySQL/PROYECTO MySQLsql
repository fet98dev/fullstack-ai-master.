



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


