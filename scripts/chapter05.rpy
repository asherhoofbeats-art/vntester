# ==========================================
# FILE: chapter05.rpy
# TEMA: Trance di Ruang Autopsi & Konspirasi
# ==========================================

# ------------------------------------------
# DEFINISI KARAKTER & GAMBAR TAMBAHAN
# ------------------------------------------
define darmi = Character("Mbok Darmi", color="#d3b88b")
image darmi_normal = "images/chars/darmi_normal.webp"
image darmi_panik = "images/chars/darmi_panik.webp"
image cg_chap05_citra_jatuh = "images/cg/cg_chap05_citra_jatuh.webp"
image cg_chap05_renggo_kabur = "images/cg/cg_chap05_renggo_kabur.webp"
image bg_parkiran_puskesmas = "images/bg/bg_parkiran_puskesmas.webp"
image cg_chap05_darmi_ditangkap = "images/cg/cg_chap05_darmi_ditangkap.webp"
image cg_chap05_bimo_lempar_bom_asap = "images/cg/cg_chap05_bimo_lempar_bom_asap.webp"
image cg_chap05_trio_dikepung_warga = "images/cg/cg_chap05_trio_dikepung_warga.webp"
image cg_chap05_trio_kabur_asap = "images/cg/cg_chap05_trio_kabur_asap.webp"
image cg_chap05_rina_peluk_raka = "images/cg/cg_chap05_rina_peluk_raka.webp"

label chapter_05:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Inisialisasi variabel untuk chapter ini
    $ ch5_dapat_speaker = False
    $ ch5_rina_hidup = False

    # Tampilan Judul Chapter di awal
    scene black with bangun_tidur
    play music "bgm_04_teror_tak_kasatmata.ogg" fadein 2.0 
    centered "{size=+20}CHAPTER 05{/size}\n\nTrance di Ruang Autopsi" with dissolve_lambat
    pause 2.0
    
# ==========================================
    # SCENE 1: JALANAN BERKABUT (MINIGAME 05A & 05B)
    # ==========================================
    "Trio Investigator melaju membelah malam menuju Puskesmas Desa. Ki Renggo yang sudah diikat duduk di jok belakang, dijaga ketat oleh Citra dan Bimo."
    "Namun, saat melewati jalanan sepi di pinggir hutan, kabut tebal tiba-tiba turun menutupi pandangan."

    # Panggil Minigame Mengemudi 05A
    call play_mg_chap05a
    
    if _return == "win":
        show citra_panik at center with dissolve_kilat
        c "Kak Raka! Astaga, wanita itu... dia pucet banget. Hawanya juga sedingin es."
        hide citra_panik
        
        # Panggil Minigame Arah Gaib 05B (Raka Solo)
        call play_mg_chap05b
        
        # Set variabel berdasarkan hasil dari dalam mg_chap05b.rpy
        if _return == "win":
            $ ch5_dapat_speaker = True
            $ poin_investigasi +=2
            $ citra_resonansi_gaib +=1
            $ item_speaker_hantu = True
        else:
            $ ch5_dapat_speaker = False
            $ poin_investigasi -=1
            

    else:
        # Jika kalah di Minigame 05A (Nabrak)
        show raka_marah at center with dissolve_kilat
        r "Sialan! Mobil gue nabrak pembatas jalan gara-gara kabut! Mesinnya langsung mati total!"
        hide raka_marah
        
        show bimo_lelah at center with dissolve_kilat
        b "Tidak ada waktu untuk mengeluh. Tadi aku melihat ada patroli anak buah Pak Kades di kejauhan. Biar aku panggil mereka untuk membantu memperbaiki mobil ini."
        hide bimo_lelah
        
        "Bimo keluar menembus kabut, sementara Raka dan Citra menunggu di mobil bersama Ki Renggo."

    # ==========================================
    # SCENE 2: MOBIL SUV - KI RENGGO KABUR 
    # ==========================================
    stop music fadeout 1.0
    scene bg_jalanan_malam with transisi_asap
    play music "bgm_creepy_ambient.ogg" fadein 1.0 loop
    
    "Kini mesin mobil SUV itu sudah kembali menyala normal berkat 'bantuan' anak buah Pak Kades."
    
    show raka_lega at center with dissolve_kilat
    r "Ya udahlah, yang penting mobil udah bener. Geser Bim, gue aja yang nyetir ke Puskesmas."
    hide raka_lega
    
    "Saat Raka hendak membuka pintu kemudi..."
    "Tiba-tiba terdengar suara debukan keras dari arah jok belakang!"
    
    play sound "sfx_pintu_mobil_dibanting.ogg"
    scene bg_jalanan_malam with hpunch
    
    show raka_panik at center with dissolve_kilat
    r "CITRA?! KAU KENAPA, CIT?!"
    hide raka_panik
    scene cg_chap05_renggo_kabur
    "Pintu belakang terbuka paksa. Citra terlempar setengah keluar dari pintu dalam keadaan setengah sadar. Tali ikatan Ki Renggo telah terpotong, dan dukun itu sudah lenyap menembus kegelapan hutan!"
    scene cg_chap05_citra_jatuh
    show citra_lelah at center with mata_mengerjap
    c "Aduh... Kak Raka... kepalaku dihantam... Si dukun palsu itu menyembunyikan pecahan kaca di bajunya, lalu memotong tali saat kita sedang ngobrol..."
    hide citra_lelah
    
    show bimo_marah at center with dissolve_kilat
    b "Sial! Kita kehilangan saksi kunci utama kita. Sepertinya perhatian kita teralihkan karena memperbaiki mobil tadi. Sekarang Ki Renggo jadi bisa kabur!"
    hide bimo_marah
    
    show raka_marah at center with dissolve_kilat
    r "Kurang ajar! Untung mesinnya udah nyala. Ayo cepat masuk mobil, kita langsung labrak Dokter Rina di Puskesmas sebelum konspirasi ini ditutup rapat!"
    hide raka_marah
    # ==========================================
    # SCENE 3: RUANG AUTOPSI (MINIGAME 05C & 05D)
    # ==========================================
    stop music fadeout 1.0
    play sound "sfx_heavy_door_open.ogg"
    scene bg_ruang_autopsi with dorong_atas
    
    "Raka dan Bimo menerobos masuk ke Ruang Autopsi. Udara di dalam sangat dingin dan berbau formalin pekat."
    
    # Panggil Minigame Interogasi 05C
    call play_mg_chap05c
    if _return == "win":
        $ ch5_punya_bukti_autopsi = True
        $ item_bukti_otopsi = True
        $ poin_investigasi +=2
    else:
        $ ch5_punya_bukti_autopsi = False
        $ poin_investigasi -=1
    
    # Panggil Minigame Keseimbangan Trance 05D
    call play_mg_chap05d

    # ==========================================
    # SCENE 4: MINUMAN BERACUN (MINIGAME 05E)
    # ==========================================
    stop music fadeout 1.0
    play music "bgm_11_senyum_koruptor.ogg" fadein 1.0
    scene bg_ruang_autopsi with dissolve
    
    "Suasana di ruang autopsi masih sangat tegang setelah arwah berhasil dikeluarkan dari tubuh Citra."
    
    play sound "sfx_creaky_door_open.ogg"
    "Tiba-tiba pintu ruangan terbuka perlahan."
    
    show darmi_normal at center with dissolve_kilat
    darmi "Permisi, Bu Dokter... Maaf mengganggu waktunya."
    hide darmi_normal
    
    show rina_lelah at center with dissolve_kilat
    dr "Hah... hah... M-Mbok Darmi? Ada apa?"
    hide rina_lelah
    
    show darmi_normal at center with dissolve_kilat
    darmi "Ini, Dok. Teh hijau hangat kesukaan Bu Dokter. Tadi Pak Kades Tirto mampir dan pesan supaya saya buatin teh ini untuk Dokter yang lagi lembur."
    darmi "Katanya biar Bu Dokter lebih tenang kerjanya."
    hide darmi_normal
    
    show rina_lelah at center with dissolve_kilat
    dr "O-oh... iya, taruh saja di meja. T-terima kasih, Mbok."
    hide rina_lelah
    
    "Mbok Darmi meletakkan segelas teh hijau itu di atas meja autopsi, lalu menunduk hormat dan berjalan keluar."
    
    # Panggil Minigame Meracik Penawar 05E
    call play_mg_chap05e
    
    # ==========================================
    # KESIMPULAN & PERCABANGAN ENDING CHAPTER 05
    # ==========================================
    if _return == "win":
        # RINA SELAMAT -> LANJUT CHAPTER SARAH
        $ ch5_rina_hidup = True
        $ dr_rina_selamat = True
        $ poin_investigasi += 1
        scene cg_chap05_rina_peluk_raka with hpunch
        dr "Oh Pahlawanku.. Kamu telah menyelamatkan nyawaku.."
        r "Hey tenang dulu Bu Dokter... Emm.. Rina.. ini bukan saatnya"
        scene bg_ruang_autopsi with transisi_asap
        "Setelah keadaan Dokter Rina stabil, Raka menyeret Mbok Darmi yang ketakutan kembali ke dalam ruangan."
        
        show darmi_panik at center with tv_rusak
        darmi "Ampun, Den Raka! Ampun Bu Dokter! Saya berani sumpah, saya tidak tahu kalau itu racun!"
        darmi "Pak Kades Tirto yang ngasih saya bungkusan serbuk putih itu. Katanya itu cuma vitamin biar Bu Dokter Rina nggak gampang stres! Saya cuma disuruh nyampurin ke tehnya!"
        hide darmi_panik
        
        show bimo_marah at center with dissolve_kilat
        b "Licik sekali... Pak Kades memanfaatkan kepolosan Mbok Darmi. Dan anak buah Pak Kades yang pura-pura memperbaiki mobil kita di jalan tadi..."
        b "Mereka sengaja menahan kita agar kita terlambat tiba di puskesmas, memastikan racunnya bekerja sebelum kita sempat menginterogasi Dokter Rina!"
        hide bimo_marah
        
        show raka_lega at center with dissolve_kilat
        r "Tapi rencana mereka gagal. Kita punya Dokter Rina sebagai saksi hidup, kita punya bukti rekaman suara, dan kita tahu 100 persen kalau Pak Tirto adalah dalang di balik kejadian ini."
        hide raka_lega
        
        stop music fadeout 2.0
        stop sound fadeout 2.0
        scene black with pingsan
        centered "{size=+15}END OF CHAPTER 05{/size}" with dissolve_lambat
        pause 1.5
        
        "KESIMPULAN CHAPTER:\nMalam yang penuh manipulasi berhasil digagalkan! Meski Ki Renggo melarikan diri, Trio Investigator berhasil menyelamatkan nyawa dr. Rina dari percobaan pembunuhan yang direncanakan oleh Pak Kades Tirto."
        "Plot licik sang Kades yang pura-pura mengundang Trio untuk dijadikan kambing hitam kini terbongkar. Berbekal kesaksian Mbok Darmi dan dr. Rina, mereka kini bersiap menghadapi ancaman selanjutnya."
        "Merasa Belum cukup bukti. Trio detektif menghubungi Sarah untuk minta bantuan"
        pause 3.0
        
        jump chapter_sarah

    else:
        # RINA TEWAS -> GAME OVER -> CHAPTER ARWAH
        $ ch5_rina_hidup = False
        $ poin_investigasi -=2
        scene cg_mg05c_raka_diusir with vpunch
        play sound "sfx_door_banging_massive.ogg"
        
        "Mendengar suara pecahan kaca dan keributan dari dalam, beberapa warga desa dan sekuriti yang sudah dihasut oleh anak buah Pak Kades mendobrak masuk!"
        
        "Sekuriti" "Astaga! Dokter Rina! Apa yang kalian lakukan padanya?!"
        scene cg_chap05_trio_dikepung_warga with flashmerah
        "Warga" "Ini mereka orang kotanya! Pak Kades benar, Orany-orang ini datang untuk membunuh Dokter puskesmas! Tangkap mereka!"
        
        
        show raka_panik at left with dissolve_kilat
        r "Wah Kacau.. Kita harus segera kabur kalau tidak ingin dihakimi masa"
        hide raka_panik
        
        show bimo_fokus at right with dissolve_kilat
        b "serahkan padaku, aku membawa bom asap yang pernah kau rakit dulu."
        hide bimo_marah
        
        scene cg_chap05_bimo_lempar_bom_asap with vpunch
        b "Mohon maaf para warga, kalian kelak akan mengetahui Kebenaran di Waktu yang tepat!!"

        scene cg_chap05_trio_kabur_asap with transisi_asap
        "Boom, kepulan asap menyeruak di tengah kepungan warga. Raka, Bimo dan Citra akhirnya berhasil kabur dari kepungan Warga yang marah"

        stop music fadeout 2.0
        stop sound fadeout 2.0
        scene black with pingsan
        centered "{size=+15}TRAGIC END OF CHAPTER 05{/size}" with dissolve_lambat
        pause 1.5
        
        "KESIMPULAN CHAPTER:\nJebakan sempurna Pak Kades Tirto berhasil. Menggunakan Mbok Darmi yang tak tahu apa-apa, ia membunuh dr. Rina dan menjebak Trio Investigator sebagai pelakunya."
        "Tanpa saksi, tanpa bukti, dan dikejar oleh seluruh warga desa yang marah, Trio Investigator kini menjadi buronan di desa yang seharusnya mereka selamatkan."
        pause 3.0
        
        jump chapter_arwah