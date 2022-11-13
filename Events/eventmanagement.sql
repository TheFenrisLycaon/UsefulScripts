SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
DROP TABLE IF EXISTS `customer`;
CREATE TABLE IF NOT EXISTS `customer` (
  `cust_no` int NOT NULL,
  `cust_name` varchar(20) NOT NULL,
  `event_book` varchar(20) NOT NULL,
  `payment` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `customer` (`cust_no`, `cust_name`, `event_book`, `payment`) VALUES
(1, 'Tannu', 'Birthday', 5000),
(2, 'Shefali', 'Sports  Event', 4789);
DROP TABLE IF EXISTS `event`;
CREATE TABLE IF NOT EXISTS `event` (
  `event_name` varchar(20) NOT NULL,
  `event_type` varchar(20) NOT NULL,
  `event_location` varchar(20) NOT NULL,
  `event_theme` varchar(20) NOT NULL,
  `start_time` varchar(20) NOT NULL,
  `interval` varchar(20) NOT NULL,
  `end_time` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `event` (`event_name`, `event_type`, `event_location`, `event_theme`, `start_time`, `interval`, `end_time`) VALUES
('Birthday', 'Public', 'Kanpur', 'Bollywood', '6 PM', '10 minutes', '10 PM'),
('Wedding', 'Private', 'Chandigarh', 'Bollywood', '7 PM', '30 minutes', '11 PM'),
('Sports Event', 'Professional', 'Mumbai', 'Sports', '10 AM', '60 minutes', '6 PM');
DROP TABLE IF EXISTS `event_equipments`;
CREATE TABLE IF NOT EXISTS `event_equipments` (
  `equipment_name` varchar(20) NOT NULL,
  `equipment_type` varchar(20) NOT NULL,
  `availbility` varchar(20) NOT NULL,
  `cost` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `event_equipments` (`equipment_name`, `equipment_type`, `availbility`, `cost`) VALUES
('Disco Balls', 'Lighting', 'Yes', 300),
('Guitar', 'Musical', 'No', 1600),
('Table Tennis Racket', 'Sports', 'Yes', 640),
('Basket Ball', 'Sports', 'No', 897);
COMMIT;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
