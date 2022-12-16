-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3306
-- Tiempo de generación: 01-12-2022 a las 20:32:31
-- Versión del servidor: 5.7.36
-- Versión de PHP: 7.4.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inacap`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumno`
--

DROP TABLE IF EXISTS `alumno`;
CREATE TABLE IF NOT EXISTS `alumno` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rut` varchar(12) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellidos` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `carrera_id` bigint(20) NOT NULL,
  `contraseña` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `alumno_carrera_id_b43cbb67` (`carrera_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `alumno`
--

INSERT INTO `alumno` (`id`, `rut`, `nombre`, `apellidos`, `correo`, `carrera_id`, `contraseña`) VALUES
(1, '205027998', 'Elias Sebastian', 'Martinez Muñoz', 'eliasmartinezm05@gmail.com', 1, '123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

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
(25, 'Can add Carrera', 7, 'add_carrera'),
(26, 'Can change Carrera', 7, 'change_carrera'),
(27, 'Can delete Carrera', 7, 'delete_carrera'),
(28, 'Can view Carrera', 7, 'view_carrera'),
(29, 'Can add Alumno', 8, 'add_alumno'),
(30, 'Can change Alumno', 8, 'change_alumno'),
(31, 'Can delete Alumno', 8, 'delete_alumno'),
(32, 'Can view Alumno', 8, 'view_alumno'),
(33, 'Can add Encargado', 9, 'add_encargado'),
(34, 'Can change Encargado', 9, 'change_encargado'),
(35, 'Can delete Encargado', 9, 'delete_encargado'),
(36, 'Can view Encargado', 9, 'view_encargado'),
(37, 'Can add Usuario', 10, 'add_usuario'),
(38, 'Can change Usuario', 10, 'change_usuario'),
(39, 'Can delete Usuario', 10, 'delete_usuario'),
(40, 'Can view Usuario', 10, 'view_usuario'),
(41, 'Can add Solicitud', 11, 'add_solicitud'),
(42, 'Can change Solicitud', 11, 'change_solicitud'),
(43, 'Can delete Solicitud', 11, 'delete_solicitud'),
(44, 'Can view Solicitud', 11, 'view_solicitud');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrera`
--

DROP TABLE IF EXISTS `carrera`;
CREATE TABLE IF NOT EXISTS `carrera` (
  `nombre` varchar(100) NOT NULL,
  `carrera_id` bigint(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`carrera_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `carrera`
--

INSERT INTO `carrera` (`nombre`, `carrera_id`) VALUES
('Analista Programador', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

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
(7, 'Alumnado', 'carrera'),
(8, 'Alumnado', 'alumno'),
(9, 'Alumnado', 'encargado'),
(10, 'Alumnado', 'usuario'),
(11, 'Alumnado', 'solicitud');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Alumnado', '0001_initial', '2022-11-30 20:15:01.566220'),
(2, 'Alumnado', '0002_alter_carrera_carrera_id', '2022-11-30 20:15:01.568733'),
(3, 'Alumnado', '0003_encargado_usuario', '2022-11-30 20:15:01.608932'),
(4, 'Alumnado', '0004_alter_alumno_options_alumno_contraseña', '2022-11-30 20:15:01.630999'),
(5, 'Alumnado', '0005_alter_alumno_contraseña', '2022-11-30 20:15:01.645538'),
(6, 'contenttypes', '0001_initial', '2022-11-30 20:15:01.670729'),
(7, 'auth', '0001_initial', '2022-11-30 20:15:01.913728'),
(8, 'admin', '0001_initial', '2022-11-30 20:15:01.975723'),
(9, 'admin', '0002_logentry_remove_auto_add', '2022-11-30 20:15:01.980746'),
(10, 'admin', '0003_logentry_add_action_flag_choices', '2022-11-30 20:15:01.985748'),
(11, 'contenttypes', '0002_remove_content_type_name', '2022-11-30 20:15:02.019363'),
(12, 'auth', '0002_alter_permission_name_max_length', '2022-11-30 20:15:02.036283'),
(13, 'auth', '0003_alter_user_email_max_length', '2022-11-30 20:15:02.054691'),
(14, 'auth', '0004_alter_user_username_opts', '2022-11-30 20:15:02.060712'),
(15, 'auth', '0005_alter_user_last_login_null', '2022-11-30 20:15:02.079576'),
(16, 'auth', '0006_require_contenttypes_0002', '2022-11-30 20:15:02.081585'),
(17, 'auth', '0007_alter_validators_add_error_messages', '2022-11-30 20:15:02.086581'),
(18, 'auth', '0008_alter_user_username_max_length', '2022-11-30 20:15:02.106562'),
(19, 'auth', '0009_alter_user_last_name_max_length', '2022-11-30 20:15:02.124757'),
(20, 'auth', '0010_alter_group_name_max_length', '2022-11-30 20:15:02.142917'),
(21, 'auth', '0011_update_proxy_permissions', '2022-11-30 20:15:02.148934'),
(22, 'auth', '0012_alter_user_first_name_max_length', '2022-11-30 20:15:02.166311'),
(23, 'sessions', '0001_initial', '2022-11-30 20:15:02.191417'),
(24, 'Alumnado', '0006_solicitud', '2022-12-01 17:01:05.310452'),
(25, 'Alumnado', '0007_solicitud_deporte', '2022-12-01 19:54:26.188975');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('jgb4mk53lpxsd1t63y8dq80dxdztmlbl', 'eyJjb3JyZW8iOiJlbGlhc21hcnRpbmV6bTA1QGdtYWlsLmNvbSJ9:1p0qE5:RncxhxNwHoketogL-ZQxiPsnah2hLQb7aTW62HEJqAA', '2022-12-15 20:32:09.755518');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `encargado`
--

DROP TABLE IF EXISTS `encargado`;
CREATE TABLE IF NOT EXISTS `encargado` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `rut` varchar(10) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `sexo` varchar(10) NOT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `encargado`
--

INSERT INTO `encargado` (`id`, `rut`, `nombre`, `sexo`, `fecha_nacimiento`) VALUES
(1, '829039456', 'Miguel Angel', 'm', '1986-12-23');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `solicitud`
--

DROP TABLE IF EXISTS `solicitud`;
CREATE TABLE IF NOT EXISTS `solicitud` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `estado` varchar(3) NOT NULL,
  `fecha_solicitud` datetime(6) NOT NULL,
  `alumno_id` bigint(20) NOT NULL,
  `deporte` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `solicitud_alumno_id_680b5539` (`alumno_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

DROP TABLE IF EXISTS `usuario`;
CREATE TABLE IF NOT EXISTS `usuario` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre_usuario` varchar(100) NOT NULL,
  `contraseña` varchar(100) NOT NULL,
  `correo` varchar(100) NOT NULL,
  `encargado_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `usuario_encargado_id_5326cea4` (`encargado_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre_usuario`, `contraseña`, `correo`, `encargado_id`) VALUES
(2, 'Roberto', '123', 'alberto123@gmail.com', 1),
(3, 'Carlos Diaz', '123', 'alopresidente@gmail.com', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
