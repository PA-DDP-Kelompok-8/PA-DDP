#Last Update 19.07
import pwinput
import csv
from prettytable import PrettyTable
from datetime import datetime
import random

csv_file = 'data.csv'

simbol  = [  # Daftar simbol yang tidak boleh ada dalam nama
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", 
    "{", "}", "[", "]", ":", ";", "\"", "'", "<", ">", ",", ".", "?", "/", "|", "~"
]
angka = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

def tarik_uang(nama_user):
    try:
        with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        user_found = False
        for row in data:
            if row['nama'] == nama_user:
                user_found = True
                saldo = float(row['saldo'].replace('Rp. ', '').replace('.', '').replace(',', '').strip())
                break

        if not user_found:
            print("Pengguna tidak ditemukan.")
            return
        
        print(f"Saldo Anda saat ini: {format_nominal(saldo)}")
        
        # input jumlah yang ingin ditarik
        try:
            jumlah_tarik = float(input("Masukkan jumlah uang yang ingin ditarik: ").replace('Rp. ', '').replace('.', '').replace(',', '').strip())
        except ValueError:
            print("Jumlah yang dimasukkan tidak valid. Harap masukkan angka.")
            return
        
        # apakah saldo cukup
        if jumlah_tarik > saldo:
            print("Saldo Anda tidak cukup untuk melakukan penarikan tersebut.")
            return
        
        # Mengurangi saldo
        saldo -= jumlah_tarik
        row['saldo'] = format_nominal(saldo)  

        with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

        print(f"Penarikan berhasil. Saldo Anda sekarang: {format_nominal(saldo)}.")
    
    except FileNotFoundError:
        print("File data.csv tidak ditemukan.")
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan oleh pengguna.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Buat cek akun sudah terdaftar belum
def cek_akun_terdaftar(nama):
    try:
        with open(csv_file, mode="r", newline="", encoding="utf-8") as akun_file:
            reader = csv.DictReader(akun_file)
            for row in reader:
                if row["nama"] == nama:
                    return True
        return False
    except FileNotFoundError:
        return False

def cek_beasiswa_update(beasiswa_id):
    try:
        with open("beasiswa.csv", mode="r", newline="", encoding="utf-8") as akun_file:
            reader = csv.DictReader(akun_file)
            for row in reader:
                if row["id"] == str(beasiswa_id):  
                    return True
        return False  
    except FileNotFoundError:
        return False  
    
def cek_beasiswa_terdaftar_admin(nama):
    try:
        with open("beasiswa.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["nama"] == nama:
                    return True
        return False
    except FileNotFoundError:
        return False

# Buat nyimpan nama akun di file csv dengan role sebagai "user"
def simpan_data_akun(nama, password, ipk):
    dataheader_akun = ["nama", "password", "role", "ipk", "saldo"]
    data_akun = [
        {"nama": nama, "password": password, "role": "user", "ipk": ipk, "saldo": 0} 
    ]
    try:
        with open(csv_file, "a", newline="", encoding="utf-8") as akun_file:
            writer = csv.DictWriter(akun_file, fieldnames=dataheader_akun)
            akun_file.seek(0, 2)  
            if akun_file.tell() == 0:  
                writer.writeheader()
            writer.writerows(data_akun)  
        print("Data berhasil disimpan!")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Buat cek login berdasarkan nama dan password
def cek_login(nama, password):
    try:
        with open(csv_file, mode="r", newline="", encoding="utf-8") as akun_file:
            reader = csv.DictReader(akun_file)
            for row in reader:
                if row['nama'] == nama and row['password'] == password:
                    return row['role']  
        return None  
    except FileNotFoundError:
        print("Database akun tidak ditemukan.")
        return None

def format_nominal(nominal):
    return f"Rp. {nominal:,.0f}".replace(',', '.')

# Buat lihat beasiswa
def lihat_beasiswa():
    table = PrettyTable()
    table.field_names = ["ID", "Nama Beasiswa", "Minimal IPK", "Jumlah Hadiah", "Kuota"]

    try:
        with open('beasiswa.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                formatted_jumlah = format_nominal(float(row['jumlah'].replace('Rp. ', '').replace('.', '').replace(',', '')))
                table.add_row([row['id'], row['nama'], row['ipk'], formatted_jumlah, row['kuota']])
        
        print(table)
    except FileNotFoundError:
        print("File beasiswa.csv tidak ditemukan.")

def lihat_data_user():
    table = PrettyTable()
    table.field_names = ["Nama", "Password", "Role", "IPK", "Saldo"]
    
    try:
        with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.add_row([row['nama'], row['password'], row['role'], row["ipk"], row["saldo"]])

        print(table)
    except FileNotFoundError:
        print("File data.csv tidak ditemukan.")

def tambah_beasiswa(nama, ipk, jumlah, kuota):
    dataheader_beasiswa = ["id", "nama", "ipk", "jumlah", "kuota"]
    
    try:
        with open('beasiswa.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            id_terakhir = max([int(row['id']) for row in reader], default=0) + 1
    except FileNotFoundError:
        id_terakhir = 1 

    data_beasiswa = [
        {"id": id_terakhir, "nama": nama, "ipk": ipk, "jumlah": jumlah, "kuota": kuota}
    ]

    try:
        with open('beasiswa.csv', mode='a', newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=dataheader_beasiswa)
            file.seek(0, 2)  
            if file.tell() == 0:  
                writer.writeheader()
            writer.writerows(data_beasiswa)  
        print(f"Beasiswa berhasil ditambahkan dengan jumlah: {format_nominal(float(jumlah))}")

    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Buat update beasiswa
def update_beasiswa(beasiswa_id, ipk=None, jumlah=None, kuota=None):
    updated = False
    data = []
    try:
        with open('beasiswa.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

        for row in data:
            if row['id'] == beasiswa_id:
                if ipk is not None:
                    row['ipk'] = ipk  # Hanya diperbarui jika diberikan nilai
                if jumlah is not None:
                    row['jumlah'] = format_nominal(jumlah)  # Memformat sebelum menyimpan
                if kuota is not None:
                    row['kuota'] = kuota  # Hanya diperbarui jika diberikan nilai
                updated = True
                break  # Keluar dari loop setelah menemukan dan memperbarui yang sesuai

        if updated:
            with open('beasiswa.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"Data beasiswa dengan ID {beasiswa_id} berhasil diperbarui.")
        else:
            print(f"Beasiswa dengan ID {beasiswa_id} tidak ditemukan.")
    except FileNotFoundError:
        print("File beasiswa.csv tidak ditemukan.")

# Buat update data user
def update_data_user(nama, role=None, saldo=None):
    updated = False
    data = []
    try:
        with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        for row in data:
            if row['nama'] == nama:
                if role:
                    row['role'] = role
                if saldo is not None:
                    row['saldo'] = saldo
                updated = True
        
        if updated:
            with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"Data user {nama} berhasil diperbarui.")
        else:
            print(f"User {nama} tidak ditemukan.")
    except FileNotFoundError:
        print("File data.csv tidak ditemukan.")

# Hapus akun
def hapus_akun(nama):
    data = []
    found = False  
    try:
        with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        for row in data:
            if row['nama'] == nama:
                found = True  
                continue  
        
        if found:
            data = [row for row in data if row['nama'] != nama]
            with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['nama', 'password', 'role', 'ipk', 'saldo'])
                writer.writeheader()
                writer.writerows(data)
            print(f"Akun dengan nama {nama} berhasil dihapus.")
        else:
            print(f"Akun dengan nama {nama} tidak ditemukan.")
    
    except FileNotFoundError:
        print("File data.csv tidak ditemukan.")
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan oleh pengguna.")
        menu_admin()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def get_nama_beasiswa_by_id(beasiswa_id):
    try:
        with open('beasiswa.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['id'] == str(beasiswa_id):
                    return row['nama']  
        return None  
    except FileNotFoundError:
        print("File beasiswa.csv tidak ditemukan.")
        return None

# Hapus beasiswa
def hapus_beasiswa(beasiswa_id):
    data = []
    deleted = False
    try:
        with open('beasiswa.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        data = [row for row in data if row['id'] != str(beasiswa_id)]
        
        for i, row in enumerate(data, start=1):
            row['id'] = str(i)
        
        deleted = True
    except FileNotFoundError:
        print("File beasiswa.csv tidak ditemukan.")
    
    if deleted:
        with open('beasiswa.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'nama', 'ipk', 'jumlah', 'kuota'])
            writer.writeheader()
            writer.writerows(data)
        print(f"Beasiswa dengan ID {beasiswa_id} berhasil dihapus.")

# Invoice
def invoice():
    try:
        with open("transaksi.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            transaksi = list(reader)
            if transaksi:
                last_transaction = transaksi[-1]
                print("\n=== INVOICE PENDAFTARAN BEASISWA ===")
                print("Anda berhasil mendaftar beasiswa")
                print(f"Nama          : {last_transaction['nama_user']}")
                print(f"Nama Beasiswa : {last_transaction['nama_beasiswa']}")
                print(f"Jumlah        : {last_transaction['jumlah_beasiswa']}")  
                print(f"Tanggal       : {last_transaction['tanggal']}")
                print("=====================================\n")
    except FileNotFoundError:
        print("File transaksi.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")


def simpan_transaksi(nama_user, beasiswa_id, jumlah_beasiswa):
    dataheader_transaksi = ["id_transaksi", "nama_user", "nama_beasiswa", "jumlah_beasiswa", "tanggal"]
    
    try:
        # Cek apakah beasiswa ada
        nama_beasiswa = get_nama_beasiswa_by_id(beasiswa_id)
        if not nama_beasiswa:
            print("Beasiswa dengan ID tersebut tidak ditemukan.")
            menu_user(nama_user)
            return
        
        # Cek apakah user sudah mendaftar beasiswa ini sebelumnya
        if cek_beasiswa_terdaftar(nama_user, nama_beasiswa):
            print("Kamu telah mendaftar beasiswa ini")
            return
            
        # Jika belum terdaftar, lanjut menyimpan transaksi
        try:
            with open('Transaksi.csv', mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                id_terakhir = max([int(row['id_transaksi']) for row in reader], default=0) + 1
        except FileNotFoundError:
            id_terakhir = 1

        if isinstance(jumlah_beasiswa, str):
            jumlah_str = jumlah_beasiswa.replace('Rp. ', '').replace('.', '').replace(',', '')
            jumlah_beasiswa = float(jumlah_str)

        # Data transaksi baru
        data_transaksi = [{
            "id_transaksi": id_terakhir,
            "nama_user": nama_user,
            "nama_beasiswa": nama_beasiswa,
            "jumlah_beasiswa": format_nominal(jumlah_beasiswa),  
            "tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }]
        
        # Simpan transaksi ke file
        file_exists = True
        try:
            with open('Transaksi.csv', 'r') as file:
                pass
        except FileNotFoundError:
            file_exists = False
        
        mode = 'a' if file_exists else 'w'
        with open('Transaksi.csv', mode=mode, newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=dataheader_transaksi)
            if not file_exists:
                writer.writeheader()
            writer.writerows(data_transaksi)
            
        invoice()
        
        menu_user(nama_user)

    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan transaksi: {e}")

def cek_beasiswa_terdaftar(nama_user, nama_beasiswa):
    try:
        with open("Transaksi.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["nama_user"] == nama_user and row["nama_beasiswa"] == nama_beasiswa:
                    return True
        return False
    except FileNotFoundError:
        return False

def daftar_beasiswa(nama_user, beasiswa_id):
    beasiswa_data = []
    user_data = []
    registered = False

    try:
        with open('beasiswa.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            beasiswa_data = list(reader)

        with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['nama'] == nama_user:
                    user_data = row
                    break

        for row in beasiswa_data:
            if row['id'] == str(beasiswa_id):  
                if float(user_data['ipk']) >= float(row['ipk']):
                    if int(row['kuota']) > 0:
                        row['kuota'] = str(int(row['kuota']) - 1)
                        registered = True
                        break
                    else:
                        print("Kuota untuk beasiswa ini sudah habis.")
                        return
                else:
                    print("IPK Anda tidak memenuhi syarat minimal untuk beasiswa ini.")
                    return

        if registered:
            with open('beasiswa.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['id', 'nama', 'ipk', 'jumlah', 'kuota'])
                writer.writeheader()
                writer.writerows(beasiswa_data)
            print(f"{nama_user} berhasil mendaftar ke beasiswa dengan ID {beasiswa_id}.")

            jumlah_beasiswa = next((row['jumlah'] for row in beasiswa_data if row['id'] == str(beasiswa_id)), None)
            if jumlah_beasiswa:
                simpan_transaksi(nama_user, beasiswa_id, jumlah_beasiswa)
        else:
            print("Beasiswa dengan ID tersebut tidak ditemukan.")

    except FileNotFoundError as e:
        print(f"File tidak ditemukan: {e}")

def lihat_beasiswa_terdaftar(nama_user):
    table = PrettyTable()
    table.field_names = ["ID", "Nama Beasiswa", "Jumlah Beasiswa", "Tanggal Pendaftaran"]

    try:
        with open('Transaksi.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['nama_user'] == nama_user:  
                    table.add_row([row['id_transaksi'], row['nama_beasiswa'], row['jumlah_beasiswa'], row['tanggal']])
        
        if table.rowcount == 0:  
            print(f"Tidak ada beasiswa yang terdaftar untuk pengguna: {nama_user}")
        else:
            print(table)
    except FileNotFoundError:
        print("File Transaksi.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def lihat_data_diri(nama_user):
    try:
        with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['nama'] == nama_user:
                    print("\n=== Data Diri ===")
                    print(f"Nama     : {row['nama']}")
                    print(f"Password : {row['password']}")
                    print(f"IPK      : {row['ipk']}")
                    
                    try:
                        saldo_value = float(row['saldo'].replace('Rp. ', '').replace('.', '').replace(',', '').strip())
                        print(f"Saldo    : {format_nominal(saldo_value)}")  
                    except ValueError:
                        print("Saldo tidak valid, tidak dapat dikonversi ke format angka.")
                    
                    return
            print("Data pengguna tidak ditemukan.")
    except FileNotFoundError:
        print("File data.csv tidak ditemukan.")
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan.")

def undi_beasiswa(nama_user):
    try:
        with open('Transaksi.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            berkas_transaksi = [row for row in reader if row['nama_user'] == nama_user]

        if not berkas_transaksi:
            print("Anda belum mendaftar untuk beasiswa manapun.")
            return

        print("=== Pilihan Beasiswa ===")
        for index, row in enumerate(berkas_transaksi, start=1):
            print(f"{index}. {row['nama_beasiswa']} - Jumlah: {row['jumlah_beasiswa']} (ID: {row['id_transaksi']})")

        pilihan = input("Pilih beasiswa yang ingin diundi (masukkan nomor): ").strip()  

        if pilihan == "":  
            menu_user(nama_user)  
            
        try:
            pilihan = int(pilihan) - 1  
        except ValueError:  
            print("Pilihan tidak valid. Silakan masukkan nomor yang tepat.")
            return

        if pilihan < 0 or pilihan >= len(berkas_transaksi):
            print("Pilihan tidak valid. Silakan pilih nomor yang terdaftar.")
            return
            
        beasiswa_terpilih = berkas_transaksi[pilihan]
        print(f"\nAnda telah memilih beasiswa: {beasiswa_terpilih['nama_beasiswa']}")

        # Mengundi
        jika_beruntung = random.choice([True, False])  # 50% peluang
        if jika_beruntung:
            jumlah_beasiswa = float(beasiswa_terpilih['jumlah_beasiswa'].replace('Rp. ', '').replace('.', '').replace(',', ''))
            print(f"Selamat! Anda mendapatkan beasiswa sebesar {format_nominal(jumlah_beasiswa)}!")  
            
            update_saldo(nama_user, jumlah_beasiswa)
        else:
            print("Sayang sekali, Anda tidak mendapatkan beasiswa ini. Coba lagi lain waktu.")

    except FileNotFoundError:
        print("File Transaksi.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def update_saldo(nama_user, jumlah):
    updated = False
    data = []
    try:
        with open('data.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        
        for row in data:
            if row['nama'] == nama_user:
                try:
                    saldo_float = float(row['saldo'].replace('Rp. ', '').replace('.', '').replace(',', '').strip())
                    new_saldo = saldo_float + jumlah
                    row['saldo'] = format_nominal(new_saldo)  
                    updated = True
                except ValueError:
                    print("Saldo tidak valid, tidak dapat diperbarui.")
        
        if updated:
            with open('data.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)
            print(f"Saldo Anda berhasil diperbarui. Saldo saat ini: {format_nominal(new_saldo)}.")  
        else:
            print("Pengguna tidak ditemukan.")
    except FileNotFoundError:
        print("File data.csv tidak ditemukan.")
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def search():
    nama = input("Nama beasiswa: ").lower()
    found = False
    
    try:
        table = PrettyTable()
        table.field_names = ["ID", "Nama Beasiswa", "IPK Minimal", "Jumlah", "Kuota"]
        
        with open("beasiswa.csv", mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if nama in row['nama'].lower():
                    table.add_row([row['id'], row['nama'], row['ipk'], row['jumlah'], row['kuota']])
                    found = True
        
        if found:
            print("\nHasil pencarian:")
            print(table)
        else:
            print("\nBeasiswa tidak ditemukan.")
            
    except FileNotFoundError:
        print("File beasiswa.csv tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def sorting(file_path, urutkan_berdasarkan='ipk', menurun=False):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            data = list(reader)

            if urutkan_berdasarkan not in ['ipk', 'jumlah', 'id']:
                print("Kriteria pengurutan tidak valid. Gunakan 'ipk', 'jumlah', atau 'id'.")
                return
            
            if urutkan_berdasarkan == 'jumlah':
                for entry in data:
                    entry['jumlah'] = float(entry['jumlah'].replace('Rp. ', '').replace('.', '').replace(',', ''))
            
            if urutkan_berdasarkan == 'id':
                sorted_data = sorted(data, key=lambda x: int(x['id']), reverse=menurun)  
            else:
                sorted_data = sorted(data, key=lambda x: float(x[urutkan_berdasarkan]), reverse=menurun)

        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(sorted_data)
        
        print("\nData beasiswa berhasil diurutkan.")
        table = PrettyTable()
        table.field_names = ["ID", "Nama Beasiswa", "IPK Minimal", "Jumlah", "Kuota"]
        for row in sorted_data:
            table.add_row([row['id'], row['nama'], row['ipk'], row['jumlah'], row['kuota']])
        print(table)

    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Buat menu Admin
def menu_admin():
    while True:
        print("==== Menu Admin ====")
        print("1. Lihat beasiswa/user")
        print("2. Tambah beasiswa")
        print("3. Update beasiswa/user")
        print("4. Hapus beasiswa/user")
        print("5. Logout")
        try:
            pilihan = input("Masukan pilihan: ")

            if pilihan == "1":
                print("1. Lihat akun")
                print("2. Lihat Beasiswa")
                pil_1 = input("Masukan pilihan: ")
                if pil_1 == "1":
                    lihat_data_user()
                elif pil_1 == "2":
                    lihat_beasiswa()
                else:
                    print("Pilihan tidak Valid")
                    menu_admin()
            
            elif pilihan == "2":
                while True:
                    nama = input("Masukan nama beasiswa: ")
                    if cek_beasiswa_terdaftar_admin(nama):
                        print("Nama ini sudah didaftarkan")
                        continue
                    if nama == "":
                        menu_admin()
                    try:
                        ipk = float(input("Masukan jumlah minimal ipk: "))
                        if ipk > 4.0:
                            print("IPK tidak boleh melebihi 4")
                            continue
                        jumlah = float(input("Masukan nominal beasiswa: "))
                        kuota = int(input("Masukan kuota beasiswa: "))
                        if ipk < 0 or jumlah < 0 or kuota < 0:
                            print("Angka tidak boleh negatif")
                            break
                        tambah_beasiswa(nama, ipk, jumlah, kuota)
                        break
                    except ValueError:
                        print("Nilai yang anda masukan bukan merupakan angka")

            elif pilihan == "3":
                print("1. Update akun")
                print("2. Update Beasiswa")
                pil_1 = input("Masukan pilihan: ")
                
                if pil_1 == "1":
                    lihat_data_user()
                    nama = input("Masukkan nama user: ")
                    print("Pilih Role Baru:")
                    print("1. Admin")
                    print("2. User")
                    valid_input = True  
                    
                    role_option = input("Masukkan pilihan role (1 untuk Admin, 2 untuk User): ")
                    if role_option == "1":
                        role = "admin"
                    elif role_option == "2":
                        role = "user"
                    else:
                        print("Pilihan role tidak valid.")
                        valid_input = False  

                    if valid_input:  
                        saldo_input = input("Masukkan saldo baru (kosongkan jika tidak ingin mengubah): ")
                        if saldo_input:  # Memeriksa apakah ada input
                            try:
                                saldo = float(saldo_input)  
                                if saldo < 0:  # Memastikan saldo tidak negatif
                                    print("Saldo tidak boleh negatif.")
                                    valid_input = False
                            except ValueError:
                                print("Nilai saldo yang anda masukan bukan merupakan angka.")
                                valid_input = False  

                    if valid_input:
                        update_data_user(nama, role, saldo)
                    else:
                        print("Data tidak dapat diperbarui karena input tidak valid.")

                elif pil_1 == "2":
                    lihat_beasiswa()
                    beasiswa_id = input("Masukkan ID beasiswa: ")
                    if not cek_beasiswa_update(beasiswa_id):
                        print("ID beasiswa tidak ditemukan.")
                        continue  
                    
                    valid_input = True  
                    ipk_input = input("Masukkan IPK baru (kosongkan jika tidak ingin mengubah): ")
                    
                    if ipk_input:  
                        try:
                            ipk = float(ipk_input)
                            if ipk < 0 or ipk > 4:
                                print("IPK tidak valid, harus antara 0 dan 4.")
                                valid_input = False
                        except ValueError:
                            print("Nilai IPK yang anda masukkan bukan merupakan angka.")
                            valid_input = False  

                    if valid_input:
                        if not ipk_input:  
                            ipk = None
                        else:
                            ipk = float(ipk_input)

                        jumlah_input = input("Masukkan nominal beasiswa baru (kosongkan jika tidak ingin mengubah): ")
                        if jumlah_input: 
                            try:
                                jumlah = float(jumlah_input)
                                if jumlah < 0:  # Memastikan jumlah beasiswa tidak negatif
                                    print("Nominal beasiswa tidak boleh negatif.")
                                    valid_input = False
                            except ValueError:
                                print("Nilai nominal beasiswa yang anda masukkan bukan merupakan angka.")
                                valid_input = False 
                        else:
                            jumlah = None  

                        kuota_input = input("Masukkan kuota beasiswa baru (kosongkan jika tidak ingin mengubah): ")
                        if kuota_input:
                            try:
                                kuota = int(kuota_input)
                                if kuota < 0:  # Memastikan kuota tidak negatif
                                    print("Kuota tidak boleh negatif.")
                                    valid_input = False  
                            except ValueError:
                                print("Nilai kuota yang anda masukkan bukan merupakan angka.")
                                valid_input = False  
                        else:
                            kuota = None  

                        if valid_input:
                            update_beasiswa(beasiswa_id, ipk, jumlah, kuota)
                        else:
                            print("Data beasiswa tidak dapat diperbarui karena input tidak valid.")

            elif pilihan == "4":
                print("1. Hapus Akun")
                print("2. Hapus Beasiswa")
                pil_1 = input("Masukan pilihan: ")
                if pil_1 == "1":
                    lihat_data_user()
                    nama = input("Masukan nama yang ingin di hapus: ")
                    if nama == "":
                        print("Nama yang dimasukan tidak boleh kosong")
                    else:
                        hapus_akun(nama)
                elif pil_1 == "2":  # 
                    lihat_beasiswa()

                    beasiswa_id = input("Masukan ID beasiswa yang ingin dihapus: ")
                    if not beasiswa_id.isdigit():  
                        print("ID yang dimasukkan tidak valid. Harap masukkan angka.")
                        continue  

                    beasiswa_id = int(beasiswa_id)  
                    
                    if not cek_beasiswa_update(beasiswa_id):  
                        print("ID beasiswa tidak ditemukan.")
                        continue  
                    
                    hapus_beasiswa(beasiswa_id)  

            elif pilihan == "5":
                menu_login()  
        except KeyboardInterrupt:
            print("Operasi dibatalkan")
            menu_admin()

# Buat menu user
def menu_user(nama_user):
    print("==== Menu User ====")
    print("1. Daftar beasiswa")
    print("2. Biodata diri")
    print("3. Status pendaftaran")
    print("4. Pengumuman")
    print("5. Tarik uang")
    print("6. Logout")
    pilihan = input("Masukkan pilihan: ")

    if pilihan == "1":
        lihat_beasiswa()
        beasiswa_id = input("Masukkan ID beasiswa yang ingin didaftarkan (ketik s untuk search, ketik r untuk sorting): ").lower()
        
        if beasiswa_id == "s":
            search()
            menu_user(nama_user)
        elif beasiswa_id == "r":
            print("Pilih kriteria pengurutan:")
            print("1. IPK")
            print("2. Nominal Beasiswa")
            print("3. ID")  
            pilihan = input("Masukkan pilihan (1, 2, atau 3): ")
            if pilihan == "":
                menu_user(nama_user)
            if pilihan == '1':
                urutkan_berdasarkan = 'ipk'
            elif pilihan == '2':
                urutkan_berdasarkan = 'jumlah'
            elif pilihan == '3':
                urutkan_berdasarkan = 'id'  
            else:
                print("Pilihan tidak valid.")
                menu_user(nama_user)
                return

            print("Pilih urutan:")
            print("1. Tertinggi ke Terendah")
            print("2. Terendah ke Tertinggi")
            
            urutan = input("Masukkan pilihan (1 atau 2): ")
            if urutan == "":
                menu_user(nama_user)
            if urutan == '1':
                menurun = True  
            elif urutan == '2':
                menurun = False  
            else:
                print("Pilihan tidak valid.")
                menu_user(nama_user)
                return
            
            sorting("beasiswa.csv", urutkan_berdasarkan, menurun)
            menu_user(nama_user)
        else:
            if not beasiswa_id.isdigit():  
                print("ID yang dimasukkan tidak valid. Harap masukkan angka.")
                menu_user(nama_user)
                return
            
            nama_beasiswa = get_nama_beasiswa_by_id(beasiswa_id)
            if nama_beasiswa:
                print(f"Anda mendaftarkan diri untuk beasiswa: {nama_beasiswa}")
                daftar_beasiswa(nama_user, beasiswa_id)
            else:
                print("Beasiswa dengan ID tersebut tidak ditemukan.")
    
    elif pilihan == "2":
        lihat_data_diri(nama_user)
        menu_user(nama_user)
    elif pilihan == "3":
        lihat_beasiswa_terdaftar(nama_user)
        menu_user(nama_user)
    elif pilihan == "4":
        undi_beasiswa(nama_user)
        menu_user(nama_user)
    elif pilihan == "5":
        tarik_uang(nama_user)
        menu_user(nama_user)
    elif pilihan == "6":
        menu_login()
    else:
        print("Pilihan tidak valid")
        menu_user(nama_user)

def akses_pengguna(nama, password):
    role = cek_login(nama, password)
    if role == "admin":
        print(f"Selamat datang, {nama}! Anda login sebagai Admin.")
        menu_admin()
    elif role == "user":
        print(f"Selamat datang, {nama}! Anda login sebagai User.")
        menu_user(nama)
    else:
        print("Nama atau password salah, atau peran tidak ditemukan.")

def menu_login():
    while True:
        print("======== Menu Login =========")
        print("1. Register")
        print("2. Login")
        print("3. Keluar Program")
        try:
            pil_1 = input("Masukan Pilihan: ")
            # Buat register
            if pil_1 == "1": 
                print("==== Register ====")
                while True:
                    nama = input("Masukan nama: ")
                    if nama == "":
                        menu_login()
                        continue
                    if any(char in simbol for char in nama) or any(char in angka for char in nama):
                        print("Nama tidak boleh mengandung angka atau simbol. Coba lagi.")
                        continue
                    if cek_akun_terdaftar(nama):
                        print("Nama sudah terdaftar! Coba nama lain.")
                        continue
                    else:
                        password = pwinput.pwinput("Masukan Password: ")
                        if password == "":
                            print("Password tidak boleh kosong")
                            continue
                        try:
                            ipk = float(input("Masukan IPK: "))
                            if ipk > 4:
                                print("IPK tidak boleh melebihi 4")
                                continue
                            simpan_data_akun(nama, password, ipk)
                            break
                        except ValueError:
                            print("Nilai yang anda masukan bukan merupakan angka")

            # Buat login
            elif pil_1 == "2": 
                print("===== Login ======") 
                nama = input("Masukan nama: ")
                password = pwinput.pwinput("Masukan Password: ")
                akses_pengguna(nama, password)

            # Buat keluar program
            elif pil_1 == "3": 
                print("Keluar Program.")
                exit()

            # Buat pilihan tidak valid
            else:
                print("Pilihan tidak valid, coba lagi.")
        except KeyboardInterrupt:
            print("Operasi dibatalkan")
            menu_login()

menu_login()
