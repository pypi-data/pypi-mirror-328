from src.yoklama.yoklama import *
from datetime import datetime

# Sabitler
dersAdi = "Bilgisayar Programlama II"
dersKisaAdi = "Bil. Prog. II"
kaynakDosyaYolu = f"Kaynaklar/{dersAdi}.xlsx"
hedefDosyaYolu = f"Ciktilar/{dersAdi} - Yoklama.xlsx"
universiteAdi = "Ağrı İbrahim Çeçen Üniversitesi"
birimAdi = "Fen Edebiyat Fakültesi"
bolumAdi = "Matematik"
donem = 2
yariyilBaslangicTarihi = "17/02/2025"
yariyilBitisTarihi = "04/06/2025"
dersinSorumlusu = "Kadirhan POLAT"
dersinKodu = "MATE208"
dersinHaftalikProgrami = [
    {"haftaGunu":"Çarşamba", "baslangicSaati":"10:00", "dersSayisi":2},
    {"haftaGunu":"Cuma", "baslangicSaati":"11:00", "dersSayisi":1}
    ]

yariyilTatilGunleri = [
    {"adi":"Ramazan Bayramı Arifesi","baslangicTarihi":"29/03/2025 12:00","gunSayisi":0.5},
    {"adi":"Ramazan Bayramı","baslangicTarihi":"30/03/2025 00:00","gunSayisi":3},
    {"adi":"Ulusal Egemenlik ve Çocuk Bayramı","baslangicTarihi":"23/04/2025 00:00","gunSayisi":1},
    {"adi":"Emek ve Dayanışma Günü","baslangicTarihi":"01/05/2025 00:00","gunSayisi":1},
    {"adi":"Atatürk'ü Anma Gençlik ve Spor Bayramı","baslangicTarihi":"19/05/2025 00:00","gunSayisi":1},
    {"adi":"Kurban Bayramı Arifesi","baslangicTarihi":"05/06/2025 12:00","gunSayisi":0.5},
    {"adi":"Kurban Bayramı","baslangicTarihi":"06/06/2025 00:00","gunSayisi":4}
]

yoklama = Yoklama(kaynakDosyaYolu,
                  hedefDosyaYolu,
                  universiteAdi,
                  birimAdi,
                  bolumAdi,
                  donem,
                  yariyilBaslangicTarihi,
                  yariyilBitisTarihi,
                  yariyilTatilGunleri,
                  dersAdi,
                  dersKisaAdi,
                  dersinSorumlusu,
                  dersinKodu,
                  dersinHaftalikProgrami)

# print(yoklama.ders.ad)
# print(yoklama.ders.sorumlu)
# print(yoklama.ders.kod)
# print(yoklama.ders.kredi)
# print(yoklama.ders.haftalikGunler)
# print(yoklama.ders.haftalikGunSiralari)
# print(yoklama.yariyil.baslangicTarihi)
# print(yoklama.yariyil.bitisTarihi)
# print(yoklama.yariyil.toplamSaniye)
# print(yoklama.yariyil.toplamGun)
# print(yoklama.yariyil.toplamHafta)
# print(yoklama.toplamSutun)

yoklama.yoklamaDosyasiOlustur()



