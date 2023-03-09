import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="biblioteka"
)

menu_options = {
    1: 'Szukaj ksiazek',
    2: 'Wyswietl historie',
    3: 'Dodaj ksiazke',
    4: 'Dodaj czytelnika',
    5: 'Wyswietl wszystkie ksiazki',
    6: 'Wypozycz ksiazke',
    0: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )

def option1():
     print('Handle option \'Option 1\'')
     name = input("Podaj nazwisko autora: ")
     mycursor = mydb.cursor()
     mycursor.execute("SELECT ksiazki.tytul, autorzy.imie, autorzy.nazwisko FROM ksiazki INNER JOIN autorzy ON ksiazki.id_autor=autorzy.id WHERE autorzy.nazwisko = '" + name + "'")
     myresult = mycursor.fetchall()
     for x in myresult:
      print(x)

def option2():
     print('Handle option \'Option 2\'')
     mycursor = mydb.cursor()
     mycursor.execute("SELECT wypozyczenia.id, czytelnicy.imie, czytelnicy.nazwisko, ksiazki.tytul, data_wypozyczenia, data_oddania FROM ((wypozyczenia LEFT JOIN czytelnicy ON wypozyczenia.id_czytelnik = czytelnicy.id) LEFT JOIN ksiazki ON wypozyczenia.id_ksiazka = ksiazki.id)")
     myresult = mycursor.fetchall()
     for x in myresult:
      print(x)

def option3():
     print('Handle option \'Option 3\'')
     mycursor = mydb.cursor()
     rodzaj = input("Podaj id rodzaj: ")
     tytul = input("Podaj tutul: ")
     autor = input("Podaj id autora: ")
     wydawnictwo = input("Podaj id wydawnictwa: ")

     sql = "INSERT INTO `ksiazki` (`id`, `id_kategoria`, `tytul`, `id_autor`, `id_wydawnictwo`) VALUES (%s, %s, %s, %s, %s)"
     val = ('NULL', rodzaj, tytul, autor, wydawnictwo)
     mycursor.execute(sql, val)
     mydb.commit()


  
def option4():
    print('Handle option \'Option 5\'')
    mycursor = mydb.cursor()
    imie = input("Podaj imie czytelnika: ")
    nazwisko = input("Podaj nazwisko czytelnika: ")
    sql = "INSERT INTO 'czytelnicy' ('id', 'imie', 'nazwisko')) VALUES (%s, %s, %s)"
    val = ('NULL', imie, nazwisko)
    mycursor.execute(sql, val)
    mydb.commit()
   


def option5():
    print('Handle option \'Option 4\'')
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM `ksiazki` ORDER BY `id` ASC")
    myresult = mycursor.fetchall()
    for x in myresult:
     print(x)

def option6():
    print('/handle option \'Option 4\'')
    mycursor = mydb.cursor()
    id_czytelnik = input("Podaj id czytelnika: ")
    id_ksiazka = input("Podaj id ksiazki")
    data_wyp = input("Podaj nazwisko czytelnika: ")
    data_odd = input("podaj date oddania")
    sql = "INSERT INTO 'czytelnicy' ('id', 'id_czytelnik', 'id_ksiazka', 'data_wypozyczenia', 'data_oddania')) VALUES (%s, %s, %s, %s, %s)"
    val = ('NULL', id_czytelnik, id_ksiazka, data_wyp, data_odd)
    mycursor.execute(sql, val)
    mydb.commit()

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
          option5()
        elif option == 6:
          option6()
        elif option == 0:
            print('Goodbye')
            mydb.close()
            exit()
                
        else:
            print('Invalid option. Please enter a number between 1 and 5.')


