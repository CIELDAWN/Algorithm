import pandas as pd
import csv
import os
from tabulate import tabulate
import pyfiglet
from datetime import datetime

best_seller_data = pd.DataFrame({
    "No": [1, 2, 3, 4, 5, 6],
    "Best Seller": [
        "Beef Rendang",
        "Semarang Spring Roll",
        "Surabaya's Rawon",
        "Mont Blanc",
        "Mango Lassi",
        "Indoesia Luwak Coffe"]
})

menu_makanan = pd.DataFrame({
    "Tipe Menu": [
        "Main Course", 
        "Main Course", 
        "Main Course",
        "Main Course", 
        "Main Course", 
        "Main Course", 
        "Main Course", 
        "Side Dish", 
        "Side Dish", 
        "Side Dish", 
        "Side Dish",
        "Dessert",
        "Dessert",
        "Dessert",
        "Dessert",
        "Dessert",
        "Dessert",
        "Drink",
        "Drink",
        "Drink",
        "Drink",
        "Drink",
        "Drink",
        ],
    "Nama Menu" : [
        "Gado-Gado Jakarta",
        "Sour Palembang Ribs",
        "Lamongan Chiken Soup",
        "Oxtail Soup",
        "Rawon Surabaya",
        "Beef Rendang",
        "Purwakarta Maranggi Beef Satay",
        "Fried Cassava",
        "Fried Tofu",
        "Corn Fritters",
        "Semarang Spring Rolls",
        "Egg Tart",
        "Mont Blanc",
        "Baumkuchen",
        "Basque Cheesecake",
        "Castella",
        "Souffle Pancakes",
        "Virgin Mojito",
        "Indonesia Luwak Coffee",
        "Mango Lassi",
        "Macha Latte",
        "Chocolate Milkshake",
        "Mineral Water",
        ],
    "Description": [
        "Steamed Vegetable Salad With Egg, Tofu and Bean Cake, Spicy Peanut Sauce",
        "Braised Beef Ribs With Green Tomato And Belimbing Wuluh",
        "Sliced Chicken Soup With Glass Noodles In A Turmeric, Lemongrass And Chicken Broth",
        "Braised Or Fried Oxtail Marinated With Soya Sauce, Chill With Aromatic Herb Broth",
        "Braised Beef In Black Nut Broth Served With Bean Sprout And Salted Duck Egg",
        "Dry Spicy Indonesian Beef Curry With Coconut Milk, Galangal, Turmeric Leaf And Ginger Served With Eggplant Balado",
        "Coriander And Palm Sugar Marinated Beef Satay Served With Pickled Tomato, Chilli And Sweet Soya Sauce",
        "Traditional Indonesian Deep Fried Cassava Roots Served With Variety Of Coconut Sauces",
        "Deep Fried Bean Curd With Spicy Peanut Dipping Sauce And Bird's Eye Chili",
        "Corn Kernel Fritters With Topping Selections Of Salsa Mango - Chili Shallot-Lime And Com",
        "Fried Spring Rolls Of Bamboo Shot And Chicken Served With Garlic, Tauco Sauce And Pickles",
        "Egg Yolk Milk And Sugar",
        "Sponge Cake With Chestnut Cream",
        "Egg Whites Sugar Margarine And Liquid Milk",
        "Egg Sugar Cream Cheese Heavy Cream And Flour",
        "Flour Sugar And Eggs",
        "Medium Protein Flour, Sugar, Eggs, Liquid Milk, Baking Powder, Salt, And Vanilla Powder",
        "Made from fresh mint and soda water",
        "Luwak coffee is brewed coffee using coffee beans taken from the remains of civet/coconut civet droppings",
        "Mix of mango yogurt milk and a little sugar",
        "Matcha powder mixed with warm milk and sugar",
        "Milk ice cream and flavored syrup then shaken together",
        "Usual mineral water",
        ],
     "Price": [
        "175k",
        "265k",
        "215k",
        "256k",
        "225k",
        "275k",
        "215k",
        "10k",
        "10k",
        "10k",
        "10k",
        "90k",
        "115k",
        "100k",
        "115k",
        "95k",
        "95k",
        "115k",
        "90k",
        "70k",
        "115k",
        "80k",
        "55k",
    ]     
})
text = pyfiglet.figlet_format(text="G-CLASS", font= "slant")
print(text)


def kustomer():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("\n>> Best Seller Menu:")
        print(f"+{'-'*4}+{'-'*30}+")
        print(f"| {'No':<2} | {'Best Seller':<28} |")
        print(f"+{'-'*4}+{'-'*30}+")
        for _, row in best_seller_data.iterrows():
            print(f"| {row['No']:<2} | {row['Best Seller']:<28} |")
        print(f"+{'-'*4}+{'-'*30}+")
        print("=== Selamat Datang ===")
        print("1. Daftar Menu")
        print("2. Reservasi")
        print("3. Keluar")

        Pilihan = input("Pilih menu (1-3): ").strip()
        if Pilihan == '1':
            tampilkan_menu(menu_makanan)
        elif Pilihan == '2':
            reservasi()
        elif Pilihan == '3':
            print("Keluar dari program. Terima kasih!")
            break

def tampilkan_menu(menu_makanan):
    os.system("cls" if os.name == "nt" else "clear")
    print("Daftar Menu Restoran:\n")
    table = tabulate(
        menu_makanan.values,
        headers=menu_makanan.columns,
        tablefmt="grid",
        maxcolwidths=[12, 20, 50, 15],
        numalign="center",
        stralign="center"
    )
    print(table)
    while True:
        pilihan = input("\nKetik 'Kembali' untuk kembali ke menu utama: ").strip().lower()
        if pilihan == "kembali":
            break
        else:
            print("Input tidak valid. Silakan coba lagi.")

def reservasi():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("1. Pilihan VIP")
        print("2. Pilihan Publik")
        print("3. Keluar")

        Pilihan = input("Pilih Menu (1-3): ").strip()
        if Pilihan == '1':
            ruangan_vip()
        elif Pilihan == '2':
            ruangan_publik()
        elif Pilihan == '3':
            print("Keluar Dari Program. Terima kasih!")
            break

def ruangan_vip():
    os.system("cls" if os.name == "nt" else "clear")
    try:
        with open('data_meja_vip.csv', mode='r') as file:
            reader = csv.DictReader(file)
            meja_vip = list(reader)
            if not meja_vip:
                raise FileNotFoundError 
    except (FileNotFoundError, IOError):
        print("File data_meja_vip.csv tidak ditemukan atau kosong. Membuat data baru...")
        meja_vip = [
            {'Meja': '1A', 'Status': 'Tersedia'},
            {'Meja': '1B', 'Status': 'Tersedia'},
            {'Meja': '1C', 'Status': 'Tersedia'},
            {'Meja': '1D', 'Status': 'Tersedia'},
            {'Meja': '1E', 'Status': 'Tersedia'}
        ]
        with open('data_meja_vip.csv', mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['Meja', 'Status'])
            writer.writeheader()
            writer.writerows(meja_vip)
        print("File data_meja_vip.csv berhasil dibuat.")

    print("Daftar Meja VIP:")
    meja_headers = ["Meja", "Status"]
    meja_table = [[meja['Meja'], meja['Status']] for meja in meja_vip]
    print(tabulate(meja_table, headers=meja_headers, tablefmt="grid"))

    while True:
        meja_pilihan = input("Pilih Meja (1A-1E): ").strip().upper()
        if meja_pilihan in [meja['Meja'] for meja in meja_vip if meja['Status'] == 'Tersedia']:
            break
        print("Meja tidak tersedia atau sudah dipesan. Silakan pilih meja lain.")

    for meja in meja_vip:
        if meja['Meja'] == meja_pilihan:
            meja['Status'] = 'Tidak Tersedia'

    with open('data_meja_vip.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Meja', 'Status'])
        writer.writeheader()
        writer.writerows(meja_vip)

    print(f"Meja {meja_pilihan} berhasil dipilih.")

    while True:
        try:
            jumlah_orang = int(input("Masukkan jumlah orang: "))
            if jumlah_orang <= 0:
                print("Jumlah orang harus lebih dari 0.")
            else:
                break
        except ValueError:
            print("Jumlah orang harus berupa angka.")

    nama_pelanggan = input("Masukkan nama pelanggan: ").strip()
    no_telepon = input("Masukkan nomor telepon pelanggan: ").strip()
    
    print("\nPilih Tanggal:")
    print("Masukkan tanggal, buka jam (18.00-21.00)")
    while True:
        try:
            jam_pilihan = int(input("Masukkan pilihan tanggal: "))  
            if jam_pilihan == 1-31: 
                print("Harus dari 1-31")
            else:
                break
        except ValueError:
            print("Tanggal harus berupa angka.")

    print("pilih bulan: ")
    while True:
        try:
            bulan = str(input("Masukkan nama bulan: "))
            if bulan == str:
                print(" berhasil ditambahkan ")
            else:
                break
        except ValueError:
                print("Bulan harus berupa kata.")

    try:
        with open('stok_menu.csv', mode='r') as file:
            reader = csv.DictReader(file)
            stok_menu = list(reader)
    except FileNotFoundError:
        print("File stok_menu.csv tidak ditemukan.")
        stok_menu = []
        exit()

    for menu in stok_menu:
        try:
            menu['harga'] = int(menu['harga'].replace('k', '').strip()) * 1000 if 'k' in menu['harga'] else int(menu['harga'])
            menu['Stok_Menu'] = int(menu['Stok_Menu'])
        except ValueError:
            menu['harga'] = 0
            menu['Stok_Menu'] = 0

    print("\nDaftar Menu:")
    menu_headers = ["Tipe Menu", "Nama Menu","Harga (Rp)"]
    menu_table = [
        [menu['Tipe_Menu'], menu['Nama_Menu'], f"{menu['harga']:,}"]
        for menu in stok_menu
    ]
    print(tabulate(menu_table, headers=menu_headers, tablefmt="grid"))

    pesanan_list = []
    total_harga = 0

    while True:
        nama_menu = input("\nPilih Nama Menu (atau ketik 'Selesai' untuk mengakhiri): ").strip()
        if nama_menu.lower() == 'selesai':
            if not pesanan_list:
                print("Anda belum memilih menu. Pesanan gagal.")
                return  
        if nama_menu.lower() == 'selesai':
            break

        menu_item = next((menu for menu in stok_menu if menu['Nama_Menu'].lower() == nama_menu.lower()), None)
        if not menu_item:
            print("Nama Menu Tidak Tersedia.")
            continue

        while True:
            try:
                jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
                if jumlah_pesanan <= 0:
                    print("Jumlah pesanan harus lebih dari 0.")
                    continue
                break
            except ValueError:
                print("Jumlah Pesanan Harus Berupa Angka.")

        if jumlah_pesanan > menu_item['Stok_Menu']:
            print("Stok tidak cukup. Stok tersedia:", menu_item['Stok_Menu'])
            continue

        total_harga += jumlah_pesanan * menu_item['harga']
        menu_item['Stok_Menu'] -= jumlah_pesanan

        pesanan_list.append({
            'Meja': meja_pilihan,
            'nama_pelanggan': nama_pelanggan,
            'no_telepon': no_telepon,
            'jam_pilihan': jam_pilihan,
            'bulan': bulan,
            'jumlah_orang': jumlah_orang,
            'nama_menu': nama_menu,
            'jumlah_pesanan': jumlah_pesanan,
            'total_harga': jumlah_pesanan * menu_item['harga']
        })

    if pesanan_list:
        with open('data_pesanan.csv', mode='a', newline='') as file:
            fieldnames = ['Meja', 'nama_pelanggan', 'no_telepon', 'jam_pilihan', 'bulan', 'jumlah_orang', 'nama_menu', 'jumlah_pesanan', 'total_harga']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file.tell() == 0:
                writer.writeheader()
            writer.writerows(pesanan_list)

        print("\nRingkasan Pesanan:")
        for pesanan in pesanan_list:
            print(f"- {pesanan['nama_menu']} x{pesanan['jumlah_pesanan']} = Rp{pesanan['total_harga']:,}")
        print(f"Total Harga: Rp{total_harga:,}")
        print("\nPesanan berhasil dicatat.")
    else:
        print("Tidak ada pesanan yang dicatat.")

    with open('stok_menu.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Tipe_Menu', 'Nama_Menu', 'Stok_Menu', 'harga'])
        writer.writeheader()
        writer.writerows(stok_menu)
    print("\nPesanan berhasil dicatat.")
    print("=" * 80)
    print("G-CLASS".center(80, " ").upper())
    print("VIP".center(80, " ").upper())
    print("=" * 80)
    data_tiket = [
        ["Meja", meja_pilihan],
        ["Nama", nama_pelanggan],
        ["Tanggal", jam_pilihan],
        ["Bulan", bulan]
    ]

    tiket_table = tabulate(data_tiket, headers=["Detail", "Informasi"], tablefmt="grid", numalign="center", stralign="center")
    print(tiket_table)

    print("=" * 80)
    print("Terima kasih atas reservasi Anda!".center(80))
    print(f"Total harga semua pesanan: Rp{total_harga:,}".center(80))          
    print("=" * 80)


def ruangan_publik():
    os.system("cls" if os.name == "nt" else "clear")
    try:
        with open('data_meja_publik.csv', mode='r') as file:
            reader = csv.DictReader(file)
            meja_publik = list(reader)
            if not meja_publik:
                raise FileNotFoundError
    except (FileNotFoundError, IOError):
        print("File data_meja_publik.csv tidak ditemukan atau kosong. Membuat data baru...")
        meja_publik = [
            {'Meja': '1a', 'Status': 'Tersedia'},
            {'Meja': '2a', 'Status': 'Tersedia'},
            {'Meja': '1b', 'Status': 'Tersedia'},
            {'Meja': '2b', 'Status': 'Tersedia'},
            {'Meja': '1c', 'Status': 'Tersedia'},
            {'Meja': '2c', 'Status': 'Tersedia'},
            {'Meja': '1d', 'Status': 'Tersedia'},
            {'Meja': '2d', 'Status': 'Tersedia'},
            {'Meja': '1e', 'Status': 'Tersedia'},
            {'Meja': '2e', 'Status': 'Tersedia'}
        ]
        try:
            with open('data_meja_publik.csv', mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=['Meja', 'Status'])
                writer.writeheader()
                writer.writerows(meja_publik)
            print("File data_meja_publik.csv berhasil dibuat.")
        except IOError:
            print("Terjadi kesalahan saat membuat file data_meja_publik.csv.")
            exit()

    print("\nDaftar Meja publik:")
    meja_headers = ["Meja", "Status"]
    meja_table = [[meja['Meja'], meja['Status']] for meja in meja_publik]
    print(tabulate(meja_table, headers=meja_headers, tablefmt="grid"))

    while True:
        meja_pilihan = input("Pilih Meja (1a-2e): ").strip().lower()
        if meja_pilihan in [meja['Meja'] for meja in meja_publik if meja['Status'] == 'Tersedia']:
            break
        print("Meja tidak tersedia atau sudah dipesan. Silakan pilih meja lain.")

    for meja in meja_publik:
        if meja['Meja'] == meja_pilihan:
            meja['Status'] = 'Tidak Tersedia'

    with open('data_meja_publik.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Meja', 'Status'])
        writer.writeheader()
        writer.writerows(meja_publik)

    print(f"Meja {meja_pilihan} berhasil dipilih.")

    while True:
        try:
            jumlah_orang = int(input("Masukkan jumlah orang: "))
            if jumlah_orang <= 0:
                print("Jumlah orang harus lebih dari 0.")
            else:
                break
        except ValueError:
            print("Jumlah orang harus berupa angka.")

    nama_pelanggan = input("Masukkan nama pelanggan: ").strip()
    no_telepon = input("Masukkan nomor telepon pelanggan: ").strip()

    print("\nPilih Tanggal:")
    print("Masukkan tanggal, buka jam (18.00-21.00)")

    while True:
        try:
            jam_pilihan = int(input("Masukkan pilihan tanggal: "))  
            if jam_pilihan == 1-31: 
                print("Harus dari 1-31")
            else:
                break
        except ValueError:
            print("Tanggal harus berupa angka.")

    print("pilih bulan: ")
    while True:
        try:
            bulan = str(input("Masukkan nama bulan: "))
            if bulan == str:
                print(" berhasil ditambahkan ")
            else:
                break
        except ValueError:
                print("Bulan harus berupa kata.")
            
    try:
        with open('stok_menu.csv', mode='r') as file:
            reader = csv.DictReader(file)
            stok_menu = list(reader)
    except FileNotFoundError:
        print("File stok_menu.csv tidak ditemukan.")
        stok_menu = []
        exit()

    for menu in stok_menu:
        try:
            menu['harga'] = int(menu['harga'].replace('k', '').strip()) * 1000 if 'k' in menu['harga'] else int(menu['harga'])
            menu['Stok_Menu'] = int(menu['Stok_Menu'])
        except ValueError:
            menu['harga'] = 0
            menu['Stok_Menu'] = 0

    print("\nDaftar Menu:")
    menu_headers = ["Tipe Menu", "Nama Menu","Harga (Rp)"]
    menu_table = [
        [menu['Tipe_Menu'], menu['Nama_Menu'], f"{menu['harga']:,}"]
        for menu in stok_menu
    ]
    print(tabulate(menu_table, headers=menu_headers, tablefmt="grid"))

    pesanan_list = []
    total_harga = 0

    while True:
        nama_menu = input("\nPilih Nama Menu (atau ketik 'Selesai' untuk mengakhiri): ").strip()
        if nama_menu.lower() == 'selesai':
            if not pesanan_list:
                print("Anda belum memilih menu. Pesanan gagal.")
                return  
        if nama_menu.lower() == 'selesai':
            break

        menu_item = next((menu for menu in stok_menu if menu['Nama_Menu'].lower() == nama_menu.lower()), None)
        if not menu_item:
            print("Nama Menu Tidak Tersedia.")
            continue

        while True:
            try:
                jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
                if jumlah_pesanan <= 0:
                    print("Jumlah pesanan harus lebih dari 0.")
                    continue
                break
            except ValueError:
                print("Jumlah Pesanan Harus Berupa Angka.")

        if jumlah_pesanan > menu_item['Stok_Menu']:
            print("Stok tidak cukup. Stok tersedia:", menu_item['Stok_Menu'])
            continue

        total_harga += jumlah_pesanan * menu_item['harga']
        menu_item['Stok_Menu'] -= jumlah_pesanan

        pesanan_list.append({
            'Meja': meja_pilihan,
            'nama_pelanggan': nama_pelanggan,
            'no_telepon': no_telepon,
            'jam_pilihan': jam_pilihan,
            'bulan': bulan,
            'jumlah_orang': jumlah_orang,
            'nama_menu': nama_menu,
            'jumlah_pesanan': jumlah_pesanan,
            'total_harga': jumlah_pesanan * menu_item['harga']
        })

    if pesanan_list:
        with open('data_pesanan.csv', mode='a', newline='') as file:
            fieldnames = ['Meja', 'nama_pelanggan', 'no_telepon', 'jam_pilihan', 'bulan', 'jumlah_orang', 'nama_menu', 'jumlah_pesanan', 'total_harga']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file.tell() == 0:
                writer.writeheader()
            writer.writerows(pesanan_list)

        print("\nRingkasan Pesanan:")
        for pesanan in pesanan_list:
            print(f"- {pesanan['nama_menu']} x{pesanan['jumlah_pesanan']} = Rp{pesanan['total_harga']:,}")
        print(f"Total Harga: Rp{total_harga:,}")
        print("\nPesanan berhasil dicatat.")
    else:
        print("Tidak ada pesanan yang dicatat.")

    with open('stok_menu.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Tipe_Menu', 'Nama_Menu', 'Stok_Menu', 'harga'])
        writer.writeheader()
        writer.writerows(stok_menu)
    print("\nPesanan berhasil dicatat.")
    print("=" * 80)
    print("G-CLASS".center(80, " ").upper())
    print("Publik".center(80, " ").upper())
    print("=" * 80)
    data_tiket = [
        ["Meja", meja_pilihan],
        ["Nama", nama_pelanggan],
        ["Tanggal", jam_pilihan],
        ["Bulan", bulan]
    ]

    tiket_table = tabulate(data_tiket, headers=["Detail", "Informasi"], tablefmt="grid", numalign="center", stralign="center")
    print(tiket_table)

    print("=" * 80)
    print("Terima kasih atas reservasi Anda!".center(80))
    print(f"Total harga semua pesanan: Rp{total_harga:,}".center(80))          
    print("=" * 80)

def pegawai():
    os.system("cls" if os.name == "nt" else "clear")
    file_path = "data_user.csv"
    print("=== Silahkan Login ===")

    while True:
        usernamee = input("Masukkan nama user Anda: ").strip()
        passwordd = input("Masukkan password Anda: ").strip()

        try:
            with open(file_path, "r") as file:
                reader = csv.reader(file, delimiter=",")
                for row in reader:
                    if len(row) == 3:
                        username, password, role = row
                        if usernamee == username and passwordd == password:
                            print(f"Berhasil login sebagai {role}")
                            if role == "manajer":
                                data_restoran()
                            elif role == "pegawai kasir":
                                transaksi()
                            elif role == "pegawai dapur":
                                stok_menu()
                            else:
                                print("Role tidak dikenali.")
                            return
            print("Username atau password salah. Silakan coba lagi.")
        except FileNotFoundError:
            print("File data_user.csv tidak ditemukan.")
            return

def data_restoran():
    os.system("cls" if os.name == "nt" else "clear")
    print("\n=== Data Restoran ===")
    print("1. Stok Menu")
    print("2. Data Karyawan")
    print("3. Transaksi")
    print("4. Kembali")

    pilihan = input("Pilih menu (1/2/3/4): ").strip()
    if pilihan == "1":
        stok_menu()
    elif pilihan == "2":
        datakaryawan()
    elif pilihan == "3":
        transaksi()
    elif pilihan == "4":
        print("Kembali ke menu sebelumnya.")
    else:
        print("Pilihan tidak valid.")

def stok_menu():
    os.system("cls" if os.name == "nt" else "clear")
    file_path = "stok_menu.csv"
    print("=== Stok Menu ===")
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            menu = list(reader)

            headers = ["No"] + menu[0]  
            data = [[idx + 1] + row for idx, row in enumerate(menu[1:])] 
            
            print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

        while True:
            pilihan = input("Ingin memperbarui stok? (y/n): ").strip().lower()
            if pilihan == "y":
                indeks_menu = int(input("Masukkan nomor menu yang ingin diperbarui: ")) - 1
                if 0 <= indeks_menu < len(menu):
                    stok_baru = input("Masukkan stok baru: ").strip()
                    menu[indeks_menu+1][2] = stok_baru

                    with open(file_path, "w", newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(menu)
                    print(f"Stok untuk {menu[indeks_menu][2]} telah diperbarui menjadi {stok_baru} unit.")
                else:
                    print("Indeks yang dimasukkan tidak valid.")
            elif pilihan == "n":
                break
            else:
                print("Pilihan tidak valid. Masukkan 'y' atau 'n'.")
    except FileNotFoundError:
        print("File stok_menu.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi error: {e}")

def datakaryawan():
    os.system("cls" if os.name == "nt" else "clear")
    file_path = "D:\\G-class\\data_karyawan.csv"
    print("\n=== Data Karyawan ===")
    try:
        df = pd.read_csv(file_path)
        if not df.empty:
            print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
        else:
            print("File data_karyawan.csv kosong.")
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di path {file_path}.")
    except Exception as e:
        print(f"Terjadi error: {e}")

    while True:
        pilihan = input("Ingin kembali ke menu Data Restoran? (y/n): ").strip().lower()
        if pilihan == "y":
            data_restoran() 
            break
        elif pilihan == "n":
            print("Kembali ke menu sebelumnya.")
            break
        else:
            print("Pilihan tidak valid. Masukkan 'y' atau 'n'.")

def transaksi():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("=== Transaksi ===")
        print("1. Data Kostumer yang Sudah Pesan")
        print("2. mengubah status meja vip")
        print("3. mengubah status meja publik")
        print("4. Kembali ke menu sebelumnya")
        pilihan = input("Pilih menu (1/2/3/4): ").strip()

        if pilihan == "1":
            data_kostumer_pesan()
        elif pilihan == "2":
            ubah_status_meja_vip()
        elif pilihan == "3":
            ubah_status_meja_publik()
        elif pilihan == "4":
            print("Kembali ke menu sebelumnya.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
def ubah_status_meja_vip():
    os.system("cls" if os.name == "nt" else "clear")
    try:
        with open('data_meja_vip.csv', mode='r') as file:
            reader = csv.DictReader(file)
            meja_publik = list(reader)

            for meja in meja_publik:
                if meja['Status'] == 'Tidak Tersedia':
                    meja['Status'] = 'Tersedia'

        with open('data_meja_vip.csv', mode='w', newline='') as file:
            fieldnames = ['Meja', 'Status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(meja_publik)

        print("Status meja berhasil diperbarui. Semua meja yang tidak tersedia telah diubah menjadi tersedia.")
    
    except FileNotFoundError:
        print("File data_meja_publik.csv tidak ditemukan.")
        
def ubah_status_meja_publik():
    os.system("cls" if os.name == "nt" else "clear")
    try:
        with open('data_meja_publik.csv', mode='r') as file:
            reader = csv.DictReader(file)
            meja_publik = list(reader)

            for meja in meja_publik:
                if meja['Status'] == 'Tidak Tersedia':
                    meja['Status'] = 'Tersedia'

        with open('data_meja_publik.csv', mode='w', newline='') as file:
            fieldnames = ['Meja', 'Status']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(meja_publik)

        print("Status meja berhasil diperbarui. Semua meja yang tidak tersedia telah diubah menjadi tersedia.")
    
    except FileNotFoundError:
        print("File data_meja_publik.csv tidak ditemukan.")

def data_kostumer_pesan():
    os.system("cls" if os.name == "nt" else "clear")
    file_path = "data_pesanan.csv"
    print("\n=== Data Kostumer yang Sudah Dipesan ===")

    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            header = next(reader, None)
            rows = [row for row in reader]
        if not rows:
            print("Tidak ada data pesanan yang ditemukan.")
            return
        print(tabulate(rows, headers=header, tablefmt="grid"))
    except FileNotFoundError:
        print("File data_pesanan.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def main_menu():
    while True:
        print("===Selamat datang===")
        print("1. Kostumer")
        print("2. Pegawai")
        print("3. Keluar")

        Pilihan = input("Pilih menu (1-3): ").strip()
        if Pilihan == '1':
            kustomer()
        elif Pilihan == '2':
            pegawai()
        elif Pilihan == '3':
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")
if __name__ == "__main__":
    main_menu()