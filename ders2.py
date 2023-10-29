# isimler = ["Kadir" ,"Ahmet"  , "Mert"   , "Muhammed"   ,"Yusuf"   , "Atakan" ]
# yas = [26,30,25,24,31,21]

# *sor() ile küçükten büyüğe sıralama yaparız.
# isimler.sort()
# print(isimler)
# yas.sort() 
# print(yas)

# *sort(reverse = True) ile küçükten büyüğe sıralama yaparız
# isimler.sort(reverse=True)
# print(isimler)
# yas.sort(reverse=True)
# print(yas)

# *append() ile listenin sonuna eleman eklenir
# isimler.append("emre")
# print(isimler)
# yas.append(50)
# yas.sort(reverse=True)
# print(yas)

# *İnsert() ile listelere belirtilen bir indexe eleman ekler.

# isimler.insert(4,"Mehmet")
# print(isimler)

# *Remove ile istediğimzi elemanı sileriz

# isimler.remove("Yusuf")
# print(isimler)

# *pop() listelerde belirtilen elemanın biri indexini silmek için kullanılır index beirtmezsek listenin son elemanını siler

# isimler.pop()
# print(isimler)

# del isimler[5]
# print(isimler)

# ! TUPLE 

# * Birden fazla elemanı barındıran bir veri yapısıdır. Sıralanabilir  ama oluşturmuş olduğumuz liste elemanları değiştirelemez. Yani tuple listesine ekleme silme ve güncelleme yapamayız.

# liste = [1,2,3]
# print(type(liste))
# tuple_ = 1,"iki", True
# print(type(tuple_))

# ! Tuple Metodları
# *count tekrarlayan elemeanalrın sayısını verir
# print(tuple_.count(1))

# * index bir elemanın index numarasını almak için kullanılır
# print(tuple_.index("iki"))

# !Tuple eleman ekleme

# tuples_iki = "hakan","yusuf","ahmet"
# # print(type(tuples_iki))
# liste_yap = list(tuples_iki)
# # print(type(liste_yap))
# liste_yap.append("mert")
# tuples_iki = tuple(liste_yap)
# print(type(liste_yap))


#! DİCTİONARY
# * Sözlük veri yapısıdır. Değiştirilebilir indexlenebilir bir veri yapısıdır elemanlar scop arasına yazılır {} js obje yapısı ile aynıdır. Veriler Key ve Value şeklinde saklanır.

# ogrenci = {
#    100:{
#        "isim" : "Kadir" ,
#        "soyisim" : "Kizilarslan" ,
#        "yas" : 26, 
#        "meslek" : "egitmen",
#    },
#    101:{
#        " isim":"Abdulkadir",
#        "soyisim" : "Kizilarslan",
#        "yas":22,
#        "meslek":"ogrenci"
#    }
# }
# print(ogrenci[100]["isim"]) #<< index içinden istenilen veriye ulaşma
# print(ogrenci[101]["yas"]) 

# ! Operatörler
# ! Karşılaştırma Operatörleri 
#* Neden soru soruyorum çünkü herhangi bir durumda bunları karşılaştırdığımız zaman bize bir boolean ifade dönüyor
# == eşit mi ?
# !=  eşit değil mi 
#  < küçük mü 
#  > büyük mü 
# >= büyük eşit mi 
# <= küçük eşit mi 
# print(5 == 6)

# ! MANTIKSAL OPERATÖRLER
# ! And Operatörü
# True and True => True 
#  True and False => False
# False and True => False
#  False and False => False

# ! Or Operatörü
# True or True => True
# True or False => True
# False Or True => True
# False or False => False

# ! İnputtan veri alma 
# * Kodlar yukarıdan aşağıya okunuyor inputa geldiğinde ise duruyor ve cevap bekliyor ve aldığı cevabı yazdırıyor. İnputlar kod bekleyicidir.

# isim = input("İsminiz nedir ?")
# yas = input("Kaç Yaşınızdaydınız ?")
# print(f"benim adım {isim} Ve Ben {yas} Yaşındayım")

# TODO uygulama inputtan 2 sayı al ve topla

# x = float(input("ilk sayıyı gir"))
# y = float(input("ikinci sayıyı gir"))
# toplam = x+y
# print(toplam)

#* İsim soyisim şehir yaş bilgilerini inputtan al formatlayarak ekrana yazdır

# isim = input("Adım")
# soyisim = input("soyisim")
# yas = int(input("Yaşım"))
# print(f"Benim adım {isim} Soyadım {soyisim} ve ben {yas} yaşındayım")

# isim = input("Adinizi giriniz")
# soyad = input("Soyadinizi giriniz")
# sehir = input("Sehir giriniz")
# yas = int(input("Yasinizi giriniz"))

# print(f" Benim adım {isim} , Soyadım {soyad}, {yas} yaşındayım ve ben {sehir} de yaşıyorum")  

# ! KOŞUL İFADELERİ
#* Yukarıda karşılaştırma operatörlerini gördük bu karşılaştırma operatörleri aracılığıyla belli durumları kontrol ettik bu durumlar bize boolean türünde bir değer getiriyor buna göre programın gidişatını farklı yönlere gönderebiliriz

# x = 1
# if(x == 2):
#     print("Merhaba")
# else : 
#     print("Günaydın")


# x = 4
# if x % 2 == 0: 
#    print(f"{x} Çift")
# else: 
#     print("tek")

# username = "kdr35"
# password = "1234"

# if username == "kdr3a5":
#      if password == "1234":
#           print("Merhaba Giriş yaptın")
#      else: 
#           print("Hatalı şifre")
# else: 
#     print("Hatalı kullanıcı adı")
    
# TODO Uygulama
# inputtan bir yaş ve eğitim bilgisi al yaş 18 den büyükse ve eğitim durumu lise yada üniversite ise ehliyet alabilir değilse alamaz

# yas = int(input("Yaş girin"))
# egitim = input("Eğitim düzeyi gir")

# if(yas >= 18 and egitim == " Lise" or egitim == " Üniversite" ):
#     print("başarılı giriş")

# else:
#     print("başarılı olamadın")

# ! if-elif
# x = 20
# y = 20

# if (x > y):
#     {print(" x y' den büyük")}
# elif (x == y ): {
#     print("x y birbirine eşit") }
# else:
#     print("y x' den büyük")

# TODO : bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hessapla ?

# benzinFiyat = 38.50
# dizelFiyat = 40
# toplamYakitUcreti = 0

# ortalamaYakitTuketimi = float(input("100 km de ortalama yakıt tüketimi "))
# gidilecekYol = float(input("Gidilecek Yol kaç km ?"))
# yakitTipi = input("Yakıt Tipiniz nedir ?")

# toplamYakitTuketimi = gidilecekYol * (ortalamaYakitTuketimi / 100)

# if (yakitTipi == "benzin"):
#     toplamYakitUcreti = benzinFiyat * toplamYakitTuketimi
# elif(yakitTipi == "dizel"):
#     toplamYakitUcreti = dizelFiyat * toplamYakitTuketimi
# else: 
#     print("Yanlış yakıt tipi girdiniz")

# print(f" Toplam Yakıt Maliyeti {toplamYakitUcreti} ")

# ! DÖNGÜLER 
# * Uygulamamız başladı bir koşulumz var bu koşulumuz doğruysa kod bloğu çalışır bu koşul gerçekleşene kadar uygulamanın kendini tekrar etmesi diyebiliriz. Döngüler uygulamalarımız daha etkili ve verimli bir hale getirmemize yardımcı olabilir.Koşulumuz false verene kadar çalışır

# ! for-döngüleri

# for i in range(10):
#     print(i)
    
# sayilar = [1,3,5,2,6,8,7,9]
# for i in sayilar:
#     print(i)

# isim = "atakan"
# for i in isim:
#     print(i,isim.index(i))     

# tuple_ = [(1,2,3),(3,4,3),(5,6,3)]

# for a,b,c in tuple_:
#     print(a,b,c)
    
# dict_ = {"k1": 1,"k2":2,"k3":3}
# for x in dict_:
#     print(dict_[x])

# for x in dict_.values():
#     print(x)

# for key,value in dict_.items():
#     print(value)


  
   