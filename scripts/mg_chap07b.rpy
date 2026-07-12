# ==========================================
# FILE: mg_chap07b.rpy
# MINIGAME: Resonansi Citra (Focus / Tuning)
# STYLE: 16-Bit Retro Horror
# ==========================================

# ------------------------------------------
# ASET GAMBAR KHUSUS MINIGAME 7B
# ------------------------------------------
image cg_mg_chap07b_starting_game = "images/cg/cg_mg_chap07b_starting_game.webp"
image bg_mg_chap07b = "images/bg/bg_mg_chap07b.webp"
image bg_mg_chap07b_citra_menang = "images/bg/bg_mg_chap07b_citra_menang.webp"
image bg_mg_chap07b_citra_kalah = "images/bg/bg_mg_chap07b_citra_kalah.webp"
image kalah_mgchap06e = "images/cg/kalah_mgchap06e.webp"

# ------------------------------------------
# LOGIKA MESIN MINIGAME (PYTHON)
# ------------------------------------------
init python:
    class MgResonansi:
        def __init__(self):
            # Posisi dalam persentase (0.0 sampai 100.0)
            self.player_pos = 50.0  # Aura Citra (Biru)
            self.safe_pos = 50.0    # Aura Entitas (Merah)
            
            self.safe_dir = 1
            self.safe_speed = 1.0
            
            self.progress = 0.0     # Capai 100 untuk menang
            self.time_left = 20.0   # Waktu maksimal minigame
            self.state = "playing"  # "playing", "win", "lose"

        def update(self):
            if self.state != "playing": 
                return
            
            # Hitung mundur waktu
            self.time_left -= 0.05
            if self.time_left <= 0:
                self.state = "lose"
                return
            
            # Pergerakan otomatis target aura entitas (Zona Merah)
            self.safe_pos += self.safe_speed * self.safe_dir
            
            # Pantulkan jika mencapai ujung dan acak kecepatan
            if self.safe_pos >= 90.0:
                self.safe_pos = 90.0
                self.safe_dir = -1
                self.safe_speed = renpy.random.uniform(0.5, 2.5)
            elif self.safe_pos <= 10.0:
                self.safe_pos = 10.0
                self.safe_dir = 1
                self.safe_speed = renpy.random.uniform(0.5, 2.5)
                
            # Deteksi Sinkronisasi: Jika aura Citra berdekatan (Toleransi 15%)
            if abs(self.player_pos - self.safe_pos) <= 15.0:
                self.progress += 0.6  # Sinkronisasi naik
                if self.progress >= 100.0:
                    self.progress = 100.0
                    self.state = "win"
            else:
                self.progress -= 0.2  # Sinkronisasi turun jika meleset
                if self.progress < 0:
                    self.progress = 0.0
                
            renpy.restart_interaction()

        def move(self, direction):
            if self.state != "playing": 
                return
                
            if direction == "left":
                self.player_pos -= 5.0
            elif direction == "right":
                self.player_pos += 5.0
                
            # Batasan layar
            if self.player_pos < 0.0: self.player_pos = 0.0
            if self.player_pos > 100.0: self.player_pos = 100.0
            
            renpy.restart_interaction()


# ------------------------------------------
# SCREEN MINIGAME RESONANSI
# ------------------------------------------
screen mg_chap07b_resonansi():
    modal True

    # Instance mesin minigame
    default reso = MgResonansi()

    # Timer utama (50ms per tick)
    timer 0.05 repeat True action Function(reso.update)

    # Deteksi menang/kalah
    if reso.state == "win":
        timer 0.2 action Return(True)
    elif reso.state == "lose":
        timer 0.2 action Return(False)

    # Background Game menggunakan aset asli
    add "bg_mg_chap07b"
    add "#000000aa" # Overlay gelap agar UI jelas dan tidak silau

    # -- UI Tampilan Atas --
    vbox:
        xalign 0.5 yalign 0.05 spacing 10
        text "MINIGAME: RESONANSI SPIRITUAL" size 40 color "#ffffff" bold True xalign 0.5 outlines [ (2, "#000000", 0, 0) ]
        text "GESER AURA CITRA UNTUK MENUTUPI AURA ENTITAS!" size 20 color "#00ffff" bold True xalign 0.5 outlines [ (1, "#000000", 0, 0) ]
        
        hbox:
            spacing 50 xalign 0.5
            text "WAKTU: [reso.time_left:.1f]s" size 30 color "#ffaa00" bold True outlines [ (2, "#000000", 0, 0) ]
            text "SINKRONISASI: [int(reso.progress)]%" size 30 color "#00ff00" bold True outlines [ (2, "#000000", 0, 0) ]

    # -- PROGRESS BAR SINKRONISASI --
    frame:
        xalign 0.5 yalign 0.25
        xsize 800 ysize 20
        background "#333333"
        frame:
            xsize int((reso.progress / 100.0) * 800) ysize 20
            background "#00ff00"

    # -- BAR FREKUENSI UTAMA --
    frame:
        xalign 0.5 yalign 0.5
        xsize 800 ysize 80
        background "#222222"
        
        # Target Zona Aura Entitas (Merah - Bergerak Otomatis)
        frame:
            xpos int((reso.safe_pos / 100.0) * 800) - 60  # -60 agar titik xpos ada di tengah kotak
            ypos 0
            xsize 120 ysize 80
            background "#ff000088"
            
        # Indikator Aura Citra (Biru - Dikontrol Pemain)
        frame:
            xpos int((reso.player_pos / 100.0) * 800) - 10
            ypos -10
            xsize 20 ysize 100
            background "#00ffff"

    # -- TOMBOL KONTROL --
    hbox:
        xalign 0.5 yalign 0.8 spacing 200
        
        # Tombol Kiri
        imagebutton:
            idle Transform("button_left", zoom=0.6)
            hover Transform("button_left", zoom=0.6, matrixcolor=BrightnessMatrix(0.3))
            action Function(reso.move, "left")
            
        # Tombol Kanan
        imagebutton:
            idle Transform("button_right", zoom=0.6)
            hover Transform("button_right", zoom=0.6, matrixcolor=BrightnessMatrix(0.3))
            action Function(reso.move, "right")

    text "TEKAN TOMBOL ARAH (KIRI/KANAN) DI LAYAR ATAU KEYBOARD" size 20 color "#cccccc" xalign 0.5 yalign 0.95 outlines [ (2, "#000000", 0, 0) ]
    
    # Deteksi Keyboard
    key "K_LEFT" action Function(reso.move, "left")
    key "K_RIGHT" action Function(reso.move, "right")


# ==========================================
# LABEL PEMICU SCENE RESONANSI CITRA
# ==========================================
label play_mg_chap07b:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Intro Scene
    play sound "sfx_whuz_gaib.ogg"
    scene cg_mg_chap07b_starting_game with transisi_asap
    play music "bgm_10_fokus_spiritual.ogg" fadein 1.0
    
    "Mata Citra memancarkan cahaya biru redup saat kabut aneh mulai memenuhi ruangan. Ia melangkah maju, mencoba menyerap amarah dari ratusan jiwa tumbal yang membentuk wujud raksasa itu."
    
    c "Aura mereka sangat kacau... Aku harus menyamakan frekuensi batinku dengan penderitaan mereka..."
    
    # Panggil Minigame
    call screen mg_chap07b_resonansi
    
    if _return == True:
        # MENANG
        $ citra_resonansi_gaib +=1
        play sound "sfx_magic_spell.ogg"
        scene bg_mg_chap07b_citra_menang with flash_biru
        
        "Pancaran energi biru terang meledak dari tubuh Citra. Cahaya itu menyelimuti bayangan raksasa tersebut, perlahan memadamkan api kebencian di mata merahnya."
        
        c "Tenanglah... rasa sakit kalian... aku merasakannya..."
        
        play sound "sfx_penyembuhan_gaib.ogg"
        "Aura entitas itu meredup, tak lagi agresif. Ia memberikan Bimo celah sempurna yang ia butuhkan untuk merapal segel."
        
        return True
        
    else:
        # KALAH
        stop music fadeout 0.5
        play sound "sfx_glass_shatter.ogg"
        scene bg_mg_chap07b_citra_kalah with tv_rusak
        
        "Energi gelap entitas itu terlalu kuat. Arus kebencian yang masif memukul mundur kesadaran Citra!"
        
        with hpunch
        play sound "sfx_elara_scream.ogg"
        c "AAARGHH! Suara mereka... kepalaku mau pecah!"
        
        scene black with pingsan
        "Citra terhempas ke lantai dengan darah mengalir dari hidungnya. Tanpa perisai spiritualnya, entitas itu mengamuk tanpa kendali dan membantai semua orang di ruangan itu."
        scene kalah_mgchap06e with blood_splatter
        play sound "sfx_game_over.ogg"
        centered "{size=+20}GAME OVER{/size}\n\nCitra kewalahan menahan aura entitas gaib dan tewas. Tirto Juga tewas dilahap entitas gaib. Raka dan Bimo Tidak tahu apa yang harus dilakukan"
        return False