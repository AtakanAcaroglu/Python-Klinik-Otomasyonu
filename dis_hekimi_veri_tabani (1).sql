-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Anamakine: 127.0.0.1
-- Üretim Zamanı: 20 Ara 2022, 02:47:48
-- Sunucu sürümü: 10.4.25-MariaDB
-- PHP Sürümü: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Veritabanı: `dis_hekimi_veri_tabani`
--

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `doktorlar`
--

CREATE TABLE `doktorlar` (
  `doktor_id` int(11) NOT NULL,
  `doktor_adi` varchar(50) DEFAULT NULL,
  `doktor_soyadi` varchar(50) DEFAULT NULL,
  `doktor_telefon_no` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `doktorlar`
--

INSERT INTO `doktorlar` (`doktor_id`, `doktor_adi`, `doktor_soyadi`, `doktor_telefon_no`) VALUES
(2, 'Doktor1', 'Doktoroğlu', '532-123-11-12'),
(3, 'Doktor2', 'Doktoroğlu', '532-123-11-13'),
(4, 'Doktor3', 'Doktoroğlu', '532-123-11-14'),
(5, 'Doktor4', 'Doktoroğlu', '532-123-11-15'),
(6, 'Doktor5', 'Doktoroğlu', '532-123-11-16'),
(7, 'Doktor6', 'Doktoroğlu', '532-123-11-17'),
(8, 'Doktor7', 'Doktoroğlu', '532-123-11-18'),
(9, 'Doktor8', 'Doktoroğlu', '532-123-11-19'),
(10, 'Doktor9', 'Doktoroğlu', '532-123-11-20'),
(11, 'Doktor10', 'Doktoroğlu', '532-123-11-21'),
(12, 'Doktor10', 'Doktoroğlu', '532-123-11-22'),
(13, 'Doktor12', 'Doktoroğlu', '532-123-11-24');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `doktor_randevu`
--

CREATE TABLE `doktor_randevu` (
  `randevu_id` int(11) DEFAULT NULL,
  `doktor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hastalar`
--

CREATE TABLE `hastalar` (
  `hasta_id` int(11) NOT NULL,
  `hasta_adi` varchar(50) DEFAULT NULL,
  `hasta_soyadi` varchar(50) DEFAULT NULL,
  `hasta_telefon_no` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `hastalar`
--

INSERT INTO `hastalar` (`hasta_id`, `hasta_adi`, `hasta_soyadi`, `hasta_telefon_no`) VALUES
(1, 'Ahmet', 'Mehmet', '532-416-48-92'),
(2, 'Atakan', 'Acaroğlu', '544-522-35-35'),
(3, 'Firuze', 'Kara', '545-111-11-11'),
(4, 'Mehmet', 'Erenli', '532-652-92-95'),
(5, 'Koray', 'Ata', '552-432-69-44'),
(6, 'Yiğit', 'Uçar', '544-535-12-14'),
(9, 'Burak', 'Evrentuğ', '532-532-32-32'),
(10, 'Mehmet', 'Karahaner', '535-321-21-48'),
(11, 'Sinan', 'Yenigün', '545-419-51-82'),
(12, 'Atakan', 'Karaca', '534-418-87-12');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `hasta_randevu`
--

CREATE TABLE `hasta_randevu` (
  `randevu_id` int(11) DEFAULT NULL,
  `hasta_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `islemler`
--

CREATE TABLE `islemler` (
  `islem_id` int(11) NOT NULL,
  `islem_adi` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `islemler`
--

INSERT INTO `islemler` (`islem_id`, `islem_adi`) VALUES
(1, 'Kanal Tedavisi'),
(2, 'Dolgu'),
(3, 'İmplant'),
(4, '20 lik diş çekimi'),
(5, 'Ortodonti'),
(6, 'Diş Taşı Temizliği'),
(7, 'Diş Beyazlatma'),
(8, 'Diş Eti Küretajı'),
(9, 'Zirkonyum Kaplama'),
(10, 'Teleskop Protez');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `islem_randevu`
--

CREATE TABLE `islem_randevu` (
  `randevu_id` int(11) DEFAULT NULL,
  `islem_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `randevu`
--

CREATE TABLE `randevu` (
  `randevu_id` int(11) NOT NULL,
  `hasta_id` int(11) DEFAULT NULL,
  `doktor_id` int(11) DEFAULT NULL,
  `islem_id` int(11) DEFAULT NULL,
  `islem_tarihi` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `randevu`
--

INSERT INTO `randevu` (`randevu_id`, `hasta_id`, `doktor_id`, `islem_id`, `islem_tarihi`) VALUES
(1, 1, 4, 1, '24-09-2022'),
(2, 1, 2, 2, '12-10-2022'),
(3, 2, 2, 1, '32-02-2022');

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `stok`
--

CREATE TABLE `stok` (
  `malzeme_id` int(11) NOT NULL,
  `malzeme_ismi` varchar(50) DEFAULT NULL,
  `malzeme_adedi` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Tablo döküm verisi `stok`
--

INSERT INTO `stok` (`malzeme_id`, `malzeme_ismi`, `malzeme_adedi`) VALUES
(1, 'Implant', 88),
(2, 'Dolgu', 97),
(3, 'Frez', 96);

-- --------------------------------------------------------

--
-- Tablo için tablo yapısı `stok_islem`
--

CREATE TABLE `stok_islem` (
  `malzeme_id` int(11) DEFAULT NULL,
  `islem_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dökümü yapılmış tablolar için indeksler
--

--
-- Tablo için indeksler `doktorlar`
--
ALTER TABLE `doktorlar`
  ADD PRIMARY KEY (`doktor_id`);

--
-- Tablo için indeksler `doktor_randevu`
--
ALTER TABLE `doktor_randevu`
  ADD KEY `randevu_id` (`randevu_id`),
  ADD KEY `doktor_id` (`doktor_id`);

--
-- Tablo için indeksler `hastalar`
--
ALTER TABLE `hastalar`
  ADD PRIMARY KEY (`hasta_id`);

--
-- Tablo için indeksler `hasta_randevu`
--
ALTER TABLE `hasta_randevu`
  ADD KEY `randevu_id` (`randevu_id`),
  ADD KEY `hasta_id` (`hasta_id`);

--
-- Tablo için indeksler `islemler`
--
ALTER TABLE `islemler`
  ADD PRIMARY KEY (`islem_id`);

--
-- Tablo için indeksler `islem_randevu`
--
ALTER TABLE `islem_randevu`
  ADD KEY `randevu_id` (`randevu_id`),
  ADD KEY `islem_id` (`islem_id`);

--
-- Tablo için indeksler `randevu`
--
ALTER TABLE `randevu`
  ADD PRIMARY KEY (`randevu_id`),
  ADD KEY `hasta_id` (`hasta_id`),
  ADD KEY `doktor_id` (`doktor_id`),
  ADD KEY `islem_id` (`islem_id`);

--
-- Tablo için indeksler `stok`
--
ALTER TABLE `stok`
  ADD PRIMARY KEY (`malzeme_id`);

--
-- Tablo için indeksler `stok_islem`
--
ALTER TABLE `stok_islem`
  ADD KEY `malzeme_id` (`malzeme_id`),
  ADD KEY `islem_id` (`islem_id`);

--
-- Dökümü yapılmış tablolar için AUTO_INCREMENT değeri
--

--
-- Tablo için AUTO_INCREMENT değeri `doktorlar`
--
ALTER TABLE `doktorlar`
  MODIFY `doktor_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- Tablo için AUTO_INCREMENT değeri `hastalar`
--
ALTER TABLE `hastalar`
  MODIFY `hasta_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- Tablo için AUTO_INCREMENT değeri `islemler`
--
ALTER TABLE `islemler`
  MODIFY `islem_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Tablo için AUTO_INCREMENT değeri `randevu`
--
ALTER TABLE `randevu`
  MODIFY `randevu_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Dökümü yapılmış tablolar için kısıtlamalar
--

--
-- Tablo kısıtlamaları `doktor_randevu`
--
ALTER TABLE `doktor_randevu`
  ADD CONSTRAINT `doktor_randevu_ibfk_1` FOREIGN KEY (`randevu_id`) REFERENCES `randevu` (`randevu_id`),
  ADD CONSTRAINT `doktor_randevu_ibfk_2` FOREIGN KEY (`doktor_id`) REFERENCES `doktorlar` (`doktor_id`);

--
-- Tablo kısıtlamaları `hasta_randevu`
--
ALTER TABLE `hasta_randevu`
  ADD CONSTRAINT `hasta_randevu_ibfk_1` FOREIGN KEY (`randevu_id`) REFERENCES `randevu` (`randevu_id`),
  ADD CONSTRAINT `hasta_randevu_ibfk_2` FOREIGN KEY (`hasta_id`) REFERENCES `hastalar` (`hasta_id`);

--
-- Tablo kısıtlamaları `islem_randevu`
--
ALTER TABLE `islem_randevu`
  ADD CONSTRAINT `islem_randevu_ibfk_1` FOREIGN KEY (`randevu_id`) REFERENCES `randevu` (`randevu_id`),
  ADD CONSTRAINT `islem_randevu_ibfk_2` FOREIGN KEY (`islem_id`) REFERENCES `islemler` (`islem_id`);

--
-- Tablo kısıtlamaları `randevu`
--
ALTER TABLE `randevu`
  ADD CONSTRAINT `randevu_ibfk_1` FOREIGN KEY (`hasta_id`) REFERENCES `hastalar` (`hasta_id`),
  ADD CONSTRAINT `randevu_ibfk_2` FOREIGN KEY (`doktor_id`) REFERENCES `doktorlar` (`doktor_id`),
  ADD CONSTRAINT `randevu_ibfk_3` FOREIGN KEY (`islem_id`) REFERENCES `islemler` (`islem_id`);

--
-- Tablo kısıtlamaları `stok_islem`
--
ALTER TABLE `stok_islem`
  ADD CONSTRAINT `stok_islem_ibfk_1` FOREIGN KEY (`malzeme_id`) REFERENCES `stok` (`malzeme_id`),
  ADD CONSTRAINT `stok_islem_ibfk_2` FOREIGN KEY (`islem_id`) REFERENCES `islemler` (`islem_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
