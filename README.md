# Mini_Project_1
Nama : Nadila Purti
Nim : 2409116052

# Flowchart
![052NadilaPutri_MinproDaspro1](https://github.com/user-attachments/assets/c90108d2-cb31-43e2-a4ba-7056070f93e2)


# Contoh Output dari awal hingga akhir
![Cuplikan layar 2024-09-30 204639](https://github.com/user-attachments/assets/d0e4145a-0be0-4150-8999-3c21e603854a)


# Penjelasan Program
Judul program
"Program : Menghitung total harga barang berdasarkan harga barang dan jumlah pembelian"

1. Registrasi Akun

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

   Penjelasan: Fungsi while True berguna untuk mengulangi code tanpa batas jika belum sesuai dengan ondisi yang kita inginkan, disini saya juga menentukan tipe data yang saya inginkan untuk pengimputan data yaitu menggunakan string pada nama dan integer pada nim dan pin. Lalu saya membuat kondisi jika maka pada while, jika nim1 dan pin1 adalah integer, maka perulangan kode akan dihentikan dengan break karena kondisi yg diinginkan telah terpenuhi. lalu jika bukan(else) saya juga memberikan statement untuk mencoba lagi dan kode akan otomatis terulang karena kondisi yang tidak terpenuhi. Selanjutnya ada perintah untuk menampilkan kalimat bahwa akun telah berhasil di buat, dan juga garis pembatas untuk kode selanjutnya.

2. Login ke Akun yang telah dibuat
   print("Silahkan login ke Akun Anda")
   while True:
    nama2= str(input("Silahkan masukkan Nama  :")) 
    pin2= int(input("Silahkan masukkan Pin  :"))
    if nama1 == nama2 and pin1 == pin2:
        print("Selamat datang,", nama1)
        break
    else:
        print("Maaf, Pin atau NIM Anda mungkin salah, silahkan coba kembali")
    print("-------------------------------------------------------------------------------------")

    Penjelasan : DI kode yang kedua saya menambahkan kode untuk login dan juga memakai while True. Disini saya hanya menggunakan 2 imputan yaitu nama2 dan pin2 yang kemudian akan dicocokkan dengan variable yang telah diisi saat menginput data untuk registrasi menggunkan kondisi if else, jika nama1 sama dengan nama2 AND  pin1 sama dengan pin2 maka akan memenuhi kondisi dari while True tersebut, kode akan menampilkan "Selamat datang, nama1"(nama1 sesuai dengan inputan) dan akan dihentikan oleh break, jika inputan tidak sesuai dengan kondisi if, maka kode akan terulang hingga kondisi yang benar terpenuhi.
   
4. Menghitung total pembayaran
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

    Penjelasan : Untuk menghitung total pembayaran saya menggunkan While true lagi, ada juga fungsi try yang berguna agar kode tetap bisa berjalan tanpa krek walaupun ada beberapa masalah seperti kesalahan input dan sebagainya. lalu ada input harga barang dan jumlah barang, untuk harga barang sendiri saya menggunakan tipe data float karena bisa jadi ada desimal, lalu ada input jumlah barang dengan tipe data integer. Selanjutnya saya menambahkan variable baru yaitu total harga, dengan rumus perhitungan seperti di kode, yaitu mengalikan antara harga barang dan jumlah barang yang di beli. Setelah itu ada kondisi if else, dimana jika total_harga lebih dari Rp 250.000 maka pembeli akan mendapatkan diskon sebesar 25%, saya juga menambah 2 variable baru untuk menampilkan diskon dan total pembayaran secara bersih yang harus dibayarkan oleh pembeli setelah mendapatkan diskon, jika harga tidak sampai Rp 250.000 mka pembeli tidak akan mendapatkan diskon dan membayar sesuai penjumlahan harga aslinya. Lalu ada except ValueError jika inputan tidak sesuai instruksi maka akan menampilkan "Input tidak valid. Harap masukkan angka.".
   
5. Menanyakan pada user apakah ingin menghitung ulang total harga atau langsung keluar
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

   Penjelasan : Terakhir ada kode untuk  menghitung ulang total harga atau langsung keluar dari loopingnya, pertama saya menulis inputan dengan variable konfirmasi untuk menanyakan "Apakah anda ingin menghitung total harga lagi?\n1. Tidak \n2. Ya\nMasukkan angka:" jika user memilih "1" maka while akan berhenti dan menampilkan staement penutup yang telah saya tulis, lalu jika user menginput "2" maka user akan kembali pada kode pengimputan harga dan jumlah barang sampai user memilih kondisi "1" untuk keluar dari program. dan jika user mengimput diluar dari "1" OR "2" maka program akan menampilkan "Pilihan tidak tersedia, silahkan pilih angka sesuai opsi".

Sekian untuk penjelasan kode yang saya tulis, terima kasih.
