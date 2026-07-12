# ==========================================
# FILE: mg_chap08a.rpy
# MINIGAME: RAKA MENANGKIS BOLA API (WHACK-A-MOLE)
# LOKASI: Lorong Gedung Kades Terbakar
# ==========================================

# ------------------------------------------
# 1. DEKLARASI ASET GAMBAR
# ------------------------------------------

image cg_susuri_lorong = "images/cg/cg_chap08_rgt_susuri_lorong_terbakar.webp"

image bg_start_mg_raka01 = "images/cg/cg_chap08_start_mg_raka01.webp"
image item_fire_bolt = "images/item/it_projectile_fire_bolt.webp" # Pastikan ekstensinya sesuai (.webp atau .png)

image cg_win_mg_raka01 = "images/cg/cg_chap08_game_win_mg_raka01.webp"
image cg_masuk_balkon = "images/cg/cg_chap08_rgt_win_masuk_balkon.webp"
image cg_lose_mg_raka01 = "images/cg/cg_chap08_game_over_mg_raka01.webp"

# ------------------------------------------
# 2. LOGIKA MESIN WHACK-A-MOLE (PYTHON)
# ------------------------------------------
init python:
    import random

    # Fungsi untuk memindahkan bola api ke posisi acak di layar
    def pindah_api():
        # Batas X: 0.1 sampai 0.9 (agar tidak terlalu ke pinggir)
        # Batas Y: 0.2 sampai 0.8 (agar tidak tertutup UI di atas/bawah)
        store.fire_x = random.uniform(0.1, 0.9)
        store.fire_y = random.uniform(0.2, 0.8)

# ------------------------------------------
# 3. SCREEN ANTARMUKA MINIGAME
# ------------------------------------------
screen mg_chap08a_play():
    modal True
    
    # Timer Mundur (Game Over jika mencapai 0)
    timer 1.0 action If(waktu_tersisa > 0, true=SetVariable("waktu_tersisa", waktu_tersisa - 1), false=Return("lose")) repeat True
    
    # Timer Pergerakan Bola Api (Api akan pindah sendiri jika terlalu lama tidak diklik)
    timer 0.9 action Function(pindah_api) repeat True

    # Background Minigame
    add "bg_start_mg_raka01"
    
    # Target Bola Api (Tombol Interaktif)
    imagebutton:
        idle "item_fire_bolt"
        # Efek membesar saat kursor diarahkan ke bola api
        hover Transform("item_fire_bolt", zoom=1.2, matrixcolor=BrightnessMatrix(0.4))
        xalign fire_x 
        yalign fire_y
        action [
            Play("sound", "sfx_serangan_cepat.ogg"), # Bunyi pukulan/tendangan Raka
            SetVariable("skor_api", skor_api + 1), 
            Function(pindah_api), 
            If(skor_api >= target_skor - 1, true=Return("win"))
        ]

    # UI Status Bar
    vbox:
        xalign 0.05 yalign 0.05 spacing 10
        text "WAKTU: [waktu_tersisa] DETIK" size 40 color "#ff5555" bold True outlines [(2, "#000", 0, 0)]
        text "DITANGKIS: [skor_api] / [target_skor]" size 35 color "#00ffcc" bold True outlines [(2, "#000", 0, 0)]

# ------------------------------------------
# 4. LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap08a:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Intro Cerita sebelum Minigame
    scene bg_lorong_gedung_kades_terbakar with wipe_kanan
    play music "bgm_05_otot_kawat.ogg" fadein 1.0
    
    "Sementara itu, Raka, Gatot, dan Pak Tirto berlari menyusuri lorong utama yang sudah dipenuhi asap pekat."
    
    scene cg_susuri_lorong with dissolve
    play sound "sfx_multiple_explosions.ogg"
    with vpunch
    
    g "Uhuk... uhuk... Mas Raka! Kayu atapnya mulai berjatuhan!"
    r "Jangan berhenti! Terus lari ke arah ujung lorong!"
    
    scene bg_start_mg_raka01 with flashmerah
    play sound "sfx_fire_burst.ogg"
    
    "Tiba-tiba, bola-bola api dari reruntuhan atap berjatuhan menghalangi jalan mereka!"
    r "Sial! Gue harus bersihin jalan ini pakai tendangan!"
    
    # Pengaturan Kesulitan Game
    $ skor_api = 0
    $ target_skor = 12       # Jumlah bola api yang harus ditangkis
    $ waktu_tersisa = 10     # Waktu dalam hitungan detik
    $ pindah_api()           # Panggil fungsi agar posisi awal api diacak
    
    # Tutorial Singkat
    "TUTORIAL: Klik bola api yang muncul di layar secepat mungkin untuk menangkisnya sebelum waktu habis!"
    
    # Memulai Minigame
    call screen mg_chap08a_play
    
    # Evaluasi Hasil Game
    if _return == "win":
        # SKENARIO MENANG
        stop music fadeout 1.0
        scene cg_win_mg_raka01 with flashbang
        play sound "sfx_explosion_one.ogg"
        with hpunch
        
        "HIAAT! Raka menendang dan meninju habis semua proyektil api yang menghalangi jalan, membuka jalur aman untuk mereka lewati."
        
        
        return True
        
    else:
        # SKENARIO KALAH
        stop music fadeout 1.0
        scene cg_lose_mg_raka01 with flashmerah
        play sound "sfx_benda_jatuh.ogg"
        with vpunch
        
        "Raka terlambat menangkis reruntuhan api. Sebuah balok kayu besar yang terbakar jatuh menimpa mereka bertiga!"
        return False