  -- Insertar Rol
  INSERT INTO "Rol" (id, nombre, descripcion) VALUES 
      (1, 'Admin',    'Usuarios Admin'),
      (2, 'Operador', 'Usuarios Operadores');

  -- Insertar Puesto
  INSERT INTO "Puesto" (id, nombre, descripcion, salario_horario) VALUES
    (1, 'It',         'Tecnología de la Información', 0.00),
    (2, 'Gerencia',    'Gerente de Proyecto', 100.00),
    (3, 'Contaduria',  'Contador', 50.00),
    (4, 'Paqueteria',  'Trabajador de Paquetería', 60.00);

  -- Insertar Ciudad
  INSERT INTO "Ciudad" (id, nombre, departamento, descripcion) VALUES
    (1, 'Guatemala', 'Guatemala', 'Capital de Guatemala');

  -- Insertar TipoSucursal
  INSERT INTO "TipoSucursal" (id, nombre) VALUES
    (1, 'Sucursal Mayor'),
    (2, 'Sucursal de Conexión');

  -- Insert para Sucursal
  INSERT INTO "Sucursal" (id, nombre, direccion, latitud, longitud, ciudad_id, tipo_sucursal_id) VALUES
    (1, 'Central', 'Dirección de la Sucursal Central', 14.634915, -90.506882, 1, 1);


  -- Insertar Usuario
  INSERT INTO "Usuario" (id, nombre, username, email, password, horas, rol_id, sucursal_id, puesto_id) VALUES (1, 'Usuario', 'usuario', 'usuario@gmail.com', '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 10, 1, 1,1);--Password Cambiame123


  -- TipoVehiculo
  INSERT INTO "TipoVehiculo" (id, nombre) VALUES
    (1, 'Camion'),
    (2, 'Panel'),
    (3, 'Furgoneta'),
    (4, 'Pick Up');


  -- TipoGasto
  INSERT INTO "TipoGasto" (id, nombre) VALUES
    (1, 'Fijos'),
    (2, 'Variables'),
    (3, 'Transporte');


  -- ConceptoGasto
  INSERT INTO "ConceptoGasto" (id, nombre) VALUES
    (1, 'Planilla'),
    (2, 'Gasolina'),
    (3, 'Luz'),
    (4, 'Agua'),
    (5, 'internet'),
    (6, 'Telefono'),
    (7, 'Alquiler');


  -- TipoSalida
  INSERT INTO "TipoSalida" (id, nombre) VALUES
    (1, 'Proyeccion'),
    (2, 'Lista para cargar'),
    (3, 'Cargando'),
    (4, 'En Ruta'),
    (5, 'Fin');

  --EstadoPaquete
  INSERT INTO "EstadoPaquete" (id, nombre, descripcion) VALUES 
    (1, 'Recepcion',  'El paquete se encuentra en recepción.'),
    (2, 'Transito',   'El paquete está en tránsito.'),
    (3, 'Ruta Final', 'El paquete está en la ruta final para la entrega.'),
    (4, 'Entregado',  'El paquete ha sido entregado con éxito.');

  --EstadoTracking
  INSERT INTO "EstadoTracking" (id, nombre, descripcion) VALUES 
    (1, 'En Espera',  'Aun no se llega a esta punto'),
    (2, 'En Bodega',  'El paquete se encuentra en bodega.'),
    (3, 'Cargando',   'El paquete se esta cargando'),
    (4, 'Cargado',    'El paquete fue cargado'),
    (5, 'En Ruta',    'Esta en ruta'),
    (6, 'Completado', 'Este tracking se concluyo');
