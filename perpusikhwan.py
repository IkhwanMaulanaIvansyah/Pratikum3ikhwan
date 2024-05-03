#Nama : Ikhwan Maulana Ivansyah
#Nim  : S120230016

class Buku:
    def __init__(self, judul, penulis, genre, status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.status = status

    def __str__(self):
        return f"{self.judul} - {self.penulis} ({self.genre}) - Status: {self.status}"


class Perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tampilkan_buku(self):
        if self.koleksi_buku:
            print("-----------------")
            print("|| DAFTAR BUKU ||")
            print("-----------------")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("Koleksi buku masih kosong.")

    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                return buku
        return None

    def pinjam_buku(self, buku, anggota):
        if buku.status == "Tersedia":
            buku.status = "Dipinjam"
            anggota.buku_pinjaman.append(buku)
            print(f"Buku '{buku.judul}' berhasil dipinjam oleh {anggota.nama}.")
        else:
            print(f"Buku '{buku.judul}' tidak tersedia untuk dipinjam.")

    def kembalikan_buku(self, buku, anggota):
        if buku in anggota.buku_pinjaman:
            buku.status = "Tersedia"
            anggota.buku_pinjaman.remove(buku)
            print(f"Buku '{buku.judul}' berhasil dikembalikan oleh {anggota.nama}.")
        else:
            print(f"{anggota.nama} tidak memiliki buku '{buku.judul}' untuk dikembalikan.")


class Anggota:
    def __init__(self, nama, ID):
        self.nama = nama
        self.id = ID
        self.buku_pinjaman = []

    def tampilkan_buku_pinjaman(self, perpustakaan):
        if self.buku_pinjaman:
            print("--------------------------------")
            print(f"|| BUKU PINJAMAN {self.nama} ||")
            print("--------------------------------")
            for buku in self.buku_pinjaman:
                print(buku)

            judul_kembali = input("Masukkan judul buku yang ingin dikembalikan (Klik Enter langsung jika tidak jadi mengembalikan buku): ")
            if judul_kembali:
                buku = perpustakaan.cari_buku(judul_kembali)
                if buku:
                    perpustakaan.kembalikan_buku(buku, self)
                else:
                    print("Buku yang dimaksud tidak ditemukan.")
        else:
            print(f"{self.nama} tidak memiliki buku pinjaman.")


def main():
    buku1 = Buku("Jojo", "Araki", "Action", "Tersedia")
    buku2 = Buku("Pelangi", "Andrea Hirata", "Drama", "Tersedia")
    buku3 = Buku("Bumi", "Tere Liye", "Fiksi", "Dipinjam")

    perpustakaan = Perpustakaan()
    perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])

    anggota1 = Anggota("Ikhwan", 12345)
    anggota2 = Anggota("Ucheey", 56789)
    daftar_anggota = [anggota1, anggota2]

    while True:
        print("\n----------------------")
        print("|| MENU PERPUSTAKAAN ||")
        print("-----------------------")
        print("1. Tampilkan Daftar Buku")
        print("2. Cari Buku")
        print("3. Pinjam Buku")
        print("4. Tampilkan Buku Pinjaman / Kembalikan Buku")
        print("5. Keluar")
        pilihan = int(input("Pilih menu: "))

        if pilihan == 1:
            perpustakaan.tampilkan_buku()
        elif pilihan == 2:
            judul = input("Masukkan judul buku: ")
            buku = perpustakaan.cari_buku(judul)
            if buku:
                print(buku)
            else:
                print(f"Buku: '{judul}' tidak ditemukan.")

        elif pilihan == 3:
            judul_buku = input("Masukkan judul buku yang ingin dipinjam: ")
            nama_anggota = input("Masukkan nama anggota yang ingin meminjam: ")

            buku = perpustakaan.cari_buku(judul_buku)
            anggota = next((a for a in daftar_anggota if a.nama.lower() == nama_anggota.lower()), None)

            if buku and anggota:
                perpustakaan.pinjam_buku(buku, anggota)
            elif not buku:
                print(f"Buku '{judul_buku}' tidak ditemukan.")
            elif not anggota:
                print(f"Anggota dengan nama '{nama_anggota}' tidak ditemukan.")

        elif pilihan  == 4:
            nama_anggota = input("Masukkan nama anggota untuk melihat daftar pinjaman atau mengembalikan buku: ")
            anggota = next((a for a in daftar_anggota if a.nama.lower() == nama_anggota.lower()), None)

            if anggota:
                anggota.tampilkan_buku_pinjaman(perpustakaan)
            else:
                print("Anggota tidak ditemukan.")

        elif pilihan == 5:
            print("Terima kasih telah menggunakan sistem perpustakaan.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
