# Fungsi untuk menghitung pekerjaan yang dilakukan oleh pelari
def hitung_pekerjaan(daya, waktu):
    pekerjaan = daya * waktu
    return pekerjaan

# Fungsi untuk menghitung energi kinetik pelari
def hitung_energi_kinetik(massa, kecepatan):
    energi_kinetik = 0.5 * massa * (kecepatan ** 2)
    return energi_kinetik

# Konstanta
jarak_km = 5  # jarak dalam kilometer
daya = 150  # daya rata-rata dalam watt
massa_pelari = 60  # massa pelari dalam kg
kecepatan_pelari = 5  # kecepatan rata-rata pelari dalam m/s

# Konversi jarak ke meter
jarak_meter = jarak_km * 1000  # 1 km = 1000 m

# Hitung waktu yang diperlukan (dalam detik)
waktu = jarak_meter / kecepatan_pelari

# Hitung pekerjaan yang dilakukan oleh pelari
pekerjaan = hitung_pekerjaan(daya, waktu)
print(f"Pekerjaan yang dilakukan oleh pelari: {pekerjaan} Joule")

# Hitung energi kinetik pelari
energi_kinetik = hitung_energi_kinetik(massa_pelari, kecepatan_pelari)
print(f"Energi kinetik pelari: {energi_kinetik} Joule")
