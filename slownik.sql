-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 27 Sty 2021, 10:44
-- Wersja serwera: 10.4.11-MariaDB
-- Wersja PHP: 7.2.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `slownik`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `akceptacja`
--

CREATE TABLE `akceptacja` (
  `id` int(11) NOT NULL,
  `tytul` varchar(300) NOT NULL,
  `tresc` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `akceptacja`
--

INSERT INTO `akceptacja` (`id`, `tytul`, `tresc`) VALUES
(11, 'QAbstractExtensionManager', 'The QAbstractExtensionManager class provides an interface for extension managers in Qt Designer.'),
(12, 'QAbstractEventDispatcher ', 'The QAbstractEventDispatcher class provides an interface to manage Qt\'s event queue.'),
(13, 'QAbstractDataProxy ', 'The QAbstractDataProxy class is a base class for all data visualization data proxies'),
(14, 'QAbstractButton', 'The QAbstractButton class is the abstract base class of button widgets, providing functionality common to buttons. '),
(15, 'QColorDialog', 'The QColorDialog class provides a dialog widget for specifying colors.'),
(16, 'QColormap', 'The QColormap class maps device independent QColors to device dependent pixel values. '),
(17, 'QColorMask', 'Allows specifying which color components should be written to the currently bound frame buffer.');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pojecia`
--

CREATE TABLE `pojecia` (
  `id` int(11) NOT NULL,
  `tytul` varchar(200) NOT NULL,
  `tresc` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `pojecia`
--

INSERT INTO `pojecia` (`id`, `tytul`, `tresc`) VALUES
(22, 'QMessageBox', 'The QMessageBox class provides a modal dialog for informing the user or for asking the user a question and receiving an answer. More...\r\n\r\n'),
(23, 'QMessageLogContext', 'The QMessageLogContext class provides additional information about a log message. '),
(24, 'QMessageAuthenticationCode', 'The QMessageAuthenticationCode class provides a way to generate hash-based message authentication codes.'),
(25, 'QMenu', 'The QMenu class provides a menu widget for use in menu bars, context menus, and other popup menus. '),
(26, 'QMessageLogger ', 'The QMessageLogger class generates log messages. '),
(27, 'QMetaClassInfo', 'The QMetaClassInfo class provides additional information about a class.'),
(28, 'QMetaDataReaderControl ', 'The QMetaDataReaderControl class provides read access to the meta-data of a QMediaService\'s media. '),
(29, 'QMetaEnum', 'The QMetaEnum class provides meta-data about an enumerator. '),
(30, 'QMetalRoughMaterial', 'The QMetalRoughMaterial provides a default implementation of PBR lighting'),
(31, 'QMetaMethod', 'he QMetaMethod class provides meta-data about a member function'),
(32, 'QMetaObject Struct', 'The QMetaObject class contains meta-information about Qt objects.'),
(33, 'QMetaProperty', 'The QMetaProperty class provides meta-data about a property.'),
(34, 'QMetaType', 'The QMetaType class manages named types in the meta-object system.'),
(35, 'QMetaType', 'The QMetaType class manages named types in the meta-object system. '),
(36, 'QMilankovicCalendar', 'The QMilankovicCalendar class provides Milanković calendar system implementation.'),
(37, 'QMimeDatabase', 'The QMimeDatabase class maintains a database of MIME types.'),
(38, 'QMimeType', 'The QMimeType class describes types of file or data, represented by a MIME type string'),
(39, 'QModbusClient', 'The QModbusClient class is the interface to send Modbus requests'),
(40, 'QCollator', 'The QCollator class compares strings according to a localized collation algorithm.'),
(41, 'QCollatorSortKey', 'The QCollatorSortKey class can be used to speed up string collation. '),
(42, 'QColor', 'The QColor class provides colors based on RGB, HSV or CMYK values');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `uzytkownicy`
--

CREATE TABLE `uzytkownicy` (
  `id` int(11) NOT NULL,
  `nazwa` varchar(250) NOT NULL,
  `haslo` varchar(250) NOT NULL,
  `uprawnienia` int(11) NOT NULL,
  `email` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `uzytkownicy`
--

INSERT INTO `uzytkownicy` (`id`, `nazwa`, `haslo`, `uprawnienia`, `email`) VALUES
(2, 'admin', '21232f297a57a5a743894a0e4a801fc3', 2, ''),
(4, 'login', '534993fc4955eb98a89a0beb4e8a92e2', 1, 'elo@gmail.com');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `akceptacja`
--
ALTER TABLE `akceptacja`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `pojecia`
--
ALTER TABLE `pojecia`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `uzytkownicy`
--
ALTER TABLE `uzytkownicy`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT dla tabeli `akceptacja`
--
ALTER TABLE `akceptacja`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT dla tabeli `pojecia`
--
ALTER TABLE `pojecia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT dla tabeli `uzytkownicy`
--
ALTER TABLE `uzytkownicy`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
