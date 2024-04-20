-- Crea la base de datos para los clientes
CREATE TABLE CLIENTES ( 
    ID INT PRIMARY KEY, 
    NOMBRE VARCHAR(100), 
    TOMATE BOOLEAN,
    LECHUGA BOOLEAN,
    CEBOLLA BOOLEAN,
    QUESO BOOLEAN,
    REFRESCO VARCHAR(100),
    RUTA VARCHAR(100)
);

--Datos de los clientes
INSERT INTO CLIENTES VALUES(1, 'Bandit', false,true,false,true,'Coca-Cola', 'src/AdminSoftware/res/img/costumers/1.png');
INSERT INTO CLIENTES VALUES(2, 'Bingo', true,false,false,false,'Fanta', 'src/AdminSoftware/res/img/costumers/2.png');
INSERT INTO CLIENTES VALUES(3, 'Bluey', false,true,true,false,'Coca-Cola', 'src/AdminSoftware/res/img/costumers/3.png');
INSERT INTO CLIENTES VALUES(4, 'Calypso', false,false,false,true,'Fresca', 'src/AdminSoftware/res/img/costumers/4.png');
INSERT INTO CLIENTES VALUES(5, 'Chilli', false,true,false,false,'Fanta', 'src/AdminSoftware/res/img/costumers/5.png');
INSERT INTO CLIENTES VALUES(6, 'Chloe', false,true,true,true,'Fanta', 'src/AdminSoftware/res/img/costumers/6.png');
INSERT INTO CLIENTES VALUES(7, 'Coco', false,true,false,true,'Agua', 'src/AdminSoftware/res/img/costumers/7.png');
INSERT INTO CLIENTES VALUES(8, 'Frisky', false,true,true,true,'Coca-Cola', 'src/AdminSoftware/res/img/costumers/8.png');
INSERT INTO CLIENTES VALUES(9, 'Honey', true,false,false,false,'Coca-Cola', 'src/AdminSoftware/res/img/costumers/9.png');
INSERT INTO CLIENTES VALUES(10, 'Indy', true,true,true,false,'Fresca', 'src/AdminSoftware/res/img/costumers/10.png');
INSERT INTO CLIENTES VALUES(11, 'Jack', true,false,false,false,'Fanta', 'src/AdminSoftware/res/img/costumers/11.png');
INSERT INTO CLIENTES VALUES(12, 'Jean-Luc', false,false,true,true,'Fresca', 'src/AdminSoftware/res/img/costumers/12.png');
INSERT INTO CLIENTES VALUES(13, 'Judo', false,false,false,true,'Fresca', 'src/AdminSoftware/res/img/costumers/13.png');
INSERT INTO CLIENTES VALUES(14, 'Lila', true,false,false,false,'Fresca', 'src/AdminSoftware/res/img/costumers/14.png');
INSERT INTO CLIENTES VALUES(15, 'Mackenzie', true,true,false,false,'Fresca', 'src/AdminSoftware/res/img/costumers/15.png');
INSERT INTO CLIENTES VALUES(16, 'Missy', false,false,true,true,'Coca-Cola', 'src/AdminSoftware/res/img/costumers/16.png');
INSERT INTO CLIENTES VALUES(17, 'Muffin', false,true,true,false,'Agua', 'src/AdminSoftware/res/img/costumers/17.png');
INSERT INTO CLIENTES VALUES(18, 'Nana', false,false,true,false,'Fanta', 'src/AdminSoftware/res/img/costumers/18.png');
INSERT INTO CLIENTES VALUES(19, 'Pom-Pom', false,false,true,true,'Fanta', 'src/AdminSoftware/res/img/costumers/19.png');
INSERT INTO CLIENTES VALUES(20, 'Rad', true,true,false,false,'Agua', 'src/AdminSoftware/res/img/costumers/20.png');
INSERT INTO CLIENTES VALUES(21, 'Rusty', true,false,true,true,'Fanta', 'src/AdminSoftware/res/img/costumers/21.png');
INSERT INTO CLIENTES VALUES(22, 'Snickers', true,true,false,true,'Fanta', 'src/AdminSoftware/res/img/costumers/22.png');
INSERT INTO CLIENTES VALUES(23, 'Stripe', false,true,true,false,'Fanta', 'src/AdminSoftware/res/img/costumers/23.png');
INSERT INTO CLIENTES VALUES(24, 'Trixie', true,true,false,true,'Fresca', 'src/AdminSoftware/res/img/costumers/24.png');
INSERT INTO CLIENTES VALUES(26,'Socks', true, true, true, true, 'Fresca', 'src/AdminSoftware/res/img/costumers/26.png')