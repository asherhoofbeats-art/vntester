# ==========================================
# FILE: mg_chap06b.rpy
# MINIGAME: Tembak Jatuh Tomahawk Gatot
# STYLE: 16-Bit Retro Arcade Shooter
# ==========================================

# ------------------------------------------
# ASET GAMBAR, BACKGROUND, CG & ITEM
# ------------------------------------------
# Background
image bg_lorong_gelap_16bit = "images/bg/bg_lorong_gelap_16bit.webp"

# CG Minigame (Sesuai 4 Kebutuhan)
image cg_mg06b_awal_konfrontasi = "images/cg/cg_mg06b_awal_konfrontasi.webp"  # Awal mula game
image cg_mg06b_pertarungan = "images/cg/cg_mg06b_pertarungan.webp"            # Latar belakang game
image cg_mg06b_gatot_sadar = "images/cg/cg_mg06b_gatot_sadar.webp"            # Jika menang
image cg_mg06b_terpukul = "images/cg/cg_mg06b_terpukul.webp"                  # Jika kalah
image cg_chap06b_raka_pukul_gatot = "images/cg/cg_chap06b_raka_pukul_gatot.webp"
image cg_chap06b_raka_tendang_gatot = "images/cg/cg_chap06b_raka_tendang_gatot.webp"
image cg_chap06b_gatot_terjerembab = "images/cg/cg_chap06b_gatot_terjerembab.webp"
image cg_chap06b_gatot_siap_serang = "images/cg/cg_chap06b_gatot_siap_serang.webp"
# Item
image it_projectile_tomahawk = "images/item/it_projectile_tomahawk.webp"
image item_kaset_rekaman_gatot = "images/item/item_kaset_rekaman_gatot.webp"

# Transformasi untuk efek kapak berputar cepat di udara
transform spin_tomahawk:
    rotate 0
    linear 0.3 rotate 360
    repeat

# ------------------------------------------
# SCREEN MINIGAME: TEMBAK PROJECTILE
# ------------------------------------------
screen mg_shoot_gatot():
    modal True
    
    # -- Variabel Waktu dan Skor --
    default time_left = 10.0
    default targets_hit = 0
    
    # -- Status Aktif 5 Tomahawk --
    default t1_active = True
    default t2_active = True
    default t3_active = True
    default t4_active = True
    default t5_active = True
    
    # -- Posisi X dan Y Acak (Asumsi resolusi standar 1920x1080) --
    default t1_x = renpy.random.randint(200, 1600)
    default t1_y = renpy.random.randint(150, 800)
    
    default t2_x = renpy.random.randint(200, 1600)
    default t2_y = renpy.random.randint(150, 800)
    
    default t3_x = renpy.random.randint(200, 1600)
    default t3_y = renpy.random.randint(150, 800)
    
    default t4_x = renpy.random.randint(200, 1600)
    default t4_y = renpy.random.randint(150, 800)
    
    default t5_x = renpy.random.randint(200, 1600)
    default t5_y = renpy.random.randint(150, 800)

    # Background layar pertempuran
    add "cg_mg06b_pertarungan"
    add "#ff000022" # Efek merah transparan agar lebih tegang

    # -- Timer Hitung Mundur --
    timer 0.1 repeat True action [
        SetScreenVariable("time_left", time_left - 0.1),
        If(time_left <= 0.0, Return(False))
    ]

    # -- Timer Gerak Acak Cepat (Tomahawk berpindah setiap 0.7 detik) --
    timer 0.7 repeat True action [
        SetScreenVariable("t1_x", renpy.random.randint(200, 1600)),
        SetScreenVariable("t1_y", renpy.random.randint(150, 800)),
        SetScreenVariable("t2_x", renpy.random.randint(200, 1600)),
        SetScreenVariable("t2_y", renpy.random.randint(150, 800)),
        SetScreenVariable("t3_x", renpy.random.randint(200, 1600)),
        SetScreenVariable("t3_y", renpy.random.randint(150, 800)),
        SetScreenVariable("t4_x", renpy.random.randint(200, 1600)),
        SetScreenVariable("t4_y", renpy.random.randint(150, 800)),
        SetScreenVariable("t5_x", renpy.random.randint(200, 1600)),
        SetScreenVariable("t5_y", renpy.random.randint(150, 800))
    ]

    # -- UI HUD --
    vbox:
        xalign 0.5 yalign 0.05 spacing 10
        text "TANGKIS SEMUA KAPAK GATOT!" size 50 color "#ff0000" bold True xalign 0.5
        text "WAKTU: [time_left:.1f] DETIK" size 40 color "#ffffff" bold True xalign 0.5
        text "HANCUR: [targets_hit] / 5" size 35 color "#00ff00" bold True xalign 0.5

    # -- Tomahawk 1 --
    if t1_active:
        imagebutton:
            idle "it_projectile_tomahawk"
            xpos t1_x ypos t1_y
            at spin_tomahawk
            action [SetScreenVariable("t1_active", False), SetScreenVariable("targets_hit", targets_hit + 1), Play("sound", "sfx_tembakan.ogg")]

    # -- Tomahawk 2 --
    if t2_active:
        imagebutton:
            idle "it_projectile_tomahawk"
            xpos t2_x ypos t2_y
            at spin_tomahawk
            action [SetScreenVariable("t2_active", False), SetScreenVariable("targets_hit", targets_hit + 1), Play("sound", "sfx_tembakan.ogg")]

    # -- Tomahawk 3 --
    if t3_active:
        imagebutton:
            idle "it_projectile_tomahawk"
            xpos t3_x ypos t3_y
            at spin_tomahawk
            action [SetScreenVariable("t3_active", False), SetScreenVariable("targets_hit", targets_hit + 1), Play("sound", "sfx_tembakan.ogg")]

    # -- Tomahawk 4 --
    if t4_active:
        imagebutton:
            idle "it_projectile_tomahawk"
            xpos t4_x ypos t4_y
            at spin_tomahawk
            action [SetScreenVariable("t4_active", False), SetScreenVariable("targets_hit", targets_hit + 1), Play("sound", "sfx_tembakan.ogg")]

    # -- Tomahawk 5 --
    if t5_active:
        imagebutton:
            idle "it_projectile_tomahawk"
            xpos t5_x ypos t5_y
            at spin_tomahawk
            action [SetScreenVariable("t5_active", False), SetScreenVariable("targets_hit", targets_hit + 1), Play("sound", "sfx_tembakan.ogg")]

    # -- Kondisi Menang --
    if targets_hit >= 5:
        timer 0.1 action Return(True)


# ==========================================
# LABEL PEMICU SCENE & MINIGAME (CUTSCENES)
# ==========================================
label play_mg_chap06b:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # -- Scene Setup Lorong Gelap --
    scene bg_lorong_gelap_16bit with transisi_asap
    
    "Suasana di dalam sangat gelap. Hanya ada sedikit cahaya rembulan yang menembus celah gorden."
    
    play sound "sfx_footsteps_approach.ogg"
    "Tiba-tiba, terdengar langkah kaki berat mendekat dari ujung lorong."

    show raka_kaget at center with hpunch
    r "Ssst! Sembunyi!"
    hide raka_kaget

    stop music fadeout 0.5
    play sound "sfx_metal_clash.ogg"
    "Sebuah linggis besar tiba-tiba menghantam dinding. Seseorang melompat dari kegelapan!"

    # Memicu CG 1: Ancaman Gatot (Awal Mula Game)
    scene cg_mg06b_awal_konfrontasi with flashmerah
    play music "bgm_05_otot_kawat.ogg" fadein 1.0
    
    g "BANGSAT! Jadi kalian anjing suruhan Pak Tirto yang mau ngilangin bukti?!"
    show raka_panik at left
    r "Gatot?! Tahan, woi! Kita bukan anak buahnya Tirto!"
    scene cg_chap06b_gatot_siap_serang with vpunch
    g "Alah, bacot! Lu kira gue bakal ampunin lu? Rasain ini!"
    
    play sound "sfx_fast_swish.ogg"
    "Gatot mengeluarkan lima buah kapak lempar dari sabuknya dan melemparkannya secara membabi buta ke arah Raka!"

    r "Sialan! Gue harus tangkis semua kapaknya sebelum kena!"

    # -- Memanggil Minigame Pertarungan Proyektil --
    call screen mg_shoot_gatot
    
    if _return == False:
        # GAGAL MENEMBAK (WAKTU HABIS)
        scene cg_mg06b_terpukul with hpunch
        play sound "sfx_flesh_tear_heavy.ogg"
        
        "Raka menendang jatuh semua target. Salah satu Tomahawk menghantam keras tubuhnya!"
        
        scene black with pingsan
        "Lemparan Kampak telak itu membuat Raka tersungkur tak berdaya. Investigasi berakhir tragis di tangan warga yang dibutakan amarah."
        
        play sound "sfx_game_over_hancur_8bit.ogg"
        centered "{size=+20}GAME OVER{/size}\n\nGagal menangkis serangan lemparan Gatot."
        return False
        
   # BERHASIL MENEMBAK SEMUA TOMAHAWK
    play sound "sfx_metal_clang.ogg"
    scene bg_lorong_gelap_16bit with flash_hijau
    
    "BAK! BUK! Tendangan terakhir Raka tepat menghantam kapak kelima Gatot, mementalkannya ke dinding hingga jatuh berdentang."
    
    "Gatot terkejut melihat serangan pamungkasnya dipatahkan begitu saja. Ia terdiam sejenak."
    
# Raka menyerang balik
    play sound "sfx_punch.ogg"
    scene cg_chap06b_raka_pukul_gatot with hpunch
    r "Ini buat serangan lu di gudang beras waktu itu, bangsat!!"
    
    play sound "sfx_bashing.ogg"
    scene cg_chap06b_raka_tendang_gatot with vpunch
    r "Dan ini... buat kapak-kapak gila lu barusan!"
    
    play sound "sfx_barang_berat_jatuh.ogg"
    scene cg_chap06b_gatot_terjerembab with hpunch
    "Kombinasi pukulan telak dan tendangan keras Raka menghantam Gatot. Pria berotot itu terhuyung dan jatuh terjerembab ke lantai kayu."
    
    r "Udah puas lu?! Sekarang buka mata lu dan dengerin gue!"
    
    # --- PERCABANGAN BUKTI BERDASARKAN HASIL CHAPTER 5 ---
    
    # Asumsi variabel 'ch5_punya_bukti_autopsi' bernilai True jika menang di mg_chap05c
    if ch5_punya_bukti_autopsi:
        "Raka melempar sebuah dokumen Rekam Medis ke arah Gatot yang masih tersungkur."
        
        r "Temen lu bukan mati dimakan Buto Ijo! Mereka sengaja diracun sama dr. Rina buat nutupin korupsi bahan makanan Tirto!"
        
        "Napas Gatot memburu sambil menahan sakit, matanya menatap tajam ke arah bukti Laporan Autopsi Asli di dekat tangannya."
        
        stop music fadeout 2.0
        
        # Memicu CG 3: Kesadaran Gatot
        scene cg_mg06b_gatot_sadar with dissolve_lambat
        
        g "...Jadi temen gue... dibunuh pake dalih pesugihan cuma buat nutupin borok mereka? Bajingan..."
        
    else:
        "Raka menyodorkan ponselnya yang memutar sebuah rekaman CCTV dari Puskesmas ke depan wajah Gatot yang tersungkur."
        
        r "Liat rekaman CCTV ini! Mbok Darmi nyampur racun ke minuman temen lu atas suruhan Tirto! Kita nyelinap ke sini justru buat cari bukti kejahatan Kades keparat itu!"
        
        "Napas Gatot memburu sambil menahan sakit, matanya menatap nanar ke arah layar ponsel di tangan Raka."
        
        stop music fadeout 2.0
        
        # Memicu CG 3: Kesadaran Gatot
        scene cg_mg06b_gatot_sadar with dissolve_lambat
        
        g "...Jadi temen gue... diracun sama orang suruhan Tirto dan ditutupin pake dalih pesugihan? Bajingan..."

    # --- KEMBALI KE ALUR UTAMA ---

    c "Iya, Mas Gatot. Ki Renggo cuma dibayar buat bikin TKP palsu agar warga takut."
    
    play music "bgm_10_fokus_spiritual.ogg" fadein 1.0
    g "Gue minta maaf... Gue sempet nguping pembicaraan Tirto sama Ki Renggo minggu lalu. Gue rekam pake kaset ini."

    # Mendapatkan Item Kaset Rekaman Gatot
    play sound "sfx_suara_ting.ogg"
    show item_kaset_rekaman_gatot at truecenter with dissolve_kilat
    "Mendapatkan [Rekaman Suara Rahasia Gatot]!"
    
    # Variabel akan digunakan di script utama
    $ has_kaset_gatot = True
    $ point_investigasi += 1
    
    hide item_kaset_rekaman_gatot with dissolve_kilat
    
    g "Kalian bawa kaset ini. Kalau tujuan kita sama buat hancurin Tirto, ayo bangunin gue. Kita ke lantai dua."
    

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP06B SELESAI")
    # -----------------------------------
    return True