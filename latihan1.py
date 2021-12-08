print ("Jujun Junaedi")
print ("312110568")
print ("TI21C5")
print ("Tugas Pertemuan ke 9")
print('='*50)
#1. membuat dictionary daftar kontak
daftar_kontak = {
    "dina":'089123111',
    "ucup":'0853131444',
}
print(daftar_kontak)

#2. menambah kontak baru
daftar_kontak['riko'] = '087654544'
print(daftar_kontak)

#3. mengubah kontak dina dengan nomor baru
daftar_kontak['dina'] = '088999776'

#4. menampilkan semua nama
print(daftar_kontak.keys())

#5. menampilkan semua nomor
print(daftar_kontak.values())

#6. menampilkan daftar nama dan nomornya
print(daftar_kontak.items())

#7. menghapus kontak dina
del daftar_kontak['dina']
print(daftar_kontak)