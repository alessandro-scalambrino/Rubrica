-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Feb 11, 2024 alle 18:21
-- Versione del server: 10.4.25-MariaDB
-- Versione PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `rubrica`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `contatti`
--

CREATE TABLE `contatti` (
  `nome` varchar(50) NOT NULL,
  `cognome` varchar(50) NOT NULL,
  `eta` varchar(3) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `creatore` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `contatti`
--

INSERT INTO `contatti` (`nome`, `cognome`, `eta`, `telefono`, `creatore`) VALUES
('Mario', 'Rossi', '30', '3391234567', 'ale.scala@gmail.com'),
('Luigi', 'Bianchi', '25', '3402345678', 'ale.scala@gmail.com'),
('Giulia', 'Verdi', '35', '3473456789', 'ale.scala@gmail.com'),
('Marco', 'Russo', '40', '3334567890', 'ale.scala@gmail.com'),
('Laura', 'Ferrari', '28', '3395678901', 'ale.scala@gmail.com'),
('Paolo', 'Esposito', '33', '3406789012', 'ale.scala@gmail.com'),
('Chiara', 'Gallo', '26', '3477890123', 'ale.scala@gmail.com'),
('Francesca', 'Galli', '32', '3399012345', 'ale.scala@gmail.com'),
('Giovanni', 'Mancini', '31', '3400123456', 'ale.scala@gmail.com'),
('Simona', 'Greco', '27', '3471234567', 'ale.scala@gmail.com'),
('Matteo', 'Costa', '34', '3332345678', 'ale.scala@gmail.com'),
('Eleonora', 'Giordano', '36', '3393456789', 'ale.scala@gmail.com'),
('Andrea', 'Moretti', '38', '340456789', 'ale.scala@gmail.com'),
('Sara', 'Barbieri', '39', '3475678901', 'ale.scala@gmail.com'),
('Davide', 'Fontana', '37', '3336789012', 'ale.scala@gmail.com'),
('Martina', 'Santoro', '29', '3397890123', 'ale.scala@gmail.com'),
('Marco', 'Mariani', '28', '3408901234', 'ale.scala@gmail.com'),
('Elisa', 'Rinaldi', '31', '3479012345', 'ale.scala@gmail.com'),
('Nicola', 'Caruso', '30', '3330123456', 'ale.scala@gmail.com'),
('Federica', 'Ferrara', '32', '3391234567', 'ale.scala@gmail.com'),
('Gabriele', 'Serra', '35', '3402345678', 'ale.scala@gmail.com'),
('Valentina', 'Marini', '33', '3473456789', 'ale.scala@gmail.com'),
('Antonio', 'Fabbri', '34', '3334567890', 'ale.scala@gmail.com'),
('Roberto', 'Leone', '38', '3406789012', 'ale.scala@gmail.com'),
('Elena', 'Rizzi', '39', '3477890123', 'ale.scala@gmail.com'),
('Filippo', 'Lombardi', '37', '3338901234', 'ale.scala@gmail.com'),
('Cristina', 'Rossetti', '29', '3399012345', 'ale.scala@gmail.com'),
('Giovanni', 'Rossi', '35', '3481234567', 'ale.scala@gmail.com'),
('Anna', 'Bianchi', '28', '3402345678', 'ale.scala@gmail.com'),
('Roberto', 'Verdi', '45', '3473456789', 'ale.scala@gmail.com'),
('Francesca', 'Russo', '30', '3334567890', 'ale.scala@gmail.com'),
('Simona', 'Ferrari', '40', '3395678901', 'ale.scala@gmail.com'),
('Marco', 'Esposito', '32', '3406789012', 'ale.scala@gmail.com'),
('Laura', 'Gallo', '27', '3477890123', 'ale.scala@gmail.com'),
('Luigi', 'Galli', '36', '3399012345', 'ale.scala@gmail.com'),
('Sara', 'Mancini', '31', '3400123456', 'ale.scala@gmail.com'),
('Paolo', 'Greco', '33', '3471234567', 'ale.scala@gmail.com'),
('Alessandra', 'Costa', '29', '3332345678', 'ale.scala@gmail.com'),
('Davide', 'Giordano', '38', '3393456789', 'ale.scala@gmail.com'),
('Elisa', 'Moretti', '42', '3404567890', 'ale.scala@gmail.com'),
('Marco', 'Barbieri', '25', '3475678901', 'ale.scala@gmail.com'),
('Martina', 'Fontana', '34', '3336789012', 'ale.scala@gmail.com'),
('Giuseppe', 'Santoro', '39', '3397890123', 'ale.scala@gmail.com'),
('Chiara', 'Mariani', '26', '3408901234', 'ale.scala@gmail.com'),
('Andrea', 'Rinaldi', '37', '3479012345', 'ale.scala@gmail.com'),
('Valentina', 'Caruso', '41', '3330123456', 'ale.scala@gmail.com'),
('Federico', 'Ferrara', '29', '3391234567', 'ale.scala@gmail.com'),
('Elena', 'Serra', '43', '3402345678', 'ale.scala@gmail.com'),
('Gabriele', 'Marini', '38', '3473456789', 'ale.scala@gmail.com'),
('Cristina', 'Fabbri', '30', '3334567890', 'ale.scala@gmail.com'),
('Nicola', 'Leone', '44', '3406789012', 'ale.scala@gmail.com'),
('Roberta', 'Rizzi', '28', '3477890123', 'ale.scala@gmail.com'),
('Filippo', 'Lombardi', '37', '3338901234', 'ale.scala@gmail.com'),
('Silvia', 'Rossetti', '32', '3399012345', 'ale.scala@gmail.com'),
('Luca', 'Ferraro', '35', '3401234567', 'ale.scala@gmail.com'),
('Martina', 'Marchetti', '29', '3472345678', 'ale.scala@gmail.com'),
('Riccardo', 'Villa', '39', '3333456789', 'ale.scala@gmail.com'),
('Elena', 'Gatti', '33', '3404567890', 'ale.scala@gmail.com'),
('Daniele', 'Ferri', '42', '3475678901', 'ale.scala@gmail.com'),
('Roberta', 'Marconi', '31', '3336789012', 'ale.scala@gmail.com'),
('Fabio', 'Mazza', '45', '3397890123', 'ale.scala@gmail.com'),
('Sara', 'Bruno', '27', '3408901234', 'ale.scala@gmail.com'),
('Andrea', 'Piras', '36', '3479012345', 'ale.scala@gmail.com'),
('Jessica', 'Orlando', '40', '3330123456', 'ale.scala@gmail.com'),
('Luigi', 'Pellegrini', '28', '3391234567', 'ale.scala@gmail.com'),
('Elisa', 'Battaglia', '37', '3402345678', 'ale.scala@gmail.com'),
('Nicola', 'Pagano', '44', '3473456789', 'ale.scala@gmail.com'),
('Silvia', 'Mancini', '32', '3334567890', 'ale.scala@gmail.com'),
('Davide', 'Giuliani', '41', '3406789012', 'ale.scala@gmail.com'),
('Federica', 'Martini', '29', '3477890123', 'ale.scala@gmail.com'),
('Giacomo', 'Ruggiero', '39', '3338901234', 'ale.scala@gmail.com'),
('Giulia', 'Rossetti', '30', '3399012345', 'ale.scala@gmail.com');

-- --------------------------------------------------------

--
-- Struttura della tabella `utente`
--

CREATE TABLE `utente` (
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `utente`
--

INSERT INTO `utente` (`email`, `password`) VALUES
('a', 'a'),
('ale.scala@gmail.com', '6caratteri');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `contatti`
--
ALTER TABLE `contatti`
  ADD KEY `creatore_fk` (`creatore`);

--
-- Indici per le tabelle `utente`
--
ALTER TABLE `utente`
  ADD PRIMARY KEY (`email`);

--
-- Limiti per le tabelle scaricate
--

--
-- Limiti per la tabella `contatti`
--
ALTER TABLE `contatti`
  ADD CONSTRAINT `creatore_fk` FOREIGN KEY (`creatore`) REFERENCES `utente` (`email`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
