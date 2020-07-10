#4 basamaklı, rakamları farklı, random bir sayı seç. (GDJ-4)
import random
for i in range(4):
    a1 = random.randint(1, 9)
    a2 = random.randint(0, 9)
    while a2 == a1:
        a2 = random.randint(0, 9)
    a3 = random.randint(0, 9)
    while (a3 == a2) or (a3 == a1):
        a3 = random.randint(0, 9)
    a4 = random.randint(0, 9)
    while (a4 == a3) or (a4 == a2) or (a4 == a1):
        a4 = random.randint(0, 9)

#Seçilen sayıyı, her basamağı bir eleman olacak şekilde dört elemandan oluşan bir diziye kopyala (Asıl[]). (GDJ-5)
Asıl = [str(a1), str(a2), str(a3), str(a4)]

#Kullanıcıdan bir tahmin al. (GDJ-6)
giris = input("Rakamları farklı dört basamaklı bir sayı tuttum, bakalım bilebilecek misin? Tahminini söyle :")

#Kullanıcının tahminini her basamağı bir eleman olacak şekilde dört elemandan oluşan bir diziye kopyala (Tahmin[]). (GDJ-7)
Tahmin = list(giris)

while True:
#İki dizinin aynı sıradaki elemanlarını karşılaştır (Asıl[1] ile Tahmin[1]; Asıl[2] ile Tahmin[2] vs. (GDJ-8)
#"Artı = 0" değişkenini oluştur ve dizilerin aynı sıra elemanlarının karşılaştırmasında,
#aynı çıkan karşılaştırma sayısı kadar Artı değişkenini 1 artır. (1'inci ve 3'üncü elemanlar aynıysa Artı=2 olacak). (GDJ-9)
    Artı = 0
    for i in range(0, 4):
        if Asıl[i] == Tahmin[i]:
            Artı += 1

#İki dizinin farklı sıradaki elemanlarını karşılaştır (Asıl[1] ile Tahmin[2], Tahmin[3] ve Tahmin[4];
#Asıl[2] ile Tahmin[3], Tahmin[4] ve Tahmin[1]; Asıl[3] ile Tahmin[4], Tahmin[1] ve Tahmin[2];
#Asıl[4] ile Tahmin[1], Tahmin[2] ve Tahmin[3]) (GDJ-11)            
#"Eksi = 0" değişkenini oluştur ve farklı sıra karşılartırmasında, aynı çıkan karşılaştırma sayısı kadar
#Eksi değişkenini 1 artır. (Asıl[1] ile Tahmin[3]; Asıl[3] ile Tahmin[4] aynıysa Eksi=2 olacak) (GDJ-12)
    Eksi = 0
    for i in range(0, 4):
        if (Asıl[i] == Tahmin[(i+1)%4]) or (Asıl[i] == Tahmin[(i+2)%4]) or (Asıl[i] == Tahmin[(i+3)%4]):
            Eksi += 1
    
#Artı = 4 olduğunda kullanıcıya tahmininin doğru olduğunu bildir ve kullanıcıyı tebrik et. (GDJ-10)
    if Artı == 4:
        print('Tebrikler tahmininiz doğru.')
        break
#Kullanıcıya "f(Tahmin sonucunuz : + {Artı}, - {Eksi})" mesajını ver. (GDJ-13)
    else:
        print("Tahmin sonucunuz : +{}, -{}".format(Artı,Eksi))

#Kullanıcıdan yeni tahminini iste. (GDJ-14)
        giris = input("Yeni tahmininiz? :")
        Tahmin = list(giris)
