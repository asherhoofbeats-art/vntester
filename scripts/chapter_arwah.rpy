# ==========================================
# FILE: chapter_arwah.rpy
# TEMA: Peringatan dari Ambang Kematian (Escape Route)
# ==========================================

# ------------------------------------------
# DEFINISI ASET CHAPTER ARWAH
# ------------------------------------------
define arya = Character("Arya", color="#ff5555")
image arwah_normal = "images/chars/arwah_normal.webp"
image arya_normal = "images/chars/arya_normal.webp"
image citra_kerasukan = "images/chars/citra_kesurupan.webp"
image bg_gang_sempit = "images/cg/bg_gang_sempit.webp"
image bg_area_pertemuan_arya = "images/cg/bg_area_pertemuan_arya.webp"

# CG & Background
image cg_arwah_arya_menengok = "images/cg/cg_arwah_arya_menengok.webp"
image cg_arwah_raka_gila = "images/cg/cg_arwah_raka_gila.webp"
image cg_arwah_hantu_kaget = "images/cg/cg_arwah_hantu_kaget.webp"
image cg_arwah_bimo_berhasil = "images/cg/cg_arwah_bimo_berhasil.webp"
image cg_arwah_akhir_chapter = "images/cg/cg_arwah_akhir_chapter.webp"

# ------------------------------------------
# MAIN STORY CHAPTER ARWAH
# ------------------------------------------
label chapter_arwah:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Inisialisasi variabel lokal chapter
    $ arwah_ritual_success = False

    scene black with bangun_tidur
    play music "bgm_06_panggilan_arwah.ogg" fadein 2.0
    centered "{size=+20}CHAPTER ARWAH{/size}\n\nPeringatan dari Ambang Kematian" with dissolve_lambat
    pause 2.0

    # 1. SCENE PELARIAN DARI PUSKESMAS
    play sound "sfx_footsteps_fast.ogg"
    scene bg_gang_sempit with dorong_atas
    
    show raka_panik at center with dissolve_kilat
    r "Hah... hah... gila! Cepat masuk ke gang ini! Jangan sampai senter warga nyorot kita!"
    hide raka_panik
    
    play music "bgm_tense_chase.ogg" fadein 1.0
    show bimo_lelah at center with dissolve_kilat
    b "Sialan, skenario Pak Tirto terlalu rapi. Kita benar-benar dijebak sebagai pembunuh Dokter Rina. Seluruh aparat desa pasti sedang memburu kita sekarang."
    hide bimo_lelah
    
    "Trio Investigator bersembunyi di sudut gang sempit yang lembap dan gelap, mencoba menetralkan napas mereka yang terengah-engah setelah berlari kencang dari Puskesmas."
    "Namun, di saat mereka mengira sudah aman..."

    # 2. CITRA KESURUPAN
    show citra_lelah at center with dissolve_kilat
    c "Kak... badanku kok... d-dingin sekali ya... leherku..."
    hide citra_lelah
    
    stop music fadeout 0.5
    play sound "sfx_glitch_kesurupan.ogg"
    show citra_kerasukan at center with flashmerah
    with hpunch
    c "{b}K..AA...DEEEE...SSSS{/b}"
    
    play music "bgm_04_teror_tak_kasatmata.ogg" fadein 1.0
    show bimo_panik at center with dorong_kiri
    b "Citra! Bertahanlah! Sepertinya Arwah korban dapur MBG menempel padanya! Mereka mencoba memberikan petunjuk terakhir, tapi aura kemarahan ini terlalu merusak tubuhnya!"
    hide bimo_panik
    
    # 3. KEDATANGAN POLISI ARYA
    play sound "sfx_footsteps_approach.ogg"
    scene cg_arwah_arya_menengok with flashbang
    
    arya "HEI! Siapa di sana?! Kalian buronan dari puskesmas tadi ya?! Berhenti di tempat!"
    
    "Raka tersentak. Senter Polisi Arya mulai menyorot ke arah ujung gang. Dalam sepersekian detik, Raka harus mengambil keputusan gila agar Bimo punya waktu mengurus Citra."
    
    # 4. AKSI KONYOL RAKA
    scene cg_arwah_raka_gila with hpunch
    play sound "sfx_menabrak_kocak.ogg"
    r "EH, BAPAK POLISI! Siap Ndan! Anu... kami bukan buronan, Pak! Kami mahasiswa KKN yang lagi latihan tari tradisional buat acara desa besok pagi!"
    r "Ini lihat, teman saya lagi kesurupan mendalami peran jadi... jadi Siluman Bambu Hitam!"
    
    arya "Tari bambu? Jam segini di gang gelap?! Jangan main-main kalian!"
    r "Beneran Pak! Nih, liat gayanya! Asik-asik joss!"
    
    "Raka mendadak melompat ke tengah cahaya senter dan mulai menari dengan gerakan patah-patah yang luar biasa konyol sambil sesekali berteriak 'Hup! Ha!'."
    
    play sound "sfx_hah_bingung_apa.ogg"
    arya "Hah? Apa-apaan ini... Kalian mabuk ya?"
    "Arya mengernyitkan dahi, senternya kini sepenuhnya fokus pada tingkah Raka yang sangat aneh dan tidak masuk akal."
    
    # 5. RITUAL PENGUSIRAN (MINIGAME)
    scene bg_gang_sempit with dissolve
    show bimo_fokus at center with dissolve_kilat
    b "(Bagus, Raka berhasil mengalihkan perhatiannya. Aku harus menarik arwah ini keluar sekarang atau Citra tidak akan tertolong!)"
    hide bimo_fokus
    
    # Panggilan ke Minigame
    call play_mg_arwah_ritual
    $ arwah_ritual_success = _return
    
    # 6. HASIL RITUAL
    if arwah_ritual_success:
        $ citra_resonansi_gaib += 1
        scene cg_arwah_bimo_berhasil with flash_hijau
        play sound "sfx_wangsit_datang.ogg"
        "Bimo menempelkan jarinya ke dahi Citra. Segel biru bercahaya terang dan arwah itu berhasil ditenangkan dengan sempurna. Citra perlahan jatuh tersadar ke pelukan Bimo."
    else:
        scene cg_arwah_hantu_kaget with flashmerah
        play sound "sfx_gasp.ogg"
        $ citra_resonansi_gaib -= 2
        "Ritual terganggu! Polisi Arya membentak keras ke arah Raka, membuat konsentrasi Bimo pecah. Arwah itu terlempar kasar keluar dari tubuh Citra."

    play sound "sfx_wuzz_menghilang.ogg"
    scene cg_arwah_akhir_chapter with dissolve_lambat
    "Sebelum menghilang sepenuhnya, kabut tipis dari arwah itu melayang ke arah utara, berbisik berulang kali tentang 'Padepokan Ki Renggo' sebelum akhirnya memudar menjadi abu tertiup angin malam."
    
    show arya_normal at center with dissolve_kilat
    arya "Oke, lupakan tariannya, bikin pusing saja! Cepat bubar dan bawa teman kalian yang pingsan itu pulang. Ingat, warga sedang berjaga mencari pembunuh dokter!"
    hide arya_normal with wipe_kiri
    
    play music "bgm_03_bayang_petunjuk.ogg" fadein 2.0
    show raka_lelah at center with dissolve_kilat
    r "Hah... gila. Hampir aja gue digiring ke polsek gara-gara joget nggak jelas."
    hide raka_lelah
    
    show bimo_lega at center with dissolve_kilat
    b "Pengorbanan harga dirimu tidak sia-sia, Raka. Para arwah tidak bisa berbohong di ambang batasnya. Pak Kades-lah dalang semua ini"
    b "Sekarang kita harus mencari bukti di tempat pak Kades"
    hide bimo_lega
    
    # 7. PENUTUP CHAPTER
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with pingsan
    centered "{size=+15}END OF CHAPTER ARWAH{/size}" with dissolve_lambat
    pause 1.5

    if arwah_ritual_success:
        "KESIMPULAN CHAPTER:\nLolos dari maut dan fitnah! Lewat aksi pengalihan konyol Raka dan ritual sempurna Bimo, kalian berhasil lolos dari interogasi Polisi Arya. Citra mendapatkan peningkatkan resonansi gaib, dan kini target kalian selanjutnya sangat jelas: Mencari Bukti Kekejaman Pak Kades!"
    else:
        "KESIMPULAN CHAPTER:\nKalian berhasil lolos dari kejaran warga dan Polisi Arya, meski ritual Bimo berakhir kurang sempurna. Meskipun fisik Citra kelelahan dan tidak ada bonus resonansi, pesan terakhir dari para arwah tetap tersampaikan: Pak Kades adalah Dalang Semuanya"

    pause 3.0
    
    # Melanjutkan ke chapter selanjutnya berdasarkan alur (Misal: Ke sarang dukun)

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_ARWAH SELESAI")
    # -----------------------------------
    jump chapter_06