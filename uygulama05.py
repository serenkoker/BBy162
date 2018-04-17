import random
hak = 6
i = 0
kelimeler = random.choice(["ingilizce","edebiyat","kimya","matematik","beden eğitimi","coğrafya"])
kelimekılavuzu = []
for a in kelimeler:
    kelimekılavuzu.append("-")
print(kelimekılavuzu)


while hak > 0:
    alınanharf = input("\nBir harf giriniz: ")
    if alınanharf in kelimeler:
        for kontrolet in kelimeler:
            if kelimeler [i] == alınanharf:
                kelimekılavuzu [i] = alınanharf
            i+=1
        print(kelimekılavuzu)
        i=0



    else:
        i=0
        hak-=1
        print('Yanlış harf girdiniz. Kalan hakkınız: {}'.format(hak))

if hak == 0:
    print('Oyunu kaybettiniz. Doğru kelime "{}".\n'.format(kelimeler))