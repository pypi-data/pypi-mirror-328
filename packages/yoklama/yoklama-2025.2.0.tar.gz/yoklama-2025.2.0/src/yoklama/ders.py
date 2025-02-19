from datetime import datetime, timedelta

class Ders:
    def __init__(self, ad, kisaAd, sorumlu, kod, haftalikProgram):
        self.__haftaGunSirasi = {"Pazartesi":0, "Salı":1, "Çarşamba":2, "Perşembe":3, "Cuma":4, "Cumartesi":5, "Pazar":6}
        self.__haftaGunIsmi = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
        self.__ad = ad
        self.__kisaAd = kisaAd
        self.__sorumlu = sorumlu
        self.__kod = kod
        self.__haftalikProgram = []
        for i in range(len(haftalikProgram)):
            self.__haftalikProgram.append({
                "haftaGunu":haftalikProgram[i]["haftaGunu"],
                "haftaGunSirasi":self.__haftaGunSirasi[haftalikProgram[i]["haftaGunu"]],
                "baslangicSaati":datetime.strptime(haftalikProgram[i]["baslangicSaati"],"%H:%M"),
                "dersSayisi":haftalikProgram[i]["dersSayisi"]
            })

    @property
    def ad(self) -> str:
        return self.__ad
    
    @property
    def kisaAd(self) -> str:
        return self.__kisaAd
    
    @property
    def sorumlu(self) -> str:
        return self.__sorumlu
    
    @property
    def kod(self) -> str:
        return self.__kod
    
    @property
    def haftalikProgram(self):
        return self.__haftalikProgram