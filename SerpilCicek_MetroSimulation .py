import heapq
from collections import deque

class Istasyon:
    def __init__(self, isim):
        """
        Bir metro istasyonunu temsil eden sınıf.
        """
        self.isim = isim
        self.komsular = []

    def komsu_ekle(self, komsu, sure):
        """
        İstasyona bir komşu istasyon ekler.
        """
        self.komsular.append((komsu, sure))

class MetroAgi:
    def __init__(self):
        """
        Metro ağını temsil eden sınıf.
        """
        self.istasyonlar = {}

    def istasyon_ekle(self, isim):
        """
        Yeni bir istasyon ekler.
        """
        if isim not in self.istasyonlar:
            self.istasyonlar[isim] = Istasyon(isim)

    def baglanti_ekle(self, isim1, isim2, sure):
        """
        İki istasyon arasında bağlantı ekler.
        """
        self.istasyon_ekle(isim1)
        self.istasyon_ekle(isim2)
        self.istasyonlar[isim1].komsu_ekle(self.istasyonlar[isim2], sure)
        self.istasyonlar[isim2].komsu_ekle(self.istasyonlar[isim1], sure)

    def en_az_aktarma_bul(self, baslangic, hedef):
        """
        BFS algoritmasını kullanarak en az aktarmalı rotayı bulur.
        """
        kuyruk = deque([(self.istasyonlar[baslangic], [baslangic])])
        ziyaret_edilen = set()
        
        while kuyruk:
            mevcut, yol = kuyruk.popleft()
            
            if mevcut.isim == hedef:
                return yol
            
            if mevcut.isim not in ziyaret_edilen:
                ziyaret_edilen.add(mevcut.isim)
                for komsu, _ in mevcut.komsular:
                    if komsu.isim not in ziyaret_edilen:
                        kuyruk.append((komsu, yol + [komsu.isim]))
        return None

    def heuristik(self, istasyon, hedef):
        """
        Basit heuristik fonksiyon: istasyon adlarının harf farkını kullanır.
        """
        return abs(ord(istasyon[0]) - ord(hedef[0]))

    def en_hizli_rota_bul(self, baslangic, hedef):
        """
        A* algoritmasını kullanarak en hızlı rotayı bulur.
        """
        oncelik_kuyrugu = [(0, self.istasyonlar[baslangic], [baslangic])]
        ziyaret_edilen = {}
        
        while oncelik_kuyrugu:
            mevcut_sure, mevcut, yol = heapq.heappop(oncelik_kuyrugu)
            
            if mevcut.isim == hedef:
                return yol
            
            if mevcut.isim not in ziyaret_edilen or mevcut_sure < ziyaret_edilen[mevcut.isim]:
                ziyaret_edilen[mevcut.isim] = mevcut_sure
                for komsu, sure in mevcut.komsular:
                    tahmini_maliyet = mevcut_sure + sure + self.heuristik(komsu.isim, hedef)
                    heapq.heappush(oncelik_kuyrugu, (tahmini_maliyet, komsu, yol + [komsu.isim]))
        return None

    def test_senaryolari(self):
        """
        Test senaryolarını çalıştırır.
        """
        print("En az aktarma ile rota:", self.en_az_aktarma_bul("A", "C"))
        print("En hızlı rota:", self.en_hizli_rota_bul("A", "C"))

if __name__ == "__main__":
    metro = MetroAgi()
    metro.baglanti_ekle("A", "B", 5)
    metro.baglanti_ekle("B", "C", 10)
    metro.baglanti_ekle("A", "D", 7)
    metro.baglanti_ekle("D", "C", 2)
    metro.test_senaryolari()
