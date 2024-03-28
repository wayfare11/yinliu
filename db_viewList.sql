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

/*Table structure for table `view_list` */

DROP TABLE IF EXISTS `view_list`;

CREATE TABLE `view_list` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_list` int(11) DEFAULT NULL,
  `MaterialCode` varchar(20) DEFAULT NULL,
  `DrawingCode` varchar(20) DEFAULT NULL,
  `Name` varchar(20) DEFAULT NULL,
  `ProductSize` varchar(20) DEFAULT NULL,
  `Material` varchar(20) DEFAULT NULL,
  `Color` varchar(20) DEFAULT NULL,
  `Quantity` varchar(20) DEFAULT NULL,
  `Unit` varchar(20) DEFAULT NULL,
  `MaterialCategory` varchar(20) DEFAULT NULL,
  `Note` varchar(20) DEFAULT NULL,

  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;

INSERT INTO view_list(id_list, MaterialCode, DrawingCode, Name, ProductSize, Material, Color, Quantity, Unit, MaterialCategory, Note) 
VALUES 
(1, 12345, 'ABC', 'Product1', '10x20', 'Steel', 'Red', '100', 'pcs', 'Raw Material', 'Sample note 1'),
(2, 54321, 'XYZ', 'Product2', '15x30', 'Plastic', 'Blue', '50', 'pcs', 'Raw Material', 'Sample note 2'),
(3, 98765, 'LMN', 'Product3', '8x8', 'Aluminum', 'Silver', '75', 'pcs', 'Raw Material', 'Sample note 3'),
(4, 24680, 'PQR', 'Product4', '12x24', 'Copper', 'Gold', '120', 'pcs', 'Raw Material', 'Sample note 4'),
(5, 13579, 'STU', 'Product5', '6x12', 'Glass', 'Transparent', '200', 'pcs', 'Raw Material', 'Sample note 5'),
(6, 11111, 'AAA', 'Product6', '5x10', 'Wood', 'Brown', '90', 'pcs', 'Raw Material', 'Sample note 6'),
(7, 22222, 'BBB', 'Product7', '7x14', 'Steel', 'Gray', '150', 'pcs', 'Raw Material', 'Sample note 7'),
(8, 33333, 'CCC', 'Product8', '9x18', 'Plastic', 'Green', '80', 'pcs', 'Raw Material', 'Sample note 8'),
(9, 44444, 'DDD', 'Product9', '11x22', 'Aluminum', 'White', '110', 'pcs', 'Raw Material', 'Sample note 9'),
(10, 55555, 'EEE', 'Product10', '13x26', 'Copper', 'Black', '130', 'pcs', 'Raw Material', 'Sample note 10'),
(11, 66666, 'FFF', 'Product11', '14x28', 'Glass', 'Blue', '75', 'pcs', 'Raw Material', 'Sample note 11'),
(12, 77777, 'GGG', 'Product12', '16x32', 'Wood', 'Red', '100', 'pcs', 'Raw Material', 'Sample note 12'),
(13, 88888, 'HHH', 'Product13', '18x36', 'Steel', 'Silver', '120', 'pcs', 'Raw Material', 'Sample note 13'),
(14, 99999, 'III', 'Product14', '20x40', 'Plastic', 'Yellow', '200', 'pcs', 'Raw Material', 'Sample note 14'),
(15, 101010, 'JJJ', 'Product15', '22x44', 'Aluminum', 'Gold', '90', 'pcs', 'Raw Material', 'Sample note 15'),
(16, 111111, 'KKK', 'Product16', '24x48', 'Copper', 'Brown', '150', 'pcs', 'Raw Material', 'Sample note 16'),
(17, 121212, 'LLL', 'Product17', '26x52', 'Glass', 'Gray', '100', 'pcs', 'Raw Material', 'Sample note 17'),
(18, 131313, 'MMM', 'Product18', '28x56', 'Wood', 'Green', '80', 'pcs', 'Raw Material', 'Sample note 18'),
(19, 141414, 'NNN', 'Product19', '30x60', 'Steel', 'White', '110', 'pcs', 'Raw Material', 'Sample note 19'),
(20, 151515, 'OOO', 'Product20', '32x64', 'Plastic', 'Black', '130', 'pcs', 'Raw Material', 'Sample note 20'),
(21, 161616, 'PPP', 'Product21', '34x68', 'Aluminum', 'Blue', '75', 'pcs', 'Raw Material', 'Sample note 21'),
(22, 171717, 'QQQ', 'Product22', '36x72', 'Copper', 'Red', '100', 'pcs', 'Raw Material', 'Sample note 22'),
(23, 181818, 'RRR', 'Product23', '38x76', 'Glass', 'Silver', '120', 'pcs', 'Raw Material', 'Sample note 23'),
(24, 191919, 'SSS', 'Product24', '40x80', 'Wood', 'Yellow', '200', 'pcs', 'Raw Material', 'Sample note 24'),
(25, 202020, 'TTT', 'Product25', '42x84', 'Steel', 'Gold', '90', 'pcs', 'Raw Material', 'Sample note 25'),
(26, 212121, 'UUU', 'Product26', '44x88', 'Plastic', 'Brown', '150', 'pcs', 'Raw Material', 'Sample note 26'),
(27, 222222, 'VVV', 'Product27', '46x92', 'Aluminum', 'Gray', '100', 'pcs', 'Raw Material', 'Sample note 27'),
(28, 232323, 'WWW', 'Product28', '48x96', 'Copper', 'Green', '80', 'pcs', 'Raw Material', 'Sample note 28'),
(29, 242424, 'XXX', 'Product29', '50x100', 'Glass', 'White', '110', 'pcs', 'Raw Material', 'Sample note 29'),
(30, 252525, 'YYY', 'Product30', '52x104', 'Wood', 'Black', '130', 'pcs', 'Raw Material', 'Sample note 30'),
(31, 262626, 'ZZZ', 'Product31', '54x108', 'Steel', 'Blue', '75', 'pcs', 'Raw Material', 'Sample note 31'),
(32, 272727, 'AAA1', 'Product32', '56x112', 'Plastic', 'Red', '100', 'pcs', 'Raw Material', 'Sample note 32'),
(33, 282828, 'BBB1', 'Product33', '58x116', 'Aluminum', 'Silver', '120', 'pcs', 'Raw Material', 'Sample note 33'),
(34, 292929, 'CCC1', 'Product34', '60x120', 'Copper', 'Yellow', '200', 'pcs', 'Raw Material', 'Sample note 34'),
(35, 303030, 'DDD1', 'Product35', '62x124', 'Glass', 'Gold', '90', 'pcs', 'Raw Material', 'Sample note 35');


/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
