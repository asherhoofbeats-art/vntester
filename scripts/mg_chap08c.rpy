# ==========================================
# FILE: mg_chap08c.rpy
# MINIGAME: RAKA MENANGKIS LEMPARAN OBOR (WHACK-A-MOLE)
# LOKASI: Balkon Belakang Balai Desa
# ==========================================

# ------------------------------------------
# 1. DEKLARASI ASET GAMBAR LOKAL
# ------------------------------------------
# Background saat minigame berlangsung
image bg_start_mg_obor = "images/cg/cg_mg_chap08_raka_siap_tangkis_obor.webp"

# Target proyektil
image item_obor = "images/item/it_obor_terlempar.webp" 

# CG Hasil Akhir (Menang/Kalah)
image cg_win_mg_obor = "images/cg/cg_chap08_raka_terjebak_balkon.webp"
image cg_lose_mg_obor = "images/cg/cg_chap08_balkon_kebakaran_game_over.webp"

# ------------------------------------------
# 2. LOGIKA MESIN WHACK-A-MOLE (PYTHON)
# ------------------------------------------
init python:
    import random

    # Fungsi untuk memindahkan obor ke posisi acak di layar
    def pindah_obor():
        # Batas X: 0.1 sampai 0.9 (agar tidak keluar layar)
        # Batas Y: 0.2 sampai 0.8 (menghindari UI teks di atas/bawah)
        store.obor_x = random.uniform(0.1, 0.9)
        store.obor_y = random.uniform(0.2, 0.8)

# ------------------------------------------
# 3. SCREEN ANTARMUKA MINIGAME
# ------------------------------------------
screen mg_chap08c_play():
    modal True
    
    # Timer Mundur Global (Game Over jika mencapai 0)
    timer 1.0 action If(waktu_tersisa_obor > 0, true=SetVariable("waktu_tersisa_obor", waktu_tersisa_obor - 1), false=Return("lose")) repeat True
    
    # Timer Pergerakan Obor (Obor pindah setiap 0.8 detik karena warga melempar dengan cepat!)
    timer 0.8 action Function(pindah_obor) repeat True

    # Background Minigame
    add "bg_start_mg_obor"
    
    # Target Lemparan Obor (Tombol Interaktif)
    imagebutton:
        idle "item_obor"
        hover Transform("item_obor", zoom=1.2, matrixcolor=BrightnessMatrix(0.4))
        xalign obor_x 
        yalign obor_y
        action [
            Play("sound", "sfx_fast_swoosh.ogg"), # Suara tendangan membelah angin
            SetVariable("skor_obor", skor_obor + 1), 
            Function(pindah_obor), 
            If(skor_obor >= target_skor_obor, true=Return("win"))
        ]

    # UI Status Bar
    vbox:
        xalign 0.05 yalign 0.05 spacing 10
        text "WAKTU: [waktu_tersisa_obor] DETIK" size 40 color "#ff5555" bold True outlines [(2, "#000", 0, 0)]
        text "OBOR DITANGKIS: [skor_obor] / [target_skor_obor]" size 35 color "#ffaa00" bold True outlines [(2, "#000", 0, 0)]

# ------------------------------------------
# 4. LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap08c:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # BGM Tegang
    play music "bgm_05_otot_kawat.ogg" fadein 1.0
    
    # Pengaturan Kesulitan Game
    $ skor_obor = 0
    $ target_skor_obor = 15       # Lebih banyak dari lorong karena warga ramai
    $ waktu_tersisa_obor = 12     # Waktu hitung mundur
    $ pindah_obor()               # Acak posisi awal
    
    # Tutorial Singkat
    "TUTORIAL: Klik obor yang dilemparkan warga ke arah balkon secepat mungkin! Jangan sampai ada yang lolos membakar balkon!"
    
    # Memulai Minigame
    call screen mg_chap08c_play
    
    # Evaluasi Hasil Game
    if _return == "win":
        # SKENARIO MENANG
        stop music fadeout 1.0
        scene cg_win_mg_obor with flashbang
        play sound "sfx_serangan_cepat.ogg"
        with hpunch
        
        "Raka bergerak secepat kilat, menendang jatuh setiap obor yang melayang ke arah balkon tanpa sisa!"
        return True
        
    else:
        # SKENARIO KALAH
        stop music fadeout 1.0
        scene cg_lose_mg_obor with flashmerah
        play sound "sfx_fire_burst.ogg"
        with vpunch
        
        "Raka kewalahan menahan hujan obor. Salah satu obor lolos dan mengenai tumpukan kayu di sudut balkon!"
        return False