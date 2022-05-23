print("Perhitungan Tiket Kereta Api")
print("-"* 25)
print("Jurusan :")
print("1. Jakarta")
print("2. Yogyakarta")
print("3. Surabaya")
kode=int(input("Pilihan Jurusan [1/2/3] :"))
if kode==1 :
    harga=150000
elif kode==2 :
    harga=300000
elif kode==3 :
    harga=400000
else :
    print("Inputan salah")

banyak_tiket = int(input("Banyak Tiket    :"))
print(f"Harga tiket : RP. {harga :10.0f}")
total=harga*banyak_tiket
print(f"Total Bayar : Rp. {total: 10.0f}")