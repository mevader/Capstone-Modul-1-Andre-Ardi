yellowPages = [
    {
        'numYp' : '001',
        'nama' : 'abu ubaidah',
        'alamat': 'jakarta',
        'pekerjaan': 'karyawan swasta',
        'nomor HP': '+62 877 86510914',
        'email': 'ubaidah07@gmail.com'
    },
    {
        'numYp' : '002',
        'nama' : 'roger waters',
        'alamat': 'bali',
        'pekerjaan': 'dosen',
        'nomor HP': '+62 821 22125075',
        'email': 'roger_waters@yahoo.com'
    },
    {
        'numYp' :'003',
        'nama' : 'dave mustaine',
        'alamat': 'palembang',
        'pekerjaan': 'pegawai negeri',
        'nomor HP': '+62 856 7044322',
        'email': 'davemustaine666@yahoo.com'
    },
    {
        'numYp' :'004',
        'nama' : 'izzudin alqasam',
        'alamat': 'jogjakarta',
        'pekerjaan': 'dokter',
        'nomor HP': '+62 821 1138327',
        'email': 'alqassam07@gmail.com '
    },
    {
        'numYp' :'005',
        'nama' : 'ismail haniyeh',
        'alamat': 'makasar',
        'pekerjaan': 'wiraswasta',
        'nomor HP': '+62 878 89941186',
        'email': 'ismail24haniyeh@gmail.com'
    },
    {
        'numYp':'006',
        'nama' : 'james hetfield',
        'alamat': 'palembang',
        'pekerjaan': 'pegawai negeri',
        'nomor HP': '+62 821 1138501',
        'email': 'papa999het@gmail.com'
    },
    {
        'numYp':'007',
        'nama' : 'scott ian',
        'alamat': 'palembang',
        'pekerjaan': 'pegawai negeri',
        'nomor HP': '+62 856 70422334',
        'email': 'ianscott@yahoo.com'
    },
    {
        'numYp' :'008',
        'nama' : 'herman li',
        'alamat': 'makasar',
        'pekerjaan': 'pegawai negeri',
        'nomor HP': '+62 856 7041111',
        'email': 'dragonli@gmail.com'
    }
]

#pilihan 1: tampil seluruh data
def tampilSeluruhData():
    print('\nDATA YELLOW PAGES')
    print ('IDX |NoYP|\tNAMA       \t| ALAMAT      \t|\tPEKERJAAN    \t|\tNO HP        \t|\tEMAIL\t')
    for i in range(len(yellowPages)):
        print(' {}  |{} |{}      \t| {}   \t| {}       \t| {}\t| {}\t'.format(i, yellowPages[i]['numYp'], yellowPages[i]['nama'], yellowPages[i]['alamat'], yellowPages[i]['pekerjaan'], yellowPages[i]['nomor HP'], yellowPages[i]['email']) )

#pilihan 2: panggil nomor Yellow Pages
def panggilNumYpData():
    tampilSeluruhData()
    masukkanNumYp = input('\nMasukkan nomor Yellow Pages: ')
    print('\nDATA YELLOW PAGES')
    print ('IDX |NoYP|\tNAMA       \t| ALAMAT      \t|\tPEKERJAAN    \t|\tNO HP        \t|\tEMAIL\t')
    
    for i in range(len(yellowPages)):
        if yellowPages[i]['numYp'] == str(masukkanNumYp):
            print(' {}  |{} |{}      \t| {}   \t| {}       \t| {}\t| {}\t'.format(i, yellowPages[i]['numYp'], yellowPages[i]['nama'], yellowPages[i]['alamat'], yellowPages[i]['pekerjaan'], yellowPages[i]['nomor HP'], yellowPages[i]['email'])) 

   
    if not list(filter(lambda d : d['numYp'] == masukkanNumYp, yellowPages)):
        print('\nMaaf nomor Yellow Pages tidak ditemukan')
    
    cekNumYp = input('\nMasih ada data yang nomor Yellow Pages yang ingin ditampilkan (ya/tidak:): ')
    if cekNumYp == 'ya':
        panggilNumYpData()

#pilihan 3: panggil nama tertentu
def panggilNama():
    tampilSeluruhData()
    masukkanNama = input('\nMasukkan nama yang dicari(gunakan huruf kecil): ')
    print('\nDATA YELLOW PAGES')
    print ('IDX |NoYP|\tNAMA       \t| ALAMAT      \t|\tPEKERJAAN    \t|\tNO HP        \t|\tEMAIL\t')
    for i in range(len(yellowPages)):
        if yellowPages[i]['nama'] == str(masukkanNama):
            print(' {}  |{} |{}      \t| {}   \t| {}       \t| {}\t| {}\t'.format(i, yellowPages[i]['numYp'], yellowPages[i]['nama'], yellowPages[i]['alamat'], yellowPages[i]['pekerjaan'], yellowPages[i]['nomor HP'], yellowPages[i]['email']) )

    if not list(filter(lambda d : d['nama'] == masukkanNama, yellowPages)):
        print('\nMaaf nama tidak ditemukan')


    cekNama = input('\nMasih ada data nama yang ingin ditampilkan (ya/tidak:): ')
    if cekNama == 'ya':
        panggilNama()


#pilihan 4: panggil alamat tertentu
def panggilAlamat():
    tampilSeluruhData()
    masukkanAlamat = input('\nMasukkan alamat yang dicari(gunakan huruf kecil): ')
    print('\nDATA YELLOW PAGES')
    print ('IDX |NoYP|\tNAMA       \t| ALAMAT      \t|\tPEKERJAAN    \t|\tNO HP        \t|\tEMAIL\t')
    for i in range(len(yellowPages)):
        if yellowPages[i]['alamat'] == str(masukkanAlamat):
            print(' {}  |{} |{}      \t| {}   \t| {}       \t| {}\t| {}\t'.format(i, yellowPages[i]['numYp'], yellowPages[i]['nama'], yellowPages[i]['alamat'], yellowPages[i]['pekerjaan'], yellowPages[i]['nomor HP'], yellowPages[i]['email']) )

    if not list(filter(lambda d : d['alamat'] == masukkanAlamat, yellowPages)):
        print('\nMaaf alamat tidak ditemukan')
    
    cekAlamat = input('\nMasih ada data alamat yang ingin ditampilkan (ya/tidak:): ')
    if cekAlamat == 'ya':
        panggilAlamat()


#pilihan 5: panggil pekerjaan tertentu
def panggilPekerjaan():
    tampilSeluruhData()
    masukkanPekerjaan = input('\nMasukkan pekerjaan yang dicari(gunakan huruf kecil): ')
    print('\nDATA YELLOW PAGES')
    print ('IDX |NoYP|\tNAMA       \t| ALAMAT      \t|\tPEKERJAAN    \t|\tNO HP        \t|\tEMAIL\t')   
    for i in range(len(yellowPages)):
        if yellowPages[i]['pekerjaan'] == str(masukkanPekerjaan):
            print(' {}  |{} |{}      \t| {}   \t| {}       \t| {}\t| {}\t'.format(i, yellowPages[i]['numYp'], yellowPages[i]['nama'], yellowPages[i]['alamat'], yellowPages[i]['pekerjaan'], yellowPages[i]['nomor HP'], yellowPages[i]['email']) )

    if not list(filter(lambda d : d['pekerjaan'] == masukkanPekerjaan, yellowPages)):
        print('\nMaaf pekerjaan tidak ditemukan')

    cekPekerjaan = input('\nMasih ada data pekerjaan yang ingin ditampilkan (ya/tidak:): ')
    if cekPekerjaan == 'ya':
        panggilPekerjaan()



#pilihan 6: menambah data
def tambahData():
    tampilSeluruhData()
    tambahNum = input('\nMasukkan nomor Yellow Pages baru: ')
    tambahNama = input('Masukkan nama baru (huruf kecil semua): ')
    tambahAlamat = input('Masukkan alamat baru(huruf kecil semua): ')
    tambahpekerjaan = input('Masukkan pekerjaan baru(huruf kecil semua): ')
    tambahHp = input('Masukkan nomor HP baru: ')
    tambahEmail = input('Masukkan alamat email baru: ')
    yellowPages.append({
        'numYp' : tambahNum,
        'nama' : tambahNama,
        'alamat' : tambahAlamat,
        'pekerjaan' : tambahpekerjaan,
        'nomor HP' : tambahHp,
        'email' : tambahEmail 
    })
    tampilSeluruhData()

    cekTambahData = input('\nMasih ada data yang ingin ditambahkan (ya/tidak:): ')
    if cekTambahData == 'ya':
        tambahData()
    

#pilihan 7: perbarui data tertentu
def upDateValue():
    tampilSeluruhData()
    
    inputindex = int(input('\nmasukkan nomor index data yang ingin diperbarui: '))
    if inputindex > (int(len(yellowPages)-1)):
        print('Maaf index tidak ditemukan\n')
        upDateValue()

    inputKey = str(input('Masukkan key data yang ingin diperbarui: '))
    if not any(inputKey in d for d in yellowPages):
        print(f"Maaf 'key = {inputKey}' tidak ditemukan\n")
        upDateValue()

    inputValueBaru = str(input('Masukkan value baru: '))
    yellowPages[inputindex][inputKey] = inputValueBaru
    tampilSeluruhData()

    cekUpdateValue = input('\nMasih ada data alamat yang ingin diperbarui (ya/tidak:): ')
    if cekUpdateValue == 'ya':
        upDateValue()


#pilihan 8: menghapus data tertentu
def hapusData():
    tampilSeluruhData()
    inputHapusData = int(input('\nMasukkan nomor index data yang akan dihapus: '))
    if inputHapusData > (int(len(yellowPages)-1)):
        print('Maaf index tidak ditemukan\n')
        hapusData()

    del yellowPages[inputHapusData]
    tampilSeluruhData()
    

    cekHapusData = input('\nMasih ada data yang ingin dihapus (ya/tidak:): ')
    if cekHapusData == 'ya':
        hapusData()


#pilihan 9: menghapus seluruh data 
def hapusSemuaData():
    tampilSeluruhData()
    inputHapusAll = input('\nAnda yakin akan menghapus seluruh data Yellow Pages (ya/tidak): ')
    if inputHapusAll == 'ya':
        yellowPages.clear()
        print('\nData telah terhapus seluruhnya')
    else:
        print('\nData tidak jadi dihapus')

    tampilSeluruhData()
    

while True:
    pilihanMenu = input('''
SELAMAT DATANG DI YELOWPAGES
Daftar Menu:
1. Menampilkan seluruh daftar 
2. Menampilkan data berdasarkan nomor Yellow Pages 
3. Menampilkan data berdasarkan nama tertentu
4. Menampilkan data berdasarkan alamat tertentu
5. Menampilkan data berdasarkan pekerjaan tertentu
6. Menambah data
7. Memperbarui data tertentu
8. Menghapus data tertentu
9. Menghapus seluruh data                        
10. Keluar

Silakan masukkan nomor menu yang dibutuhkan: ''')
    
    if(pilihanMenu == '1') :
        tampilSeluruhData()
    
    elif(pilihanMenu == '2'):
        panggilNumYpData()
         
    elif(pilihanMenu == '3'):
        panggilNama()

    elif(pilihanMenu == '4'):
        panggilAlamat()

    elif(pilihanMenu == '5'):
        panggilPekerjaan()    
   
    elif(pilihanMenu == '6'):
        tambahData()

    elif(pilihanMenu == '7'):
        upDateValue()
   
    elif(pilihanMenu == '8'):
        hapusData()
    
    elif(pilihanMenu == '9'):
        hapusSemuaData()

    elif(pilihanMenu == '10'):
        break