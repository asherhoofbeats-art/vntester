# ==========================================
# FILE: cheat_tester.rpy
# CHEAT MENU UNTUK TESTING ENDING (DENGAN UI AUDIOVISUAL)
# ==========================================

label cheat_tester_ending:
    scene black with dissolve
    play music "bgm_tense_investigation.ogg" fadein 1.0
    
    # Reset semua variabel ke nilai dasar agar aman dari tumpang tindih
    $ poin_investigasi = 0 #Dari Chapter Awal
    $ citra_resonansi_gaib = 0 #Dari Chapter Awal Setiap MG Gaib
    $ item_jenglot = False #Dari Chapter Melawan Renggo Pilihan
    $ item_gembok_berlendir = False #Dari Chapter 01
    $ item_gembok_rusak = False #Dari Chapter 01
    $ item_lendir_hijau = False #Dari Chapter 02
    $ item_bukti_otopsi = False #Dari Chapter 05
    $ item_rekaman_tirto = False #Dari Chapter 05
    $ item_rekaman_renggo = False #Dari Chapter 04
    $ item_buku_kas_merah = False #Dari Chapter 07
    $ item_speaker_hantu = False #Dari Chapter 05
    $ item_koin_kuno = False #Dari Chapter 04
    $ item_boneka_jerami = False #Dari Chapter 04
    $ item_kristal_merah = False #Dari Chapter 04
    $ item_kalung_galih = False #Dari Chapter 03
    $ dr_rina_selamat = False #Dari Chapter 05
    $ gatot_trust = False #Dari Chapter 06
    $ darmi_trust = False #Dari Chapter 02

    menu:
        "PILIH ENDING YANG INGIN DI-TEST SEKARANG:"

        "Ending 3 (TRUE ENDING): Penjara Fisik & Batin":
            play sound "sfx_magic_charge.ogg"
            "SISTEM: Menginjeksi nilai Perfect Run."
            "NILAI: Investigasi = 10, Resonansi = 10, Rina = Hidup, Gatot = Trust."
            "ITEM: Jenglot, Gembok, Lendir, Otopsi, Rekaman Tirto & Renggo, Buku Kas, Speaker, Koin Kuno."
            "PENJELASAN LOGIKA: Kombinasi sempurna. Bukti hukum memberatkan Kades agar dipenjara seumur hidup, sementara benda gaib memancing entitas mistis untuk terus menerornya di dalam sel."
            
            $ poin_investigasi = 10
            $ citra_resonansi_gaib = 10
            $ item_jenglot = True
            $ item_gembok_berlendir = True
            $ item_lendir_hijau = True
            $ item_bukti_otopsi = True
            $ item_rekaman_tirto = True
            $ item_rekaman_renggo = True
            $ item_buku_kas_merah = True
            $ gatot_trust = True
            $ dr_rina_selamat = True
            $ item_speaker_hantu = True
            $ item_koin_kuno = True
            jump evaluasi_ending_utama

        "Ending 5 (GOOD ENDING): Startup Detektif Mistis":
            play sound "sfx_serangan_cepat.ogg"
            "SISTEM: Menginjeksi nilai Good Ending."
            "NILAI: Investigasi = 7, Darmi = Trust."
            "ITEM: Buku Kas Merah, Rekaman Tirto."
            "PENJELASAN LOGIKA: Pemain memiliki bukti hukum kuat untuk memenjarakan Tirto dan reputasi baik (Darmi Trust) untuk diangkat jadi pahlawan. Namun, ketiadaan item mistis mencegah terpicunya Absolute True Ending."
            
            $ poin_investigasi = 7
            $ item_buku_kas_merah = True
            $ item_rekaman_tirto = True
            $ darmi_trust = True
            jump evaluasi_ending_utama

        "Ending 6 (BAD KARMA): Lahirnya Dukun Baru":
            play sound "sfx_demonic_growl.ogg"
            "SISTEM: Menginjeksi nilai Bad Karma."
            "NILAI: Item Boneka Jerami = True, Item Kristal Merah = False."
            "PENJELASAN LOGIKA: Pemain membawa kutukan kesialan (Boneka Jerami) dan gagal merebut sumber ilmu Ki Renggo (Kristal Merah). Hal ini memberi jalan bagi Tirto untuk mengambil benda pusaka tersebut dan meneruskan estafet ilmu hitam."
            
            $ item_boneka_jerami = True
            $ item_kristal_merah = False
            jump evaluasi_ending_utama

        "Ending 4 (DARK COMEDY): Tirto Gila di Hutan":
            play sound "sfx_creaky_door_open.ogg"
            "SISTEM: Menginjeksi nilai Dark Comedy."
            "NILAI: Gatot Trust = False, Item Kalung Galih = True."
            "PENJELASAN LOGIKA: Gatot tidak mempercayai Trio sehingga ia lengah menahan Tirto saat kekacauan terjadi. Tirto berhasil kabur, namun Kalung Galih bersamanya memancarkan energi negatif yang merusak kewarasannya secara perlahan."
            
            $ gatot_trust = False
            $ item_kalung_galih = True
            jump evaluasi_ending_utama

        "Ending 2 (BAD INVESTIGATION): Tirto Bebas":
            play sound "sfx_benda_jatuh.ogg"
            "SISTEM: Menginjeksi nilai Bad Investigation."
            "NILAI: Investigasi = 2, Buku Kas = False, Rekaman Tirto = False."
            "PENJELASAN LOGIKA: Poin investigasi terlalu rendah dan absennya bukti fisik kuat membuat laporan ke polisi dimentahkan. Pengacara mahal Tirto berhasil membebaskannya dari segala tuduhan."
            
            $ poin_investigasi = 2
            $ item_buku_kas_merah = False
            $ item_rekaman_tirto = False
            jump evaluasi_ending_utama

        "Ending 1 (DEFAULT): Koruptor Dapat Remisi":
            play sound "sfx_magic_spell.ogg"
            "SISTEM: Menginjeksi nilai Default/Normal."
            "NILAI: Investigasi = 5, Buku Kas = True, Rekaman Tirto = False, Gatot = Trust."
            "PENJELASAN LOGIKA: Pemain memiliki bukti standar untuk memenjarakan Tirto. Namun, tanpa efek karma gaib atau reputasi absolut, hukum berjalan seperti biasa di mana koneksi politik Tirto memberinya banyak remisi."
            
            $ poin_investigasi = 5
            $ item_buku_kas_merah = True 
            $ item_rekaman_tirto = False 
            $ gatot_trust = True
            jump evaluasi_ending_utama

        "Batal & Kembali":
            play sound "sfx_fast_swoosh.ogg"
            return