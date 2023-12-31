-- Insertar Ciudad
  INSERT INTO "Ciudad" (id, nombre, departamento, descripcion, test) VALUES
    (2, 'Villa Nueva',      'Guatemala',        'Municipio de Guatemala',   false),
    (3, 'Huehuetenango',    'Huehuetenango',    'Ciudad de Huehuetenango',  false),
    (4, 'Quetzaltenango',   'Quetzaltenango',   'Ciudad de xela',           false);

  -- Insert para Sucursal
  INSERT INTO "Sucursal" (id, nombre, direccion, latitud, longitud, ciudad_id, tipo_sucursal_id, test) VALUES
    (2, 'Anexa Guatemala',      'Dirección 2', 14.634915, -90.506882, 1, 2, false),
    (3, 'Sucursal Villa Nueva', 'Dirección 3', 14.634915, -90.506882, 2, 1, false),
    (4, 'Sucursal Huehue',      'Dirección 4', 14.634915, -90.506882, 3, 1, false),
    (5, 'Sucursal Xela',        'Dirección 5', 14.634915, -90.506882, 4, 1, false);

  -- Insertar Usuario
  INSERT INTO "Usuario" (id, nombre, username, email, password, horas, rol_id, sucursal_id, puesto_id, test) VALUES 
                        (2,  'Usuario_2',   'usuario_2',    'usuario2@gmail.com',   '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 30, 2, 1, 2, false),
                        (3,  'Usuario_3',   'usuario_3',    'usuario3@gmail.com',   '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 30, 2, 2, 3, false),
                        (4,  'Usuario_4',   'usuario_4',    'usuario4@gmail.com',   '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 55, 2, 2, 4, false),
                        (5,  'Usuario_5',   'usuario_5',    'usuario5@gmail.com',   '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 40, 2, 3, 1, false),
                        (6,  'Usuario_6',   'usuario_6',    'usuario6@gmail.com',   '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 45, 2, 3, 2, false),
                        (7,  'Usuario_7',   'usuario_7',    'usuario7@gmail.com',   '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 50, 2, 4, 3, false),
                        (8,  'Usuario_8',   'usuario_8',    'usuario8@gmail.com',   '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 35, 2, 4, 4, false),
                        (9,  'Usuario_9',   'usuario_9',    'usuario9@gmail.com',   '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 40, 2, 5, 1, false),
                        (10, 'Usuario_10',  'usuario_10',   'usuario10@gmail.com',  '$2b$12$KgOW9J/732zxoXBmmcxmSeKFRpOSMfkgDSI/17OlcvliLHCGBTX3y', 35, 2, 5, 2, false);

-- Insertar Vehiculos
INSERT INTO public."Vehiculo"(id, placa, capacidad_lb, costo_km, tipo_vehiculo_id, sucursal_id, test)VALUES 
                             (1, 'P-0001', 200, 25, 1, 1, false),
                             (2, 'P-0002', 100, 25, 2, 2, false),
                             (3, 'P-0003', 150, 25, 3, 3, false),
                             (4, 'P-0004', 200, 25, 4, 4, false),
                             (5, 'P-0005', 250, 25, 1, 5, false),
                             (6, 'P-0006', 300, 25, 2, 1, false),
                             (7, 'P-0007', 210, 25, 3, 2, false),
                             (8, 'P-0008', 180, 25, 4, 3, false),
                             (9, 'P-0009', 200, 25, 1, 4, false),
                             (10, 'P-0010', 230, 25, 2, 5, false);




--Extras
INSERT INTO public."Segmento" VALUES 
(1, 1, 2, 'Ruta Capital', 20, false),
(2, 2, 1, 'Ruta Capital', 20, false),
(3, 1, 5, 'Ruta Guate-Xela', 180, false),
(4, 5, 1, 'Ruta Guate-Xela', 180, false),
(5, 5, 4, 'Ruta Xela-Huehu', 76, false),
(6, 4, 5, 'Ruta Xela-Huehu', 76, false),
(7, 1, 3, 'Ruta Guate-Villa Nueva', 35, false),
(8, 3, 1, 'Ruta Guate-Villa Nueva', 35, false);


INSERT INTO public."Salida" VALUES 
(5, 1, 6, 1, NULL, NULL, '2023-11-28 19:36:13.62', '', 1.67, 300, 0, 0, false),
(6, 1, 6, 2, NULL, NULL, '2023-11-28 19:36:13.62', '', 1.67, 300, 0, 0, false),
(7, 1, 8, 8, NULL, NULL, '2023-11-28 19:37:43.892', '', 4.86, 180, 0, 0, false),
(8, 1, 8, 7, NULL, NULL, '2023-11-28 19:37:43.892', '', 4.86, 180, 0, 0, false),
(9, 1, 9, 6, NULL, NULL, '2023-11-28 19:38:14.564', '', 9.5, 200, 0, 0, false),
(10, 1, 9, 5, NULL, NULL, '2023-11-28 19:38:14.564', '', 9.5, 200, 0, 0, false),
(11, 1, 10, 4, NULL, NULL, '2023-11-28 19:39:14.681', '', 19.57, 230, 0, 0, false),
(12, 1, 10, 3, NULL, NULL, '2023-11-28 19:39:14.681', '', 19.57, 230, 0, 0, false);


{
  "email": "usuario@gmail.com",
  "password": "Cambiame123"
}
