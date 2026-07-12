# ==========================================
# FILE: chapter01.rpy
# TEMA: Kedatangan & Panggilan Jarak Jauh
# ==========================================

label chapter_01:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Inisialisasi variabel petunjuk khusus untuk chapter ini
    $ ch1_jejak_gembok = False

    # Tampilan Judul Chapter di awal
    scene black with bangun_tidur
    play music "bgm_01_jejak_misteri.ogg" fadein 2.0
    centered "{size=+20}CHAPTER 01{/size}\n\nPanggilan Jarak Jauh & Gerbang Kematian" with dissolve_lambat
    pause 2.0
    
    # Scene 1: Di dalam mobil, perjalanan menuju TKP
    scene bg_mobil_trio with transisi_asap
    stop music fadeout 2.0
    play sound "sfx_suara_berkendara.ogg" loop fadein 1.0
    
    "Malam itu, di dalam mobil yang melaju menuju lokasi kejadian, suasana terasa sedikit tegang."
    
    stop sound fadeout 1.0
    play sound "sfx_cellphone_ring.ogg"
    "Namun, ketegangan itu pecah oleh dering panggilan video dengan frekuensi khusus dari benua Eropa."

    # --- CUT SCENE: Alat Komunikasi Raka ---
    scene cg_mg01a_alat_komunikasi with dissolve
    play sound "sfx_static_noise.ogg" loop
    "Raka mengeluarkan alat komunikasi modifikasinya untuk menstabilkan sinyal panggilan yang masuk."
    
    # Panggil Minigame A (Tuning Frekuensi Sinyal)
    window hide
    call screen mg_radio_tuning
    
    stop sound fadeout 1.0
    play sound "sfx_bip.ogg"
    play music "bgm_02_canda_trio.ogg" fadein 1.0

    # --- CUT SCENE: Panggilan Sarah Terhubung ---
    scene cg_mg01a_sarah_vcall with dissolve_kilat
    s "Heh! Kalian bertiga dengerin gue ya!"
    s "Gue emang lagi sibuk nugas di kampus Eropa nih, tapi gue tetep pantau berita gila dari Indo!"

    # --- CUT SCENE: Trio Investigator Bercanda di Mobil ---
    scene cg_ch01_canda_di_mobil with dissolve
    pause 2.0 # Jeda sebentar agar pemain bisa menikmati CG
    
    # Kembali ke Background dalam mobil untuk dialog dengan Sprite Karakter
    scene bg_mobil_trio with dissolve

    show raka_normal at center with dissolve_kilat
    r "Iya, iya, Bu Bos. Cerewet banget sih, fokus aja sama kuliah lu di sana."
    r "Ini cuma kasus pembunuhan biasa yang ditutup-tutupin pakai mitos konyol Buto Ijo. Gue yakin ada mafia di baliknya."
    hide raka_normal

    show sarah_lega at center with dissolve_kilat
    s "Biasa pala lu! Ingat ya Raka, jangan mentang-mentang lu jago karate terus lu pikir bisa nonjok hantu."
    s "Pokoknya kalau ada apa-apa, jangan nekat! Jagain tuh si Citra sama Bimo."
    hide sarah_lega

    show bimo_normal at center with dissolve_kilat
    b "Tenang saja, Sarah. Aku sudah merapal pagar gaib untuk berjaga-jaga sejak kita berangkat."
    b "Fokuslah pada studimu. Kami akan bertindak hati-hati."
    hide bimo_normal

    show sarah_normal at center with dissolve_kilat
    s "Nah, baguslah kalau Bimo yang ngomong, gue agak lega. Citra, lu jangan pingsan melulu ya!"
    hide sarah_normal

    show citra_panik at center with dissolve_kilat
    c "A-aku usahakan, Kak Sarah... Tapi jujur, dari jarak sejauh ini saja perasaanku udah nggak enak banget soal tempat itu."
    hide citra_panik

    show sarah_lega at center with dissolve_kilat
    s "Hadeh... Ya udah, dosen gue udah masuk nih. Good luck, Trio! Kabari gue kalau ada update. Awas lu pada mati konyol!"
    hide sarah_lega with tv_rusak
    
    play sound "sfx_bip.ogg"
    "Panggilan video terputus. Layar ponsel Raka kembali gelap."
    
    stop music fadeout 2.0

    # Scene 2: Tiba di luar Dapur MBG
    scene bg_luar_dapur with dorong_bawah
    show kabut_tebal
    show daun_gugur
    play sound "sfx_angin_malam_kencang.ogg" loop fadein 2.0
    play music "bgm_creepy_ambient.ogg" fadein 2.0
    
    "Mobil perlahan berhenti di depan bangunan besar yang dikelilingi garis polisi."
    "Ini adalah Dapur Sentral Program MBG. Tempat di mana tiga pegawai tewas mengenaskan secara misterius."

    # --- CUT SCENE: Pagar Gaib Bimo & Citra Ketakutan ---
    
    
    # Kembali ke Background luar dapur untuk dialog
    scene bg_luar_dapur with dissolve
    
    show bimo_berpikir at center with dissolve_lambat
    b "Hati-hati saat melangkah, Ka... Hawanya sangat pekat. Udara di sini terasa berat dan... anyir."
    hide bimo_berpikir
    
    show citra_lelah at center with dissolve_kilat
    c "Kak Bimo benar... Dadaku sesak banget. Seperti ada banyak 'mata' yang mengawasi kita dari balik jendela gelap itu."
    hide citra_lelah

    # --- CUT SCENE: Raka Skeptis & Membuka Pita Polisi ---
    scene cg_ch01_raka_skeptis with dissolve
    pause 1.5
    
    scene bg_luar_dapur with dissolve
    
    show raka_lega at center with dissolve_kilat
    r "Halah, itu cuma sugesti karena kalian kebanyakan baca berita soal pesugihan Buto Ijo."
    r "Logika aja, mana ada jin butuh makan katering gratis?"
    hide raka_lega

    show raka_berpikir at center with dissolve_kilat
    r "Tunggu sebentar... Coba lihat area gerbang ini."
    hide raka_berpikir
    
    # Panggil Minigame B (Investigasi Gerbang Point & Click)
    window hide
    call screen mg_investigasi_gerbang

    # Evaluasi Pilihan Minigame
    if _return == "gembok":
        $ ch1_jejak_gembok = True
        $ item_gembok_rusak = True
        $ item_gembok_berlendir = True
        $ poin_investigasi += 1
        # --- CUT SCENE: Temuan Gembok Kimia ---
        play sound "sfx_ding_idea.ogg"
        scene cg_mg01b_jejak_gembok with transisi_senter
        r "Gemboknya dipotong pakai alat pemotong besi hidrolik, dan ada noda bahan kimia di sini."
        
        # --- CUT SCENE: Raka Mengambil Sampel Residu ---
        scene cg_mg01c_ambil_sampel with dissolve
        play sound "sfx_kamera_digital.ogg"
        "Raka mengeluarkan alat scanner portabelnya dan mengambil sampel lendir hijau yang menempel."
        
        # Panggil Minigame C (Analisis Kimia)
        window hide
        call screen mg_analisis_kimia
        
        # --- CUT SCENE: Hasil Scanner Positif ---
        play sound "sfx_level_up.ogg"
        scene cg_mg01c_hasil_scanner with flashbang
        "BEEP! Analisis Selesai: 99.8%% Korosif Industri."
        
        # Kembali ke BG dan tampilkan Item Gembok, lalu ke dialog karakter
        scene bg_luar_dapur with dissolve
        play sound "sfx_dapat_item.ogg"
        show item_broken_padlock at truecenter with dissolve_kilat
        pause 1.5
        hide item_broken_padlock with dissolve
        $ item_gembok_berlendir = True
        $ poin_investigasi += 1
        show raka_normal at center with dissolve_kilat
        r "Jelas banget ini bukan ulah hantu. Buto ijo mana yang bawa-bawa tang potong industri?"
        hide raka_normal
        
        show bimo_lega at center with dissolve_kilat
        b "Pengamatan yang tajam, Raka. Setidaknya kita punya bukti awal adanya campur tangan manusia."
        hide bimo_lega

    elif _return == "garis_polisi":
        $ ch1_jejak_gembok = False
        
        # --- CUT SCENE: Raka Mendobrak Pintu ---
        play sound "sfx_fast_swoosh.ogg"
        scene cg_mg01b_dobrak_masuk with hpunch
        r "Ah udahlah, buang waktu mikirin gembok. Mending kita langsung dobrak aja pintu utamanya!"
        
        scene bg_luar_dapur with dissolve
        show citra_panik at center with mata_mengerjap
        c "K-kak Raka, jangan buru-buru dong! Gimana kalau ada jebakan di dalam?"
        hide citra_panik

    play sound "sfx_footsteps_approach.ogg"
    "Raka menyibak garis polisi kuning tersebut."
    scene cg_ch01_pagar_gaib with dissolve_lambat
    pause 2.0
    play sound "sfx_mantra_whisper.ogg"
    "Bimo memejamkan mata sejenak, komat-kamit membaca doa perlindungan, sementara Citra berpegangan erat pada ujung jaket Bimo sambil gemetar."
    scene cg_ch01_masuk_gerbang
    "Mereka bertiga melangkah masuk ke dalam pekarangan Dapur MBG yang gelap."

    # Penutup Chapter & Kesimpulan Dinamis
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with pingsan
    centered "{size=+15}END OF CHAPTER 01{/size}" with dissolve_lambat
    pause 1.5

    # Teks Teaser/Kesimpulan berdasarkan pilihan pemain
    if ch1_jejak_gembok:
        "KESIMPULAN CHAPTER:\nRaka berhasil menemukan jejak sabotase bahan kimia pada gembok gerbang. Bukti fisik ini memperkuat dugaan adanya konspirasi manusia di balik teror klenik. Namun, apakah penemuan kecil ini cukup untuk menyelamatkan nyawa mereka dari kengerian sejati yang menunggu di dalam Dapur Maut?"
    else:
        "KESIMPULAN CHAPTER:\nSikap skeptis Raka membuat Trio Investigator melangkah masuk dengan ceroboh, mengabaikan jejak penting pada gembok gerbang. Mereka kini masuk ke sarang pembunuh tanpa petunjuk awal. Apakah kecerobohan ini akan menjadi awal dari bencana maut yang mengancam nyawa mereka di dalam kegelapan?"
    
    pause 3.0

    # Lanjut ke Chapter berikutnya

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_01 SELESAI")
    # -----------------------------------
    jump chapter_02