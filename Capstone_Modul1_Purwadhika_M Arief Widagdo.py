# Library import
from tabulate import tabulate
import sys
import time
import numpy as np #percobaan mengaplikasikan numpy


# The aim for this project is to simulate the interface of a shop front end of an RPG game
# The main objectives would be to do CRUD (Create, Read, Update, Delete) on the shop's and player's menu
# while making it immersive

uang_anda = 400
current_day = 1

# Tipe dan Kelangkaan
Alloweed_type = ["Senjata", "Artefak", "Pertahanan", "Konsumsi", "Perlengkapan"]
Alloweed_rare = ["Pasaran", "Langka", "Mistis"]

###Kode untuk fungsi dibawah adalah AI generated, semata-mata digunakan untuk masking password menjadi *, saya sudah coba beberapa cara lain tapi tidak bisa###
def input_with_asterisk(prompt=""):
    print(prompt, end="", flush=True)
    result = ""
    try:
        import msvcrt  # Only available on Windows
        while True:
            char = msvcrt.getch()
            if char in {b'\r', b'\n'}:  # Enter key
                print()
                break
            elif char == b'\x08':  # Backspace
                if len(result) > 0:
                    result = result[:-1]
                    sys.stdout.write('\b \b')
                    sys.stdout.flush()
            elif char == b'\x03':  # Ctrl+C
                raise KeyboardInterrupt
            else:
                result += char.decode('utf-8')
                sys.stdout.write('*')
                sys.stdout.flush()
    except ImportError:

        import getpass
        result = getpass.getpass(prompt)
    return result

###Akhir baris kode AI generated###

# Inventori utama toko, data dummy untuk tiap barang
barang_toko = [
    {"nama": "Pedang Besi", "harga": 100, "jumlah": 3, "tipe": "Senjata", "rarity": "Pasaran"},
    {"nama": "Perisai Tembaga", "harga": 150, "jumlah": 2, "tipe": "Pertahanan", "rarity": "Pasaran"},
    {"nama": "Potion", "harga": 50, "jumlah": 5, "tipe": "Konsumsi", "rarity": "Pasaran"},
    {"nama": "Keris Diponegoro", "harga": 5200, "jumlah": 1, "tipe": "Artefak", "rarity": "Mistis"},
    {"nama": "Obor", "harga": 20, "jumlah": 3, "tipe": "Perlengkapan", "rarity": "Pasaran"},
    {"nama": "Topi Antik", "harga": 50, "jumlah": 1, "tipe": "Perlengkapan", "rarity": "Pasaran"},
    {"nama": "Sepatu Baja", "harga": 180, "jumlah": 4, "tipe": "Perlengkapan", "rarity": "Pasaran"},
]

# Inventori pemain, untuk menyimpan barang yang dibeli
inventory_player = []
# Daftar untuk menyimpan barang yang dihapus dari toko, bekerja seperti inventory juga
history_hapus_barang = []


# Fungsi typewriter tambahan untuk lebih immersive
def typewriter(text, delay=0.02):
    #Efek typewriter untuk menampilkan kata per kata dengan jeda waktu
    for char in text: #looping tiap karakter di text
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

#Nyari abrang berdasarkan nama
def find_item_in_shop(nama_barang):
    for barang in barang_toko:
        if barang["nama"].lower() == nama_barang.lower():
            return barang
    return None

# [CREATE] - Menambahkan tipe barang baru ke toko
def create_item():
    typewriter("Menambahkan Barang Baru ke Stok Toko ")
    pesan_random = ["Serius harganya segitu? Turunin", "Yang bener aja harganya segitu! Turunkan!", "Turunkan Harga! jangan berkontribusi terhadap inflasi", "Cari ke toko sebelah aja kalau harga segini"] #buat test numpy

    # Input nama barang
    while True: #loop untuk menambahkkan nama barang
        nama_baru = input("Masukkan nama barang baru (atau 'q' untuk batal): ").title()
        if nama_baru.lower() == 'q':
            return
        if not nama_baru.strip(): #strip agar tidak kosong
            typewriter("ERROR: Nama barang tidak boleh kosong.")
            continue #balik ke atas
        if find_item_in_shop(nama_baru):
            typewriter(f"ERROR: Barang dengan nama '{nama_baru}' sudah ada di toko.")
            continue #balik ke atas
        break #keluar fungsi

    # Input harga barang
    while True: #loop harga
        harga_brg = input(f"Masukkan harga untuk {nama_baru} (atau 'q' untuk batal): ")
        if harga_brg.lower() == 'q':
            return
        if not harga_brg.isdigit():
            typewriter("ERROR: Harga harus berupa angka.")
            continue
        harga_baru = int(harga_brg)
        if harga_baru <= 0:
            typewriter("ERROR: Harga harus lebih besar dari 0.")
            continue
        if harga_baru >= 10000:
            nomor_random = np.random.randint(0, len(pesan_random)) #ambil index random dari length variable
            typewriter(pesan_random[nomor_random]) #menampilkan pesan berdasarkan index random yang dipilih
            continue
        break

    # Input jumlah stok
    while True: #loop jumlah stok
        jumlah_barang = input(f"Masukkan jumlah stok awal untuk {nama_baru} (atau 'q' untuk batal): ")
        if jumlah_barang.lower() == 'q':
            return
        if not jumlah_barang.isdigit():
            typewriter("ERROR: Jumlah harus berupa angka.")
            continue
        jumlah_baru = int(jumlah_barang)
        if jumlah_baru < 0:
            typewriter("ERROR: Jumlah stok tidak boleh negatif.")
            continue
        break

    # Input tipe barang dengan validasi
    # Alloweed_type = ["Senjata", "Artefak", "Pertahanan", "Konsumsi", "Perlengkapan"]
    while True: #loop tipe 
        tipe_baru = input(f"Masukkan tipe untuk {nama_baru} {Alloweed_type} (atau 'q' untuk batal): ").title()
        if tipe_baru.lower() == 'q':
            return
        if tipe_baru not in Alloweed_type:
            typewriter(f"ERROR: Tipe harus salah satu dari {Alloweed_type}.")
            continue
        break

    # Input rarity barang dengan validasi
    # Alloweed_rare = ["Pasaran", "Langka", "Mistis"]
    while True: #loop rarity 
        rarity_baru = input(f"Masukkan rarity untuk {nama_baru} {Alloweed_rare} (atau 'q' untuk batal): ").title()
        if rarity_baru.lower() == 'q':
            return
        if rarity_baru not in Alloweed_rare:
            typewriter(f"ERROR: Rarity harus salah satu dari {Alloweed_rare}.")
            continue
        break

    new_item_data = [{
        "nama": nama_baru,
        "harga": harga_baru,
        "jumlah": jumlah_baru,
        "tipe": tipe_baru,
        "rarity": rarity_baru
    }]
    print("\nData barang baru yang akan ditambahkan:")
    print(tabulate(new_item_data, headers='keys', tablefmt='rounded_outline'))
    konfirmasi = input("Simpan data barang baru ini? (y/n): ").lower()

    if konfirmasi == 'y':
        barang_toko.append(new_item_data[0])
        typewriter(f"\nSukses! '{nama_baru}' telah ditambahkan ke stok toko.")
        time.sleep(1.5)
    else:
        typewriter("\nPenambahan barang dibatalkan.")

# [READ] - Menampilkan data barang di toko
def read_data():
    while True:
        typewriter("\n--- Menu Lihat Stok Toko ---")
        if not barang_toko:
            typewriter("Stok toko saat ini kosong.")
            return

        print("1. Tampilkan Semua Barang")
        print("2. Cari Barang Berdasarkan Nama")
        print("3. Urutkan Harga: Termurah ke Termahal")
        print("4. Urutkan Harga: Termahal ke Termurah")
        print("5. Filter Berdasarkan Tipe")
        print("6. Kembali")
        choice = input("Pilih menu (1-6): ")

        if choice == '1':
            typewriter("\nDaftar semua barang di toko:")
            print(tabulate(barang_toko, headers='keys', tablefmt='rounded_outline'))
        elif choice == '2':
            nama_barang = input("Masukkan nama barang yang ingin dicari: ")
            item_found = find_item_in_shop(nama_barang)
            if item_found:
                typewriter(f"\nData untuk '{item_found['nama']}':")
                print(tabulate([item_found], headers='keys', tablefmt='rounded_outline'))
            else:
                typewriter(f"Barang dengan nama '{nama_barang}' tidak ditemukan.")
        elif choice == '3':
            sorted_data = sorted(barang_toko, key=lambda x: x['harga'])
            typewriter("\nDaftar barang diurutkan dari termurah:")
            print(tabulate(sorted_data, headers='keys', tablefmt='rounded_outline'))
        elif choice == '4':
            sorted_data = sorted(barang_toko, key=lambda x: x['harga'], reverse=True)
            typewriter("\nDaftar barang diurutkan dari termahal:")
            print(tabulate(sorted_data, headers='keys', tablefmt='rounded_outline'))
        elif choice == '5':
            typewriter("Pilih tipe untuk difilter:")
            for i, tipe in enumerate(Alloweed_type):
                print(f"{i + 1}. {tipe}")
            
            tipe_choice_str = input(f"Pilih tipe (1-{len(Alloweed_type)}): ")
            if tipe_choice_str.isdigit():
                tipe_choice_idx = int(tipe_choice_str) - 1 #buat nyamain sama angka yg diketik user
                if 0 <= tipe_choice_idx < len(Alloweed_type):
                    chosen_type = Alloweed_type[tipe_choice_idx]
                    filtered_data = [item for item in barang_toko if item['tipe'] == chosen_type]
                    if filtered_data:
                        typewriter(f"\nDaftar barang dengan tipe '{chosen_type}':")
                        print(tabulate(filtered_data, headers='keys', tablefmt='rounded_outline'))
                    else:
                        typewriter(f"Tidak ada barang dengan tipe '{chosen_type}' ditemukan.")
                else:
                    typewriter("Pilihan tipe tidak valid.")
            else:
                typewriter("Input tidak valid. Harap masukkan angka.")
        elif choice == '6':
            break
        else:
            typewriter("Pilihan tidak valid.")

# [UPDATE] - Mengubah detail barang di toko
def update_item():
    
    typewriter("\n--- Mengubah Data Barang di Toko ---")
    if not barang_toko:
        typewriter("Stok toko kosong, tidak ada yang bisa diubah.")
        return

    item_to_update = None
    while True: 
        print(tabulate(barang_toko, headers='keys', tablefmt='rounded_outline'))
        nama_barang = input("Masukkan nama barang yang ingin diubah (atau 'q' untuk batal): ").title()
        if nama_barang.lower() == 'q':
            return #keluar

        item_to_update = find_item_in_shop(nama_barang)
        if not item_to_update:
            typewriter(f"ERROR: Barang '{nama_barang}' tidak ditemukan.")
            continue #balik ke atas
        break 

    while True: # loop modifikasi setelah konsultasi
        typewriter(f"\nAnda akan mengubah data untuk '{item_to_update['nama']}'.")
        print("Pilih data yang ingin diubah:")
        print("1. Harga")
        print("2. Jumlah Stok")
        print("3. Tipe")
        print("4. Rarity")
        print("5. Selesai Mengubah / Kembali")
        pilihan_edit = input("Pilih (1-5): ")
        
        updated = False

        
        if pilihan_edit == '1':
            
            while True: # Loop untuk harga
                nilai_str = input(f"Masukkan harga baru (saat ini: {item_to_update['harga']}) (atau 'q' untuk batal): ")
                if nilai_str.lower() == 'q': break
                if not nilai_str.isdigit():
                    typewriter("ERROR: Harga harus berupa angka.")
                    continue
                nilai_baru = int(nilai_str)
                if nilai_baru <= 0:
                    typewriter("ERROR: Harga baru harus lebih besar dari 0.")
                    continue
                if nilai_baru >= 10000:
                    typewriter("Janganlah anda berkontribusi terhadap inflasi.")
                    continue
                item_to_update['harga'] = nilai_baru
                updated = True
                break
        elif pilihan_edit == '2':
            while True: # Loop untuk stok
                nilai_str = input(f"Masukkan jumlah stok baru (saat ini: {item_to_update['jumlah']}) (atau 'q' untuk batal): ")
                if nilai_str.lower() == 'q': break
                if not nilai_str.isdigit():
                    typewriter("ERROR: Jumlah stok harus berupa angka.")
                    continue
                nilai_baru = int(nilai_str)
                if nilai_baru < 0:
                    typewriter("ERROR: Jumlah stok baru tidak boleh negatif.")
                    continue
                item_to_update['jumlah'] = nilai_baru
                updated = True
                break
        elif pilihan_edit == '3':
            while True:
                nilai_baru = input(f"Masukkan tipe baru {Alloweed_type} (saat ini: {item_to_update['tipe']}) (atau 'q' untuk batal): ").title()
                if nilai_baru.lower() == 'q': break
                if nilai_baru not in Alloweed_type:
                    typewriter(f"ERROR: Tipe harus salah satu dari {Alloweed_type}.")
                    continue
                item_to_update['tipe'] = nilai_baru
                updated = True
                break
        elif pilihan_edit == '4':
            while True:
                nilai_baru = input(f"Masukkan rarity baru {Alloweed_rare} (saat ini: {item_to_update['rarity']}) (atau 'q' untuk batal): ").title()
                if nilai_baru.lower() == 'q': break
                if nilai_baru not in Alloweed_rare:
                    typewriter(f"ERROR: Rarity harus salah satu dari {Alloweed_rare}.")
                    continue
                item_to_update['rarity'] = nilai_baru
                updated = True
                break
        elif pilihan_edit == '5':
            typewriter("Kembali ke menu manajemen toko.")
            break
        else:
            typewriter("Pilihan edit tidak valid. Silakan pilih dari 1-5.")
            continue
        
        if updated:
            typewriter(f"\nSukses! Data untuk '{item_to_update['nama']}' telah diubah.")
            print(tabulate([item_to_update], headers='keys', tablefmt='rounded_outline'))

# [DELETE] - Menghapus tipe barang dari toko
def delete_item():
    typewriter("\n--- Menghapus Barang dari Stok Toko ---")
    if not barang_toko:
        typewriter("Stok toko kosong, tidak ada yang bisa dihapus.")
        return

    item_to_delete = None
    while True: # Loop untuk memilih barang yang mau dihapus
        print(tabulate(barang_toko, headers='keys', tablefmt='rounded_outline'))
        nama_barang = input("Masukkan nama barang yang ingin dihapus (atau 'q' untuk batal): ").title()
        if nama_barang.lower() == 'q':
            return

        item_to_delete = find_item_in_shop(nama_barang)
        if not item_to_delete:
            typewriter(f"ERROR: Barang '{nama_barang}' tidak ditemukan.")
            continue # 
        break 

    konfirmasi = input(f"Anda yakin ingin menghapus '{item_to_delete['nama']}' dari daftar toko? (y/n): ").lower()
    #konfirmasi biar ga kepencet
    if konfirmasi == 'y':
        history_hapus_barang.append(item_to_delete) #tambahin barang yang dihapus ke sini
        barang_toko.remove(item_to_delete)
        typewriter(f"Sukses! '{nama_barang}' telah dihapus dari toko dan dicatat dalam history.")
        time.sleep(1.5)
    else:
        typewriter("Penghapusan dibatalkan.")

def view_deleted_items():
    typewriter("\n--- History Barang yang Dihapus ---")
    if not history_hapus_barang:
        typewriter("Tidak ada barang dalam history penghapusan.")
        input("Tekan Enter untuk kembali...")
        return

    print(tabulate(history_hapus_barang, headers='keys', tablefmt='rounded_outline'))
    input("\nTekan Enter untuk kembali ke menu manajemen.")

def restore_item():
    typewriter("\n--- Restore Barang dari History ---")
    if not history_hapus_barang:
        typewriter("History penghapusan kosong, tidak ada yang bisa di-restore.")
        return

    print("Daftar barang yang bisa di-restore:")
    print(tabulate(history_hapus_barang, headers='keys', tablefmt='rounded_outline'))

    while True:
        nama_barang = input("\nMasukkan nama barang yang ingin di-restore (atau 'q' untuk batal): ").title()
        if nama_barang.lower() == 'q':
            typewriter("Proses restore dibatalkan.")
            return

        item_to_restore = None
        for item in history_hapus_barang:
            if item['nama'].lower() == nama_barang.lower():
                item_to_restore = item
                break
        
        if not item_to_restore:
            typewriter(f"ERROR: Barang '{nama_barang}' tidak ditemukan di history.")
            continue

        existing_shop_item = find_item_in_shop(item_to_restore['nama'])

        if existing_shop_item:
            typewriter(f"Barang '{nama_barang}' sudah ada di toko. Jumlah akan ditambahkan.")
            existing_shop_item['jumlah'] += item_to_restore['jumlah']
        else:
            barang_toko.append(item_to_restore)

        history_hapus_barang.remove(item_to_restore)
        typewriter(f"\nSukses! '{nama_barang}' telah di-restore ke toko.")
        time.sleep(1.5)
        break

# Player yang beli barang
def beli_barang():
    global uang_anda
    typewriter("\nBarang yang tersedia di toko:")
    print(tabulate(barang_toko, headers='keys', tablefmt='rounded_outline'))
    while True:
        nama_barang = input("Masukkan nama barang yang ingin dibeli (atau 'q' untuk kembali): ").title()
        if nama_barang.lower() == 'q':
            return

        barang_found = find_item_in_shop(nama_barang)
        if barang_found:
            if barang_found['jumlah'] == 0:
                typewriter(f"Maaf, stok {barang_found['nama']} sudah habis.")
                continue

            while True: # Loop untuk input jumlah
                jumlah_beli_str = input(f"Berapa banyak {barang_found['nama']} yang ingin dibeli? (tersedia {barang_found['jumlah']}) (atau 'q' untuk batal): ")
                
                if jumlah_beli_str.lower() == 'q':
                    typewriter(f"Pembelian {barang_found['nama']} dibatalkan.")
                    break

                if not jumlah_beli_str.isdigit():
                    typewriter("Input tidak valid. Harap masukkan angka.")
                    continue

                jumlah_beli = int(jumlah_beli_str)

                if jumlah_beli <= 0:
                    typewriter("Jumlah beli harus lebih dari 0.")
                    continue
                if jumlah_beli > barang_found["jumlah"]:
                    typewriter(f"Maaf, stok {barang_found['nama']} hanya tersisa {barang_found['jumlah']}. Mohon masukkan jumlah yang sesuai.")
                    continue
                
                total_harga = barang_found["harga"] * jumlah_beli
                if uang_anda >= total_harga:
                    uang_anda -= total_harga
                    barang_found["jumlah"] -= jumlah_beli

                    # Tambahkan barang ke inventory player
                    inventory_found = False
                    for item_inv in inventory_player: # biar ga ketuker antar var
                        if item_inv["nama"].lower() == barang_found["nama"].lower():
                            item_inv["jumlah"] += jumlah_beli
                            inventory_found = True
                            break
                    if not inventory_found:
                        harga_beli_player = barang_found["harga"] // 2  # Harga dibuat setengah karena slogan toko ---Menjual engan harga mahal membeli dengan harga Murah---
                        inventory_player.append({
                        "nama": barang_found["nama"],
                        "harga": harga_beli_player,
                        "jumlah": jumlah_beli,
                        "tipe": barang_found["tipe"],
                        "rarity": barang_found["rarity"]
                    })
                    typewriter(f"\nAnda berhasil membeli {jumlah_beli} {barang_found['nama']} seharga {total_harga} Emas.")
                    typewriter(f"Sisa uang Anda: {uang_anda} Emas.")
                    time.sleep(1.5) #biar ga jegrak langsung return, tambah imersi
                    return # keluar beli_barang function
                else:
                    typewriter("Maaf, kekuatan Kapitalis anda tidak cukup.")
                    break # kembali ke pemilihan barang
        else:
            typewriter("Barang tidak ditemukan di toko.")

def jual_barang():
    global uang_anda
    if not inventory_player:
        typewriter("\nInventory Anda kosong.")
        return

    typewriter("\nInventory Anda:")
    print(tabulate(inventory_player, headers='keys', tablefmt='rounded_outline'))

    while True:
        nama_barang_jual = input("Masukkan nama barang yang ingin Anda jual (atau 'q' untuk kembali): ").title()
        if nama_barang_jual.lower() == 'q':
            return

        item_in_inventory = None
        for barang_inv in inventory_player:
            if barang_inv["nama"].lower() == nama_barang_jual.lower():
                item_in_inventory = barang_inv
                break

        if item_in_inventory:
            jumlah_jual_str = input(f"Berapa banyak {item_in_inventory['nama']} yang ingin dijual? (Anda punya {item_in_inventory['jumlah']}): ")
            if not jumlah_jual_str.isdigit():
                typewriter("Input tidak valid. Harap masukkan angka.")
                continue

            jumlah_jual = int(jumlah_jual_str)

            if jumlah_jual <= 0:
                typewriter("Jumlah jual harus lebih dari 0.")
                continue
            if jumlah_jual <= item_in_inventory["jumlah"]:
                harga_jual_per_item = item_in_inventory["harga"] 
                total_pendapatan = harga_jual_per_item * jumlah_jual
                uang_anda += total_pendapatan
                item_in_inventory["jumlah"] -= jumlah_jual

                # Restore
                shop_item_ref = find_item_in_shop(item_in_inventory["nama"])
                if shop_item_ref:
                    shop_item_ref['jumlah'] += jumlah_jual
                else:
                    # Barang tidak ada di toko
                    barang_toko.append({
                        "nama": item_in_inventory["nama"],
                        "harga": item_in_inventory["harga"],  # Harga awal
                        "jumlah": jumlah_jual,
                        "tipe": item_in_inventory["tipe"],
                        "rarity": item_in_inventory["rarity"]
                    })

                if item_in_inventory["jumlah"] == 0:
                    inventory_player.remove(item_in_inventory)

                typewriter(f"\nAnda berhasil menjual {jumlah_jual} {item_in_inventory['nama']} seharga {total_pendapatan} Emas.")
                typewriter(f"Uang Anda sekarang: {uang_anda} Emas.")
                time.sleep(1.5)
                return 
            else:
                typewriter(f"Maaf, Anda hanya memiliki {item_in_inventory['jumlah']} {item_in_inventory['nama']}.")
        else:
            typewriter("Barang tidak ditemukan di inventory Anda.")

def view_player_inventory():
    if not inventory_player:
        typewriter("\nInventory Anda kosong.")
        input("Tekan Enter untuk melanjutkan ")
        return

    typewriter("\nInventory Anda:")
    print(tabulate(inventory_player, headers='keys', tablefmt='rounded_outline'))
    input("Tekan Enter untuk melanjutkan ")

def next_day():
    global current_day, uang_anda
    konfirmasi = input("\nAnda yakin pergi ke hari selanjutnya? (y/n): ").lower()
    if konfirmasi == 'y':
        typewriter("Anda telah pergi ke hari selanjutnya.", delay=0.03)
        current_day += 1
        uang_anda += 50  # Add 50 gold every new day
        typewriter("Uang anda bertambah 50 Emas.")
        typewriter("Berganti hari")
        typewriter(". . .", delay=0.25)
    else:
        typewriter("Hari ini masih berlanjut, silakan pilih menu lain.")

# Menu khusus Manajemen Toko
def shop_management_menu():
    while True:
        print("\n*** Menu Manajemen Toko ***")
        print("1. Lihat Data Barang Toko")
        print("2. Tambah Barang Baru ke Toko")
        print("3. Ubah Data Barang Toko")
        print("4. Hapus Barang dari Toko")
        print("5. Lihat Barang yang Dihapus")
        print("6. Restore Barang")
        print("7. Kembali ke Menu Utama")

        choice = input("\nPilih Menu (1-7): ")
        if choice == '1':
            read_data()
        elif choice == '2':
            create_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            view_deleted_items()
        elif choice == '6':
            restore_item()
        elif choice == '7':
            break
        else:
            typewriter("Pilihan tidak valid, silakan coba lagi.")

# Menu khusus Interaksi Pemain
def player_interaction_menu():
    first_run = True #Buat run pertama saja
    while True:
        if first_run:
            typewriter("="*20)
            typewriter("Selamat datang di Toko Loak Er Pi Ji")
            typewriter("Kami membeli barang anda dengan harga murah")
            typewriter("Kami menjual ke anda dengan harga mahal")
            first_run = False #Setelah run pertama Welcome bannernya tidak dimunculkan lagi

        print(f"\n*** [Hari ke-{current_day} | Uang: {uang_anda} Emas] ***")
        print("\n*** Menu Interaksi Pemain ***")
        print("1. Beli Barang")
        print("2. Jual Barang")
        print("3. Lihat Inventory Anda")
        print("4. Hari Selanjutnya")
        print("5. Kembali ke Menu Utama")

        choice = input("\nPilih Menu (1-5): ")
        if choice == '1':
            beli_barang()
        elif choice == '2':
            jual_barang()
        elif choice == '3':
            view_player_inventory()
        elif choice == '4':
            next_day()
        elif choice == '5':
            break
        else:
            typewriter("Pilihan tidak valid, silakan coba lagi.")


# Menu Utama
def main_menu():
    while True:
        print("="*20)
        print("MENU UTAMA")
        print("1. Manajemen Toko")
        print("2. Interaksi Pemain")
        print("3. Keluar")
        choice = input("\nPilih Menu (1-3): ")

        if choice == '1':
            try:
                password = input_with_asterisk("Masukkan Password (angka apapun): ")
                if not password:
                    typewriter("Password tidak boleh kosong.")
                    time.sleep(1)
                    continue
                int(password) 
                typewriter("Password diterima. Memasuki mode manajemen...")
                time.sleep(1)
                shop_management_menu()
            except ValueError:
                typewriter("Password salah. Harus berupa angka.")
                time.sleep(1)

        elif choice == '2':
            player_interaction_menu()
        elif choice == '3':
            typewriter("Terima kasih telah berkunjung!")
            break
        else:
            typewriter("Pilihan tidak valid, silakan coba lagi.")

# Menu utama untuk menjalankan program
if __name__ == "__main__":
    main_menu()