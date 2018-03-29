import random

kelime = random.choice(['asit','element','ametal','elektron','atom', 'periyot', 'oksijen'])

harfHavuzu = []

kalanHak   = 6

karakter = '_'    #kelimeyi örtülü bir şekilde göstermek için.

gosterimYazisi = list(karakter*len(kelime))
# '_' karakterini kelimenin uzunluğuyla çarpıp bir diziye dönüştürdük

dongu = 1

while dongu:
    print(' '.join(gosterimYazisi),end='\n\n')
    #dizinin elemanlarını aralarında boşluk olacak şekilde birleştirdik

    alinanHarf = input('Bir harf giriniz: ').lower() #alınan harfi sıkıntı olmasın diye küçültüyoruz

    try:
        int(alinanHarf)
        print('Doğru bir şeyler girdiğinden emin ol.\n')
    except:
        if len(alinanHarf) > 1:
            print('Harf giriniz!\n')
        else:
            if alinanHarf in harfHavuzu:
                print('Bu harfi zaten girdiniz.\n')
            else:
                bulduk = None
                for i in range(len(kelime)):
                    #0'dan bulunacak kelimenin uzunluğuna kadar olan sayıları teker teker "i" değişkenine aktarıyoruz.

                    if alinanHarf == kelime[i]:  ## kullanıcının girdiği harf, bulunucak kelimenin "i" nin taşıdığı sayı değerindeki indexteki harfe eşit ise
                            bulduk = True
                            gosterimYazisi[i] = alinanHarf
                            harfHavuzu.append(alinanHarf)

                            if karakter not in gosterimYazisi:
                                #gösterim karakterimiz, gosterimYazisi değişkeninin içinde mi diye kontrol ediyoruz. Eğer içinde değilse kullanıcının bütün harfleri bulduğunu anlayıp ona gerekli mesajı yazıyoruz.

                                print(' '.join(gosterimYazisi))
                                print('\nTebrikler kelimeyi buldunuz!')
                                dongu = 0
                else:
                    if bulduk != True:
                        kalanHak -= 1
                        print('Yanlış harf. Kalan hakkınız: {}\n'.format(kalanHak))
                        harfHavuzu.append(alinanHarf)

                if kalanHak == 0:
                    print('Kaybettin. Doğru kelime "{}" idi.\n'.format(kelime))
                    break
