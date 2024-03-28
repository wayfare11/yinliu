/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 5.7.18-log : Database - db_book3
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`yinliu` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `yinliu`;

/*Table structure for table `yinliu_home` */

DROP TABLE IF EXISTS `yinliu_home`;

CREATE TABLE `yinliu_home` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(20) DEFAULT NULL,
  `FileCode` varchar(20) DEFAULT NULL,
  `VersionCode` varchar(20) DEFAULT NULL,
  `ProductSize` varchar(20) DEFAULT NULL,
  `ProductCode` varchar(20) DEFAULT NULL,
  `DandaoSize` varchar(20) DEFAULT NULL,
  `DandaoStyle` varchar(20) DEFAULT NULL,
  `DandaoCode` varchar(20) DEFAULT NULL,
  `YinliuSize` varchar(20) DEFAULT NULL,
  `YinliuLock` varchar(20) DEFAULT NULL,
  `YinliuStyle` varchar(20) DEFAULT NULL,
  `YinliuCode` varchar(20) DEFAULT NULL,
  `MaterialCode` varchar(20) DEFAULT NULL,

  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO yinliu_home(id, Name, FileCode, VersionCode, ProductSize, MaterialCode) VALUES 
(1, '名称1', '1', 'v0.0.1', '60*90', '1001'),
(2, '名称2', '2', 'v0.0.2', '70*90', '1002'),
(3, '名称3', '3', 'v0.0.3', '80*90', '1003'),
(4, '名称4', '4', 'v0.0.4', '90*90', '1004'),
(5, '名称5', '5', 'v0.0.5', '100*90', '1005'),
(6, '名称6', '6', 'v0.0.6', '110*90', '1006'),
(7, '名称7', '7', 'v0.0.7', '120*90', '1007'),
(8, '名称8', '8', 'v0.0.8', '130*90', '1008'),
(9, '名称9', '9', 'v0.0.9', '140*90', '1009'),
(10, '名称10', '10', 'v0.0.10', '150*90', '1010'),
(11, '名称11', '11', 'v0.0.11', '160*90', '1011'),
(12, '名称12', '12', 'v0.0.12', '170*90', '1012'),
(13, '名称13', '13', 'v0.0.13', '180*90', '1013'),
(14, '名称14', '14', 'v0.0.14', '190*90', '1014'),
(15, '名称15', '15', 'v0.0.15', '200*90', '1015'),
(16, '名称16', '16', 'v0.0.16', '210*90', '1016'),
(17, '名称17', '17', 'v0.0.17', '220*90', '1017'),
(18, '名称18', '18', 'v0.0.18', '230*90', '1018'),
(19, '名称19', '19', 'v0.0.19', '240*90', '1019'),
(20, '名称20', '20', 'v0.0.20', '250*90', '1020'),
(21, '名称21', '21', 'v0.0.21', '260*90', '1021'),
(22, '名称22', '22', 'v0.0.22', '270*90', '1022'),
(23, '名称23', '23', 'v0.0.23', '280*90', '1023'),
(24, '名称24', '24', 'v0.0.24', '290*90', '1024'),
(25, '名称25', '25', 'v0.0.25', '300*90', '1025'),
(26, '名称26', '26', 'v0.0.26', '310*90', '1026'),
(27, '名称27', '27', 'v0.0.27', '320*90', '1027'),
(28, '名称28', '28', 'v0.0.28', '330*90', '1028'),
(29, '名称29', '29', 'v0.0.29', '340*90', '1029'),
(30, '名称30', '30', 'v0.0.30', '350*90', '1030'),
(31, '名称31', '31', 'v0.0.31', '360*90', '1031'),
(32, '名称32', '32', 'v0.0.32', '370*90', '1032');


       

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
