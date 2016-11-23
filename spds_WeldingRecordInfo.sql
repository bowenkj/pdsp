-- MySQL dump 10.13  Distrib 5.7.13, for linux-glibc2.5 (x86_64)
--
-- Host: localhost    Database: spds
-- ------------------------------------------------------
-- Server version	5.5.49-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `WeldingRecordInfo`
--

DROP TABLE IF EXISTS `WeldingRecordInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `WeldingRecordInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `docid` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  `part` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `welder` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `material` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `preparation` tinyint(1) DEFAULT NULL,
  `cur` int(11) DEFAULT NULL,
  `voltage` int(11) DEFAULT NULL,
  `speed` int(11) DEFAULT NULL,
  `height` varchar(255) CHARACTER SET latin1 DEFAULT NULL,
  `result` tinyint(1) DEFAULT NULL,
  `productid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `productid` (`productid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WeldingRecordInfo`
--

LOCK TABLES `WeldingRecordInfo` WRITE;
/*!40000 ALTER TABLE `WeldingRecordInfo` DISABLE KEYS */;
INSERT INTO `WeldingRecordInfo` VALUES (3,'A',4,'S','s','g',0,1,2,3,'t',0,NULL),(4,'A',4,'S','s','g',0,1,2,3,'t',0,NULL),(5,'A',4,'S','s','g',0,1,2,3,'t',0,NULL),(6,'A',4,'S','s','g',0,1,2,3,'t',0,NULL),(7,'A',4,'S','s','g',0,1,2,3,'t',0,NULL),(8,'A',4,'S','s','g',0,1,2,3,'t',0,NULL),(9,'A',4,'S','s','g',0,1,2,3,'t',0,NULL),(18,'A',4,'S','s','g',0,1,2,3,'t',0,NULL),(20,'A',4,'S','s','g',0,1,2,3,'t',0,2);
/*!40000 ALTER TABLE `WeldingRecordInfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-23 12:47:30
