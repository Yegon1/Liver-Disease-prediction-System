-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 14, 2024 at 11:31 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `abc_hospital`
--

-- --------------------------------------------------------

--
-- Table structure for table `ld_patients`
--

CREATE TABLE `ld_patients` (
  `id` int(20) NOT NULL,
  `Full_names` varchar(255) NOT NULL,
  `age` varchar(3) NOT NULL,
  `Gender` varchar(100) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Contact` int(10) NOT NULL,
  `Status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `ld_patients`
--

INSERT INTO `ld_patients` (`id`, `Full_names`, `age`, `Gender`, `Address`, `Contact`, `Status`) VALUES
(1, 'Yegon shadrack', '16', 'male', '0100, Nairobi', 715006068, 'Positive'),
(2, 'daniel mokaya', '4', 'male', '0100, Nairobi', 715006068, 'Negative'),
(3, 'Diana Nzoika', '8', 'male', '03033,kisii', 750144532, 'Positive');

-- --------------------------------------------------------

--
-- Table structure for table `patients`
--

CREATE TABLE `patients` (
  `id` int(20) NOT NULL,
  `Full_names` varchar(255) NOT NULL,
  `Gender` varchar(5) NOT NULL,
  `DOB` date NOT NULL,
  `Age` int(3) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Phone_number` int(10) NOT NULL,
  `Next_of_kin` varchar(255) NOT NULL,
  `Relationship` varchar(20) NOT NULL,
  `Contact` int(10) NOT NULL,
  `Insurance_scheme` varchar(100) NOT NULL,
  `Insurance_number` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patients`
--

INSERT INTO `patients` (`id`, `Full_names`, `Gender`, `DOB`, `Age`, `Address`, `Phone_number`, `Next_of_kin`, `Relationship`, `Contact`, `Insurance_scheme`, `Insurance_number`) VALUES
(1, 'Yegon shadrack', 'male', '2007-07-12', 16, '0100, Nairobi', 715006068, 'peter', 'guardian', 715006068, 'madison', 'ac202312345'),
(2, 'daniel mokaya', 'male', '2019-09-10', 4, '0100, Nairobi', 715006068, 'peter', 'guardian', 715006068, 'madison', 'ac202312345'),
(3, 'Diana Nzoika', 'male', '2015-11-04', 8, '03033,kisii', 750144532, 'meshack nzoika', 'Father', 715006068, 'NHIF', 'nhif203234'),
(4, 'joseph irungu', 'male', '1966-10-04', 57, '3020, Nyeri', 745678098, 'daniel irungu', 'Others', 715006068, 'NHIF', 'nhif2000012');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `Full_names` varchar(255) NOT NULL,
  `Username` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `Full_names`, `Username`, `Email`, `Password`) VALUES
(1, 'yegon shadrack', 'Yegon', 'cheruiyotshadrack800@gmail.com', '12345'),
(2, 'mike kebenei', 'kebenei', 'kebeneimike@gmail.com', '123456'),
(4, 'miano betty', 'miano', 'miano@gmail.com', '12345678');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `ld_patients`
--
ALTER TABLE `ld_patients`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patients`
--
ALTER TABLE `patients`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `ld_patients`
--
ALTER TABLE `ld_patients`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `patients`
--
ALTER TABLE `patients`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
