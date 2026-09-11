print("Ayo buat playlist lagu Anda, masukkan lagu-lagu favorit ke dalamnya!")
# pemilihan nama playlist
nama_playlist = input("Masukkan nama playlist Anda: ")

# Tupple lagu
print ("\nBerikut adalah lagu-lagu yang tersedia: ")
lagu = ("kiss me - Ariana Grande", "Drag Path - Twenty One Pilots", "Enter Sandman - Metallica", "Autumn - NIKI", "Sound Of Rain - Lany", "Join Me - HIM", "4ME 4ME - Malcolm Todd", "Bila Kau Tidak Disampingku - Sheila On 7", "Evanescence - your star", "Besame Mucho - Andrea Bocelli")
for i in range(len(lagu)):
    print(f"{i+1}. {lagu[i]}")

playlist = []
# menu playlist
while True :
    print ()
    print ("=====Daftar Menu Playlist=====")
    print ("1. Tambah lagu")
    print ("2. Hapus lagu")
    print ("0. Selesai")
    print ("=" * 31)
    menu = input("Pilih menu: ")

# Tambah lagu
    if menu == "1":
        print()
        while True :
            pilih = input("Pilih nomor lagu yang ingin Anda masukkan ke playlist Anda ('0' untuk selesai): ")
            if pilih == "0":
                break

            if pilih.isdigit():
                nomor = int(pilih)
        
                if nomor >= 1 and nomor <= len(lagu):
                    handak_dipilih = lagu[nomor - 1 ]
        
                    if handak_dipilih not in playlist:
                        playlist.append(handak_dipilih)
                        print(f"\x1B[3mMenambahkan lagu '{handak_dipilih}' ke playlist\x1B[0m")
                    else:
                        print(f"Lagu \x1B[3m{handak_dipilih}\x1B[0m sudah ada di playlist")
        
                else:
                    print("Nomor lagu tidak tersedia")
                    continue
            else:
                print("Harus berupa nomor!")
                continue

# Hapus lagu
    elif menu == "2":
        # List lagu sementara
        if len(playlist) == 0:
            print(f"\nPlaylist '{nama_playlist}' masih kosong! ૮(˶╥︿╥)ა")
        else:
            print (f"\nPlaylist '{nama_playlist}' terbuat!")
            for i in range (len(playlist)):
                print(i + 1, ".", playlist[i])

        # Pembatalan lagu
        while True :
            if len(playlist) == 0:
                break
            hapus = input("\nKetik nomor lagu yang ingin dihapus ('0' untuk batal): ")
            if hapus == "0":
                break
            if hapus.isdigit():
                nomor = int(hapus)
                if nomor >= 1 and nomor <= len(playlist):
                    lagu_hapus = playlist.pop(nomor - 1)
                    print(lagu_hapus, "berhasil dihapus dari playlist")
                else:
                    print ("Nomor lagu tidak tersedia")
            else:
                print("Harus berupa nomor!")

    # Selesai
    elif menu == "0":
        break
    else:
        print("Pilihan tidak tersedia")

# akhir tapi bukan berakhir ASIQQQQ
print()
print("𓆝 𓆟 𓆞 𓆝 𓆟" * 5)
teks = (f"Playlist '{nama_playlist}'")
print (f"{teks:^40}")
if len(playlist) == 0:
    print(f"Tambahkan lagu favorit Anda untuk mengisi playlist '{nama_playlist}' ᕙ( •̀ ᗜ •́ )ᕗ")
else:
    for i in range (len(playlist)):
        print(i + 1, ".", playlist[i])
print("𓆝 𓆟 𓆞 𓆝 𓆟" * 5)