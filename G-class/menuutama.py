import pandas as pd
import csv
from rich.console import Console
import os
from tabulate import tabulate

console = Console()
console.print("G-CLASS".center(54), style="bold")


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

def kustomer() :
    print("=== Selamat datang ===")
    usernamee= input("Masukkan nama lengkap anda:")
    data_kostumer=[]
    with open ("data_kostumer.csv", "r") as file :
        baca_csv = csv.reader(file, delimiter=",")
        for row in baca_csv:
            data_kostumer.append({'username' : row [0]})
    username= True
    if username == True :
        row= ("username")
        with open ("data_kostumer.csv", "a", newline="") as file:
            file.write(usernamee+"\n")
           
def pegawai():
    file_path = "data_user.csv"
    print("=== Silahkan Login ===")
    usernamee = input("Masukkan nama user Anda: ")
    passwordd = input("Masukkan password Anda: ")
    
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
                            print("Role tidak memiliki akses tambahan.")
                        return

        print("Username atau password salah.")
    except FileNotFoundError:
        print("File data_user.csv tidak ditemukan.")

def data_restoran():
    print("=== Data Restoran ===")
    print("1. Stok Menu")
    print("2. Data Karyawan")
    print("3. Transaksi")
    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "1":
        stok_menu()
    elif pilihan == "2":
        datakaryawan()
    elif pilihan == "3":
        transaksi()
    else:
        print("Pilihan tidak valid.")

def stok_menu():
    file_path = "stok_menu.csv"
    print("=== Stok Menu ===")
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            print("Stok yang tersedia:")
            for row in reader:
                if row:
                    print(f"- {row[0]}: {row[1]} unit")

        pilihan = input("Ingin memperbarui stok? (y/n): ")
        if pilihan.lower() == "y":
            nama_menu = input("Masukkan nama menu: ")
            stok_baru = input("Masukkan stok baru: ")

            data = []
            updated = False
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row and row[0] == nama_menu:
                        data.append([nama_menu, stok_baru])
                        updated = True
                    else:
                        data.append(row)

            if not updated:
                data.append([nama_menu, stok_baru])

            with open(file_path, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            print(f"Stok untuk {nama_menu} telah diperbarui.")
    except FileNotFoundError:
        print("File stok_menu.csv tidak ditemukan.")

def datakaryawan():
    file_path = "D:\\G-class\\data_karyawan.csv"
    try:
        df = pd.read_csv(file_path)
        print("\n=== Data Karyawan ===")

        if not df.empty:
            print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
        else:
            print("File data_karyawan.csv kosong.")
    except FileNotFoundError:
        print(f"Error: File tidak ditemukan di path {file_path}.")
    except Exception as e:
        print(f"Terjadi error: {e}")

def transaksi():
    print("=== Transaksi ===")
    print("1. Jadwal Kostumer Datang")
    print("2. Data Kostumer yang Sudah Dipesan")
    pilihan = input("Pilih menu (1/2): ")

    if pilihan == "1":
        jadwal_kostumer()
    elif pilihan == "2":
        data_kostumer_pesan()
    else:
        print("Pilihan tidak valid.")

def jadwal_kostumer():
    file_path = "jadwal_kostumer.csv"
    print("=== Jadwal Kostumer ===")
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print(f"{row[0]} - {row[1]} - {row[2]}")
    except FileNotFoundError:
        print("File jadwal_kostumer.csv tidak ditemukan.")

def data_kostumer_pesan():
    file_path = "data_pesanan.csv"
    print("=== Data Kostumer yang Sudah Dipesan ===")
    try:
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    print(f"{row[0]} - {row[1]} - Rp{row[2]}")
    except FileNotFoundError:
        print("File data_pesanan.csv tidak ditemukan.")

pilihan = input("1.Pegawai atau 2.Kustomer? (1/2):")
if pilihan == "1":
    pegawai()
elif pilihan == "2":
    kustomer()
else:
    ("inputan salah")