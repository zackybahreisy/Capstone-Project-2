from prettytable import PrettyTable

#Data Awal
daftar_buku_novel = [
    # NOVEL (N)
    ['N001', 'Laskar Pelangi', 'Andrea Hirata', 10, 3],
    ['N002', 'Bumi Manusia', 'Pramoedya A. Toer', 8, 2],
    ['N003', 'Dilan 1990', 'Pidi Baiq', 5, 1],
    ['N004', 'Perahu Kertas', 'Dee Lestari', 6, 4],
    ['N005', 'Hujan', 'Tere Liye', 7, 0],
]
daftar_buku_pengetahuan = [
    # PENGETAHUAN (P)
    ['P001', 'Ensiklopedia Sains', 'Tim Sains', 8, 2],
    ['P002', 'Fisika Dasar', 'Giancoli', 6, 6],
    ['P003', 'Biologi Modern', 'Campbell', 5, 1],
    ['P004', 'Kimia Dasar', 'Chang', 7, 4],
    ['P005', 'Sejarah Dunia', 'E.H. Gombrich', 6, 2],
]
daftar_buku_teknologi = [
    # TEKNOLOGI (T)
    ['T001', 'Python Programming', 'Mark Lutz', 9, 4],
    ['T002', 'Data Science Handbook', 'Jake VanderPlas', 6, 2],
    ['T003', 'Machine Learning', 'Andrew Ng', 7, 3],
    ['T004', 'Artificial Intelligence', 'Stuart Russell', 5, 1],
    ['T005', 'Web Development', 'Jon Duckett', 8, 2]
]
daftar_buku_semua = daftar_buku_novel + daftar_buku_pengetahuan + daftar_buku_teknologi
recyclebin = []

def program_utama():
    while True:
        print('\n==== SELAMAT DATANG DI PERPUSTAKAAN ====\n')
        print('List Menu :')
        print('1. Daftar Buku')
        print('2. Tambah Buku')
        print('3. Ubah Buku')
        print('4. Hapus Buku')
        print('5. Pinjam Buku')
        print('6. Recycle Bin')
        print('7. Keluar''')
        try:
            menu = int(input('\nPilih Menu (1-7): '))             
        except ValueError:
            print('Tolong Masukan Pilihan Berupa Angka!')
            continue
        if menu == 1: #Fitur Daftar Buku
            daftar_buku()  
        elif menu == 2: #Fitur Tambah Buku  
            tambah_buku()    
        elif menu == 3: #Fitur Ubah Buku
            ubah_buku()
        elif menu == 4: #Fitur Hapus Buku
            hapus_buku()
        elif menu == 5: #Fitur Pinjam Buku
            pinjam_buku()   
        elif menu == 6: #Fitur Recycle Bin 
            recycle_bin()   
        elif menu == 7: #Keluar
            print('\nTerima Kasih! 😊') 
            break
        else :
            print('\nNomor tidak valid ❌')    
                   
def menu(menu = ''):
    def menu_utama():
        input('Tekan Enter untuk ke Menu Utama: ')
        program_utama()  
        
    def menu_kategori():
        print('Pilih Kategori :')
        print('1. Novel')
        print('2. Pengetahuan')
        print('3. Teknologi')
        print('4. Kembali')
        print('5. Menu Utama')
    
    if menu == 'utama':
        menu_utama()
    elif menu == 'kategori':
        menu_kategori()

def display():
    global daftar_buku_semua
    daftar_buku_semua = daftar_buku_novel + daftar_buku_pengetahuan + daftar_buku_teknologi
    
    table = PrettyTable()
    table.field_names = ['No', 'ID', 'Judul Buku', 'Pengarang', 'Total Stok', 'Dipinjam']
    for i, buku in enumerate(daftar_buku_semua, start=1):
        table.add_row([i]+buku)
    print(table)
            
def generate_id(daftar_buku, prefix):
    if not daftar_buku:
        return f"{prefix}001"
    
    # Mengambil ID dari baris terakhir di list
    last_id = daftar_buku[-1][0]
    
    # Mengambil angka setelah huruf pertama
    last_num = int(last_id[1:])
    
    #angka terakhir + 1
    new_num = last_num + 1
    
    # Mengubah format menjadi 3 digit
    return f"{prefix}{new_num:03d}"

def update_buku(kolom, nilai_baru, is_number=False):
    display()
    while True:
        try:
            no = int(input(f'Buku nomer berapa yang ingin diubah {nilai_baru}-nya: '))
        except:
            print('Tolong Masukan Pilihan Berupa Angka!')
            continue  
        
        if no < 1 or no > len(daftar_buku_semua):
            print("Nomor tidak valid ❌")
            continue  
        
        baru = input(f'Masukan {nilai_baru} Baru: ')
        
        #Khusus Stok
        if is_number:
            while True:
                try:
                    baru = int(baru)
                except:
                    print('Hanya Bisa Berupa Angka')
                    continue 
                
                break
        
        #Proses Pengubahan Buku    
        daftar_buku_semua[no -1][kolom] = baru            
        print(f'{nilai_baru} Berhasil Diubah ✅')  
        display()
        
        break

#Fitur
def daftar_buku(): 
    while True:
        print('\nList Daftar Buku :')
        print('1. Lihat Semua Buku')
        print('2. Lihat Berdasarkan Kategori')
        print('3. Kembali')
        print('4. Menu Utama')
        try:
            pilihan_menu = int(input('\nPilih Menu (1-4): '))
        except ValueError:
            print('Tolong Masukan Pilihan Berupa Angka! ')   
            continue
        
        if pilihan_menu == 1: #Menampilkan Semua Buku
            display()
        elif pilihan_menu == 2: #Menampilkan Buku Berdasarkan Pilihan Kategori
            while True:
                menu('kategori')
                try:
                    pilihan_kat = int(input('\nPilih Menu (1-5): '))
                except ValueError:
                    print('Tolong Masukan Pilihan Berupa Angka!')
                    continue
                
                #Kondisi untuk mana yang ingin ditampilkan 
                if pilihan_kat == 1:
                    table = PrettyTable()
                    table.field_names = ['No', 'ID', 'Judul Buku', 'Pengarang', 'Total Stok', 'Dipinjam']
                    for i, buku in enumerate(daftar_buku_novel, start=1):
                        table.add_row([i]+buku)
                    print(table)   
                       
                elif pilihan_kat == 2:
                    table = PrettyTable()
                    table.field_names = ['No', 'ID', 'Judul Buku', 'Pengarang', 'Total Stok', 'Dipinjam']
                    for i, buku in enumerate(daftar_buku_pengetahuan, start=1):
                        table.add_row([i]+buku)
                    print(table) 
                    
                elif pilihan_kat == 3:
                    table = PrettyTable()
                    table.field_names = ['No', 'ID', 'Judul Buku', 'Pengarang', 'Total Stok', 'Dipinjam']
                    for i, buku in enumerate(daftar_buku_teknologi, start=1):
                        table.add_row([i]+buku)
                    print(table)
                    
                elif pilihan_kat == 4:
                    break
                elif pilihan_kat == 5:
                    menu('utama')
                else:  
                    print('Nomor tidak valid ❌')
                    
        elif pilihan_menu == 3: 
            break
        elif pilihan_menu == 4:
            menu('utama')
        else:
            print('Nomor tidak valid ❌')   
            
def tambah_buku(): 
    menu('kategori')
    while True:    
        try:
            pilihan_kat = int(input('\nPilih Kategori untuk buku baru (1-5): '))
        except ValueError:
            print('Tolong Masukan Pilihan Berupa Angka!')
            continue
        
        #Memilih Kategori Untuk Buku Baru
        kategori = {
            1: (daftar_buku_novel, 'N'),
            2: (daftar_buku_pengetahuan, 'P'),
            3: (daftar_buku_teknologi, 'T')
        }
        
        if pilihan_kat in kategori:
            target_list, prefix = kategori[pilihan_kat]    
        elif pilihan_kat == 4:
            break
        elif pilihan_kat == 5:
            menu('utama')
        else:
            print("Nomor tidak valid! ❌")
            continue
        
        #Input Buku Baru   
        id_buku = generate_id(target_list, prefix)
        print(f"Buku Diberi ID : {id_buku}")
        judul = input('Masukan Judul Buku : ')
        nama_pengarang = input('Masukan Nama Pengarang Buku : ')
        dipinjam = 0
        try:
            jumlah = int(input('Masukan Jumlah Buku : '))
        except:
            print('Tolong Masukan Pilihan Berupa Angka!')
            continue
        
        #Preview Buku Baru
        table_pinjam = PrettyTable()
        table_pinjam.field_names = (['ID', 'Judul Buku', 'Pengarang', 'Jumlah'])
        table_pinjam.add_row([id_buku, judul, nama_pengarang, jumlah])
        print('\nInformasi Penambahan Buku')
        print(table_pinjam)          
        
        #Konfirmasi
        konfirmasi = input(f"Apakah data sudah benar? (Y/N): ").lower()
        if konfirmasi == 'y':
            target_list.append([id_buku, judul, nama_pengarang, jumlah, dipinjam])
            print(f'\nBuku "{judul}" Berhasil Ditambahkan dengan ID: {id_buku} ✅')
            display()
            break
        else:
            print("\nPenambahan buku dibatalkan.")         
            menu('kategori')   
            
def ubah_buku():
    while True:    
        print('List Ubah Buku: ')
        print('1. Ubah Judul Buku')
        print('2. Ubah Nama Pengarang')
        print('3. Ubah Stok')
        print('4. Ubah Kategori Buku')
        print('5. Kembali')
        print('6. Menu Utama')
        try:
            pilihan_menu = int(input('\nPilih Menu (1-6): '))
        except ValueError:
            print('Tolong Masukan Pilihan Berupa Angka!')
            continue
        
        #Kondisi Yang Ingin Diubah
        if pilihan_menu == 1:
            update_buku(1, 'Judul')
        elif pilihan_menu == 2:
            update_buku(2, 'Nama Pengarang')
        elif pilihan_menu == 3:
            update_buku(3, 'Stok', True)
        elif pilihan_menu == 4:
            display()
            while True:
                try:
                    no_kat = int(input('Buku nomer berapa yang ingin diubah Kategori-nya: '))
                except ValueError:
                    print('Tolong Masukan Pilihan Berupa Angka!')
                    continue  
                
                if no_kat < 1 or no_kat > len(daftar_buku_semua):
                    print("Nomor tidak valid ❌")
                    continue 
                
                # Ambil Data Buku Lama
                buku = daftar_buku_semua[no_kat - 1]
                id_buku, judul, pengarang, stok, dipinjam = buku
                
                #Memilih Kategori Untuk Buku Baru
                menu('kategori')
                while True:
                    try:
                        kat_baru = int(input('Pilih Kategori Buku Baru: '))
                    except ValueError:
                        print('Tolong Masukan Pilihan Berupa Angka!')
                        continue
                    
                    kategori = {
                        1: (daftar_buku_novel, 'N'),
                        2: (daftar_buku_pengetahuan, 'P'),
                        3: (daftar_buku_teknologi, 'T')
                    }
                
                    if kat_baru in kategori:
                        target_list, prefix = kategori[kat_baru]
                    elif kat_baru == 4:
                        break
                    elif kat_baru == 5:
                        menu('utama')
                    else:
                        print("Nomor tidak valid ❌")   
                        continue
                    
                    #Hapus ID yang ditemukan
                    for id_lama in [daftar_buku_novel, daftar_buku_pengetahuan, daftar_buku_teknologi]:
                        for i, buku in enumerate(id_lama):  
                            if buku[0] == id_buku:
                                del id_lama[i]      
                                break
                
                    #Buat ID Baru
                    id_baru = generate_id(target_list, prefix) 
                    target_list.append([id_baru, judul, pengarang, stok, dipinjam])       
                
                    print(f'Kategori Buku {judul} Berhasil Diubah ✅')  
                    display()
                    break
                
                break

        elif pilihan_menu == 5:
            break
        elif pilihan_menu == 6:
            menu('utama')
        else:
            print("Nomor tidak valid ❌")
            
def hapus_buku(): 
    while True:
        print('\nList Hapus Buku: ')
        print('1. Hapus Berdasarkan ID Buku')
        print('2. Hapus Kategori Buku')
        print('3. Hapus Semua Buku')
        print('4. Kembali')
        print('5. Menu Utama')
        try:
            pilihan_menu = int(input('\nPilih Menu (1-5): '))
        except ValueError:
            print('Tolong Masukan Pilihan Berupa Angka!')
            continue
        
        if pilihan_menu == 1: #Hapus Berdasarkan ID Buku
            display()
            while True:
                id_hapus = input('\nMasukan ID Buku yang ingin dihapus? : ').upper()

                kategori = {
                    'N': daftar_buku_novel,
                    'P': daftar_buku_pengetahuan,
                    'T': daftar_buku_teknologi
                }
                
                prefix = id_hapus[0]
                if prefix not in kategori:
                    print('Format ID : 1 Huruf + 3 angka. (contoh : N001)') 
                    continue 
                
                target_list = kategori[prefix]
                index_hapus = None
                
                #Cari Buku Berdasarkan ID
                for i, buku in enumerate(target_list):
                    if buku[0] == id_hapus:
                        index_hapus = i
                        break
                        
                #Jika Buku Tidak Ditemukan
                if index_hapus is None:
                    print('Buku tidak ditemukan ❌')
                    continue
                    
                buku = target_list[index_hapus]
            
                #Jika Buku Ditemukan
                table_hapus = PrettyTable()
                table_hapus.field_names = (['ID', 'Judul', 'Pengarang'])
                table_hapus.add_row([buku[0], buku[1], buku[2]])
                print(table_hapus)
                    
                konfirmasi = (input(f'\nYakin hapus buku ini? (Y/N)')).lower()   
                if konfirmasi == 'y':
                    recyclebin.append(target_list.pop(index_hapus))
                    print('\nBuku Berhasil dihapus ✅')
                    display()
                    break  
                else:
                    print('\nHapus Buku dibatalkan.')
                    break
                             
        elif pilihan_menu == 2: #Hapus Kategori Buku    
            while True:
                menu('kategori')
                try:
                    pilihan_kat = int(input('Kategori yang ingin dihapus (1-3): '))
                except ValueError:
                    print('Tolong Masukan Pilihan Berupa Angka!')
                    continue
            
                if pilihan_kat == 1: #Menghapus Kategori Novel
                    konfirmasi = (input(f'\nYakin hapus kategori buku ini? (Y/N)')).lower() 
                    if konfirmasi == 'y':
                        recyclebin.extend(daftar_buku_novel)
                        daftar_buku_novel.clear()
                        display()
                        break
                    else:
                        print('\nHapus Buku dibatalkan.')
                        break
                if pilihan_kat == 2: #Menghapus Kategori Pengetahuan
                    konfirmasi = (input(f'\nYakin hapus kategori buku ini? (Y/N)')).lower() 
                    if konfirmasi == 'y':
                        recyclebin.extend(daftar_buku_pengetahuan)
                        daftar_buku_pengetahuan.clear()
                        display()
                        break
                    else:
                        print('\nHapus Buku dibatalkan.')
                        break
                if pilihan_kat == 3:#Menghapus Kategori Teknologi
                    konfirmasi = (input(f'\nYakin hapus kategori buku ini? (Y/N)')).lower() 
                    if konfirmasi == 'y':
                        recyclebin.extend(daftar_buku_teknologi)
                        daftar_buku_pengetahuan.clear()
                        display()
                        break
                    else:
                        print('\nHapus Buku dibatalkan.')
                        break
                elif pilihan_menu == 4:
                    break
                elif pilihan_menu == 5:
                    menu('utama')
                else:
                    print("Nomor tidak valid ❌")
        
        elif pilihan_menu == 3: #Hapus Semua Buku 
            konfirmasi = (input(f'\nYakin hapus semua buku ini? (Y/N)')).lower() 
            if konfirmasi == 'y':
                recyclebin.extend(daftar_buku_novel)
                recyclebin.extend(daftar_buku_pengetahuan)
                recyclebin.extend(daftar_buku_teknologi)

                daftar_buku_novel.clear()
                daftar_buku_pengetahuan.clear()
                daftar_buku_teknologi.clear()
                print('\nSemua Buku Berhasil dihapus ✅')
            else:
                print('\nHapus Buku dibatalkan.')
                break
        elif pilihan_menu == 4: 
            break
        elif pilihan_menu == 5: 
            menu('utama')
        else:
            print('\nNomor tidak valid ❌')
            
def pinjam_buku(): 
    display()   
    nama_peminjam = input('Masukan Nama Peminjam : ')
    while True:
        id_pinjam = (input('\nMasukan ID Buku yang ingin dipinjam? : ')).lower()
        index_pinjam = False
        
        #Cari Buku Berdasarkan ID
        for i, buku in enumerate(daftar_buku_semua):
            if buku[0].lower() == id_pinjam:
                index_pinjam = i
                break
        
        judul = daftar_buku_semua[index_pinjam][1]
        total_stok = daftar_buku_semua[index_pinjam][3]
        dipinjam = daftar_buku_semua[index_pinjam][4]
        sisa_stok = total_stok - dipinjam
        
        #Jika Buku Ditemukan    
        if index_pinjam is not False:
            if sisa_stok <=0 :
                print(f'\nMohon maaf, stok buku "{judul}" sedang tidak tersedia ❌')
                continue
            
            #Tabel Konfirmasi   
            table_pinjam = PrettyTable()
            table_pinjam.field_names = (['Nama Peminjam', 'Judul Buku', 'ID Buku'])
            table_pinjam.add_row([nama_peminjam, daftar_buku_semua[index_pinjam][1], daftar_buku_semua[index_pinjam][0]])
            print('\nInformasi Peminjaman')
            print(table_pinjam)          
            konfirmasi = (input('\nApakah Data Sudah Benar?. Konfirmasi peminjaman (Y/N)')).lower()       
            
            if konfirmasi == 'y':                  
                daftar_buku_semua[index_pinjam][4] += 1
                print('\nBuku berhasil dipinjam ✅')
                break
                
            else:
                print('Peminjaman buku dibatalkan.')
                break
        else:
            print('Buku tidak ditemukan ❌')  
            print('Format ID : 1 Huruf + 3 angka. (contoh : N001)')      
                            
def recycle_bin(): 
    while True:
        print('List Recycle Bin: ')
        print('1. Lihat Buku')
        print('2. Restore Buku')
        print('3. Hapus Permanen')
        print('4. Kembali')
        print('5. Menu Utama')
        try:
            pilihan_menu = int(input('\nPilih Menu (1-5): '))
        except ValueError:
            print('Tolong Masukan Pilihan Berupa Angka!')
            continue  
        
        if pilihan_menu == 1: #Lihat Buku
            table_recyclebin = PrettyTable()
            table_recyclebin.field_names = ['No','ID','Judul','Pengarang']
            if not recyclebin:
                print(table_recyclebin)
                continue
                
            for i, buku in enumerate(recyclebin, start=1):
                table_recyclebin.add_row([i, buku[0],buku[1],buku[2]])
            print(table_recyclebin)
            
        elif pilihan_menu == 2: #Restore Buku
            if not recyclebin:
                print('\nRecycle Bin kosong 📂')
                continue
            
            print(table_recyclebin)
            no = int(input('Pilih nomor buku yang ingin direstore: '))

            if no < 1 or no > len(recyclebin):
                print('Nomor tidak valid ❌')
                continue

            buku_restore = recyclebin.pop(no-1)

            prefix = buku_restore[0][0]

            if prefix == 'N':
                daftar_buku_novel.append(buku_restore)
            elif prefix == 'P':
                daftar_buku_pengetahuan.append(buku_restore)
            elif prefix == 'T':
                daftar_buku_teknologi.append(buku_restore)

            print(f'\nBuku "{buku_restore[1]}" berhasil direstore ✅')
            display()
              
        elif pilihan_menu == 3: #Hapus Permanen
            if not recyclebin:
                print('\nRecycle Bin kosong 📂')
                continue
            print(table_recyclebin)
            no = int(input("Pilih nomor buku yang ingin dihapus permanen: "))

            if no < 1 or no > len(recyclebin):
                print('Nomor tidak valid ❌')
                continue

            del recyclebin[no-1]
            print("Buku dihapus permanen ✅")

        elif pilihan_menu == 4:
            break
        elif pilihan_menu == 5:
            menu('utama')
        else:
            print("Nomor tidak valid ❌")   
            continue  
        
program_utama()