# Günler listesi ve sözlüğü 06.03.2018

gunler= ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

print(gunler)

gunler_dict = {"Pazartesi" :"İngilizce", "Salı": "Boş gün", "Çarşamba": "Programlama", "Perşembe": "Bilgi Erişim",
              "Cuma": "Bilgi Hizmetleri", "Cumartesi": "Gezme", "Pazar": "Ödevler"}
print(gunler_dict)

print("Cumartesi" in gunler_dict)

print(gunler_dict.values())

print(gunler_dict[input("Gün yazınız:")])

