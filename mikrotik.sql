-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: mikrotik
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `destination_address`
--

DROP TABLE IF EXISTS `destination_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `destination_address` (
  `destination_address_id` int NOT NULL AUTO_INCREMENT,
  `destination_address` varchar(100) NOT NULL,
  `destination_address_regex` varchar(100) NOT NULL,
  `destination_id` int NOT NULL,
  `destination_key` varchar(100) NOT NULL,
  PRIMARY KEY (`destination_address_id`),
  UNIQUE KEY `destination_address_destination_address_regex_uindex` (`destination_address_regex`),
  UNIQUE KEY `destination_address_destination_key_uindex` (`destination_key`),
  KEY `destination_address___fk_destination_id` (`destination_id`),
  CONSTRAINT `destination_address___fk_destination_id` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`destination_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destination_address`
--

LOCK TABLES `destination_address` WRITE;
/*!40000 ALTER TABLE `destination_address` DISABLE KEYS */;
INSERT INTO `destination_address` VALUES (1,'149.154.0.0/16','149\\.154\\.[0-9]{1,3}\\.[0-9]{1,3}',9,'149.154.0.0/16-9'),(2,'157.240.0.0/16','157\\.240\\.[0-9]{1,3}\\.[0-9]{1,3}',14,'157.240.0.0/16-14'),(13,'91.108.8.0/22','91\\.108\\.([8-9]|1[0-1])\\.[0-9]{1,3}',9,'91.108.8.0/22-9'),(14,'91.108.4.0/22','91\\.108\\.[4-7]\\.[0-9]{1,3}',9,'91.108.4.0/22-9'),(15,'91.108.56.0/22','91\\.108\\.5[6-9]\\.[0-9]{1,3}',9,'91.108.56.0/22-9'),(16,'95.161.64.0/20','95\\.161\\.(6[4-9]|7[0-9])\\.[0-9]{1,3}',9,'95.161.64.0/20-9'),(17,'85.132.0.0/16','85\\.132\\.[0-9]{1,3}\\.[0-9]{1,3}',14,'85.132.0.0/16-14'),(18,'52.45.0.0/16','52\\.45\\.[0-9]{1,3}\\.[0-9]{1,3}',14,'52.45.0.0/16-14'),(19,'52.87.0.0/16','52\\.87\\.[0-9]{1,3}\\.[0-9]{1,3}',14,'52.87.0.0/16-14'),(20,'34.199.0.0/16','34\\.199\\.[0-9]{1,3}\\.[0-9]{1,3}',14,'34.199.0.0/16-14'),(21,'3.208.0.0/16','3\\.208\\.[0-9]{1,3}\\.[0-9]{1,3}',14,'3.208.0.0/16-14'),(22,'34.193.0.0/16','34\\.193\\.[0-9]{1,3}\\.[0-9]{1,3}',14,'34.193.0.0/16-14'),(23,'94.20.0.0/16','94\\.20\\.[0-9]{1,3}\\.[0-9]{1,3}',14,'94.20.0.0/16-14'),(24,'62.212.0.0/16','62\\.212\\.[0-9]{1,3}\\.[0-9]{1,3}',14,'62.212.0.0/16-14');
/*!40000 ALTER TABLE `destination_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `destinations`
--

DROP TABLE IF EXISTS `destinations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `destinations` (
  `destination_id` int NOT NULL AUTO_INCREMENT,
  `destination_name` varchar(100) NOT NULL,
  `descriptions` varchar(200) DEFAULT NULL,
  `color_id` varchar(100) NOT NULL,
  PRIMARY KEY (`destination_id`),
  UNIQUE KEY `destinations_destination_name_uindex` (`destination_name`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `destinations`
--

LOCK TABLES `destinations` WRITE;
/*!40000 ALTER TABLE `destinations` DISABLE KEYS */;
INSERT INTO `destinations` VALUES (9,'Telegram','Telegram Address List','#71c3fa'),(14,'Instagram','Instagram Address List','#bc2461');
/*!40000 ALTER TABLE `destinations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `device_type`
--

DROP TABLE IF EXISTS `device_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device_type` (
  `type_id` int NOT NULL AUTO_INCREMENT,
  `type_name` varchar(50) NOT NULL,
  PRIMARY KEY (`type_id`),
  UNIQUE KEY `device_type_type_name_uindex` (`type_name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device_type`
--

LOCK TABLES `device_type` WRITE;
/*!40000 ALTER TABLE `device_type` DISABLE KEYS */;
INSERT INTO `device_type` VALUES (5,'Accessories'),(2,'Laptop'),(1,'Mobile'),(6,'Network'),(7,'Other'),(3,'PC'),(4,'Server');
/*!40000 ALTER TABLE `device_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `devices`
--

DROP TABLE IF EXISTS `devices`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `devices` (
  `device_id` int NOT NULL AUTO_INCREMENT,
  `device_name` varchar(20) NOT NULL,
  `model` varchar(20) DEFAULT NULL,
  `type_id` int NOT NULL,
  `user_id` int DEFAULT NULL,
  `device_key` varchar(100) NOT NULL,
  PRIMARY KEY (`device_id`),
  UNIQUE KEY `devices_device_key_uindex` (`device_key`),
  KEY `devices___fk_id` (`user_id`),
  KEY `devices___fk_type_id` (`type_id`),
  CONSTRAINT `devices___fk_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE,
  CONSTRAINT `devices___fk_type_id` FOREIGN KEY (`type_id`) REFERENCES `device_type` (`type_id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `devices`
--

LOCK TABLES `devices` WRITE;
/*!40000 ALTER TABLE `devices` DISABLE KEYS */;
INSERT INTO `devices` VALUES (40,'other','other',7,17,'other-other-17');
/*!40000 ALTER TABLE `devices` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ip`
--

DROP TABLE IF EXISTS `ip`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ip` (
  `ip_id` int NOT NULL AUTO_INCREMENT,
  `ip_value` varchar(255) NOT NULL,
  `device_id` int NOT NULL,
  PRIMARY KEY (`ip_id`),
  UNIQUE KEY `ip_ip_value_uindex` (`ip_value`),
  KEY `ip___fk_device_ip` (`device_id`),
  CONSTRAINT `ip___fk_device_ip` FOREIGN KEY (`device_id`) REFERENCES `devices` (`device_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=158 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ip`
--

LOCK TABLES `ip` WRITE;
/*!40000 ALTER TABLE `ip` DISABLE KEYS */;
INSERT INTO `ip` VALUES (20,'NONE',40);
/*!40000 ALTER TABLE `ip` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `local_range`
--

DROP TABLE IF EXISTS `local_range`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `local_range` (
  `local_range_name` varchar(50) NOT NULL,
  `local_range_address` varchar(20) NOT NULL,
  `local_range_regex` varchar(200) NOT NULL,
  `mikrotik_id` int NOT NULL,
  `local_range_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`local_range_id`),
  KEY `local_range___fk_local` (`mikrotik_id`),
  CONSTRAINT `local_range___fk_local` FOREIGN KEY (`mikrotik_id`) REFERENCES `mikrotiks` (`mikrotik_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `local_range`
--

LOCK TABLES `local_range` WRITE;
/*!40000 ALTER TABLE `local_range` DISABLE KEYS */;
INSERT INTO `local_range` VALUES ('Floor-0','172.16.0.0/24','172\\.16\\.0\\.[0-9]{1,3}',1,1),('Floor-1','172.16.1.0/24','172\\.16\\.1\\.[0-9]{1,3}',1,2),('Floor-2','172.16.2.0/24','172\\.16\\.2\\.[0-9]{1,3}',1,3),('Floor-3','172.16.3.0/24','172\\.16\\.3\\.[0-9]{1,3}',1,4),('Floor-4','172.16.4.0/24','172\\.16\\.4\\.[0-9]{1,3}',1,5);
/*!40000 ALTER TABLE `local_range` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mikrotiks`
--

DROP TABLE IF EXISTS `mikrotiks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mikrotiks` (
  `mikrotik_id` int NOT NULL AUTO_INCREMENT,
  `mikrotik_name` varchar(50) NOT NULL,
  `mikrotik_address` varchar(20) NOT NULL,
  `mikrotik_port` int NOT NULL,
  `descriptions` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`mikrotik_id`),
  UNIQUE KEY `mikrotiks_mikrotik_address_uindex` (`mikrotik_address`),
  UNIQUE KEY `mikrotiks_mikrotik_name_uindex` (`mikrotik_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mikrotiks`
--

LOCK TABLES `mikrotiks` WRITE;
/*!40000 ALTER TABLE `mikrotiks` DISABLE KEYS */;
INSERT INTO `mikrotiks` VALUES (1,'Home','172.16.1.1',8080,'RB750g');
/*!40000 ALTER TABLE `mikrotiks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `role_id` int NOT NULL AUTO_INCREMENT,
  `role_name` varchar(2000) NOT NULL,
  `role_name_en` varchar(2000) NOT NULL DEFAULT 'User',
  PRIMARY KEY (`role_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'کاربر','User'),(2,'ادمین','Admin'),(3,'گزارشگر','Reporter');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `traffic`
--

DROP TABLE IF EXISTS `traffic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `traffic` (
  `download` float NOT NULL,
  `upload` float NOT NULL,
  `date` date NOT NULL,
  `ip_id` int NOT NULL,
  `traffic_key` varchar(100) NOT NULL,
  `destination_id` int DEFAULT NULL,
  PRIMARY KEY (`traffic_key`),
  KEY `traffic___fk_ip_id` (`ip_id`),
  KEY `traffic___fk_destination_id` (`destination_id`),
  CONSTRAINT `traffic___fk_destination_id` FOREIGN KEY (`destination_id`) REFERENCES `destinations` (`destination_id`) ON DELETE CASCADE,
  CONSTRAINT `traffic___fk_ip_id` FOREIGN KEY (`ip_id`) REFERENCES `ip` (`ip_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `traffic`
--

LOCK TABLES `traffic` WRITE;
/*!40000 ALTER TABLE `traffic` DISABLE KEYS */;
INSERT INTO `traffic` VALUES (39.33,13.96,'2022-03-09',20,'2022-03-09-20-None',NULL);
/*!40000 ALTER TABLE `traffic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `user_id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `user_name` varchar(100) NOT NULL,
  `user_password` varchar(200) NOT NULL,
  `mikrotik_id` int NOT NULL DEFAULT '1',
  `group_id` int DEFAULT NULL,
  `role_id` int NOT NULL DEFAULT '1',
  `profile_pic` varchar(200) NOT NULL DEFAULT '../assets/img/profiles/default_profile.jpg',
  `date_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `users_username_uindex` (`user_name`),
  KEY `users___fk__mikrotik_id` (`mikrotik_id`),
  KEY `users___fk_group_id` (`group_id`),
  KEY `users___fk_role` (`role_id`),
  CONSTRAINT `users___fk__mikrotik_id` FOREIGN KEY (`mikrotik_id`) REFERENCES `mikrotiks` (`mikrotik_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users___fk_group_id` FOREIGN KEY (`group_id`) REFERENCES `users_groups` (`group_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `users___fk_role` FOREIGN KEY (`role_id`) REFERENCES `roles` (`role_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='Users Table';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (17,'Other Users','','','other','other@123',1,6,1,'../assets/img/profiles/default_profile.jpg','2020-12-30 18:51:08'),(59,'admin ','admin','admin@mikrotik.com','admin','21232f297a57a5a743894a0e4a801fc3',1,6,2,'../assets/img/profiles/default_profile.jpg','2022-02-25 08:23:34');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users_groups`
--

DROP TABLE IF EXISTS `users_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users_groups` (
  `group_id` int NOT NULL AUTO_INCREMENT,
  `group_name` varchar(50) NOT NULL,
  `description` varchar(2000) DEFAULT ' ',
  PRIMARY KEY (`group_id`),
  UNIQUE KEY `users_groups_group_name_uindex` (`group_name`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users_groups`
--

LOCK TABLES `users_groups` WRITE;
/*!40000 ALTER TABLE `users_groups` DISABLE KEYS */;
INSERT INTO `users_groups` VALUES (6,'Other',' ');
/*!40000 ALTER TABLE `users_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `websites`
--

DROP TABLE IF EXISTS `websites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `websites` (
  `web_key` char(255) NOT NULL,
  `domain` char(255) NOT NULL,
  `count` bigint NOT NULL DEFAULT '0',
  `ip_id` int NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`web_key`),
  KEY `websites_ip_ip_id_fk` (`ip_id`),
  CONSTRAINT `websites_ip_ip_id_fk` FOREIGN KEY (`ip_id`) REFERENCES `ip` (`ip_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `websites`
--

LOCK TABLES `websites` WRITE;
/*!40000 ALTER TABLE `websites` DISABLE KEYS */;
/*!40000 ALTER TABLE `websites` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-30 14:00:08
