# AkbankPython
# README.md içeriği
readme_content = """# Sürücüsüz Metro Simülasyonu (Rota Optimizasyonu)

## Proje Açıklaması
Bu proje, bir metro ağında en az aktarmalı ve en hızlı rotaları bulmayı amaçlayan bir simülasyondur.

## Kullanılan Teknolojiler
- Python
- collections (deque)
- heapq

## Algoritmalar
### BFS (En Az Aktarmalı Rota)
- Genişlik Öncelikli Arama (BFS) kullanarak en az aktarmalı rotayı bulur.

### A* (En Hızlı Rota)
- Öncelik kuyruğu ile en kısa süreli rotayı belirler.
- Heuristik fonksiyon eklenerek en iyi tahminli maliyet hesaplanır.

## Örnek Kullanım
python
metro = MetroAgi()
metro.baglanti_ekle("A", "B", 5)
metro.baglanti_ekle("B", "C", 10)
metro.baglanti_ekle("A", "D", 7)
metro.baglanti_ekle("D", "C", 2)

print("En az aktarma ile rota:", metro.en_az_aktarma_bul("A", "C"))
print("En hızlı rota:", metro.en_hizli_rota_bul("A", "C"))


## Geliştirme Fikirleri
- Daha büyük bir metro ağı eklenebilir.
- Arayüz ile görselleştirme yapılabilir.

## Test Sonuçları
| Başlangıç | Hedef | En Az Aktarma | En Hızlı Rota |
|-----------|-------|--------------|--------------|
| A         | C     | A → B → C    | A → D → C    |

