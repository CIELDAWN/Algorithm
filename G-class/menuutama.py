import pandas as pd
import csv
from rich.console import Console
import os
from tabulate import tabulate
from datetime import datetime
from textwrap import wrap

console = Console()
console.print("G-CLASS".center(54), style="bold")

menu_makanan = pd.DataFrame({
    "Tipe Menu": [
        "maincourse", 
        "maincourse", 
        "maincourse",
        "maincourse", 
        "maincourse", 
        "maincourse", 
        "maincourse", 
        "sidedish", 
        "sidedish", 
        "sidedish", 
        "sidedish",
        "Dessert",
        "Dessert",
        "Dessert",
        "Dessert",
        "Dessert",
        "Dessert",
        "drink",
        "drink",
        "drink",
        "drink",
        "drink",
        "drink",
        ],
    "Nama Menu" : [
        "Gado-Gado Jakarta",
        "Sour Palembang Ribs",
        "Lamongan Chiken Soup",
        "Oxtail Soup",
        "Rawon Surabaya",
        "Beef Rendang",
        "Purwakarta Maranggi Beef Satay",
        "Madura Chiken Satay",
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
        "Turkish Coffe",
        "Mango Lassi",
        "Macha Latte",
        "Chocolate Milkshake",
        "Mineral Water",
        ],
    "Description": [
        "Steamed Vegetable Salad With Egg, Tofu and Bean Cake, Spicy Peanut Sauce",
        "Braised Beef Ribs With Green Tomato And Belimbing Wuluh",
        "Sliced Chicken Soup With Glass Noodles In  A Turmeric, Lemongrass And Chicken Broth",
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
        "Coffee served in a cezve pot with fine coffee grounds with a little added sugar",
        "Mix of mango yogurt milk and a little sugar",
        "Matcha powder mixed with warm milk and sugar",
        "Milk ice cream and flavored syrup then shaken together",
        "Usual mineral water",
        ]

})
promo_data = pd.DataFrame({
    "Promo": ["Buy tempat + paket menu - A, B, C"],
    "Potongannya": ["20% - All menu"]
})

best_seller_data = pd.DataFrame({
    "No": [1, 2, 3, 4],
    "Best Seller": [
        "Pizza Flameé",
        "Spaghetti Carbonara",
        "Rib Eye",
        "Basque Cheesecake - Tropical"]
})

print("=" * 54)
print("SELAMAT DATANG DI RESTORAN".center(54))
print("G-CLASS".center(54))
print("=" * 54)

print("\n>> Promo Hari Ini:")
print(f"|{'-'*35}|{'-'*16}|")
print(f"| {'Promo':<33} | {'Potongannya':<14} |")
print(f"|{'-'*35}|{'-'*16}|")
for _, row in promo_data.iterrows():
    print(f"| {row['Promo']:<32} | {row['Potongannya']:<12} |")
print(f"|{'-'*35}|{'-'*16}|")

print("\n>> Best Seller Menu:")
print(f"+{'-'*4}+{'-'*30}+")
print(f"| {'No':<2} | {'Best Seller':<28} |")
print(f"+{'-'*4}+{'-'*30}+")
for _, row in best_seller_data.iterrows():
    print(f"| {row['No']:<2} | {row['Best Seller']:<28} |")
print(f"+{'-'*4}+{'-'*30}+")

print("\n" + "-" * 54)
print("Terima kasih, Silahkan Menikmati Hidangan Kami!".center(54))
print("-" * 54)

def kustomer():
    while True:
        print("\n=== Selamat datang ===")
        print("1. Daftar Menu")
        print("2. Reservasi")
        print("3. Keluar")

        choice = input("Pilih menu (1-3): ").strip()
        if choice == '1':
            tampilkan_menu()
        elif choice == '2':
            reservasi()
        elif choice == '3':
            print("Keluar dari program. Terima kasih!")
            break

# def main_menu_kostumer():
#     while True:
#         print("\n=== Selamat datang ===")
#         print("1. Daftar Menu")
#         print("2. Reservasi")
#         print("3. Keluar")

#         choice = input("Pilih menu (1-3): ").strip()
#         if choice == '1':
#             menu_makanan()
#         elif choice == '2':
#             reservasi()
#         elif choice == '3':
#             print("Keluar dari program. Terima kasih!")
#             break

# def menu_makanan():
#     os.system("cls" if os.name == "nt" else "clear")

# best_seller_data = pd.DataFrame({
#     "No": [1, 2, 3, 4],
#     "Best Seller": [
#         "Pizza Flameé",
#         "Spaghetti Carbonara",
#         "Rib Eye",
#         "Basque Cheesecake - Tropical"]
# })

# print("\n>> Best Seller Menu:")
# print(f"+{'-'*4}+{'-'*30}+")
# print(f"| {'No':<2} | {'Best Seller':<28} |")
# print(f"+{'-'*4}+{'-'*30}+")
# for _, row in best_seller_data.iterrows():
#     print(f"| {row['No']:<2} | {row['Best Seller']:<28} |")
# print(f"+{'-'*4}+{'-'*30}+")


def ruangan_vip():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("\n=== Selamat datang ===")
        print("1. paket pilih bebas")
        print("2. paket pilih sendiri")
        print("3. Keluar")

        choice = input("Pilih menu (1-3): ").strip()
        if choice == '1':
            pilih_bebas_vip()
        elif choice == '2':
            paketan_vip()
        elif choice == '3':
            print("Keluar dari program. Terima kasih!")
            break

def pilih_bebas_vip():
    meja_vip = pd.read_csv('data_meja_vip.csv')
    print("Daftar Meja VIP:")
    print(meja_vip)

    meja_pilihan = input("Pilih meja (1A-1E): ")
    
    # Mengecek apakah meja tersedia
    if meja_pilihan not in meja_vip['meja'].values:
        print("Meja tidak tersedia.")
        return

    # Mengurangi jumlah meja yang dipilih
    meja_vip = meja_vip[meja_vip['meja'] != meja_pilihan]
    meja_vip.to_csv('data_meja_vip.csv', index=False)

    # Memasukkan jumlah orang
    jumlah_orang = input("Masukkan jumlah orang: ")

    # Membaca data menu
    stok_menu = pd.read_csv('stok_menu.csv')
    print("Daftar Menu:")
    print(stok_menu)

    # Memilih menu
    menu_pilihan = input("Pilih menu: ")

    # Mengecek apakah menu tersedia
    if menu_pilihan not in stok_menu['menu'].values:
        print("Menu tidak tersedia.")
        return


    jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))


    stok_tersedia = stok_menu.loc[stok_menu['menu'] == menu_pilihan, 'stok'].values[2]
    if jumlah_pesanan > stok_tersedia:
        print("Stok tidak cukup.")
        return


    stok_menu.loc[stok_menu['menu'] == menu_pilihan, 'stok'] -= jumlah_pesanan
    stok_menu.to_csv('stok_menu.csv', index=False)

    pesanan = {
        'meja': meja_pilihan,
        'jumlah_orang': jumlah_orang,
        'menu': menu_pilihan,
        'jumlah_pesanan': jumlah_pesanan
    }

    try:
        pesanan_df = pd.read_csv('data_pesanan.csv')
    except FileNotFoundError:
        pesanan_df = pd.DataFrame(columns=['meja', 'jumlah_orang', 'menu', 'jumlah_pesanan'])

    pesanan_df = pesanan_df.append(pesanan, ignore_index=True)
    pesanan_df.to_csv('data_pesanan.csv', index=False)

    print("Pesanan berhasil dicatat.")

def paketan_vip():
    # Membaca data meja VIP
    meja_vip = pd.read_csv('data_meja_vip.csv')
    
    # Memilih meja secara acak yang masih tersedia
    if meja_vip.empty:
        print("Tidak ada meja yang tersedia.")
        return
    
    meja_pilihan = meja_vip.sample(n=1).iloc[0]
    meja = meja_pilihan['meja']
    print(f"Meja yang dipilih: {meja}")

    # Memasukkan jumlah orang
    jumlah_orang = input("Masukkan jumlah orang: ")

    # Membaca data menu
    stok_menu = pd.read_csv('stok_menu.csv')
    
    # Memilih menu dengan stok terbanyak
    if stok_menu.empty:
        print("Tidak ada menu yang tersedia.")
        return
    
    menu_terbanyak = stok_menu.loc[stok_menu['stok'].idxmax()]
    menu = menu_terbanyak['menu']
    stok_tersedia = menu_terbanyak['stok']
    
    print(f"Menu yang dipilih: {menu} (Stok: {stok_tersedia})")

    # Memasukkan jumlah porsi yang ingin dipesan
    jumlah_pesanan = int(input("Masukkan jumlah porsi yang ingin dipesan: "))

    # Mengecek stok menu
    if jumlah_pesanan > stok_tersedia:
        print("Stok tidak cukup.")
        return

    # Mengurangi stok menu
    stok_menu.loc[stok_menu['menu'] == menu, 'stok'] -= jumlah_pesanan
    stok_menu.to_csv('stok_menu.csv', index=False)

    pesanan = {
        'meja': meja,
        'jumlah_orang': jumlah_orang,
        'menu': menu,
        'jumlah_pesanan': jumlah_pesanan
    }

    try:
        pesanan_df = pd.read_csv('data_pesanan.csv')
    except FileNotFoundError:
        pesanan_df = pd.DataFrame(columns=['meja', 'jumlah_orang', 'menu', 'jumlah_pesanan'])

    pesanan_df = pesanan_df.append(pesanan, ignore_index=True)
    pesanan_df.to_csv('data_pesanan.csv', index=False)

    meja_vip = meja_vip[meja_vip['meja'] != meja]
    meja_vip.to_csv('data_meja_vip.csv', index=False)

    print("Pesanan berhasil dicatat.")

def paketan_vip():
    # Membaca data meja VIP
    meja_vip = pd.read_csv('data_meja_vip.csv')
    
    # Memilih meja secara acak yang masih tersedia
    if meja_vip.empty:
        print("Tidak ada meja yang tersedia.")
        return
    
    meja_pilihan = meja_vip.sample(n=1).iloc[0]
    meja = meja_pilihan['meja']
    print(f"Meja yang dipilih: {meja}")

    # Memasukkan jumlah orang
    jumlah_orang = input("Masukkan jumlah orang: ")

    # Membaca data menu
    stok_menu = pd.read_csv('stok_menu.csv')
    
    # Memilih menu dengan stok terbanyak
    if stok_menu.empty:
        print("Tidak ada menu yang tersedia.")
        return
    
    # Menemukan menu dengan stok terbanyak
    menu_terbanyak = stok_menu.loc[stok_menu['Stok_Menu'].idxmax()]
    nama_menu = menu_terbanyak['Nama_Menu']
    stok_tersedia = menu_terbanyak['Stok_Menu']
    
    print(f"Menu yang dipilih: {nama_menu} (Stok: {stok_tersedia})")

    # Memasukkan jumlah porsi yang ingin dipesan
    jumlah_pesanan = int(input("Masukkan jumlah porsi yang ingin dipesan: "))

    if jumlah_pesanan > stok_tersedia:
        print("Stok tidak cukup.")
        return

    stok_menu.loc[stok_menu['Nama_Menu'] == nama_menu, 'Stok_Menu'] -= jumlah_pesanan
    stok_menu.to_csv('stok_menu.csv', index=False)

    pesanan = {
        'meja': meja,
        'jumlah_orang': jumlah_orang,
        'menu': nama_menu,
        'jumlah_pesanan': jumlah_pesanan
    }

    try:
        pesanan_df = pd.read_csv('data_pesanan.csv')
    except FileNotFoundError:
        pesanan_df = pd.DataFrame(columns=['meja', 'jumlah_orang', 'menu', 'jumlah_pesanan'])

    pesanan_df = pesanan_df.append(pesanan, ignore_index=True)
    pesanan_df.to_csv('data_pesanan.csv', index=False)

    meja_vip = meja_vip[meja_vip['meja'] != meja]
    meja_vip.to_csv('data_meja_vip.csv', index=False)

    print("Pesanan berhasil dicatat.")

# def menu_reservasi():
#     print("=== Menu Reservasi ===")
#     print("1. Tambah Reservasi")
#     print("2. Tampilkan Reservasi")
#     print("3. Keluar")

# def main():
#     reservasi_list = baca_dari_csv()
#     while True:
#         menu_reservasi()
#         pilihan = input("Pilih menu (1/2/3): ").strip()
        
#         if pilihan == '1':
#             print("Pilih Tipe Reservasi:")
#             print("a. Paket Makanan")
#             print("b. Tempat Saja")
#             tipe_pilihan = input("Masukkan pilihan (a/b): ").strip()
#             if tipe_pilihan == 'a':
#                 print("Pilih Paket Makanan yang sedang tersedia")
#                 with open('stok_menu', mode='r',):
#                     stok_menu = pd.read_csv('stok_menu.csv'):
#                     print(stok_menu)
#                     Paket_Makanan = input("Pilihan Paket: ").strip()
#             elif tipe_pilihan == 'b':

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
                            pegawai_menu(role)
                            return
            print("Username atau password salah. Silakan coba lagi.")
        except FileNotFoundError:
            print("File data_user.csv tidak ditemukan.")
            return

def pegawai_menu(role):
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print(f"\n=== Menu {role.title()} ===")
        if role == "manajer":
            print("1. Data Restoran")
        if role in ["manajer", "pegawai kasir"]:
            print("2. Transaksi")
        if role in ["manajer", "pegawai dapur"]:
            print("3. Stok Menu")
        print("4. Logout")

        pilihan = input("Pilih menu (1/2/3/4): ").strip()
        
        if role == "manajer" and pilihan == "1":
            data_restoran()
        elif role in ["manajer", "pegawai kasir"] and pilihan == "2":
            transaksi()
        elif role in ["manajer", "pegawai dapur"] and pilihan == "3":
            stok_menu()
        elif pilihan == "4":
            print("Logout berhasil. Kembali ke menu utama.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

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

def transaksi():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("=== Transaksi ===")
        print("1. Reservasi Kostumer Datang")
        print("2. Data Kostumer yang Sudah Dipesan")
        print("3. Kembali ke menu sebelumnya")
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            reservasi_kostumer()
        elif pilihan == "2":
            data_kostumer_pesan()
        elif pilihan == "3":
            print("Kembali ke menu sebelumnya.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def reservasi_kostumer():
    os.system("cls" if os.name == "nt" else "clear")
    file_path = "jadwal_kostumer.csv"
    print("\n=== Jadwal Kostumer ===")
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print(f"{row[0]} - {row[1]} - {row[2]}")
    except FileNotFoundError:
        print("File jadwal_kostumer.csv tidak ditemukan.")

def data_kostumer_pesan():
    os.system("cls" if os.name == "nt" else "clear")
    file_path = "data_pesanan.csv"
    print("\n=== Data Kostumer yang Sudah Dipesan ===")
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print(f"{row[0]} - {row[1]} - Rp{row[2]}")
    except FileNotFoundError:
        print("File data_pesanan.csv tidak ditemukan.")

def main_menu():
    os.system("cls" if os.name == "nt" else "clear")
    while True:
        print("\n=== Menu Registrasi ===")
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