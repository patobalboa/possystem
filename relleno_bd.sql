INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Bebidas', 'Bebidas', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Carnes', 'Carnes', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Lacteos', 'Lacteos', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Frutas', 'Frutas', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Verduras', 'Verduras', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Granos', 'Granos', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Aseo', 'Aseo', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Dulces', 'Dulces', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Panaderia', 'Panaderia', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Cereales', 'Cereales', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Enlatados', 'Enlatados', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Licores', 'Licores', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Higiene', 'Higiene', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Cuidado Personal', 'Cuidado Personal', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Cuidado del Hogar', 'Cuidado del Hogar', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Mascotas', 'Mascotas', TRUE);
INSERT INTO public.core_categoria (nombre_categoria, descripcion, estado) VALUES ('Otros', 'Otros', TRUE);

INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone, estado) VALUES ('Coca Cola', '12345678-9', 'contacto@cocacola.cl', '+56912345678', TRUE);
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone, estado) VALUES ('Nestle', '12424678-9', 'contacto@nestle.cl', '+56912345678', TRUE);
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone, estado) VALUES ('Soprole', '12367678-9', 'contacto@soprole.cl', '+56912345678', TRUE);
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone, estado) VALUES ('Carozzi', '12525678-9', 'carozzi@carozzi.cl', '+56912345678', TRUE);
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone, estado) VALUES ('Unilever', '17545678-9', 'unilever@carozzi.cl', '+56912345678', TRUE);
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone, estado) VALUES ('Kellogs', '12345322-9', 'contacto@kellogs.cl', '+56912345678', TRUE);


INSERT INTO public.core_producto (codigo_producto, nombre_producto, descripcion, precio, stock, categoria_id, estado) VALUES 
('123456789', 'Coca Cola 1.5L', 'Coca Cola 1.5L', 1000, 100, 2, TRUE),  -- Bebidas
('123456790', 'Nestle Chocolate', 'Nestle Chocolate Barra', 500, 50, 10, TRUE),  -- Dulces
('123456791', 'Soprole Leche', 'Soprole Leche Entera 1L', 800, 80, 5, TRUE),  -- Lácteos
('123456792', 'Carozzi Pasta', 'Carozzi Pasta Espagueti', 700, 90, 8, TRUE),  -- Granos
('123456793', 'Unilever Shampoo', 'Unilever Shampoo 500ml', 1500, 70, 16, TRUE),  -- Cuidado Personal
('123456794', 'Kellogs Cereal', 'Kellogs Cereal 500g', 2000, 75, 12, TRUE),  -- Cereales
('223456789', 'Sprite 1.5L', 'Sprite 1.5L', 900, 90, 2, TRUE),  -- Bebidas
('223456790', 'Nestle Helado', 'Nestle Helado Vainilla', 1200, 60, 4, TRUE),  -- Carnes (puede que debas ajustar esto)
('223456791', 'Soprole Queso', 'Soprole Queso Gauda', 1500, 70, 5, TRUE),  -- Lácteos
('223456792', 'Carozzi Arroz', 'Carozzi Arroz Integral', 700, 80, 8, TRUE),  -- Granos
('223456793', 'Unilever Jabon', 'Unilever Jabon 200g', 500, 100, 16, TRUE),  -- Cuidado Personal
('223456794', 'Kellogs Granola', 'Kellogs Granola 500g', 1500, 80, 12, TRUE),  -- Cereales
('323456789', 'Pepsi 1.5L', 'Pepsi 1.5L', 900, 85, 2, TRUE),  -- Bebidas
('323456790', 'Nestle Yogurt', 'Nestle Yogurt Frutilla', 400, 100, 5, TRUE),  -- Lácteos
('323456791', 'Soprole Mantequilla', 'Soprole Mantequilla 250g', 800, 70, 5, TRUE),  -- Lácteos
('323456792', 'Carozzi Fideos', 'Carozzi Fideos Tallarines', 600, 100, 8, TRUE),  -- Granos
('323456793', 'Unilever Pasta de Dientes', 'Unilever Pasta de Dientes 100g', 700, 90, 16, TRUE),  -- Cuidado Personal
('323456794', 'Kellogs Corn Flakes', 'Kellogs Corn Flakes 500g', 1500, 60, 12, TRUE);


INSERT INTO public.core_producto_proveedores (proveedor_id, producto_id)
VALUES 
(4, 55), -- Coca Cola provee Coca Cola 1.5L
(5, 56), -- Nestle provee Nestle Chocolate
(6, 57), -- Soprole provee Soprole Leche
(7, 58), -- Carozzi provee Carozzi Pasta
(8, 59), -- Unilever provee Unilever Shampoo
(9, 60), -- Kellogs provee Kellogs Cereal
(4, 61), -- Coca Cola provee Sprite 1.5L
(5, 62), -- Nestle provee Nestle Helado
(6, 63), -- Soprole provee Soprole Queso
(7, 64), -- Carozzi provee Carozzi Arroz
(8, 65), -- Unilever provee Unilever Jabon
(9, 66), -- Kellogs provee Kellogs Granola
(4, 67), -- Coca Cola provee Pepsi 1.5L
(5, 68), -- Nestle provee Nestle Yogurt
(6, 69), -- Soprole provee Soprole Mantequilla
(7, 70), -- Carozzi provee Carozzi Fideos
(8, 71), -- Unilever provee Unilever Pasta de Dientes
(9, 72); -- Kellogs provee Kellogs Corn Flakes
=======
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Bebidas', 'Bebidas');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Carnes', 'Carnes');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Lacteos', 'Lacteos');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Frutas', 'Frutas');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Verduras', 'Verduras');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Granos', 'Granos');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Aseo', 'Aseo');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Dulces', 'Dulces');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Panaderia', 'Panaderia');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Cereales', 'Cereales');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Enlatados', 'Enlatados');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Licores', 'Licores');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Higiene', 'Higiene');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Cuidado Personal', 'Cuidado Personal');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Cuidado del Hogar', 'Cuidado del Hogar');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Mascotas', 'Mascotas');
INSERT INTO public.core_categoria (nombre_categoria, descripcion) VALUES ('Otros', 'Otros');

INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone) VALUES ('Coca Cola', '12345678-9', 'contacto@cocacola.cl', '+56912345678');
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone) VALUES ('Nestle', '12345678-9', 'contacto@nestle.cl', '+56912345678');
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone) VALUES ('Soprole', '12345678-9', 'contacto@soprole.cl', '+56912345678');
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone) VALUES ('Carozzi', '12345678-9', 'carozzi@carozzi.cl', '+56912345678');
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone) VALUES ('Unilever', '12345678-9', 'unilever@carozzi.cl', '+56912345678');
INSERT INTO public.core_proveedor (nombre_proveedor, rut, email, phone) VALUES ('Kellogs', '12345678-9', 'contacto@kellogs.cl', '+56912345678');


INSERT INTO public.core_producto (codigo_producto, nombre_producto, descripcion, precio, stock, categoria_id) VALUES ('123456789', 'Coca Cola 1.5L', 'Coca Cola 1.5L', 1000, 100, 1),
('123456790', 'Nestle Chocolate', 'Nestle Chocolate Barra', 500, 50, 8),
('123456791', 'Soprole Leche', 'Soprole Leche Entera 1L', 800, 80, 3),
('123456792', 'Carozzi Pasta', 'Carozzi Pasta Espagueti', 700, 90, 6),
('123456793', 'Unilever Shampoo', 'Unilever Shampoo 500ml', 1500, 70, 14),
('123456794', 'Kellogs Cereal', 'Kellogs Cereal 500g', 2000, 75, 10),
('223456789', 'Sprite 1.5L', 'Sprite 1.5L', 900, 90, 1),
('223456790', 'Nestle Helado', 'Nestle Helado Vainilla', 1200, 60, 2),
('223456791', 'Soprole Queso', 'Soprole Queso Gauda', 1500, 70, 3),
('223456792', 'Carozzi Arroz', 'Carozzi Arroz Integral', 700, 80, 6),
('223456793', 'Unilever Jabon', 'Unilever Jabon 200g', 500, 100, 14),
('223456794', 'Kellogs Granola', 'Kellogs Granola 500g', 1500, 80, 10),
('323456789', 'Pepsi 1.5L', 'Pepsi 1.5L', 900, 85, 1),
('323456790', 'Nestle Yogurt', 'Nestle Yogurt Frutilla', 400, 100, 3),
('323456791', 'Soprole Mantequilla', 'Soprole Mantequilla 250g', 800, 70, 3),
('323456792', 'Carozzi Fideos', 'Carozzi Fideos Tallarines', 600, 100, 6),
('323456793', 'Unilever Pasta de Dientes', 'Unilever Pasta de Dientes 100g', 700, 90, 14),
('323456794', 'Kellogs Corn Flakes', 'Kellogs Corn Flakes 500g', 1500, 60, 10);

INSERT INTO public.core_proveedor_producto (proveedor_id, producto_id)
VALUES 
(1, 1), -- Coca Cola provee Coca Cola 1.5L
(2, 2), -- Nestle provee Nestle Chocolate
(3, 3), -- Soprole provee Soprole Leche
(4, 4), -- Carozzi provee Carozzi Pasta
(5, 5), -- Unilever provee Unilever Shampoo
(6, 6), -- Kellogs provee Kellogs Cereal
(1, 7), -- Coca Cola provee Sprite 1.5L
(2, 8), -- Nestle provee Nestle Helado
(3, 9), -- Soprole provee Soprole Queso
(4, 10), -- Carozzi provee Carozzi Arroz
(5, 11), -- Unilever provee Unilever Jabon
(6, 12), -- Kellogs provee Kellogs Granola
(1, 13), -- Coca Cola provee Pepsi 1.5L
(2, 14), -- Nestle provee Nestle Yogurt
(3, 15), -- Soprole provee Soprole Mantequilla
(4, 16), -- Carozzi provee Carozzi Fideos
(5, 17), -- Unilever provee Unilever Pasta de Dientes
(6, 18); -- Kellogs provee Kellogs Corn Flakes
>>>>>>> b821b924ba1c62db04d1985b746770ffc1fabe88



INSERT INTO public.core_empleado (nombres, rut, birth_date, fecha_contrato, fecha_fin_contrato, usuario, password, email, phone, salario, estado, avatar)
VALUES 
('Juan Perez', '12345678-9', '1980-01-01', '2020-01-01', '2023-01-01', 'juanperez', 'password', 'juanperez@email.com', '+56912345678', 1000000, true, 'avatar1.png'),
('Maria Rodriguez', '12345678-0', '1985-05-05', '2021-05-05', NULL, 'mariarodriguez', 'password', 'mariarodriguez@email.com', '+56987654321', 1200000, true, 'avatar2.png'),
('Pedro Sanchez', '12345678-1', '1982-02-02', '2019-02-02', '2023-02-02', 'pedrosanchez', 'password', 'pedrosanchez@email.com', '+56911223344', 1100000, true, 'avatar3.png'),
('Ana Morales', '12345678-2', '1990-10-10', '2022-10-10', NULL, 'anamorales', 'password', 'anamorales@email.com', '+56999887766', 1150000, true, 'avatar4.png');

INSERT INTO public.core_perfil (nombre_perfil, descripcion)
VALUES 
('Administrador', 'Encargado de administrar el sistema'),
('Cajero', 'Encargado de operaciones diarias'),
('Gerente', 'Encargado de supervisar las operaciones y tomar decisiones');

INSERT INTO public.core_empleado_perfiles (empleado_id, perfil_id)
VALUES 
(1, 1),  -- Juan Perez es un administrador
(2, 2),  -- Maria Rodriguez es un empleado
(3, 3),  -- Pedro Sanchez es un gerente
(4, 2),  -- Ana Morales es un empleado
(1, 2), -- Juan Perez tambien es un empleado
(3, 1); -- Pedro Sanchez tambien es un administrador

INSERT INTO public.core_venta (subtotal, iva, total, fecha_venta, numero_venta, empleado_id, descuento)
VALUES 
(1000, 190, 1190, '2023-05-15', 1, 1, 0),  -- Venta realizada por el empleado 1
(500, 95, 595, '2023-05-16', 2, 2, 0),  -- Venta realizada por el empleado 2
(2000, 380, 2380, '2023-05-17', 3, 3, 0),  -- Venta realizada por el empleado 3
(1500, 285, 1785, '2023-05-18', 4, 1, 100),  -- Venta realizada por el empleado 1 con un descuento de 100
(2500, 475, 2975, '2023-05-19', 5, 2, 200),  -- Venta realizada por el empleado 2 con un descuento de 200
(3000, 570, 3570, '2023-05-20', 6, 3, 300);  -- Venta realizada por el empleado 3 con un descuento de 300