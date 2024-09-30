print("-------------------------------------------------------------------------------------")
print("Program : Menghitung total harga barang berdasarkan harga barang dan jumlah pembelian")
print("-------------------------------------------------------------------------------------")

#Registrasi Akun
print("Silahkan Registrasi Akun Anda")
while True:
    nama1= str(input("Silahkan masukkan nama   :"))
    nim1= int(input("Silahkan masukkan NIM   :"))
    pin1= int(input("Silahkan masukkan Pin   :"))
    if nim1.is_integer and pin1.is_integer():
        break
    else:
        print("NIM dan Pin harus berupa angka. Slahkan coba lagi")

#Tanda Akun telah berhasil dibuat
print("Akun berhasil dibuat")
print("-------------------------------------------------------------------------------------")

#Login ke Akun yang telah dibuat
print("Silahkan login ke Akun Anda")
while True:
    nama2= str(input("Silahkan masukkan Nama  :")) 
    pin2= int(input("Silahkan masukkan Pin  :"))
    if nama1 == nama2 and pin1 == pin2:
        print("Selamat datang,", nama1)
        break
    else:
        print("Maaf, Pin atau Nama Anda mungkin salah, silahkan coba kembali")
print("-------------------------------------------------------------------------------------")
#Menghitung total pembayaran
while True:
    try:
        hrg_barang = float(input("Silahkan masukkan Harga Barang   : Rp "))
        jmlh_barang = int(input("Silahkan masukkan Jumlah Barang   :"))
        total_harga = hrg_barang*jmlh_barang
        if total_harga >= 250000: #Memeriksa apakah mendapatkan diskon
            total_diskon = total_harga*25/100
            total_pembayaran = total_harga - total_diskon
            print("Total Harga barang: Rp", total_harga)
            print("Diskon yang didapatkan: Rp", total_diskon)
            print("Total yang harus dibayar (setelah dikurangi diskon): Rp", total_pembayaran)
        else: #Tidak mendapatkan diskon
            print("Total Harga barang(Tidak ada Diskon): Rp", total_harga)
    except ValueError: #Jika input tidak sesuai instruksi
        print("Input tidak valid. Harap masukkan angka.")
    #Menanyakan pada user apakah ingin menghitung ulang total harga atau langsung keluar 
    while True: 
        konfirmasi = input("\nApakah anda ingin menghitung total harga lagi?\n1. Tidak \n2. Ya\nMasukkan angka:")
        if konfirmasi == "1" :
            print("Program Selesai")
            # Statement penutup
            print("Terima kasih sudah berbelanja di Toko Silver Light")
            print("Kami tunggu kunjungan Anda selanjutnya.")
            exit() #keluar dari semua looping
        elif konfirmasi == "2":
            print("Baik silahkan hitung ulang")
            break
        else:
            print("Pilihan tidak tersedia, silahkan pilih angka sesuai opsi")
