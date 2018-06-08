#       __                 _   _____ _   _                 
#      /__\ ___  ___ _   _| | /__   (_) (_)_______ _ __    
#     / \/// _ \/ __| | | | |   / /\/ | | |_  / _ \  _ \   
#    / _  \  __/\__ \ |_| | |  / /  | |_| |/ /  __/ | | |  
#    \/ \_/\___||___/\__,_|_|  \/    \__,_/___\___|_| |_|  
#

# Bu program Python 3X sürümü ile hazırlanmıştır.
# Oluşturulma Tarhi: 30.05.2018 / Resul TÜZEN

import os
import sqlite3 as sql
import time

clean = lambda: os.system("cls")


def Homepage():
    
    clean()
    
    print('''

  MyLibrary'e hoşgeldin! \n\n
 
  1) Kitap Ekle
  2) Kitap Listele
  3) Kitap Bul
  4) Kitap Sil
  5) Kitap Düzenle
  6) Çıkış
    
    ''')

    choose = int(input(" \n  Lütfen bir seçenek seçiniz: "))

    if(choose == 1): AddBook()
    elif(choose == 2): ListBook()
    elif(choose == 3): FindBook()
    elif(choose == 4): DeleteBook()
    elif(choose == 5): EditBook()
    elif(choose == 6):
        
        clean()
        print("\n\n  Teşekkürler :)")
        time.sleep(2) 
        exit
        
    else: print("\n  Üzgünüm, böyle bir seçenek yok.\n")
        


def Open():
    db = sql.connect("Kitaplar.db")
    command = db.cursor()
    command.execute('''
    
    CREATE TABLE IF NOT EXISTS BookDatabase(
    BarcodeNumber CHAR(40) PRIMARY KEY NOT NULL,
    BookName CHAR(40) NOT NULL,
    AuthorName TEXT NOT NULL,
    Publisher CHAR(40) NOT NULL,
    BookType TEXT NOT NULL,
    PageNumber CHAR(5))
    
    ''')


def AddBook():
    
    db = sql.connect("Kitaplar.db")
    command = db.cursor()

    clean()
    
    barcode = input("\n  Kitabın barkod numarasını giriniz: ")
    bookName = input("  Kitabın ismini giriniz: ")
    authorName = input("  Kitabın yazar ismini giriniz: ")
    publisher = input("  Kitabın yayınevi ismini giriniz: ")
    bookType = input("  Kitabın türünü giriniz: ")
    pageNumber = int(input("  Kitabın sayfa numarasını giriniz: "))
    
    information = []
    information.append(barcode)
    information.append(bookName)
    information.append(authorName)
    information.append(publisher)
    information.append(bookType)
    information.append(pageNumber)

    command.execute('''
    INSERT INTO BookDatabase(BarcodeNumber, BookName, AuthorName, Publisher, BookType, PageNumber)
    VALUES (?, ?, ?, ?, ?, ?) ''', information)

    db.commit()
    db.close()

    clean()
    print("\n  Kitap bilgileri başarıyla eklendi.")
    time.sleep(2)
    Homepage()

def ListBook():
    
    db = sql.connect("Kitaplar.db")
    command = db.cursor()

    command.execute("SELECT * FROM BookDatabase")
    read = command.fetchall()

    clean()
    
    print("\n\n  Sonuçlar\n\n")
    
    count = 0
    
    for line in read:

        barcode, bookName, authorName, publisher, bookType, pageNumber = line
        
        print("  Barkod Numarası:", barcode)
        print("  Kitap İsmi:", bookName)
        print("  Yazar İsmi:", authorName)
        print("  Yayınevi:", publisher)
        print("  Kitap Türü:", bookType)
        print("  Sayfa Sayısı:", pageNumber)
        print("\n")

        count = count + 1
         
    print("  Toplam", count , "adet kitap var.")

    condition = input("\n\n  Ana menüye dönmek ister misin? (E / H): ")

    if(condition == "E" or condition == "e"):

        Homepage()

    elif(condition == "H" or condition == "h"):

        exit
    
def FindBook():
    db = sql.connect("Kitaplar.db")
    command = db.cursor()

    clean()

    find = input("\n\n  Aranılacak olan kitabın adını giriniz: ")

    command.execute("SELECT * FROM BookDatabase WHERE BookName = ?", (find, ))
    result = command.fetchall()

    clean()
    
    print("\n\n  Sonuçlar\n\n")

    count = 0
        
    for line in result:

        barcode, bookName, authorName, publisher, bookType, pageNumber = line

        print("  Barkod Numarası:", barcode)
        print("  Kitap İsmi:", bookName)
        print("  Yazar İsmi:", authorName)
        print("  Yayınevi:", publisher)
        print("  Kitap Türü:", bookType)
        print("  Sayfa Sayısı:", pageNumber)
        print("\n")
        
        count = count + 1

    if(count == 0):

        clean()
        print("  Üzgünüm, aradığın bilgiye göre bir kitap bulamadım.")
        
    else:
        
        print("  Toplam", count , "adet kitap bulundu.")
        

    condition = input("\n\n  Ana menüye dönmek ister misin? (E / H): ")

    if(condition == "E" or condition == "e"):

        Homepage()

    elif(condition == "H" or condition == "h"):

        exit
    
def DeleteBook():

    db = sql.connect("Kitaplar.db")
    command = db.cursor()

    clean()
    
    delete = input("\n\n  Silinecek olan kitabın adını giriniz: ")

    command.execute("SELECT * FROM BookDatabase WHERE BookName = ?",(delete,))
    result = command.fetchall()

    clean()
    
    print("\n\n  Sonuçlar\n\n")

    count = 0
    
    for line in result:

        barcode, bookName, authorName, publisher, bookType, pageNumber = line

        print("  Barkod Numarası:", barcode)
        print("  Kitap İsmi:", bookName)
        print("  Yazar İsmi:", authorName)
        print("  Yayınevi:", publisher)
        print("  Kitap Türü:", bookType)
        print("  Sayfa Sayısı:", pageNumber)
        print("\n")

        count = count + 1

    if(count == 0):
        
        clean()
        print("\n\n  Üzgünüm, aradığın bilgiye göre bir kitap bulamadım.")

    else:
        
        condition = input("\n  Yukarıdaki bilgileri silmek istediğine emin misin? (E / H): ")

        if(condition == "E" or condition == "e"):
        
            command.execute("DELETE FROM BookDatabase WHERE BarcodeNumber = ?",(delete,))
            db.commit()
            db.close()
            
            clean()
            print("\n\n  '"+ delete +"' barkod numaralı kitap başarıyla silindi.\n")
            
        elif(condition == "H" or condition == "h"):

            clean()
            print("\n\n  Silme işlemi iptal edildi.")

    time.sleep(2)
    Homepage()

def EditBook():

    db = sql.connect("Kitaplar.db")
    command = db.cursor()

    clean()

    edit = input("\n\n  Düzenlenecek olan kitabın adını giriniz: ")
    
    command.execute("SELECT * FROM BookDatabase WHERE BookName = ?",(edit,))
    result = command.fetchall()

    clean()
    
    print("\n\n  Sonuçlar\n\n")

    count = 0

    for line in result:

        barcode, bookName, authorName, publisher, bookType, pageNumber = line

        print("  Barkod Numarası:", barcode)
        print("  Kitap İsmi:", bookName)
        print("  Yazar İsmi:", authorName)
        print("  Yayınevi:", publisher)
        print("  Kitap Türü:", bookType)
        print("  Sayfa Sayısı:", pageNumber)
        print("\n")
        
        count = count + 1

    if(count == 0):

        clean()
        print("\n\n  Üzgünüm, aradığın bilgiye göre bir kitap bulamadım.")
        time.sleep(2)
        
    else:
        
        print("\n  Aramanıza uygun toplam", count , "adet kitap bulundu.")

        edit = input("\n\n  Yukarıdaki sonuçlardan düzenlemek istediğin kitabın barkod numarasını giriniz: ")

        command.execute("SELECT * FROM BookDatabase WHERE BarcodeNumber = ?",(edit,))
        result = command.fetchall()

        clean()
        
        print("\n\n  Sonuçlar\n\n")

        for line in result:

            barcode, bookName, authorName, publisher, bookType, pageNumber = line

            print("  Barkod Numarası:", barcode)
            print("  Kitap İsmi:", bookName)
            print("  Yazar İsmi:", authorName)
            print("  Yayınevi:", publisher)
            print("  Kitap Türü:", bookType)
            print("  Sayfa Sayısı:", pageNumber)
            print("\n")

        condition = input("\n  Yukarıdaki bilgileri düzenlemek istediğine emin misin? (E / H): ")

        if(condition == "E" or condition == "e"):
            
            clean()
            
            NewBarcode = input("\n\n  Yeni kitabın barkod numarasını giriniz: ")
            NewBookName = input("  Yeni kitabın ismini giriniz: ")
            NewAuthorName = input("  Yeni kitabın yazar ismini giriniz: ")
            NewPublisher = input("  Yeni kitabın yayınevi ismini giriniz: ")
            NewBookType = input("  Yeni kitabın türünü giriniz: ")
            NewPageNumber = int(input("  Yeni kitabın sayfa numarasını giriniz: "))
            
            
            command.execute("UPDATE BookDatabase SET BarcodeNumber = ? , BookName = ? , AuthorName = ? , Publisher = ? , BookType = ? , PageNumber = ? WHERE BarcodeNumber = ?",(NewBarcode, NewBookName, NewAuthorName, NewPublisher, NewBookType, NewPageNumber, edit,))

            db.commit()
            db.close()

            clean()
            print("\n  Kitap bilgileri başarıyla güncellendi.")

            time.sleep(2)

        elif(condition == "H" or condition == "h"):

            print("\n\n  Üzgünüm, aradığın bilgiye göre bir kitap bulamadım.")
            time.sleep(2)
    
    Homepage()

Open()
Homepage()
