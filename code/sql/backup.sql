-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: CulturalHeritageDB
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `artifactinfo`
--

DROP TABLE IF EXISTS `artifactinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artifactinfo` (
  `ArtifactID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Category` varchar(100) DEFAULT NULL,
  `HistoricalBackground` text,
  `Material` varchar(100) DEFAULT NULL,
  `Dimensions` varchar(50) DEFAULT NULL,
  `ArchaeologicalInfo` text,
  `ExpertAnalysis` text,
  `CreatedDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `UpdatedDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ArtifactID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artifactinfo`
--

LOCK TABLES `artifactinfo` WRITE;
/*!40000 ALTER TABLE `artifactinfo` DISABLE KEYS */;
INSERT INTO `artifactinfo` VALUES (1,'商代·司母辛方鼎','青铜器','通高80.1cm，重128kg，1976年河南安阳妇好墓出土。','青铜','通高80.1cm，重128kg','双层复合范铸造，鼎腹三层纹饰带（饕餮纹-夔龙纹-蝉纹）构成商代典型\"三层花\"装饰体系。','鼎腹内壁\"司母辛\"铭文印证商王武丁配偶妇好的传奇生平，四棱铸接处的镂空扉棱展现早商青铜铸造巅峰技艺，足部兽面纹瞳孔镶嵌绿松石，现藏中国社会科学院考古研究所。','2025-03-16 14:08:04',NULL),(2,'西周·大盂鼎','青铜器','高101.9cm，重153.5kg，1849年陕西郿县出土。','青铜','高101.9cm，重153.5kg','浑铸法一次成型，鼎腹波曲纹开西周中期纹饰革新先河。','291字铭文记载康王训诰，创金文书法\"雍容浑厚\"典范，鼎足上部浮雕立体饕餮，传承商代狞厉之美，清代潘祖荫\"海内三宝\"之一，现藏中国国家博物馆。','2025-03-16 14:08:04',NULL),(3,'西周·虢季子白盘','青铜器','长137.2cm，宽86.5cm，重215.3kg，1840年陕西宝鸡出土。','青铜','长137.2cm，宽86.5cm，重215.3kg','失蜡法铸造的现存最大青铜盘，盘壁厚度均匀控制在3mm。','111字铭文记载西周宣王时期对猃狁作战，开后世碑刻章法先河，盘内四壁饰环带纹，盘底铸有八组卷体龙纹，太平天国时期曾作马槽，现藏中国国家博物馆。','2025-03-16 14:08:04',NULL),(4,'春秋·莲鹤方壶','青铜器','通高126cm，重64.28kg，1923年河南新郑出土。','青铜','通高126cm，重64.28kg','分铸焊接技术典范，盖顶立鹤采用榫卯活链结构。','壶身蟠龙纹间饰立雕双兽，莲瓣形盖沿铸有18只回首灵兽，郭沫若称其\"时代精神之象征\"，故宫博物院与河南博物院各藏一件。','2025-03-16 14:08:04',NULL),(5,'商代·四方风名甲骨','甲骨文','长24.5cm，宽19cm，1899年河南安阳殷墟出土。','龟甲','长24.5cm，宽19cm','单刀契刻与双刀复刻结合，朱砂填涂笔划。','记载四方神名与风神名，印证《山海经》天文体系，骨版裂纹体现商代占卜灼烧技法，现藏中国国家博物馆。','2025-03-16 14:08:44',NULL),(6,'商代·大龟四版','甲骨文','长28cm，宽18cm，1928年殷墟科学发掘首获。','龟甲','长28cm，宽18cm','整龟腹甲分段契刻，钻凿排列呈螺旋结构。','完整记录干支表与气象占卜，发现\"贞人\"群体证据，开创甲骨断代研究体系，现藏台北历史语言研究所。','2025-03-16 14:08:44',NULL),(7,'商代·鹿顶骨记事刻辞','甲骨文','长32cm，宽21cm，1936年YH127坑出土。','鹿骨','长32cm，宽21cm','锐器刻划与颜料填涂复合工艺。','记载商王田猎获鹿二百零五只，骨面残留朱砂祭祀痕迹，契口方向反映右书书写规范，现藏中国社会科学院考古研究所。','2025-03-16 14:08:44',NULL),(8,'商代·宰丰骨匕刻辞','甲骨文','长27.3cm，宽3.8cm，传安阳出土。','骨匕','长27.3cm，宽3.8cm','错位双面契刻，字口镶嵌绿松石。','记载商王赏赐宰丰事件，字势开合如青铜铭文，骨脊血槽保留屠宰加工痕迹，现藏故宫博物院。','2025-03-16 14:08:44',NULL),(9,'北宋·汝窑天青釉弦纹樽','瓷器','高12.9cm，口径18cm，1987年河南宝丰清凉寺出土。','瓷器','高12.9cm，口径18cm','满釉支烧，釉层含玛瑙末，开片呈蝉翼纹。','现存唯一汝窑樽式器，三道弦纹间隔七组鼓钉，底留5个芝麻钉痕，2012年苏富比同类器拍出2.94亿港元，现藏北京故宫博物院。','2025-03-16 14:09:00',NULL),(10,'元·青花鬼谷子下山图罐','瓷器','高27.5cm，腹径33cm，2005年伦敦佳士得拍卖。','瓷器','高27.5cm，腹径33cm','苏麻离青料，多层次留白拓印技法。','描绘孙膑营救鬼谷子场景，青花发色呈现铁锈斑，2005年拍得2.3亿元创中国艺术品纪录，现藏英国古董商埃斯肯纳齐处。','2025-03-16 14:09:00',NULL),(11,'明成化·斗彩鸡缸杯','瓷器','高3.4cm，口径8.3cm，1999年香港苏富比释出。','瓷器','高3.4cm，口径8.3cm','釉下青花与釉上彩二次烧造工艺。','绘童子戏鸡纹，胎体厚度仅0.8mm，2014年刘益谦2.8亿港元竞得，现存上海龙美术馆。','2025-03-16 14:09:00',NULL),(12,'清乾隆·粉彩镂空转心瓶','瓷器','高40.2cm，腹径24.8cm，故宫旧藏。','瓷器','高40.2cm，腹径24.8cm','分层拉坯与活动机关嵌套技术。','外层镂空四季花卉，内胆绘婴戏图，旋转装置含12个活动部件，2010年伦敦5.5亿元成交，现藏中国国家博物馆。','2025-03-16 14:09:00',NULL),(13,'盛唐·第172窟观无量寿经变','壁画','窟高4.5m，宽3.8m，中唐吐蕃时期（781-847）。','矿物颜料','窟高4.5m，宽3.8m','矿物颜料多层叠染，金箔沥粉堆金工艺。','主尊阿弥陀佛结跏趺坐，两侧观音势至菩萨璎珞垂绦，建筑群运用焦点透视法，展现唐代青绿山水巅峰技法，1944年常书鸿团队修复。','2025-03-16 14:09:14',NULL),(14,'初唐·第220窟药师七佛图','壁画','东壁通高3.2m，贞观十六年（642）。','矿物颜料','东壁通高3.2m','朱砂铅丹叠染，白描铁线描勾形。','七佛手执药器立于莲台，眷属十二神将甲胄分明，飞天帔帛运用\"吴带当风\"笔意，1943年剥离表层宋代重绘层现真容。','2025-03-16 14:09:14',NULL),(15,'西魏·第285窟五百强盗成佛图','壁画','南壁长5.6m，大统四年（538）。','矿物颜料','南壁长5.6m','西域凹凸法与中原晕染法融合。','连环画式描绘强盗受刑、出家证道场景，战士锁甲运用\"曹衣出水\"技法，山林用石青石绿没骨画法，1908年伯希和探险队摄影记录。','2025-03-16 14:09:14',NULL),(16,'晚唐·第156窟张议潮统军出行图','壁画','南壁长8.2m，咸通六年（865）。','矿物颜料','南壁长8.2m','铁线描与兰叶描结合，铅白提亮技法。','现存最早大型历史人物壁画，绘骑兵仪仗百余人，驼马采用\"三花\"饰鞍法，榜题墨书保存完整，1944年常书鸿团队揭取保护。','2025-03-16 14:09:14',NULL);
/*!40000 ALTER TABLE `artifactinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artifactmodel`
--

DROP TABLE IF EXISTS `artifactmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artifactmodel` (
  `ModelID` int NOT NULL AUTO_INCREMENT,
  `ArtifactID` int DEFAULT NULL,
  `ModelType` varchar(50) DEFAULT NULL,
  `FilePath` varchar(255) DEFAULT NULL,
  `CreatedDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `UpdatedDate` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ModelID`),
  KEY `ArtifactID` (`ArtifactID`),
  CONSTRAINT `artifactmodel_ibfk_1` FOREIGN KEY (`ArtifactID`) REFERENCES `artifactinfo` (`ArtifactID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artifactmodel`
--

LOCK TABLES `artifactmodel` WRITE;
/*!40000 ALTER TABLE `artifactmodel` DISABLE KEYS */;
INSERT INTO `artifactmodel` VALUES (1,1,'3D模型','/models/simuxin_ding.obj','2025-03-16 14:08:11',NULL),(2,2,'3D模型','/models/dayu_ding.obj','2025-03-16 14:08:11',NULL),(3,3,'3D模型','/models/guojizibai_pan.obj','2025-03-16 14:08:11',NULL),(4,4,'3D模型','/models/lianhe_fanghu.obj','2025-03-16 14:08:11',NULL),(5,5,'3D模型','/models/sifangfeng_jiagu.obj','2025-03-16 14:08:48',NULL),(6,6,'3D模型','/models/daguisiban_jiagu.obj','2025-03-16 14:08:48',NULL),(7,7,'3D模型','/models/ludingguji_jiagu.obj','2025-03-16 14:08:48',NULL),(8,8,'3D模型','/models/zaifenggubi_jiagu.obj','2025-03-16 14:08:48',NULL),(9,9,'3D模型','/models/ruyao_zun.obj','2025-03-16 14:09:04',NULL),(10,10,'3D模型','/models/qinghua_guiguzi.obj','2025-03-16 14:09:04',NULL),(11,11,'3D模型','/models/doucai_jigangbei.obj','2025-03-16 14:09:04',NULL),(12,12,'3D模型','/models/fencai_zhuixinping.obj','2025-03-16 14:09:04',NULL),(13,13,'3D模型','/models/172ku_bihua.obj','2025-03-16 14:09:19',NULL),(14,14,'3D模型','/models/220ku_bihua.obj','2025-03-16 14:09:19',NULL),(15,15,'3D模型','/models/285ku_bihua.obj','2025-03-16 14:09:19',NULL),(16,16,'3D模型','/models/156ku_bihua.obj','2025-03-16 14:09:19',NULL);
/*!40000 ALTER TABLE `artifactmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `artifacttag`
--

DROP TABLE IF EXISTS `artifacttag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `artifacttag` (
  `TagID` int NOT NULL AUTO_INCREMENT,
  `ArtifactID` int DEFAULT NULL,
  `TagName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`TagID`),
  KEY `ArtifactID` (`ArtifactID`),
  CONSTRAINT `artifacttag_ibfk_1` FOREIGN KEY (`ArtifactID`) REFERENCES `artifactinfo` (`ArtifactID`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `artifacttag`
--

LOCK TABLES `artifacttag` WRITE;
/*!40000 ALTER TABLE `artifacttag` DISABLE KEYS */;
INSERT INTO `artifacttag` VALUES (1,1,'商代'),(2,1,'青铜器'),(3,1,'妇好墓'),(4,2,'西周'),(5,2,'青铜器'),(6,2,'大盂鼎'),(7,3,'西周'),(8,3,'青铜器'),(9,3,'虢季子白盘'),(10,4,'春秋'),(11,4,'青铜器'),(12,4,'莲鹤方壶'),(13,5,'商代'),(14,5,'甲骨文'),(15,5,'四方风名'),(16,6,'商代'),(17,6,'甲骨文'),(18,6,'大龟四版'),(19,7,'商代'),(20,7,'甲骨文'),(21,7,'鹿顶骨'),(22,8,'商代'),(23,8,'甲骨文'),(24,8,'宰丰骨匕'),(25,9,'北宋'),(26,9,'瓷器'),(27,9,'汝窑'),(28,10,'元'),(29,10,'瓷器'),(30,10,'青花'),(31,11,'明成化'),(32,11,'瓷器'),(33,11,'斗彩'),(34,12,'清乾隆'),(35,12,'瓷器'),(36,12,'粉彩'),(37,13,'盛唐'),(38,13,'壁画'),(39,13,'观无量寿经变'),(40,14,'初唐'),(41,14,'壁画'),(42,14,'药师七佛图'),(43,15,'西魏'),(44,15,'壁画'),(45,15,'五百强盗成佛图'),(46,16,'晚唐'),(47,16,'壁画'),(48,16,'张议潮统军出行图');
/*!40000 ALTER TABLE `artifacttag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinteraction`
--

DROP TABLE IF EXISTS `userinteraction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userinteraction` (
  `InteractionID` int NOT NULL AUTO_INCREMENT,
  `UserID` int DEFAULT NULL,
  `ArtifactID` int DEFAULT NULL,
  `InteractionType` varchar(50) DEFAULT NULL,
  `InteractionDate` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`InteractionID`),
  KEY `ArtifactID` (`ArtifactID`),
  CONSTRAINT `userinteraction_ibfk_1` FOREIGN KEY (`ArtifactID`) REFERENCES `artifactinfo` (`ArtifactID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinteraction`
--

LOCK TABLES `userinteraction` WRITE;
/*!40000 ALTER TABLE `userinteraction` DISABLE KEYS */;
/*!40000 ALTER TABLE `userinteraction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `versioncontrol`
--

DROP TABLE IF EXISTS `versioncontrol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `versioncontrol` (
  `VersionID` int NOT NULL AUTO_INCREMENT,
  `ArtifactID` int DEFAULT NULL,
  `ModelID` int DEFAULT NULL,
  `VersionType` varchar(50) DEFAULT NULL,
  `VersionDate` datetime DEFAULT CURRENT_TIMESTAMP,
  `Description` text,
  PRIMARY KEY (`VersionID`),
  KEY `ArtifactID` (`ArtifactID`),
  KEY `ModelID` (`ModelID`),
  CONSTRAINT `versioncontrol_ibfk_1` FOREIGN KEY (`ArtifactID`) REFERENCES `artifactinfo` (`ArtifactID`),
  CONSTRAINT `versioncontrol_ibfk_2` FOREIGN KEY (`ModelID`) REFERENCES `artifactmodel` (`ModelID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `versioncontrol`
--

LOCK TABLES `versioncontrol` WRITE;
/*!40000 ALTER TABLE `versioncontrol` DISABLE KEYS */;
/*!40000 ALTER TABLE `versioncontrol` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-16 16:05:15
