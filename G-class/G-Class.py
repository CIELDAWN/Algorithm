import pandas as pd
import csv
import os
from tabulate import tabulate
import pyfiglet
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

        choice = input("Pilih menu (1-3): ").strip()
        if choice == '1':
            tampilkan_menu(menu_makanan)
        elif choice == '2':
            reservasi()
        elif choice == '3':
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

        choice = input("Pilih Menu (1-3): ").strip()
        if choice == '1':
            ruangan_vip()
        elif choice == '2':
            ruangan_publik()
        elif choice == '3':
            print("Keluar Dari Program. Terima kasih!")
            break

def ruangan_vip():
    try:
        with open('data_meja_vip.csv', mode='r') as file:
            reader = csv.DictReader(file)
            meja_vip = list(reader)
    except FileNotFoundError:
        print("File data_meja_vip.csv tidak ditemukan.")
        return

    print("\nDaftar Meja VIP:")
    meja_headers = ["Meja"]
    meja_table = [[meja['Meja']] for meja in meja_vip]
    print(tabulate(meja_table, headers=meja_headers, tablefmt="grid"))

    meja_pilihan = input("Pilih Meja (1A-1E): ").strip()
    
    if meja_pilihan not in [meja['Meja'] for meja in meja_vip]:
        print("Meja tidak tersedia.")
        return

    meja_vip = [meja for meja in meja_vip if meja['Meja'] != meja_pilihan]

    try:
        jumlah_orang = int(input("Masukkan jumlah orang: "))
    except ValueError:
        print("Jumlah orang harus berupa angka.")
        return

    nama_pelanggan = input("Masukkan nama pelanggan: ").strip()
    no_telepon = input("Masukkan nomor telepon pelanggan: ").strip()
    print("\nPilih Jam:")
    print("1. Siang (13.00 - 15.00)")
    print("2. Malam (19.00 - 21.00)")
    
    try:
        jam_pilihan = str(input("Masukkan pilihan jam (Siang/Malam): ")).strip()
    except ValueError:
        print("Harus Berupa kalimat.")

    try:
        with open('stok_menu.csv', mode='r') as file:
            reader = csv.DictReader(file)
            stok_menu = list(reader)
    except FileNotFoundError:
        print("File stok_menu.csv tidak ditemukan.")
        return

    for menu in stok_menu:
        menu['harga'] = int(menu['harga'].replace('k', '').strip()) * 1000 if 'k' in menu['harga'] else int(menu['harga'])
        menu['Stok_Menu'] = int(menu['Stok_Menu'])

    print("\nDaftar Menu:")
    menu_headers = ["Tipe Menu", "Nama Menu", "Stok Tersedia", "Harga (Rp)"]
    menu_table = [
        [menu['Tipe_Menu'], menu['Nama_Menu'], menu['Stok_Menu'], f"{menu['harga']:,}"]
        for menu in stok_menu
    ]
    print(tabulate(menu_table, headers=menu_headers, tablefmt="grid"))

    pesanan_list = []
    total_harga = 0

    while True:
        nama_menu = input("\nPilih Nama Menu (atau ketik 'Selesai' untuk mengakhiri): ").strip()

        if nama_menu.lower() == 'selesai':
            break

        menu_item = next((menu for menu in stok_menu if menu['Nama_Menu'] == nama_menu), None)
        if not menu_item:
            print("Nama Menu Tidak Tersedia.")
            continue

        try:
            jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
        except ValueError:
            print("Jumlah Pesanan Harus Berupa Angka.")
            continue

        if jumlah_pesanan > menu_item['Stok_Menu']:
            print("Stok tidak cukup. Stok tersedia:", menu_item['Stok_Menu'])
            continue

        harga_menu = menu_item['harga']
        total_harga += jumlah_pesanan * harga_menu

        menu_item['Stok_Menu'] -= jumlah_pesanan

        pesanan_list.append ({
            'Meja': meja_pilihan,
            'nama_pelanggan': nama_pelanggan,
            'no_telepon': no_telepon,
            'jam_pilihan': jam_pilihan,
            'jumlah_orang': jumlah_orang,
            'nama_menu': nama_menu,
            'jumlah_pesanan': jumlah_pesanan,
            'total_harga': jumlah_pesanan * harga_menu
            
        })

    if not pesanan_list:
        print("Tidak ada pesanan yang dicatat.")
        return

    try:
        with open('data_pesanan.csv', mode='a', newline='') as file:
            fieldnames = ['Meja', 'nama_pelanggan', 'no_telepon', 'jam_pilihan', 'jumlah_orang', 'nama_menu', 'jumlah_pesanan', 'total_harga']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            file.seek(0, 2)
            if file.tell() == 0:
                writer.writeheader()

            writer.writerows(pesanan_list)
    except FileNotFoundError:
        with open('data_pesanan.csv', mode='w', newline='') as file:
            fieldnames = ['Meja',  'nama_pelanggan', 'no_telepon','jam_pilihan', 'jumlah_orang', 'nama_menu', 'jumlah_pesanan', 'total_harga']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(pesanan_list)

    print("\nPesanan berhasil dicatat.")
    print("=" * 80)
    print("G-CLASS".center(80, " ").upper())
    print("VIP".center(80, " ").upper())
    print("=" * 80)
    data_tiket = [
        ["Meja", meja_pilihan],
        ["Nama", nama_pelanggan],
        ["Siang/Malam", jam_pilihan]
    ]

    tiket_table = tabulate(data_tiket, headers=["Detail", "Informasi"], tablefmt="grid", numalign="center", stralign="center")
    print(tiket_table)

    print("=" * 80)
    print("Terima kasih atas reservasi Anda!".center(80))
    print(f"Total harga semua pesanan: Rp{total_harga:,}".center(80))          
    print("=" * 80)
    
def ruangan_publik():
    try:
        with open('data_meja_public.csv', mode='r') as file:
            reader = csv.reader(file)
            header = next(reader) 
            meja_data = [row for row in reader]
    except FileNotFoundError:
        print("File data_meja_public.csv tidak ditemukan.")
        return

    print("\nDaftar Meja Publik:")
    meja_table = []
    for i, row in enumerate(meja_data, start=1):  
        for j, _ in enumerate(row, start=1):  
            meja_table.append([f"{i}{chr(96 + j)}"])  

    print(tabulate(meja_table, headers=["Meja"], tablefmt="grid"))

    meja_pilihan = input("Pilih Meja (contoh: 1a-5e): ").strip()

    if meja_pilihan not in [row[0] for row in meja_table]:
        print("Meja tidak tersedia.")
        return
    try:
        jumlah_orang = int(input("Masukkan jumlah orang: "))
    except ValueError:
        print("Jumlah orang harus berupa angka.")
        return

    print(f"Meja {meja_pilihan} berhasil dipilih.")


    nama_pelanggan = input("Masukkan nama pelanggan: ").strip()
    no_telepon = input("Masukkan nomor telepon pelanggan: ").strip()
    print("\nPilih Jam:")
    print("1. Siang (13.00 - 15.00)")
    print("2. Malam (19.00 - 21.00)")
    
    try:
        jam_pilihan = str(input("Masukkan pilihan jam (Siang/Malam): ")).strip()
    except ValueError:
        print("Harus Berupa kalimat.")

    try:
        with open('stok_menu.csv', mode='r') as file:
            reader = csv.DictReader(file)
            stok_menu = list(reader)
    except FileNotFoundError:
        print("File stok_menu.csv tidak ditemukan.")
        return

    for menu in stok_menu:
        menu['harga'] = int(menu['harga'].replace('k', '').strip()) * 1000 if 'k' in menu['harga'] else int(menu['harga'])
        menu['Stok_Menu'] = int(menu['Stok_Menu'])

    print("\nDaftar Menu:")
    menu_headers = ["Tipe Menu", "Nama Menu", "Stok Tersedia", "Harga (Rp)"]
    menu_table = [
        [menu['Tipe_Menu'], menu['Nama_Menu'], menu['Stok_Menu'], f"{menu['harga']:,}"]
        for menu in stok_menu
    ]
    print(tabulate(menu_table, headers=menu_headers, tablefmt="grid"))

    pesanan_list = []
    total_harga = 0

    while True:
        nama_menu = input("\nPilih Nama Menu (atau ketik 'Selesai' untuk mengakhiri): ").strip()

        if nama_menu.lower() == 'selesai':
            break

        menu_item = next((menu for menu in stok_menu if menu['Nama_Menu'] == nama_menu), None)
        if not menu_item:
            print("Nama Menu Tidak Tersedia.")
            continue

        try:
            jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))
        except ValueError:
            print("Jumlah Pesanan Harus Berupa Angka.")
            continue

        if jumlah_pesanan > menu_item['Stok_Menu']:
            print("Stok tidak cukup. Stok tersedia:", menu_item['Stok_Menu'])
            continue

        harga_menu = menu_item['harga']
        total_harga += jumlah_pesanan * harga_menu

        menu_item['Stok_Menu'] -= jumlah_pesanan

        pesanan_list.append ({
            'Meja': meja_pilihan,
            'nama_pelanggan': nama_pelanggan,
            'no_telepon': no_telepon,
            'jam_pilihan': jam_pilihan,
            'jumlah_orang': jumlah_orang,
            'nama_menu': nama_menu,
            'jumlah_pesanan': jumlah_pesanan,
            'total_harga': jumlah_pesanan * harga_menu
            
        })

    if not pesanan_list:
        print("Tidak ada pesanan yang dicatat.")
        return

    try:
        with open('data_pesanan.csv', mode='a', newline='') as file:
            fieldnames = ['Meja', 'nama_pelanggan', 'no_telepon', 'jam_pilihan', 'jumlah_orang', 'nama_menu', 'jumlah_pesanan', 'total_harga']
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            file.seek(0, 2)
            if file.tell() == 0:
                writer.writeheader()

            writer.writerows(pesanan_list)
    except FileNotFoundError:
        with open('data_pesanan.csv', mode='w', newline='') as file:
            fieldnames = ['Meja',  'nama_pelanggan', 'no_telepon','jam_pilihan', 'jumlah_orang', 'nama_menu', 'jumlah_pesanan', 'total_harga']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(pesanan_list)
    
    print("\nPesanan berhasil dicatat.")
    print("=" * 80)
    print("G-CLASS".center(80, " ").upper())
    print("VIP".center(80, " ").upper())
    print("=" * 80)
    data_tiket = [
        ["Meja", meja_pilihan],
        ["Nama", nama_pelanggan],
        ["Siang/Malam", jam_pilihan]
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
        print("1. Data Kostumer yang Sudah Dipesan")
        print("2. Kembali ke menu sebelumnya")
        pilihan = input("Pilih menu (1/2): ").strip()

        if pilihan == "1":
            data_kostumer_pesan()
        elif pilihan == "2":
            print("Kembali ke menu sebelumnya.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

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

        choice = input("Pilih menu (1-3): ").strip()
        if choice == '1':
            kustomer()
        elif choice == '2':
            pegawai()
        elif choice == '3':
            print("Keluar dari program. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.\n")

if __name__ == "__main__":
    main_menu()