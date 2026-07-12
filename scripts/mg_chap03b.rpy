# ==========================================
# FILE: mg_chap03b.rpy
# MINIGAME: QTE Menangkis Proyektil Tomahawk
# ==========================================

# ------------------------------------------
# DEFINISI GAMBAR MINIGAME 03B
# ------------------------------------------
image it_projectile_tomahawk = "images/item/it_projectile_tomahawk.webp"
image cg_mg03b_intro = "images/cg/cg_mg03b_intro.webp"
image bg_mg03b_action = "images/cg/bg_mg03b_action.webp"
image cg_mg03b_win = "images/cg/cg_mg03b_win.webp"
image cg_mg03b_lose = "images/cg/cg_mg03b_lose.webp"

# ------------------------------------------
# TRANSFORM ANIMASI GERAK MULUS
# ------------------------------------------
transform gerak_acak_cepat(target_x, target_y):
    ease 0.4 xalign target_x yalign target_y

# ------------------------------------------
# SCREEN UI MINIGAME MENANGKIS
# ------------------------------------------
screen mg_tangkis_projectile():
    modal True
    
    # Latar Belakang Aksi Minigame
    add "bg_mg03b_action"
    
    # Tambahan layer semi-transparan tipis agar proyektil lebih menonjol dari BG
    add "#00000066"

    # Waktu batas permainan: 10 Detik
    default time_limit = 10.0

    # Titik kemunculan awal untuk 3 proyektil
    default p1_x = renpy.random.uniform(0.1, 0.3)
    default p1_y = renpy.random.uniform(0.2, 0.8)
    
    default p2_x = renpy.random.uniform(0.4, 0.6)
    default p2_y = renpy.random.uniform(0.2, 0.8)
    
    default p3_x = renpy.random.uniform(0.7, 0.9)
    default p3_y = renpy.random.uniform(0.2, 0.8)

    # Status klik (False = belum ditangkis, True = sudah ditangkis)
    default clicked_1 = False
    default clicked_2 = False
    default clicked_3 = False

    # SISTEM PERGERAKAN DINAMIS (Pembaruan Posisi tiap 0.4 Detik)
    timer 0.4 repeat True action [
        SetScreenVariable("p1_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p1_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p2_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p2_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p3_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p3_y", renpy.random.uniform(0.2, 0.9))
    ]

    # Timer kegagalan
    timer time_limit action Return(False)
    
    # Timer keberhasilan
    if clicked_1 and clicked_2 and clicked_3:
        timer 0.1 action Return(True)

    # UI Indikator Waktu Berjalan di Atas Layar
    vbox:
        xalign 0.5
        yalign 0.05
        spacing 10
        
        text "TANGKIS SERANGAN! (Waktu: 10 Detik)" size 30 color "#ffaa00" xalign 0.5 bold True
        
        bar:
            value AnimatedValue(0, time_limit, time_limit) 
            range time_limit 
            xsize 600 
            ysize 30
            xalign 0.5

    # TOMBOL PROYEKTIL 1
    if not clicked_1:
        imagebutton:
            idle "it_projectile_tomahawk"
            hover "it_projectile_tomahawk"
            at gerak_acak_cepat(p1_x, p1_y)
            action [SetScreenVariable("clicked_1", True), Play("sound", "sfx_metal_clash.ogg")]

    # TOMBOL PROYEKTIL 2
    if not clicked_2:
        imagebutton:
            idle "it_projectile_tomahawk"
            hover "it_projectile_tomahawk"
            at gerak_acak_cepat(p2_x, p2_y)
            action [SetScreenVariable("clicked_2", True), Play("sound", "sfx_metal_clash.ogg")]

    # TOMBOL PROYEKTIL 3
    if not clicked_3:
        imagebutton:
            idle "it_projectile_tomahawk"
            hover "it_projectile_tomahawk"
            at gerak_acak_cepat(p3_x, p3_y)
            action [SetScreenVariable("clicked_3", True), Play("sound", "sfx_metal_clash.ogg")]


# ==========================================
# 3. LABEL PEMICU MINIGAME QTE TANGKIS
# ==========================================
label play_mg_chap03_qte:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Cutscene Intro Minigame
    scene cg_mg03b_intro with transisi_senter
    "Waktu terasa melambat. Gatot tersenyum gila, menarik beberapa tomahawk tajam dari balik jaketnya."
    "Cepat! Klik semua proyektil yang melayang di layar sebelum waktunya habis!"
    
    # Memanggil screen minigame
    call screen mg_tangkis_projectile
    
    # Evaluasi Hasil (Menang/Kalah)
    if _return == True:
        scene cg_mg03b_win with flashbang
        play sound "sfx_metal_clang.ogg"
        $ poin_investigasi +=2
        "Trang!! Dengan kuda-kuda kokoh, Raka berhasil menangkis semua tomahawk yang mengarah padanya!"
        return True
    else:
        scene cg_mg03b_lose with hpunch
        play sound "sfx_benda_dipukul.ogg"
        $ poin_investigasi -=1
        "Bugh! Pertahanan Raka runtuh. Ia gagal menangkis dan terkena hantaman keras dari senjata Gatot!"
        return False