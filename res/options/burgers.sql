-- Crea la base de datos de la hamburguesería
CREATE TABLE CLIENTES ( 
    ID INT PRIMARY KEY, 
    NOMBRE VARCHAR(100), 
    TOMATE BOOLEAN,
    LECHUGA BOOLEAN,
    CEBOLLA BOOLEAN,
    QUESO BOOLEAN,
    REFRESCO VARCHAR(100)
);

--Datos de los clientes

INSERT INTO CLIENTES VALUES(1, 'Bandit', false,true,false,true,'Coca-Cola');
INSERT INTO CLIENTES VALUES(2, 'Bingo', true,false,false,false,'Fanta');
INSERT INTO CLIENTES VALUES(3, 'Bluey', false,true,true,false,'Coca-Cola');
INSERT INTO CLIENTES VALUES(4, 'Calyson', false,false,false,true,'Fresca');
INSERT INTO CLIENTES VALUES(5, 'Chilli', false,true,false,false,'Fanta');
INSERT INTO CLIENTES VALUES(6, 'Chloe', false,true,true,true,'Fanta');
INSERT INTO CLIENTES VALUES(7, 'Coco', false,true,false,true,'Agua');
INSERT INTO CLIENTES VALUES(8, 'Frisky', false,true,true,true,'Coca-Cola');
INSERT INTO CLIENTES VALUES(9, 'Honey', true,false,false,false,'Coca-Cola');
INSERT INTO CLIENTES VALUES(10, 'Indy', true,true,true,false,'Fresca');
INSERT INTO CLIENTES VALUES(11, 'Jack', true,false,false,false,'Fanta');
INSERT INTO CLIENTES VALUES(12, 'Jean-Luc', false,false,true,true,'Fresca');
INSERT INTO CLIENTES VALUES(13, 'Judo', false,false,false,true,'Fresca');
INSERT INTO CLIENTES VALUES(14, 'Lila', true,false,false,false,'Fresca');
INSERT INTO CLIENTES VALUES(15, 'Mackenzie', true,true,false,false,'Fresca');
INSERT INTO CLIENTES VALUES(16, 'Missy', false,false,true,true,'Coca-Cola');
INSERT INTO CLIENTES VALUES(17, 'Muffin', false,true,true,false,'Agua');
INSERT INTO CLIENTES VALUES(18, 'Nana', false,false,true,false,'Fanta');
INSERT INTO CLIENTES VALUES(19, 'Pom-Pom', false,false,true,true,'Fanta');
INSERT INTO CLIENTES VALUES(20, 'Rad', true,true,false,false,'Agua');
INSERT INTO CLIENTES VALUES(21, 'Rusty', true,false,true,true,'Fanta');
INSERT INTO CLIENTES VALUES(22, 'Snickers', true,true,false,true,'Fanta');
INSERT INTO CLIENTES VALUES(23, 'Stripe', false,true,true,false,'Fanta');
INSERT INTO CLIENTES VALUES(24, 'Trixie', true,true,false,true,'Fresca');
