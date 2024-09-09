
CREATE TABLE estados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);
INSERT INTO estados VALUES(1, 'Aguascalientes');
INSERT INTO estados VALUES(2, 'Baja California');
INSERT INTO estados VALUES(3, 'Baja California Sur');
INSERT INTO estados VALUES(4, 'Campeche');
INSERT INTO estados VALUES(5, 'Chiapas');
INSERT INTO estados VALUES(6, 'Chihuahua');
INSERT INTO estados VALUES(7, 'Coahuila');
INSERT INTO estados VALUES(8, 'Colima');
INSERT INTO estados VALUES(9, 'Durango');
INSERT INTO estados VALUES(10, 'Guanajuato');
INSERT INTO estados VALUES(11, 'Guerrero');
INSERT INTO estados VALUES(12, 'Hidalgo');
INSERT INTO estados VALUES(13, 'Jalisco');
INSERT INTO estados VALUES(14, 'Estado de México');
INSERT INTO estados VALUES(15, 'Michoacán');
INSERT INTO estados VALUES(16, 'Morelos');
INSERT INTO estados VALUES(17, 'Nayarit');
INSERT INTO estados VALUES(18, 'Nuevo León');
INSERT INTO estados VALUES(19, 'Oaxaca');
INSERT INTO estados VALUES(20, 'Puebla');
INSERT INTO estados VALUES(21, 'Querétaro');
INSERT INTO estados VALUES(22, 'Quintana Roo');
INSERT INTO estados VALUES(23, 'San Luis Potosí');
INSERT INTO estados VALUES(24, 'Sinaloa');
INSERT INTO estados VALUES(25, 'Sonora');
INSERT INTO estados VALUES(26, 'Tabasco');
INSERT INTO estados VALUES(27, 'Tamaulipas');
INSERT INTO estados VALUES(28, 'Tlaxcala');
INSERT INTO estados VALUES(29, 'Veracruz');
INSERT INTO estados VALUES(30, 'Yucatán');
INSERT INTO estados VALUES(31, 'Zacatecas');
CREATE TABLE disciplinas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    status INTEGER NOT NULL
);
INSERT INTO disciplinas VALUES(1, 'Fútbol', 1);
INSERT INTO disciplinas VALUES(2, 'Baloncesto', 1);
INSERT INTO disciplinas VALUES(3, 'Tenis', 1);
INSERT INTO disciplinas VALUES(4, 'Natación', 1);
INSERT INTO disciplinas VALUES(5, 'Atletismo', 1);
INSERT INTO disciplinas VALUES(6, 'Ciclismo', 1);
INSERT INTO disciplinas VALUES(7, 'Voleibol', 1);
INSERT INTO disciplinas VALUES(8, 'Golf', 1);
INSERT INTO disciplinas VALUES(9, 'Rugby', 1);
INSERT INTO disciplinas VALUES(10, 'Boxeo', 1);
INSERT INTO disciplinas VALUES(11, 'Béisbol', 1);
INSERT INTO disciplinas VALUES(12, 'Hockey', 1);
INSERT INTO disciplinas VALUES(13, 'Esquí', 1);
INSERT INTO disciplinas VALUES(14, 'Surf', 1);
INSERT INTO disciplinas VALUES(15, 'Gimnasia', 1);
CREATE TABLE preguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL,
    clase INTEGER NOT NULL
);
INSERT INTO preguntas VALUES(1, 'Me veo más como un perdedor que como un ganador durante las competencias.', 1);
INSERT INTO preguntas VALUES(2, 'Me enojo y frustro en los partidos.', 2);
INSERT INTO preguntas VALUES(3, 'Me distraigo y pierdo la concentración en las competencias.', 3);
INSERT INTO preguntas VALUES(4, 'Antes de competir me veo rindiendo perfectamente.', 4);
INSERT INTO preguntas VALUES(5, 'Estoy altamente motivado para jugar lo mejor que pueda.', 5);
INSERT INTO preguntas VALUES(6, 'Puedo mantener una corriente mi energía positiva durante las competencias.', 6);
INSERT INTO preguntas VALUES(7, 'Soy un pensador positivo durante las competencias.', 7);
INSERT INTO preguntas VALUES(8, 'Creo en mí mismo como deportista.', 1);
INSERT INTO preguntas VALUES(9, 'Me pongo nervioso o tengo miedo en las competencias.', 2);
INSERT INTO preguntas VALUES(10, 'Parece que mi cabeza se acelera a 100 km/h durante los momentos críticos de las competencias.', 3);
INSERT INTO preguntas VALUES(11, 'Practico mentalmente mis habilidades físicas.', 4);
INSERT INTO preguntas VALUES(12, 'Las metas que me he propuesto como deportista me hacen trabajar mucho.', 5);
INSERT INTO preguntas VALUES(13, 'Puedo disfrutar las competencias aunque tenga muchos problemas difíciles.', 6);
INSERT INTO preguntas VALUES(14, 'Me digo cosas negativas durante las competencias.', 7);
INSERT INTO preguntas VALUES(15, 'Pierdo la confianza rápidamente.', 1);
INSERT INTO preguntas VALUES(16, 'Los errores durante los partidos, me llevan a sentir y pensar negativamente.', 2);
INSERT INTO preguntas VALUES(17, 'Puedo borrar emociones que interfieren y volverme a concentrar durante las competencias.', 3);
INSERT INTO preguntas VALUES(18, 'La visualización de mi deporte me es fácil.', 4);
INSERT INTO preguntas VALUES(19, 'No me tienen que empujar para jugar o entrenar duro. Yo me estimulo solo.', 5);
INSERT INTO preguntas VALUES(20, 'Tiendo a sentirme aplastado emocionalmente cuando las cosas se vuelven en mi contra.', 6);
INSERT INTO preguntas VALUES(21, 'Yo doy un 100% de esfuerzo cuando me desempeño en mi deporte sin importarme nada.', 7);
INSERT INTO preguntas VALUES(22, 'Puedo rendir al 100% de mi talento y habilidad.', 1);
INSERT INTO preguntas VALUES(23, 'Mis músculos se tensan durante las competencias.', 2);
INSERT INTO preguntas VALUES(24, 'Me desconcentro durante las competencias.', 3);
INSERT INTO preguntas VALUES(25, 'Yo me visualizo saliendo de situaciones difíciles antes de las competencias.', 4);
INSERT INTO preguntas VALUES(26, 'Estoy dispuesto a dar todo lo necesario para llegar a mi máximo potencial como deportista.', 5);
INSERT INTO preguntas VALUES(27, 'Entreno con alta actitud positiva.', 6);
INSERT INTO preguntas VALUES(28, 'Puedo cambiar de estados emocionales (sentimientos) negativos a positivos por medio del control mental.', 7);
INSERT INTO preguntas VALUES(29, 'Soy un competidor con fortaleza mental.', 1);
INSERT INTO preguntas VALUES(30, 'Sentimientos incontrolables como el miedo, rivales tramposos y malos hábitos me molestan.', 2);
INSERT INTO preguntas VALUES(31, 'Mientras me desempeño en mi deporte me encuentro pensando en errores pasados u oportunidades perdidas.', 3);
INSERT INTO preguntas VALUES(32, 'Uso imágenes mientras me desempeño que me ayudan a rendir mejor.', 4);
INSERT INTO preguntas VALUES(33, 'Me aburro y agoto.', 5);
INSERT INTO preguntas VALUES(34, 'Me lleno de sensaciones de desafío y me inspiro en situaciones difíciles.', 6);
INSERT INTO preguntas VALUES(35, 'Mis entrenadores dirían que tengo una buena actitud.', 7);
INSERT INTO preguntas VALUES(36, 'Yo transmito la imagen de un atleta con confianza en sí mismo.', 1);
INSERT INTO preguntas VALUES(37, 'Puedo mantenerme calmado durante las competencias cuando estoy confundido por problemas.', 2);
INSERT INTO preguntas VALUES(38, 'Mi concentración se rompe fácilmente.', 3);
INSERT INTO preguntas VALUES(39, 'Cuando me visualizo jugando puedo ver y sentir las cosas vívidamente.', 4);
INSERT INTO preguntas VALUES(40, 'Me despierto por la mañana y estoy realmente excitado por practicar mi deporte y entrenar.', 5);
INSERT INTO preguntas VALUES(41, 'Practicar mi deporte me da una sensación genuina de alegría y plenitud.', 6);
INSERT INTO preguntas VALUES(42, 'Puedo transformar una crisis en oportunidad.', 7);
CREATE TABLE opciones (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pregunta_id INTEGER,
    peso INTEGER NOT NULL,
    texto TEXT NOT NULL,
    FOREIGN KEY (pregunta_id) REFERENCES preguntas(id)
);
INSERT INTO opciones VALUES(1, 1, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(2, 1, 2, 'A menudo');
INSERT INTO opciones VALUES(3, 1, 3, 'A veces');
INSERT INTO opciones VALUES(4, 1, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(5, 1, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(6, 2, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(7, 2, 2, 'A menudo');
INSERT INTO opciones VALUES(8, 2, 3, 'A veces');
INSERT INTO opciones VALUES(9, 2, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(10, 2, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(11, 3, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(12, 3, 2, 'A menudo');
INSERT INTO opciones VALUES(13, 3, 3, 'A veces');
INSERT INTO opciones VALUES(14, 3, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(15, 3, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(16, 4, 5, 'Casi Siempre');
INSERT INTO opciones VALUES(17, 4, 4, 'A menudo');
INSERT INTO opciones VALUES(18, 4, 3, 'A veces');
INSERT INTO opciones VALUES(19, 4, 2, 'Pocas Veces');
INSERT INTO opciones VALUES(20, 4, 1, 'Casi Nunca');
INSERT INTO opciones VALUES(21, 5, 5, 'Casi Siempre');
INSERT INTO opciones VALUES(22, 5, 4, 'A menudo');
INSERT INTO opciones VALUES(23, 5, 3, 'A veces');
INSERT INTO opciones VALUES(24, 5, 2, 'Pocas Veces');
INSERT INTO opciones VALUES(25, 5, 1, 'Casi Nunca');
INSERT INTO opciones VALUES(26, 6, 5, 'Casi Siempre');
INSERT INTO opciones VALUES(27, 6, 4, 'A menudo');
INSERT INTO opciones VALUES(28, 6, 3, 'A veces');
INSERT INTO opciones VALUES(29, 6, 2, 'Pocas Veces');
INSERT INTO opciones VALUES(30, 6, 1, 'Casi Nunca');
INSERT INTO opciones VALUES(31, 7, 5, 'Casi Siempre');
INSERT INTO opciones VALUES(32, 7, 4, 'A menudo');
INSERT INTO opciones VALUES(33, 7, 3, 'A veces');
INSERT INTO opciones VALUES(34, 7, 2, 'Pocas Veces');
INSERT INTO opciones VALUES(35, 7, 1, 'Casi Nunca');
INSERT INTO opciones VALUES(36, 8, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(37, 8, 2, 'A menudo');
INSERT INTO opciones VALUES(38, 8, 3, 'A veces');
INSERT INTO opciones VALUES(39, 8, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(40, 8, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(41, 9, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(42, 9, 2, 'A menudo');
INSERT INTO opciones VALUES(43, 9, 3, 'A veces');
INSERT INTO opciones VALUES(44, 9, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(45, 9, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(46, 10, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(47, 10, 2, 'A menudo');
INSERT INTO opciones VALUES(48, 10, 3, 'A veces');
INSERT INTO opciones VALUES(49, 10, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(50, 10, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(51, 11, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(52, 11, 2, 'A menudo');
INSERT INTO opciones VALUES(53, 11, 3, 'A veces');
INSERT INTO opciones VALUES(54, 11, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(55, 11, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(56, 12, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(57, 12, 2, 'A menudo');
INSERT INTO opciones VALUES(58, 12, 3, 'A veces');
INSERT INTO opciones VALUES(59, 12, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(60, 12, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(61, 13, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(62, 13, 2, 'A menudo');
INSERT INTO opciones VALUES(63, 13, 3, 'A veces');
INSERT INTO opciones VALUES(64, 13, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(65, 13, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(66, 14, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(67, 14, 2, 'A menudo');
INSERT INTO opciones VALUES(68, 14, 3, 'A veces');
INSERT INTO opciones VALUES(69, 14, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(70, 14, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(71, 15, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(72, 15, 2, 'A menudo');
INSERT INTO opciones VALUES(73, 15, 3, 'A veces');
INSERT INTO opciones VALUES(74, 15, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(75, 15, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(76, 16, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(77, 16, 2, 'A menudo');
INSERT INTO opciones VALUES(78, 16, 3, 'A veces');
INSERT INTO opciones VALUES(79, 16, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(80, 16, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(81, 17, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(82, 17, 2, 'A menudo');
INSERT INTO opciones VALUES(83, 17, 3, 'A veces');
INSERT INTO opciones VALUES(84, 17, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(85, 17, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(86, 18, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(87, 18, 2, 'A menudo');
INSERT INTO opciones VALUES(88, 18, 3, 'A veces');
INSERT INTO opciones VALUES(89, 18, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(90, 18, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(91, 19, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(92, 19, 2, 'A menudo');
INSERT INTO opciones VALUES(93, 19, 3, 'A veces');
INSERT INTO opciones VALUES(94, 19, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(95, 19, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(96, 20, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(97, 20, 2, 'A menudo');
INSERT INTO opciones VALUES(98, 20, 3, 'A veces');
INSERT INTO opciones VALUES(99, 20, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(100, 20, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(101, 21, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(102, 21, 2, 'A menudo');
INSERT INTO opciones VALUES(103, 21, 3, 'A veces');
INSERT INTO opciones VALUES(104, 21, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(105, 21, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(106, 22, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(107, 22, 2, 'A menudo');
INSERT INTO opciones VALUES(108, 22, 3, 'A veces');
INSERT INTO opciones VALUES(109, 22, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(110, 22, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(111, 23, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(112, 23, 2, 'A menudo');
INSERT INTO opciones VALUES(113, 23, 3, 'A veces');
INSERT INTO opciones VALUES(114, 23, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(115, 23, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(116, 24, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(117, 24, 2, 'A menudo');
INSERT INTO opciones VALUES(118, 24, 3, 'A veces');
INSERT INTO opciones VALUES(119, 24, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(120, 24, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(121, 25, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(122, 25, 2, 'A menudo');
INSERT INTO opciones VALUES(123, 25, 3, 'A veces');
INSERT INTO opciones VALUES(124, 25, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(125, 25, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(126, 26, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(127, 26, 2, 'A menudo');
INSERT INTO opciones VALUES(128, 26, 3, 'A veces');
INSERT INTO opciones VALUES(129, 26, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(130, 26, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(131, 27, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(132, 27, 2, 'A menudo');
INSERT INTO opciones VALUES(133, 27, 3, 'A veces');
INSERT INTO opciones VALUES(134, 27, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(135, 27, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(136, 28, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(137, 28, 2, 'A menudo');
INSERT INTO opciones VALUES(138, 28, 3, 'A veces');
INSERT INTO opciones VALUES(139, 28, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(140, 28, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(141, 29, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(142, 29, 2, 'A menudo');
INSERT INTO opciones VALUES(143, 29, 3, 'A veces');
INSERT INTO opciones VALUES(144, 29, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(145, 29, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(146, 30, 1, 'Casi Siempre');
INSERT INTO opciones VALUES(147, 30, 2, 'A menudo');
INSERT INTO opciones VALUES(148, 30, 3, 'A veces');
INSERT INTO opciones VALUES(149, 30, 4, 'Pocas Veces');
INSERT INTO opciones VALUES(150, 30, 5, 'Casi Nunca');
INSERT INTO opciones VALUES(151,31,1,'Casi Siempre');
INSERT INTO opciones VALUES(152,31,2,'A menudo');
INSERT INTO opciones VALUES(153,31,3,'A veces');
INSERT INTO opciones VALUES(154,31,4,'Pocas Veces');
INSERT INTO opciones VALUES(155,31,5,'Casi Nunca');
INSERT INTO opciones VALUES(156,32,5,'Casi Siempre');
INSERT INTO opciones VALUES(157,32,4,'A menudo');
INSERT INTO opciones VALUES(158,32,3,'A veces');
INSERT INTO opciones VALUES(159,32,2,'Pocas Veces');
INSERT INTO opciones VALUES(160,32,1,'Casi Nunca');
INSERT INTO opciones VALUES(161,33,1,'Casi Siempre');
INSERT INTO opciones VALUES(162,33,2,'A menudo');
INSERT INTO opciones VALUES(163,33,3,'A veces');
INSERT INTO opciones VALUES(164,33,4,'Pocas Veces');
INSERT INTO opciones VALUES(165,33,5,'Casi Nunca');
INSERT INTO opciones VALUES(166,34,5,'Casi Siempre');
INSERT INTO opciones VALUES(167,34,4,'A menudo');
INSERT INTO opciones VALUES(168,34,3,'A veces');
INSERT INTO opciones VALUES(169,34,2,'Pocas Veces');
INSERT INTO opciones VALUES(170,34,1,'Casi Nunca');
INSERT INTO opciones VALUES(171,35,5,'Casi Siempre');
INSERT INTO opciones VALUES(172,35,4,'A menudo');
INSERT INTO opciones VALUES(173,35,3,'A veces');
INSERT INTO opciones VALUES(174,35,2,'Pocas Veces');
INSERT INTO opciones VALUES(175,35,1,'Casi Nunca');
INSERT INTO opciones VALUES(176,36,5,'Casi Siempre');
INSERT INTO opciones VALUES(177,36,4,'A menudo');
INSERT INTO opciones VALUES(178,36,3,'A veces');
INSERT INTO opciones VALUES(179,36,2,'Pocas Veces');
INSERT INTO opciones VALUES(180,36,1,'Casi Nunca');
INSERT INTO opciones VALUES(181,37,5,'Casi Siempre');
INSERT INTO opciones VALUES(182,37,4,'A menudo');
INSERT INTO opciones VALUES(183,37,3,'A veces');
INSERT INTO opciones VALUES(184,37,2,'Pocas Veces');
INSERT INTO opciones VALUES(185,37,1,'Casi Nunca');
INSERT INTO opciones VALUES(186,38,1,'Casi Siempre');
INSERT INTO opciones VALUES(187,38,2,'A menudo');
INSERT INTO opciones VALUES(188,38,3,'A veces');
INSERT INTO opciones VALUES(189,38,4,'Pocas Veces');
INSERT INTO opciones VALUES(190,38,5,'Casi Nunca');
INSERT INTO opciones VALUES(191,39,5,'Casi Siempre');
INSERT INTO opciones VALUES(192,39,4,'A menudo');
INSERT INTO opciones VALUES(193,39,3,'A veces');
INSERT INTO opciones VALUES(194,39,2,'Pocas Veces');
INSERT INTO opciones VALUES(195,39,1,'Casi Nunca');
INSERT INTO opciones VALUES(196,40,5,'Casi Siempre');
INSERT INTO opciones VALUES(197,40,4,'A menudo');
INSERT INTO opciones VALUES(198,40,3,'A veces');
INSERT INTO opciones VALUES(199,40,2,'Pocas Veces');
INSERT INTO opciones VALUES(200,40,1,'Casi Nunca');
INSERT INTO opciones VALUES(201,41,5,'Casi Siempre');
INSERT INTO opciones VALUES(202,41,4,'A menudo');
INSERT INTO opciones VALUES(203,41,3,'A veces');
INSERT INTO opciones VALUES(204,41,2,'Pocas Veces');
INSERT INTO opciones VALUES(205,41,1,'Casi Nunca');
INSERT INTO opciones VALUES(206,42,5,'Casi Siempre');
INSERT INTO opciones VALUES(207,42,4,'A menudo');
INSERT INTO opciones VALUES(208,42,3,'A veces');
INSERT INTO opciones VALUES(209,42,2,'Pocas Veces');
INSERT INTO opciones VALUES(210,42,1,'Casi Nunca');


CREATE TABLE sexos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    descripcion TEXT NOT NULL
);

INSERT INTO sexos VALUES(1, 'Mujer');
INSERT INTO sexos VALUES(2, 'Hombre');

-- Crear tabla participantes
CREATE TABLE participantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    sexo_id INTEGER NOT NULL,
    estado_id INTEGER NOT NULL,
    disciplina_id INTEGER NOT NULL,
    encuesta_id INTEGER NOT NULL,
    datestart TIMESTAMP NOT NULL,
    FOREIGN KEY (estado_id) REFERENCES estados (id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas (id),
    FOREIGN KEY (sexo_id) REFERENCES sexos (id)
);

INSERT INTO participantes VALUES(1, 'Jose Francisco', 'Luna Hernandez', 2, 13, 11, 1, '2024-09-05 14:42:50.863846');
INSERT INTO participantes VALUES(2, 'Jose Francisco', 'Luna Hernandez', 2, 13, 11, 1, '2024-09-05 14:44:36.562450');
INSERT INTO participantes VALUES(3, 'Jose Francisco', 'Luna Hernandez', 2, 13, 11, 2, '2024-09-05 15:21:37.253164');
INSERT INTO participantes VALUES(4, 'Miguel', 'Luna Hernandez', 2, 13, 11, 1, '2024-09-05 21:19:22.998674');

CREATE TABLE respuestas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            participante_id INTEGER,
            pregunta_id INTEGER,
            opcion_id INTEGER,
            FOREIGN KEY (participante_id) REFERENCES participantes (id),
            FOREIGN KEY (opcion_id) REFERENCES opciones (id)
        );