# ==========================================
# FILE: chapter06.rpy
# TEMA: Penyusupan ke Balai Desa & Konfrontasi Gatot
# STYLE: 16-Bit Retro Horror
# ==========================================

# ------------------------------------------
# DEFINISI ASET CG & ITEM (CHAPTER 06)
# ------------------------------------------
# Intro & Jendela
image cg_mg06a_awal = "images/cg/cg_mg06a_awal.webp"
image bg_jendela_balai_16bit = "images/bg/bg_jendela_balai_16bit.webp"
image cg_mg06a_menang = "images/cg/cg_mg06a_menang.webp"
image cg_mg06a_kalah = "images/cg/cg_mg06a_kalah.webp"

# Konfrontasi Gatot
image bg_lorong_gelap_16bit = "images/bg/bg_lorong_gelap_16bit.webp"
image cg_mg06b_awal_konfrontasi = "images/cg/cg_mg06b_awal_konfrontasi.webp"
image cg_mg06b_pertarungan = "images/cg/cg_mg06b_pertarungan.webp"
image cg_mg06b_gatot_sadar = "images/cg/cg_mg06b_gatot_sadar.webp"
image cg_mg06b_terpukul = "images/cg/cg_mg06b_terpukul.webp"
image cg_mg06b_gatot_kalah = "images/cg/cg_mg06b_gatot_kalah.webp"

# Brankas & Klimaks
image cg_mg06c_brankas_rahasia = "images/cg/cg_mg06c_brankas_rahasia.webp"
image cg_mg06c_hacking = "images/cg/cg_mg06c_hacking.webp"
image cg_mg06c_sukses = "images/cg/cg_mg06c_sukses.webp"
image cg_mg06c_gagal = "images/cg/cg_mg06c_gagal.webp"
image cg_ch06_ancaman_tirto = "images/cg/cg_ch06_ancaman_tirto.webp"

# Item
image item_buku_kas_merah = "images/item/item_buku_kas_merah.webp"
image item_kaset_rekaman_gatot = "images/item/item_kaset_rekaman_gatot.webp"
default ch5_punya_bukti_autopsi = False

label chapter_06:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Inisialisasi variabel untuk chapter ini
    $ ch6_buku_kas = False
    $ ch6_kepercayaan_gatot = False
    $ has_kaset_gatot = False

    # Tampilan Judul Chapter di awal
    scene black with bangun_tidur
    play music "bgm_03_bayang_petunjuk.ogg" fadein 2.0
    centered "{size=+20}CHAPTER 06{/size}\n\nPenyusupan dan Kesalahpahaman" with dissolve_lambat
    pause 2.0
    
    # ------------------------------------------
    # SCENE 1: LUAR BALAI DESA (MINIGAME A)
    # ------------------------------------------
    scene cg_mg06a_awal with dorong_atas
    show kabut_tipis
    show daun_gugur
    play sound "sfx_angin_malam_kencang.ogg" loop fadein 1.0
    
    "Malam semakin larut. Balai Desa berdiri megah namun memancarkan aura kelam dari luar. Ini adalah pusat kekuasaan Pak Tirto, dalang di balik proyek berdarah ini."

    show raka_berpikir at left with dissolve_kilat
    r "Balai desa ini dijaga ketat. Ada dua satpam patroli di depan dan kamera CCTV di sudut jalan."
    hide raka_berpikir

    show citra_lelah at center with mata_mengerjap
    c "Kepalaku masih berdenyut, tapi kita harus cari ruang kerja Pak Tirto. Pasti ada bukti aliran dana korupsi dan pembayaran ke dr. Rina di sana."
    hide citra_lelah

    show bimo_normal at right with dissolve_kilat
    b "Ada satu celah di jendela belakang ruang arsip, tapi kuncinya berkarat dan macet. Kita harus membukanya tanpa suara."
    hide bimo_normal

    scene bg_jendela_balai_16bit with transisi_asap
    "Raka mengeluarkan peralatan kecil dari sakunya, bersiap membobol jendela."
    
    stop music fadeout 1.0
    "Raka mengambil napas panjang, memasukkan ujung kawat ke dalam lubang kunci jendela..."
    
    # PANGGIL MINIGAME A (STEALTH)
    call screen mg_lockpicking
    
    if _return == False:
        # KALAH MINIGAME A -> GAME OVER
        
        play sound "sfx_treng_besi.ogg"
        scene bg_jendela_balai_16bit with hpunch
        r "Sial! Kawatnya nyangkut dan suaranya nyaring banget!"
        
        play sound "sfx_door_slammed.ogg"
        "Suara benturan logam itu bergema di keheningan malam."
        
        scene cg_mg06a_kalah with flashbang
        play sound "sfx_teriakan_takut.ogg" 
        "Cahaya senter yang menyilaukan tiba-tiba menyorot wajah mereka. Satpam memergoki mereka!"
        
        scene black with pingsan
        play sound "sfx_game_over.ogg"
        centered "{size=+20}GAME OVER{/size}\n\nKebisingan memancing perhatian penjaga."
        return

    # MENANG MINIGAME A
    play sound "sfx_creaky_door_open.ogg"
    $ poin_investigasi += 1
    scene cg_mg06a_menang with flash_hijau
    play music "bgm_tense_chase.ogg" fadein 1.0
    "Klak! Suara pelan terdengar, dan pengait jendela berhasil terlepas. Jendela berhasil terbuka."


    # ------------------------------------------
    # SCENE 2: RUANG ARSIP & GATOT (MINIGAME B)
    # ------------------------------------------
    scene bg_lorong_gelap_16bit with dorong_atas
    "Mereka menyelinap masuk ke dalam keheningan balai desa yang mencekam."
    
    play sound "sfx_footsteps_approach.ogg"
    "Tiba-tiba, terdengar langkah kaki berat mendekat dari ujung lorong."

    show raka_panik at center with hpunch
    r "Ssst! Sembunyi!"
    hide raka_panik

    stop music fadeout 0.5
    play sound "sfx_metal_clash.ogg"
    "Sebuah linggis besar tiba-tiba menghantam dinding. Seseorang melompat dari kegelapan!"
    play sound "sfx_pecah.ogg"
    scene cg_mg06b_awal_konfrontasi with flashmerah
    play music "bgm_05_otot_kawat.ogg" fadein 1.0
    
    g "BANGSAT! Jadi kalian anjing suruhan Pak Tirto yang mau ngilangin bukti?!"
    show raka_panik at left
    r "Gatot?! Tahan, woi! Kita bukan anak buahnya Tirto!"
    g "Alah, bacot! Lu kira gue bakal ampunin lu? Rasain ini!"
    hide raka_panik
    play sound "sfx_fast_swish.ogg"
    scene cg_chap06b_gatot_siap_serang with vpunch
    "Gatot mengeluarkan lima buah kapak lempar dari sabuknya dan melemparkannya secara membabi buta ke arah Raka!"

    r "Sialan! Gue harus tendang semua kapaknya sebelum kena!"

    # PANGGIL MINIGAME B (SHOOTER)
    # PANGGIL MINIGAME B (SHOOTER)
    call screen mg_shoot_gatot
    
    if _return == False:
        # KALAH MINIGAME B -> GAME OVER
        scene cg_mg06b_terpukul with hpunch
        play sound "sfx_flesh_tear_heavy.ogg"
        "Raka gagal menangkis semua target. Salah satu Tomahawk menghantam keras tubuhnya!"
        
        scene black with pingsan
        play sound "sfx_game_over_hancur_8bit.ogg"
        centered "{size=+20}GAME OVER{/size}\n\nGagal menangkis serangan Gatot berakibat fatal. Trio Detektif dihabisi Gatot malam itu."
        return

    # BERHASIL MENEMBAK SEMUA TOMAHAWK
    play sound "sfx_metal_clang.ogg"
    scene bg_lorong_gelap_16bit with flash_hijau
    
    "BAK! BUK! Tendangan terakhir Raka tepat menghantam kapak kelima Gatot, mementalkannya ke dinding hingga jatuh berdentang."
    scene cg_mg06b_gatot_kalah
    "Gatot terkejut melihat serangan pamungkasnya dipatahkan begitu saja. Celah itu tidak disia-siakan oleh Raka."
    
    # Raka menyerang balik
    play sound "sfx_punch.ogg"
    scene cg_chap06b_raka_pukul_gatot with hpunch
    play sound "sfx_strong_punch.ogg"
    r "Ini buat serangan lu di gudang beras waktu itu, bangsat!!"
    
    play sound "sfx_strong_kick.ogg"
    scene cg_chap06b_raka_tendang_gatot with vpunch
    r "Dan ini... buat kapak-kapak gila lu barusan!"
    
    play sound "sfx_barang_berat_jatuh.ogg"
    scene cg_chap06b_gatot_terjerembab with hpunch
    "Kombinasi pukulan telak dan tendangan keras Raka menghantam Gatot. Pria berotot itu terhuyung dan jatuh terjerembab ke lantai kayu."
    show raka_marah at left
    r "Udah puas lu?! Sekarang buka mata lu dan dengerin gue!"
    
    # --- PERCABANGAN BUKTI BERDASARKAN HASIL CHAPTER 5 ---
    
    # ==========================================
    # EVALUASI KEPERCAYAAN GATOT (BUKTI OTOPSI & KALUNG)
    # ==========================================
    
    if ch5_punya_bukti_autopsi == True and item_kalung_galih == True:
        # KONDISI 1: PUNYA KEDUANYA (Gatot Trust = True)
        play music "bgm_09_air_mata_tumbal.ogg"
        "Raka melempar sebuah dokumen Rekam Medis sekaligus menyodorkan sebuah kalung usang ke arah Gatot yang masih tersungkur."
        show raka_marah at center
        r "Adek lu bukan mati dimakan Buto Ijo! Mereka sengaja diracun buat nutupin korupsi bahan makanan Pak Kades!"
        r "Dan kami nemuin Kalung Galih ini tersembunyi di dapur... bukti kalau dia memergoki kelicikan mereka!"
        hide raka_marah
        "Napas Gatot memburu sambil menahan sakit. Tangannya yang gemetar meraih Laporan Autopsi Asli dan kalung milik adiknya."
        
        stop music fadeout 2.0
        
        scene cg_mg06b_gatot_sadar with dissolve_lambat
        
        g "Kalung ini... beneran punya Galih..."
        g "...Jadi adik gue dibunuh pake dalih pesugihan cuma buat nutupin borok mereka? Bajingan..."
        g "Maafin gue udah nuduh kalian. Gue bakal bantu kalian hancurin Kades keparat itu!"
        $ item_rekaman_tirto = True
        $ gatot_trust = True
        "{color=#00ffcc}SISTEM: Bukti hukum dan ikatan emosional sempurna! (GATOT TRUST: TRUE){/color}"

    elif ch5_punya_bukti_autopsi == True and item_kalung_galih == False:
        # KONDISI 2: HANYA PUNYA OTOPSI
        play music "bgm_09_air_mata_tumbal.ogg"
        "Raka melempar sebuah dokumen Rekam Medis ke arah Gatot yang masih tersungkur."
        show raka_marah at center
        r "Adek lu bukan mati dimakan Buto Ijo! Mereka sengaja diracun buat nutupin korupsi bahan makanan Pak Kades!"
        
        "Napas Gatot memburu sambil menahan sakit, matanya menatap tajam ke arah bukti Laporan Autopsi Asli di dekat tangannya."
        hide raka_marah
        stop music fadeout 2.0
        
        scene cg_mg06b_gatot_sadar with dissolve_lambat
        
        g "...Jadi Galih.. Adik gue... dibunuh pake dalih pesugihan cuma buat nutupin borok mereka?"
        g "T-tapi... kertas begini bisa aja kalian rekayasa! Gue butuh bukti kuat dari TKP dapur tempat adik gue mati. Gue masih ragu sama kalian!"
        
        $ gatot_trust = False
        "{color=#ff5555}SISTEM: Bukti hukum ada, namun ikatan emosional kurang. (GATOT TRUST: FALSE){/color}"

    elif ch5_punya_bukti_autopsi == False and item_kalung_galih == True:
        # KONDISI 3: HANYA PUNYA KALUNG
        play music "bgm_09_air_mata_tumbal.ogg"
        "Raka menyodorkan ponselnya yang memutar rekaman CCTV dari Puskesmas dan menyerahkan sebuah kalung usang ke depan wajah Gatot."
        show raka_marah at center
        r "Liat rekaman CCTV ini! Mbok Darmi nyampur racun ke minuman dokter Puskesmas lu atas suruhan Tirto!"
        r "Dan Kalung Galih ini... kami temuin di dapur tempat dia mati!"
        hide raka_marah
        "Napas Gatot memburu sambil menahan sakit. Ia merampas kalung adiknya sambil menatap nanar layar ponsel Raka."
        
        stop music fadeout 2.0
        
        scene cg_mg06b_gatot_sadar with dissolve_lambat
        
        g "Ini kalung Galih... T-tapi video buram ini nggak langsung ngebuktiin kalau racun itu yang bunuh adik gue!"
        g "Tanpa surat otopsi medis yang sah, gue nggak bisa bawa ini ke polisi atau percaya sepenuhnya sama kalian!"
        
        $ gatot_trust = False
        "{color=#ff5555}SISTEM: Ikatan emosional ada, namun bukti hukum lemah. (GATOT TRUST: FALSE){/color}"

    else:
        # KONDISI 4: TIDAK PUNYA KEDUANYA
        play music "bgm_09_air_mata_tumbal.ogg"
        "Raka menyodorkan ponselnya yang memutar sebuah rekaman CCTV dari Puskesmas ke depan wajah Gatot yang tersungkur."
        show raka_marah at center
        r "Liat rekaman CCTV ini! Mbok Darmi nyampur racun ke minuman dokter Puskesmas lu atas suruhan Tirto! Kita nyelinap ke sini justru buat cari bukti kejahatan Kades keparat itu!"
        
        "Napas Gatot memburu sambil menahan sakit, matanya menatap nanar ke arah layar ponsel di tangan Raka."
        
        stop music fadeout 2.0
        
        scene cg_mg06b_gatot_sadar with dissolve_lambat
        
        g "...Jadi Galih.. Adik gue... diracun sama orang suruhan Tirto dan ditutupin pake dalih pesugihan?"
        g "Omong kosong! Ini cuma video rekaman buram! Kalian nggak bawa bukti otopsinya atau bahkan barang peninggalan adik gue! Kalian pasti cuma mau nipu gue!"
        
        $ gatot_trust = False
        "{color=#ff5555}SISTEM: Bukti terlalu lemah. Gatot meragukan Anda. (GATOT TRUST: FALSE){/color}"

    # --- KEMBALI KE ALUR UTAMA ---

    c "Iya, Mas Gatot. Ki Renggo dibayar buat bikin TKP palsu agar warga takut."
    
    play music "bgm_10_fokus_spiritual.ogg" fadein 1.0
    g "Gue minta maaf... Gue sempet nguping pembicaraan Tirto sama Ki Renggo minggu lalu. Gue rekam pake kaset ini."

    play sound "sfx_suara_ting.ogg"
    show item_kaset_rekaman_gatot at truecenter with dissolve_kilat
    "Mendapatkan [[Rekaman Suara Rahasia Gatot]]!"
    play sound "sfx_dapat_item.ogg"
    $ has_kaset_gatot = True
    $ point_investigasi += 1
    hide item_kaset_rekaman_gatot with dissolve_kilat
    
    g "Kalau tujuan kita sama, ayo bangunin gue. Kita ke lantai dua."
    $ ch6_kepercayaan_gatot = True


    # ------------------------------------------
    # SCENE 3: RUANG KERJA TIRTO (MINIGAME C)
    # ------------------------------------------
    stop music
    play music "bgm_03_bayang_petunjuk"
    scene bg_ruang_tirto with transisi_asap
    "Berkat bantuan Gatot, mereka tiba di kantor Pak Tirto tanpa memicu alarm. Ruangan itu sangat luas, dipenuhi ornamen mewah."

    show gatot_normal at left with dissolve_kilat
    g "Tirto pasti nyimpen 'Buku Kas Merah'. Buku itu catetan asli aliran dana suap ke dr. Rina dan Ki Renggo. Gue yakin disimpen di sini."
    
    show raka_berpikir at right with dissolve_kilat
    r "Kita mencar. Citra, Bimo, cek meja dan laci. Gatot, bantu gue cek dinding, barangkali ada brankas rahasia."
    hide gatot_normal
    hide raka_berpikir

    play sound "sfx_footsteps_fast.ogg"
    "Mereka mulai menggeledah ruangan dengan cepat dan hati-hati."

    menu:
        "Cari di balik lukisan besar di dinding":
            play sound "sfx_ding_idea.ogg"
            scene cg_mg06c_brankas_rahasia with transisi_senter
            r "Gotcha! Ada brankas tersembunyi di balik lukisan pemandangan ini."
            
            g "Tapi pake kunci kombinasi digital. Lu bisa bobol?"
            
            stop music fadeout 1.0
            "Raka menyambungkan perangkat kecilnya ke panel brankas. Waktu terus berjalan..."
            play music "bgm_tense_chase.ogg" fadein 0.5
            
            # PANGGIL MINIGAME C (HACKING)
            call screen mg_hack_brankas
            
            if _return == False:
                # KALAH MINIGAME C -> GAME OVER MUTLAK
                stop music
                play sound "sfx_error_win.ogg"
                scene cg_mg06c_gagal with flashmerah
                r "Sial! Sistem pertahanannya kekunci permanen!"
                
                play sound "sfx_buzz_listrik.ogg"
                "Lampu indikator merah menyala terang. Alarm ruangan berbunyi memekakkan telinga."
                
                play sound "sfx_door_kick.ogg"
                "Pintu utama didobrak. Pasukan anak buah Pak Tirto memergoki Raka yang sedang meretas brankas!"
                
                scene black with pingsan
                play sound "sfx_game_over_hancur_8bit.ogg"
                centered "{size=+20}GAME OVER{/size}\n\nGagal meretas brankas dan memicu alarm keamanan."
                return

            # MENANG MINIGAME C
            play sound "sfx_correct.ogg"
            stop music fadeout 1.0
            
            play sound "sfx_buka_tong.ogg"
            scene cg_mg06c_sukses with flash_hijau
            play music "bgm_08_fajar_keadilan.ogg" fadein 1.0
            
            r "Terbuka! Ini dia, Buku Kas Merah. Isinya lengkap, dari 'uang pelicin' sampai biaya pembersihan mayat."
            g "Syukurlah... Akhirnya kebrengsekan Tirto ada buktinya."

            play sound "sfx_dapat_item.ogg"
            show item_buku_kas_merah at truecenter with dissolve_kilat
            "Mendapatkan [[Buku Kas Merah]]!"
            $ ch6_buku_kas = True
            $ point_investigasi += 1
            $ item_buku_kas_merah = True
            hide item_buku_kas_merah with dissolve_kilat

        "Cari di tumpukan dokumen di atas meja":
            $ ch6_buku_kas = False
            play sound "sfx_taruh_sesuatu.ogg"
            show citra_lelah at right with dissolve_kilat
            c "Semua di sini cuma laporan fiktif. Nggak ada tanda tangan asli atau rincian tumbal."
            
            show raka_marah at left with dissolve_kilat
            r "Sial, mungkin dia udah pindahin buku aslinya atau kita butuh lebih banyak waktu!"
            hide citra_lelah
            hide raka_marah

    # ------------------------------------------
    # KLIMAKS KEMUNCULAN TIRTO
    # ------------------------------------------
    scene bg_ruang_tirto with dissolve_kilat
    stop music
    play sound "sfx_door_slammed.ogg"
    scene cg_ch06_ancaman_tirto with flashbang
    play music "bgm_11_senyum_koruptor.ogg" fadein 1.0

    "Pintu utama didobrak. Pak Tirto berdiri di ambang pintu, tersenyum sinis sambil mengisap cerutunya. Di belakangnya, Tiga pria bersenjata tajam telah memblokir jalan keluar."

   
    t "Tamu tak diundang... dan ada Gatot sang pengkhianat. Kalian pikir bisa masuk ke kerajaanku dan keluar hidup-hidup?"
    hide tirto_normal

    show gatot_marah at left with hpunch
    g "TIRTO!! Lu bayar dr. Rina buat ngeracun temen-temen gue! Hari ini lu bakal bayar semuanya!"
    hide gatot_marah
    
    show raka_marah at right with dissolve_kilat
    r "Permainan lu berakhir, Tirto!"
    hide raka_marah
    
    show tirto_marah at center with dissolve_kilat
    t "Berakhir? Hahaha! Di desa ini, AKU adalah hukum. Ki Renggo sedang butuh persembahan malam ini, dan kalian datang sendiri mengantarkan nyawa. Habisi mereka!"
    hide tirto_marah

    play sound "sfx_serangan_cepat.ogg"
    "Anak buah Pak Tirto merangsek maju. Ruang kerja yang sempit kini berubah menjadi arena pertaruhan nyawa."

    # Penutup Chapter & Kesimpulan Dinamis
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with pingsan
    centered "{size=+15}END OF CHAPTER 06{/size}" with dissolve_lambat
    pause 1.5

    if ch6_buku_kas:
        "KESIMPULAN CHAPTER:\nTrio Investigator dan Gatot berhasil mengamankan Buku Kas Merah tepat sebelum konfrontasi terjadi. Bukti pamungkas korupsi dan racun itu telah berada di tangan. Jika mereka bisa selamat dari malam ini, kejatuhan Pak Tirto sudah di depan mata."
    else:
        "KESIMPULAN CHAPTER:\nPenyusupan yang berujung buntu. Tanpa Bukti Valid, posisi Trio Investigator dan Gatot sangat terjepit. Pak Tirto kini sepenuhnya mengurung mereka di markasnya. Mereka harus bertarung mati-matian melawan pasukan Tirto tanpa memegang bukti yang cukup."

    pause 3.0

    # Lanjut ke Chapter berikutnya

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_06 SELESAI")
    # -----------------------------------
    jump chapter_07