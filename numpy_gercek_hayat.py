import numpy as np
import matplotlib.pyplot as plt

# BÖLÜM 1: Şirket Maaş Analizi

# Görev 1: Maaşları simüle etme ve analiz
np.random.seed(42)  
maaslar = np.random.randint(3000, 15001, size=500)

ortalama_maas = np.mean(maaslar)
max_maas = np.max(maaslar)
min_maas = np.min(maaslar)

print(f"Ortalama Maaş: {ortalama_maas}")
print(f"Maksimum Maaş: {max_maas}")
print(f"Minimum Maaş: {min_maas}")

# Maaş dağılımını histogram ile görselleştirme
plt.hist(maaslar, bins=20, color='blue', edgecolor='black')
plt.title('Maaş Dağılımı')
plt.xlabel('Maaş (TL)')
plt.ylabel('Çalışan Sayısı')
plt.show()


# Görev 2: Departmanlara atama ve ortalama maaş hesaplama
departmanlar = np.random.choice([1, 2, 3], size=500)

muhendislik_maas = maaslar[departmanlar == 1]
muhasebe_maas = maaslar[departmanlar == 2]
pazarlama_maas = maaslar[departmanlar == 3]

print(f"Mühendislik Ortalama Maaş: {np.mean(muhendislik_maas)}")
print(f"Muhasebe Ortalama Maaş: {np.mean(muhasebe_maas)}")
print(f"Pazarlama Ortalama Maaş: {np.mean(pazarlama_maas)}")


# BÖLÜM 2: Hava Durumu Verileri Üretme ve Analiz

# Görev 3: Günlük sıcaklık değerlerini simüle etme
sicakliklar = np.random.randint(-10, 41, size=365)

ortalama_sicaklik = np.mean(sicakliklar)
max_sicaklik = np.max(sicakliklar)
min_sicaklik = np.min(sicakliklar)

print(f"Ortalama Sıcaklık: {ortalama_sicaklik}")
print(f"Maksimum Sıcaklık: {max_sicaklik}")
print(f"Minimum Sıcaklık: {min_sicaklik}")

# Sıcaklık dağılımını histogram ile görselleştirme
plt.hist(sicakliklar, bins=20, color='red', edgecolor='black')
plt.title('Sıcaklık Dağılımı')
plt.xlabel('Sıcaklık (°C)')
plt.ylabel('Gün Sayısı')
plt.show()


# BÖLÜM 3: Ürün Satış Analizi
ürünler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"]
satışlar = np.random.randint(10, 101, (5, 30))

# Her ürün için toplam ve ortalama satış miktarlarını hesaplama
toplam_satışlar = np.sum(satışlar, axis=1)
ortalama_satışlar = np.mean(satışlar, axis=1)

for i, ürün in enumerate(ürünler):
    print(f"{ürün} Toplam Satış: {toplam_satışlar[i]}, Ortalama Satış: {ortalama_satışlar[i]}")

# Ürün bazında çubuk grafiği çizme
plt.bar(ürünler, toplam_satışlar)
plt.title("Ürün Bazında Toplam Satışlar")
plt.xlabel("Ürün")
plt.ylabel("Toplam Satış Miktarı")
plt.show()

