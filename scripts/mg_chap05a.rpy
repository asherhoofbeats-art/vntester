# ==========================================
# FILE: mg_chap05a.rpy
# MINIGAME: Mengemudi di Jalan Berkabut
# MEKANIK: 3-Lane Obstacle Dodge
# ==========================================

# ------------------------------------------
# DEFINISI GAMBAR & SFX MINIGAME 05A
# ------------------------------------------
# Latar & Objek Gameplay
image bg_mg05a_jalan = "images/cg/bg_mg05a_jalan.webp"
image it_mobil_raka = "images/item/it_mobil_raka.webp"
image it_rintangan_gaib = "images/item/it_rintangan_gaib.webp"

# CG Cut Scenes
image cg_mg05a_raka_nyetir = "images/cg/cg_mg05a_raka_nyetir.webp"
image cg_mg05a_mobil_banting_setir = "images/cg/cg_mg05a_mobil_banting_setir.webp"
image cg_mg05a_berhenti_mendadak = "images/cg/cg_mg05a_berhenti_mendadak.webp"
image cg_mg05a_mobil_nabrak = "images/cg/cg_mg05a_mobil_nabrak.webp"


# ------------------------------------------
# FUNGSI PYTHON LOGIKA MENGHINDAR
# ------------------------------------------
init python:
    import random

    class FogDrivingGame:
        def __init__(self):
            self.car_lane = 2  # Posisi awal mobil (1: Kiri, 2: Tengah, 3: Kanan)
            self.obs_lane = random.choice([1, 2, 3]) # Posisi acak rintangan awal
            self.obs_y = -0.2  # Posisi Y rintangan (mulai dari luar layar atas)
            
            self.speed = 0.025 # Kecepatan awal rintangan
            self.score = 0
            self.target_score = 5 # Harus menghindari 5 rintangan untuk menang
            
            self.status = "playing"
            self.msg = "AWAS! Rintangan di depan!"
            self.msg_color = "#ffcc00"

        def update(self):
            if self.status != "playing":
                return

            # Menggerakkan rintangan ke bawah layar
            self.obs_y += self.speed

            # Cek Tabrakan (Jika rintangan berada di area bawah dekat mobil)
            if 0.70 < self.obs_y < 0.90:
                if self.car_lane == self.obs_lane:
                    # Gagal menghindar
                    self.status = "lose"

            # Jika rintangan berhasil dilewati (keluar dari bawah layar)
            elif self.obs_y >= 1.0:
                self.score += 1
                renpy.play("sfx_wuzz_ngebut.ogg")
                
                if self.score >= self.target_score:
                    self.status = "win"
                else:
                    # Reset rintangan ke atas dan tambah kecepatan
                    self.obs_y = -0.2
                    # Pastikan rintangan muncul di lajur acak
                    self.obs_lane = random.choice([1, 2, 3])
                    self.speed += 0.003 # Semakin lama semakin ngebut
                    
                    self.msg = "Bagus! Terus fokus!"
                    self.msg_color = "#00ffcc"

        def move_car(self, lane):
            if self.status == "playing":
                self.car_lane = lane

# ------------------------------------------
# SCREEN UI MINIGAME MENGEMUDI
# ------------------------------------------
screen mg_jalanan_kabut():
    modal True
    
    default game = FogDrivingGame()
    
    # Timer utama berjalan 60fps
    timer 0.016 action Function(game.update) repeat True

    # Background utama
    add "bg_mg05a_jalan"
    add "kabut_tipis" # Partikel cuaca
    add "#00000066"   # Efek gelap malam

    # Mapping Lajur ke Koordinat X Layar
    $ lane_x = {1: 0.2, 2: 0.5, 3: 0.8}

    # ==========================
    # AREA VISUAL RINTANGAN & MOBIL
    # ==========================
    
    # Render Rintangan Gaib
    add "it_rintangan_gaib":
        xalign lane_x[game.obs_lane]
        yalign game.obs_y
        zoom 1.2
        
    # Render Mobil Raka
    add "it_mobil_raka":
        xalign lane_x[game.car_lane]
        yalign 0.85 # Mobil diam di area bawah layar
        zoom 1.0

    # ==========================
    # HUD & INFORMASI
    # ==========================
    vbox:
        xalign 0.5 ypos 30
        spacing 10
        
        text "FOKUS MENGEMUDI" size 36 color "#ffffff" xalign 0.5 bold True
        text game.msg size 24 color game.msg_color xalign 0.5 bold True
        text "Lolos: [game.score] / [game.target_score]" size 28 color "#00ffcc" xalign 0.5 bold True

    # ==========================
    # KONTROL PEMAIN (3 TOMBOL BESAR)
    # ==========================
    hbox:
        xalign 0.5
        yalign 0.95
        spacing 50
        
        textbutton "⬅️ KIRI":
            text_size 35
            xysize (250, 100)
            background Solid("#33333399")
            action Function(game.move_car, 1)
            
        textbutton "⬆️ TENGAH":
            text_size 35
            xysize (250, 100)
            background Solid("#33333399")
            action Function(game.move_car, 2)
            
        textbutton "➡️ KANAN":
            text_size 35
            xysize (250, 100)
            background Solid("#33333399")
            action Function(game.move_car, 3)

    # Keyboard Binds untuk main di PC
    key "K_LEFT" action Function(game.move_car, 1)
    key "K_DOWN" action Function(game.move_car, 2)
    key "K_RIGHT" action Function(game.move_car, 3)

    # Cek Kondisi Menang/Kalah
    if game.status == "win":
        timer 0.1 action Return("win")
    elif game.status == "lose":
        timer 0.1 action Return("lose")


# ------------------------------------------
# LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap05a:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    stop music fadeout 1.0
    play music "bgm_tense_chase.ogg" fadein 1.0 loop
    
    # INTRO CG
    scene cg_mg05a_raka_nyetir with transisi_asap
    show raka_panik at center with dissolve_kilat
    r "Sialan! Kabutnya nipu pandangan! Gue harus banting setir!"
    hide raka_panik
    
    "Gunakan tombol KIRI, TENGAH, KANAN untuk memindahkan mobil Raka. Hindari 5 rintangan gaib yang muncul dari balik kabut!"

    window hide
    call screen mg_jalanan_kabut
    
    stop music fadeout 1.0
    
    if _return == "win":
        # WIN CG & SFX
        play sound "sfx_rem_mendadak.ogg"
        scene cg_mg05a_berhenti_mendadak with hpunch
        "CIIIIITTT!"
        "Berkat refleks kilat Raka, mobil berhasil menghindari semua rintangan gaib dan berhenti tepat di samping wanita pucat tersebut."
        return "win"
        
    else:
        # LOSE CG & SFX
        play sound "sfx_nabrak_game.ogg"
        scene cg_mg05a_mobil_nabrak with vpunch
        "BRAAAKK!"
        "Mobil Raka gagal menghindari bayangan hitam dan menabrak pembatas jalan. Bemper depan mobil penyok dan mesinnya mati."
        return "lose"