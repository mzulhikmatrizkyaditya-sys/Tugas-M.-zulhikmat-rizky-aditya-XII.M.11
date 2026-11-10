print("=== APOTEK SEHAT ===")
print("1. Demam")
print("2. Batuk")
print("3. Flu")
print("4. Maag")
print("5. Diare")
print("6. Alergi")
print("7. Luka Ringan")
print("8. Dehidrasi")

pilihan = int(input("Pilih penyakit (1-8): "))

if pilihan == 1:
    penyakit = "Demam"
    nama = "Paracetamol"
    harga = 10000

elif pilihan == 2:
    penyakit = "Batuk"
    nama = "Sirup Batuk"
    harga = 18000

elif pilihan == 3:
    penyakit = "Flu"
    nama = "Saline Hidung"
    harga = 15000

elif pilihan == 4:
    penyakit = "Maag"
    nama = "Antasida"
    harga = 12000

elif pilihan == 5:
    penyakit = "Diare"
    nama = "Oralit"
    harga = 3000

elif pilihan == 6:
    penyakit = "Alergi"
    nama = "Cetirizine"
    harga = 10000

elif pilihan == 7:
    penyakit = "Luka Ringan"
    nama = "Betadine"
    harga = 15000

elif pilihan == 8:
    penyakit = "Dehidrasi"
    nama = "Oralit"
    harga = 3000

else:
    penyakit = ""
    nama = ""
    harga = 0

if pilihan >= 1 and pilihan <= 8:
    jumlah = int(input("Jumlah obat: "))
    total = harga * jumlah

    if total >= 50000:
        diskon = total * 5 / 100
    else:
        diskon = 0

    bayar = total - diskon

    print("\n=== STRUK APOTEK ===")
    print("Penyakit:", penyakit)
    print("Nama obat:", nama)
    print("Harga obat: Rp", harga)
    print("Jumlah:", jumlah)
    print("Total harga: Rp", total)
    print("Diskon: Rp", int(diskon))
    print("Total bayar: Rp", int(bayar))

else:
    print("Obat tidak tersedia")
