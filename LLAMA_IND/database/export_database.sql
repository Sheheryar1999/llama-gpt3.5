-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               11.2.0-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.3.0.6589
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Dumping structure for table law_chatbot.admin_activities
CREATE TABLE IF NOT EXISTS `admin_activities` (
  `activity_id` int(11) NOT NULL AUTO_INCREMENT,
  `admin_user_id` int(11) DEFAULT NULL,
  `action_description` text DEFAULT NULL,
  `action_timestamp` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`activity_id`),
  KEY `admin_user_id` (`admin_user_id`),
  CONSTRAINT `admin_activities_ibfk_1` FOREIGN KEY (`admin_user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.admin_activities: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.answers
CREATE TABLE IF NOT EXISTS `answers` (
  `answer_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `answer_text` text DEFAULT NULL,
  `is_reviewed` tinyint(1) DEFAULT 0,
  `reviewed_by` int(11) DEFAULT NULL,
  `reviewed_timestamp` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`answer_id`),
  KEY `question_id` (`question_id`),
  KEY `reviewed_by` (`reviewed_by`),
  CONSTRAINT `answers_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`),
  CONSTRAINT `answers_ibfk_2` FOREIGN KEY (`reviewed_by`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.answers: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.conversational_record
CREATE TABLE IF NOT EXISTS `conversational_record` (
  `record_id` int(11) NOT NULL AUTO_INCREMENT,
  `professional_user_id` int(11) DEFAULT NULL,
  `registered_client_id` int(11) DEFAULT NULL,
  `conversation_data` text DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`record_id`),
  KEY `professional_user_id` (`professional_user_id`),
  KEY `registered_client_id` (`registered_client_id`),
  CONSTRAINT `conversational_record_ibfk_1` FOREIGN KEY (`professional_user_id`) REFERENCES `users` (`user_id`),
  CONSTRAINT `conversational_record_ibfk_2` FOREIGN KEY (`registered_client_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.conversational_record: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.formula_detection
CREATE TABLE IF NOT EXISTS `formula_detection` (
  `formula_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `detected_formula` text DEFAULT NULL,
  `detection_timestamp` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`formula_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `formula_detection_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.formula_detection: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.prompt_data
CREATE TABLE IF NOT EXISTS `prompt_data` (
  `prompt_id` int(11) NOT NULL AUTO_INCREMENT,
  `professional_user_id` int(11) DEFAULT NULL,
  `prompt_text` text DEFAULT NULL,
  `correct_answer` text DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`prompt_id`),
  KEY `professional_user_id` (`professional_user_id`),
  CONSTRAINT `prompt_data_ibfk_1` FOREIGN KEY (`professional_user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.prompt_data: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.questions
CREATE TABLE IF NOT EXISTS `questions` (
  `question_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `question_text` text DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`question_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.questions: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.training_methods
CREATE TABLE IF NOT EXISTS `training_methods` (
  `method_id` int(11) NOT NULL AUTO_INCREMENT,
  `method_name` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  PRIMARY KEY (`method_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.training_methods: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.training_pool
CREATE TABLE IF NOT EXISTS `training_pool` (
  `training_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `answer_id` int(11) DEFAULT NULL,
  `method_id` int(11) DEFAULT NULL,
  `training_data` text DEFAULT NULL,
  `status` varchar(50) DEFAULT 'pending',
  `reviewed_by` int(11) DEFAULT NULL,
  `reviewed_timestamp` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`training_id`),
  KEY `question_id` (`question_id`),
  KEY `answer_id` (`answer_id`),
  KEY `method_id` (`method_id`),
  KEY `reviewed_by` (`reviewed_by`),
  CONSTRAINT `training_pool_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`),
  CONSTRAINT `training_pool_ibfk_2` FOREIGN KEY (`answer_id`) REFERENCES `answers` (`answer_id`),
  CONSTRAINT `training_pool_ibfk_3` FOREIGN KEY (`method_id`) REFERENCES `training_methods` (`method_id`),
  CONSTRAINT `training_pool_ibfk_4` FOREIGN KEY (`reviewed_by`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.training_pool: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.users
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `role` varchar(50) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.users: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.validation_pool
CREATE TABLE IF NOT EXISTS `validation_pool` (
  `validation_id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) DEFAULT NULL,
  `suggested_answer` text DEFAULT NULL,
  `comments` text DEFAULT NULL,
  `reviewed_by` int(11) DEFAULT NULL,
  `review_timestamp` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`validation_id`),
  KEY `question_id` (`question_id`),
  KEY `reviewed_by` (`reviewed_by`),
  CONSTRAINT `validation_pool_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`question_id`),
  CONSTRAINT `validation_pool_ibfk_2` FOREIGN KEY (`reviewed_by`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.validation_pool: ~0 rows (approximately)

-- Dumping structure for table law_chatbot.video_transcriptions
CREATE TABLE IF NOT EXISTS `video_transcriptions` (
  `transcription_id` int(11) NOT NULL AUTO_INCREMENT,
  `video_url` varchar(255) NOT NULL,
  `transcription_text` text DEFAULT NULL,
  `transcription_status` varchar(50) DEFAULT 'pending',
  `transcribed_by` int(11) DEFAULT NULL,
  `transcription_timestamp` timestamp NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`transcription_id`),
  KEY `transcribed_by` (`transcribed_by`),
  CONSTRAINT `video_transcriptions_ibfk_1` FOREIGN KEY (`transcribed_by`) REFERENCES `users` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- Dumping data for table law_chatbot.video_transcriptions: ~0 rows (approximately)

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
