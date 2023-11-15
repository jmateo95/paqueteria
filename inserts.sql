  -- Insertar Rol
  INSERT INTO "Rol" (id, nombre, descripcion, estatico) VALUES 
      (1, 'Admin',    'Usuarios Admin', true),
      (2, 'Operador', 'Usuarios Operadores', true);

  -- Insertar Puesto
  INSERT INTO "Puesto" (id, nombre, descripcion, salario_horario, estatico) VALUES
    (1, 'It',         'Tecnología de la Información', 0.00, true),
    (2, 'Gerencia',    'Gerente de Proyecto', 100.00, true),
    (3, 'Contaduria',  'Contador', 50.00, true),
    (4, 'Paqueteria',  'Trabajador de Paquetería', 60.00, true);

  -- Insertar Ciudad
  INSERT INTO "Ciudad" (id, nombre, departamento, descripcion, estatico) VALUES
    (1, 'Guatemala', 'Guatemala', 'Capital de Guatemala', true);

  -- Insertar TipoSucursal
  INSERT INTO "TipoSucursal" (id, nombre, estatico) VALUES
    (1, 'Sucursal Mayor', true),
    (2, 'Sucursal de Conexión', true);

  -- Insert para Sucursal
  INSERT INTO "Sucursal" (id, nombre, direccion, latitud, longitud, ciudad_id, tipo_sucursal_id, estatico, test) VALUES
    (1, 'Central', 'Dirección de la Sucursal Central', 14.634915, -90.506882, 1, 1, true, false);


  -- Insertar Usuario
  INSERT INTO "Usuario" (id, nombre, username, email, password, horas, rol_id, sucursal_id, puesto_id, estatico, test) VALUES (1, 'Usuario', 'usuario', 'usuario@gmail.com', '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 10, 1, 1, 1, true, false);--Password Cambiame123


  -- TipoVehiculo
  INSERT INTO "TipoVehiculo" (id, nombre, estatico) VALUES
    (1, 'Camion', true),
    (2, 'Panel', true),
    (3, 'Furgoneta', true),
    (4, 'Pick Up', true);


  -- TipoGasto
  INSERT INTO "TipoGasto" (id, nombre, estatico) VALUES
    (1, 'Fijos', true),
    (2, 'Variables', true),
    (3, 'Transporte', true);


  -- ConceptoGasto
  INSERT INTO "ConceptoGasto" (id, nombre, estatico) VALUES
    (1, 'Planilla', true),
    (2, 'Gasolina', true),
    (3, 'Luz', true),
    (4, 'Agua', true),
    (5, 'internet', true),
    (6, 'Telefono', true),
    (7, 'Alquiler', true);


  -- TipoSalida
  INSERT INTO "TipoSalida" (id, nombre, estatico) VALUES
    (1, 'Proyeccion', true),
    (2, 'Lista para cargar', true),
    (3, 'Cargando', true),
    (4, 'Cargado', true),
    (5, 'En Ruta', true),
    (6, 'Fin', true);

  --EstadoPaquete
  INSERT INTO "EstadoPaquete" (id, nombre, descripcion, estatico) VALUES 
    (1, 'Recepcion',    'El paquete se encuentra en recepción.', true),
    (2, 'Transito',     'El paquete está en tránsito.', true),
    (3, 'Ruta Final',   'El paquete está en la ruta final para la entrega.', true),
    (4, 'Por Entregar', 'El paquete está listo para su entrega.', true),
    (5, 'Entregado',    'El paquete ha sido entregado con éxito.', true);

  --EstadoTracking
  INSERT INTO "EstadoTracking" (id, nombre, descripcion, estatico) VALUES 
    (1, 'En Espera',  'Aun no se llega a esta punto', true),
    (2, 'En Bodega',  'El paquete se encuentra en bodega.', true),
    (3, 'Cargando',   'El paquete se esta cargando', true),
    (4, 'Cargado',    'El paquete fue cargado', true),
    (5, 'En Ruta',    'Esta en ruta', true),
    (6, 'Completado', 'Este tracking se concluyo', true);
