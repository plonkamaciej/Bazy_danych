# Bazy_danych

## Wpyożyczalnia książek 
### [MySQL + Python]

Uzyta baza danych:

![alt text](https://github.com/plonkamaciej/Bazy_danych/blob/main/bazy.png?raw=true)

Dostepne funkcje:

   1. 'Szukaj ksiazek',
   2. 'Wyswietl historie',
   3. 'Dodaj ksiazke',
   4. 'Dodaj czytelnika',    
   5. 'Wyswietl wszystkie ksiazki',
   6. 'Wyswietl czytelnikow',
   7. 'Wypozycz ksiazke',
   0. 'Exit',
  
   * Szukaj książek - "SELECT `ksiazki.tytul`, `autorzy.imie`, `autorzy.nazwisko` FROM `ksiazki` INNER JOIN `autorzy` ON `ksiazki.id_autor` = `autorzy.id` WHERE `autorzy.nazwisko` = [nazwisko]" - wyszukiwanie ksiazek po nazwisku autora
   
   * Wyswietl historie - "SELECT `wypozyczenia.id`, `czytelnicy.imie`, `czytelnicy.nazwisko`, `ksiazki.tytul`, `data_wypozyczenia`, `data_oddania` FROM ((`wypozyczenia` LEFT JOIN `czytelnicy` ON `wypozyczenia.id_czytelnik` = `czytelnicy.id`) LEFT JOIN `ksiazki` ON `wypozyczenia.id_ksiazka` = `ksiazki.id`)" - wyswietlamy historie wypozycznia książek
   
   * Dodaj książkę - "INSERT INTO `ksiazki` (`id`, `id_kategoria`, `tytul`, `id_autor`, `id_wydawnictwo`)" - dodanie książki do listy ksiażek w wypożyczalni
   
   * Dodaj czytelnika - INSERT INTO 'czytelnicy' (`id`, `imie`, `nazwisko`)) - dodaj osobe do listy czytelnikow
   
   * Wyswietl wszystkie ksiazki - "SELECT * FROM `ksiazki` ORDER BY `id` ASC"
   
   * Wyswietl czytelnikow' - "SELECT * FROM `czytelnicy`"
   
   * Wypożycz książkę - "INSERT INTO 'czytelnicy' (`id`, `id_czytelnik`, `id_ksiazka`, `data_wypozyczenia`, `data_oddania`))
   
   * Exit - zakoncz program, wyjdź z bazy danych
