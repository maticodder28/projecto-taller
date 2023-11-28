-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 28-11-2023 a las 19:06:18
-- Versión del servidor: 8.0.31
-- Versión de PHP: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `viena`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add Comanda', 7, 'add_comanda'),
(26, 'Can change Comanda', 7, 'change_comanda'),
(27, 'Can delete Comanda', 7, 'delete_comanda'),
(28, 'Can view Comanda', 7, 'view_comanda'),
(29, 'Can add Mesa', 8, 'add_mesas'),
(30, 'Can change Mesa', 8, 'change_mesas'),
(31, 'Can delete Mesa', 8, 'delete_mesas'),
(32, 'Can view Mesa', 8, 'view_mesas'),
(33, 'Can add Producto', 9, 'add_productos'),
(34, 'Can change Producto', 9, 'change_productos'),
(35, 'Can delete Producto', 9, 'delete_productos'),
(36, 'Can view Producto', 9, 'view_productos'),
(37, 'Can add TipoUsuario', 10, 'add_tipousuario'),
(38, 'Can change TipoUsuario', 10, 'change_tipousuario'),
(39, 'Can delete TipoUsuario', 10, 'delete_tipousuario'),
(40, 'Can view TipoUsuario', 10, 'view_tipousuario'),
(41, 'Can add Usuario', 11, 'add_usuarios'),
(42, 'Can change Usuario', 11, 'change_usuarios'),
(43, 'Can delete Usuario', 11, 'delete_usuarios'),
(44, 'Can view Usuario', 11, 'view_usuarios'),
(45, 'Can add DetalleComanda', 12, 'add_detallecomanda'),
(46, 'Can change DetalleComanda', 12, 'change_detallecomanda'),
(47, 'Can delete DetalleComanda', 12, 'delete_detallecomanda'),
(48, 'Can view DetalleComanda', 12, 'view_detallecomanda'),
(49, 'Can add Categoría', 13, 'add_categoria'),
(50, 'Can change Categoría', 13, 'change_categoria'),
(51, 'Can delete Categoría', 13, 'delete_categoria'),
(52, 'Can view Categoría', 13, 'view_categoria'),
(53, 'Can add user profile', 14, 'add_userprofile'),
(54, 'Can change user profile', 14, 'change_userprofile'),
(55, 'Can delete user profile', 14, 'delete_userprofile'),
(56, 'Can view user profile', 14, 'view_userprofile');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$600000$DWBF0SAmz6qHGvHeKlRLsX$li0sPkUE3ylG8VGMDz5MWD82boREZqpdWck85+tmS8Q=', '2023-11-28 19:04:57.125095', 1, 'administrador', '', '', 'mmunizagafuentes@gmail.com', 1, 1, '2023-11-17 22:45:00.908465'),
(5, 'pbkdf2_sha256$600000$Syh7EsXZ7cQv99cg84oKgA$KF65W1B0Hc5fHE8488bz8o3YrF3DALgU9w8fKcvGVwE=', '2023-11-28 18:51:08.744949', 0, 'Ipizarro', '', '', 'ipizarro@gmail.com', 0, 1, '2023-11-28 18:51:08.586914'),
(4, 'pbkdf2_sha256$600000$17OgH8Bpd6mG14rymuwe5u$7n9Z5818mHM91OPUcJpML7VYZAdCiv3ZoKwn8juGBPw=', '2023-11-28 18:29:24.888945', 0, 'Mmunizaga', '', '', 'mmunizagafuentes@gmail.com', 0, 1, '2023-11-28 18:06:02.766843');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8mb4_spanish2_ci,
  `object_repr` varchar(200) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8mb4_spanish2_ci NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2023-11-17 22:46:08.732859', '1', 'Comestibles', 1, '[{\"added\": {}}]', 13, 1),
(2, '2023-11-17 22:46:35.469690', '2', 'Bebestibles', 1, '[{\"added\": {}}]', 13, 1),
(3, '2023-11-26 22:27:54.309958', '3', 'Bebidas Alcoholicas', 1, '[{\"added\": {}}]', 13, 1),
(4, '2023-11-26 22:28:26.448997', '2', 'Bebidas', 2, '[{\"changed\": {\"fields\": [\"Nombre\", \"Descripcion\"]}}]', 13, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_spanish2_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'tiendaApp', 'comanda'),
(8, 'tiendaApp', 'mesas'),
(9, 'tiendaApp', 'productos'),
(10, 'tiendaApp', 'tipousuario'),
(11, 'tiendaApp', 'usuarios'),
(12, 'tiendaApp', 'detallecomanda'),
(13, 'tiendaApp', 'categoria'),
(14, 'tiendaApp', 'userprofile');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-11-17 22:43:50.814174'),
(2, 'auth', '0001_initial', '2023-11-17 22:43:51.179136'),
(3, 'admin', '0001_initial', '2023-11-17 22:43:51.293161'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-11-17 22:43:51.297164'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-11-17 22:43:51.301164'),
(6, 'contenttypes', '0002_remove_content_type_name', '2023-11-17 22:43:51.354176'),
(7, 'auth', '0002_alter_permission_name_max_length', '2023-11-17 22:43:51.379181'),
(8, 'auth', '0003_alter_user_email_max_length', '2023-11-17 22:43:51.406508'),
(9, 'auth', '0004_alter_user_username_opts', '2023-11-17 22:43:51.410509'),
(10, 'auth', '0005_alter_user_last_login_null', '2023-11-17 22:43:51.437516'),
(11, 'auth', '0006_require_contenttypes_0002', '2023-11-17 22:43:51.438514'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2023-11-17 22:43:51.442515'),
(13, 'auth', '0008_alter_user_username_max_length', '2023-11-17 22:43:51.483034'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2023-11-17 22:43:51.510037'),
(15, 'auth', '0010_alter_group_name_max_length', '2023-11-17 22:43:51.535043'),
(16, 'auth', '0011_update_proxy_permissions', '2023-11-17 22:43:51.541046'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2023-11-17 22:43:51.570053'),
(18, 'sessions', '0001_initial', '2023-11-17 22:43:51.602058'),
(19, 'tiendaApp', '0001_initial', '2023-11-17 22:43:51.749063'),
(20, 'tiendaApp', '0002_alter_mesas_estado', '2023-11-17 22:43:51.771068'),
(21, 'tiendaApp', '0003_comanda_estado_alter_mesas_estado_and_more', '2023-11-17 22:43:51.852056'),
(22, 'tiendaApp', '0004_alter_tipousuario_options_alter_usuarios_options_and_more', '2023-11-17 22:43:51.972330'),
(23, 'tiendaApp', '0005_categoria_alter_productos_options_and_more', '2023-11-17 22:43:52.051347'),
(24, 'tiendaApp', '0006_categoria_imagen', '2023-11-17 22:43:52.083354'),
(25, 'tiendaApp', '0007_alter_productos_options_productos_imagen', '2023-11-17 22:43:52.118995'),
(26, 'tiendaApp', '0008_userprofile_remove_usuarios_tipousuario_and_more', '2023-11-18 03:07:45.848777'),
(27, 'tiendaApp', '0009_alter_comanda_options_alter_detallecomanda_options_and_more', '2023-11-20 06:05:43.184818');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_spanish2_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('ic9b55o1ei6ndbq7z80e5ayi4xonq3nz', '.eJxVjMsOwiAQRf-FtSE8CgMu3fsNZGBAqgaS0q6M_65NutDtPefcFwu4rTVsIy9hJnZmip1-t4jpkdsO6I7t1nnqbV3myHeFH3Twa6f8vBzu30HFUb-198pIQ8aAS-BzdF4oLBYKgDA4ae-lAi1tJomTSQpR61hsAeGEEETs_QG1tzbu:1r59Ue:Wj89pn2H0aynTcPV3jPhuqAC3Ql3TxtapPtSzVFczkY', '2023-12-04 18:59:36.211950'),
('vis0t2pzgi0rpkut8o012guf6p8mior5', 'e30:1r7eKO:LplxOLd_qrb9RqCHSODH-EmqtP6T9CmJfUSMEjVCbu4', '2023-12-11 16:19:20.791384'),
('bzc1b6gnhclujb97yw543du92amaf51v', 'e30:1r7eLW:5apA8k6CiuQPX2D13JPNDc3ohPmlGzAm91ST0GDGFjg', '2023-12-11 16:20:30.692137'),
('fmxlrq0fkev8meekckivf86l6h1oxej4', 'e30:1r7eN3:E34JBEdo_VkyPjMyZXv0VwdPul8apkNVu1dQCQv2iLE', '2023-12-11 16:22:05.537329'),
('t3dahxxwgzy12vgjgid8xvorn8now55w', '.eJxVjEEOwiAQRe_C2hCmA7S4dN8zkBkYbNW0SWlXxrsbki50-997_60iHfsUjypbnLO6KlCX340pPWVpID9oua86rcu-zaybok9a9bhmed1O9-9gojq1Gosr3nD2bHs2KXGHwQkFQp-HwZAUB8EKB0CQQiCArg_OGged71F9vvoBN54:1r7eNW:xwq77frhK9OydW76WGv-AVtIEv77a64ZoJnX3aip020', '2023-12-11 16:22:34.300565'),
('qcvlmq7sgjkryya43x5odd9jdks51god', '.eJxVjEEOwiAQRe_C2hCmA7S4dN8zkBkYbNW0SWlXxrsbki50-997_60iHfsUjypbnLO6KlCX340pPWVpID9oua86rcu-zaybok9a9bhmed1O9-9gojq1Gosr3nD2bHs2KXGHwQkFQp-HwZAUB8EKB0CQQiCArg_OGged71F9vvoBN54:1r83OD:F22DUCVkbQEfdRNfmXboJLbSRzoh3UZNEHa2f1vovU4', '2023-12-12 19:04:57.126095');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiendaapp_categoria`
--

DROP TABLE IF EXISTS `tiendaapp_categoria`;
CREATE TABLE IF NOT EXISTS `tiendaapp_categoria` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `descripcion` longtext COLLATE utf8mb4_spanish2_ci NOT NULL,
  `imagen` varchar(100) COLLATE utf8mb4_spanish2_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `tiendaapp_categoria`
--

INSERT INTO `tiendaapp_categoria` (`id`, `nombre`, `descripcion`, `imagen`) VALUES
(1, 'Comestibles', 'Diferentes platos a eleccion', 'categorias/comestibles_qawtWOE.png'),
(2, 'Bebidas', 'Diferentes tipos de bebidas sin alcohol', 'categorias/bebestibles_QyZHdJF.png'),
(3, 'Bebidas Alcoholicas', 'Cervezas u otros', 'categorias/vaso-cerveza-fria-fondo-1.jpg');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiendaapp_comanda`
--

DROP TABLE IF EXISTS `tiendaapp_comanda`;
CREATE TABLE IF NOT EXISTS `tiendaapp_comanda` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fecha_creacion` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `tiendaapp_comanda`
--

INSERT INTO `tiendaapp_comanda` (`id`, `fecha_creacion`) VALUES
(1, '2023-11-20 06:16:14.019123'),
(2, '2023-11-20 06:20:06.322872'),
(3, '2023-11-20 06:20:08.437347'),
(4, '2023-11-20 06:20:09.729640'),
(5, '2023-11-20 06:22:57.610286'),
(6, '2023-11-20 06:23:20.264301'),
(7, '2023-11-20 19:00:14.242831'),
(8, '2023-11-20 19:27:33.289641'),
(9, '2023-11-20 19:40:19.114629'),
(10, '2023-11-20 19:45:54.751382'),
(11, '2023-11-20 19:54:51.225919'),
(12, '2023-11-24 17:26:21.175498'),
(13, '2023-11-27 01:17:02.949761'),
(14, '2023-11-27 01:17:39.051375'),
(15, '2023-11-27 01:23:27.191997'),
(16, '2023-11-27 01:34:42.460898'),
(17, '2023-11-27 01:38:47.025348'),
(18, '2023-11-27 01:41:04.389631'),
(19, '2023-11-27 05:29:36.099224'),
(20, '2023-11-27 05:30:05.082759'),
(21, '2023-11-27 05:30:14.250638'),
(22, '2023-11-27 05:42:57.248134'),
(23, '2023-11-27 06:04:05.811520'),
(24, '2023-11-27 06:10:38.429704'),
(25, '2023-11-27 16:50:27.680074'),
(26, '2023-11-28 15:55:20.278429'),
(27, '2023-11-28 15:55:34.596522'),
(28, '2023-11-28 18:20:57.473526');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiendaapp_detallecomanda`
--

DROP TABLE IF EXISTS `tiendaapp_detallecomanda`;
CREATE TABLE IF NOT EXISTS `tiendaapp_detallecomanda` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `cantidad` int NOT NULL,
  `comanda_id` bigint NOT NULL,
  `producto_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `tiendaApp_detallecomanda_comanda_id_bb541a59` (`comanda_id`),
  KEY `tiendaApp_detallecomanda_producto_id_fef328be` (`producto_id`)
) ENGINE=MyISAM AUTO_INCREMENT=39 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `tiendaapp_detallecomanda`
--

INSERT INTO `tiendaapp_detallecomanda` (`id`, `cantidad`, `comanda_id`, `producto_id`) VALUES
(1, 1, 5, 1),
(2, 3, 6, 1),
(3, 5, 7, 1),
(4, 3, 9, 2),
(5, 3, 9, 1),
(6, 5, 10, 2),
(7, 5, 10, 1),
(8, 4, 11, 2),
(9, 4, 11, 1),
(10, 3, 12, 2),
(11, 3, 12, 3),
(12, 3, 22, 1),
(13, 3, 22, 3),
(14, 3, 22, 2),
(15, 3, 22, 4),
(16, 3, 23, 1),
(17, 3, 23, 3),
(18, 3, 23, 2),
(19, 3, 23, 4),
(20, 2, 24, 1),
(21, 2, 24, 3),
(22, 2, 24, 2),
(23, 2, 24, 4),
(24, 1, 25, 1),
(25, 1, 25, 2),
(26, 3, 26, 1),
(27, 3, 26, 3),
(28, 3, 26, 2),
(29, 3, 26, 4),
(30, 4, 27, 1),
(31, 4, 27, 3),
(32, 4, 27, 2),
(33, 4, 27, 4),
(34, 3, 28, 1),
(35, 3, 28, 3),
(36, 3, 28, 5),
(37, 3, 28, 2),
(38, 3, 28, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiendaapp_mesas`
--

DROP TABLE IF EXISTS `tiendaapp_mesas`;
CREATE TABLE IF NOT EXISTS `tiendaapp_mesas` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `numero` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiendaapp_productos`
--

DROP TABLE IF EXISTS `tiendaapp_productos`;
CREATE TABLE IF NOT EXISTS `tiendaapp_productos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `descripcion` varchar(100) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `precio` int NOT NULL,
  `categoria_id` bigint DEFAULT NULL,
  `imagen` varchar(100) COLLATE utf8mb4_spanish2_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tiendaApp_productos_categoria_id_77bbb516` (`categoria_id`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `tiendaapp_productos`
--

INSERT INTO `tiendaapp_productos` (`id`, `nombre`, `descripcion`, `precio`, `categoria_id`, `imagen`) VALUES
(1, 'Completo Italiano', 'Pan, Vienesa, Palta, Tomate, Mayonesa Casera', 1500, 1, 'productos/citaliano_Eyazf45.png'),
(2, 'Coca Cola 350ml', 'Bebida de fantasía sabor cola', 1000, 2, 'productos/coca_0lKmjjR.png'),
(3, 'Chacarero', 'Pan, Churrasco, Porotos Verdes, Aji, Mayonesa Casera', 3000, 1, 'productos/chacarero_LkG9fBP.png'),
(4, 'Shop 500ML', 'Jarra de cerveza de 500ml', 3000, 3, 'productos/vaso-cerveza-fria-fondo-1.jpg'),
(5, 'Papas Fritas Pequeñas', 'Papas fritas con salsas a eleccion', 2000, 1, 'productos/papas_L0LPCc6.png');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiendaapp_userprofile`
--

DROP TABLE IF EXISTS `tiendaapp_userprofile`;
CREATE TABLE IF NOT EXISTS `tiendaapp_userprofile` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `apellido` varchar(100) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `cargo` varchar(100) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `rut` varchar(12) COLLATE utf8mb4_spanish2_ci NOT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish2_ci;

--
-- Volcado de datos para la tabla `tiendaapp_userprofile`
--

INSERT INTO `tiendaapp_userprofile` (`id`, `nombre`, `apellido`, `cargo`, `rut`, `user_id`) VALUES
(1, 'Matias', 'Munizaga', 'Encargado', '189234082', 2),
(2, 'Juanito', 'Perez', 'Garzon', '189234082', 3),
(3, 'Matias', 'Munizaga', 'Cajero', '189234082', 4);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
