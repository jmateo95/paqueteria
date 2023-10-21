-- Insertar Rol
INSERT INTO "Rol" (id, nombre, descripcion) VALUES 
    (1, 'Admin', 'Usuarios Admin'),
    (2, 'Operador', 'Usuarios Operadores');

-- Insertar Puesto
INSERT INTO "Puesto" (id, nombre, descripcion, salario_horario) VALUES
  (1, 'It', 'Tecnología de la Información', 0.00),
  (2, 'Gerencia', 'Gerente de Proyecto', 100.00),
  (3, 'Contaduria', 'Contador', 50.00),
  (4, 'Paqueteria', 'Trabajador de Paquetería', 60.00);

-- Insertar Ciudad
INSERT INTO "Ciudad" (id, nombre, descripcion, latitud, longitud) VALUES
  (1, 'Guatemala', 'Capital de Guatemala', 14.634915, -90.506882);

-- Insertar TipoSucursal
INSERT INTO "TipoSucursal" (id, nombre) VALUES
  (1, 'Sucursal Mayor'),
  (2, 'Sucursal de Conexión');

-- Insert para Sucursal
INSERT INTO "Sucursal" (id, nombre, direccion, ciudad_id, tiposucursal_id) VALUES
  (1, 'Central', 'Dirección de la Sucursal Central', 1, 1);


-- Insertar Usuario
INSERT INTO "Usuario" (id, nombre, username, email, password, horas, rol_id, sucursal_id, puesto_id) VALUES (1, 'Usuario', 'usuario', 'usuario@gmail.com', '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 10, 1, 1,1);--Password Cambiame123
