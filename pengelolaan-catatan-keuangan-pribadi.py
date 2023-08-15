import json

def simpan_data(laporan):
    with open("laporan.json", "w") as file:
        json.dump(laporan, file, indent="\t")

def muat_data():
    try:
        with open("laporan.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

laporan = muat_data()

def tambah_laporan(pendapatan):
    while True:
        deskripsi = input("Deskripsi: ")
        jumlah = int(input("Jumlah: "))
        print("============================================")

        valid = input("Yakin data tersebut benar? (y/t): ")
        if valid.lower() == 'y':
            hitung_penghasilan(deskripsi, jumlah, pendapatan)
            simpan_data(laporan)
            break


def hitung_penghasilan(deskripsi, jumlah, pendapatan):
    if not laporan: total = 0
    else:
        laporan_terakhir = laporan.get("laporan" + str(len(laporan)))
        total = laporan_terakhir.get("Jumlah")

    if pendapatan: total += jumlah
    else: total -= jumlah

    laporan['laporan' + str(len(laporan) + 1)] = {
        "Deskripsi": deskripsi,
        "Jumlah": total
    }

def tampil_laporan():
    if not laporan:
        print("Tidak ada laporan yang tersedia")
        print("============================================")
    else:
        k = 1
        for idx in laporan.values():
            print("Catatan Keuangan ke-" + str(k))
            k += 1
            print("============================================")
            for kolom, data in idx.items():
                print(kolom + ":", data)
            print("===========================================")

    back = input("Kembali? (Tekan Enter) ")

def main():
    try:
        while True:
            print("============================================")
            print("=== Pengelolaan Catatan Keuangan Pribadi ===")
            print("============================================")
            print("Menu:")
            print("1. Tambahkan pemasukan")
            print("2. Tambahkan pengeluaran")
            print("3. Tampilkan laporan")
            print("4. Keluar")
            print("============================================")
            pilih = int(input("Masukkan pilihan: "))
            print("============================================")

            if pilih == 1: tambah_laporan(True)
            elif pilih == 2: tambah_laporan(False)
            elif pilih == 3: tampil_laporan()
            elif pilih == 4: 
                print("Terima Kasih :)")
                print("============================================")
                simpan_data(laporan)
                break
            else: print("Mohon Maaf inputan tidak valid!!")
    except ValueError:
        print("============================================")
        print("Mohon maaf! Inputan Invalid! Terpaksa Keluar!")
        print("============================================")

main()