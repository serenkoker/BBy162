__author__ = "Seren Nur Köker"

kadinadi = input("Bir kadın adı giriniz...:")
erkekadi = input("Bir erkek adı giriniz...:")
misra    = int(input("Mısra sayısı giriniz...Maksimum 7 mısra yazdırılabilir.."))

print("-"*60)

print("")

siir     = [kadinadi +  " eşek gözlü " + erkekadi +  " uzun boylu", "İkisi buluştular gizlice", kadinadi + " çok nazlıydı" ,"Ama " +  erkekadi +"de sabırsız",erkekadi + " anası dedi o kızı istemem", "O zaman dedi" + kadinadi + "ya", "Kaçalım buralardan madem"]


for olusturulacak_siir in siir[:misra]:
    print(olusturulacak_siir)

print("")

print("-"*60)

if misra > 10:
    print("Geçerli bir mısra sayısı girmediniz..")
    print("Yazdırılan mısra sayısı: 10") # 10'den büyük bir değer girilmesi durumunda, 10 mısraya kadar yazdırıldığından hep 10 yazacak.

else:
    print("Yazdırılan mısra sayısı:", misra)
