# ==========================================
# FILE: mg_chap06a.rpy
# MINIGAME: Susup Senyap (Lockpicking Jendela)
# STYLE: 16-Bit Retro Horror
# ==========================================

# ------------------------------------------
# LOGIKA MESIN MINIGAME (PYTHON)
# ------------------------------------------
init python:
    import random

    class MgLockpick:
        def __init__(self):
            # Posisi awal (0.0 kiri, 1.0 kanan)
            self.pos = 0.0
            self.direction = 1
            self.speed = 0.025
            
            # Status permainan
            self.pin_unlocked = 0
            self.noise_level = 0
            self.state = "playing" # "playing", "win", atau "lose"
            
            # Zona hijau (Tengah)
            self.zone_min = 0.45
            self.zone_max = 0.55

        def update(self):
            # Fungsi ini dipanggil terus-menerus oleh timer
            if self.state != "playing":
                return

            self.pos += self.speed * self.direction
            
            # Pantulkan indikator jika mentok ujung
            if self.pos >= 1.0:
                self.pos = 1.0
                self.direction = -1
                self.speed = random.uniform(0.02, 0.05)
            elif self.pos <= 0.0:
                self.pos = 0.0
                self.direction = 1
                self.speed = random.uniform(0.02, 0.05)
            
            renpy.restart_interaction() # Segarkan layar

        def click(self):
            # Fungsi ini dipanggil saat tombol/SPACE ditekan
            if self.state != "playing":
                return

            # Cek apakah indikator masuk zona hijau
            if self.zone_min <= self.pos <= self.zone_max:
                renpy.play("sfx_suara_ting.ogg", channel="sound")
                self.pin_unlocked += 1
                self.pos = 0.0 # Reset ke kiri
                self.speed += 0.01 # Makin cepat setiap pin terbuka
                
                if self.pin_unlocked >= 3:
                    self.state = "win"
            else:
                # Jika meleset
                renpy.play("sfx_treng_besi.ogg", channel="sound")
                self.noise_level += 25
                
                if self.noise_level >= 100:
                    self.state = "lose"
            
            renpy.restart_interaction()


# ------------------------------------------
# SCREEN MINIGAME LOCKPICKING
# ------------------------------------------
screen mg_lockpicking():
    modal True

    # Membuat instance logika minigame
    default lp = MgLockpick()

    # -- Timer Utama (Penggerak Indikator) --
    timer 0.03 repeat True action Function(lp.update)

    # -- Pengecekan Kondisi Menang/Kalah Otomatis --
    if lp.state == "win":
        timer 0.1 action Return(True)
    elif lp.state == "lose":
        timer 0.1 action Return(False)

    # Background minigame
    add "bg_jendela_balai_16bit"
    add "#00000099" # Overlay gelap agar UI jelas

    # -- UI Tampilan Atas --
    vbox:
        xalign 0.5 yalign 0.1 spacing 15
        text "MINIGAME: BOBOL JENDELA" size 40 color "#ffffff" bold True xalign 0.5
        
        hbox:
            spacing 50 xalign 0.5
            text "Pin Terbuka: [lp.pin_unlocked]/3" size 30 color "#00ff00" bold True
            text "Tingkat Kebisingan: [lp.noise_level]%" size 30 color "#ff0000" bold True

    # -- Visualisasi Bar Lockpick --
    frame:
        xalign 0.5 yalign 0.45
        xsize 800 ysize 60
        background "#333333"
        
        # Zona Hijau (Target)
        frame:
            xpos int(800 * lp.zone_min) ypos 0
            xsize int(800 * (lp.zone_max - lp.zone_min)) ysize 60
            background "#00cc00"

        # Indikator Bergerak (Garis Merah)
        frame:
            xpos int(800 * lp.pos) ypos 0
            xsize 10 ysize 60
            background "#ff0000"

    # -- Tombol Aksi Kustom (Menggunakan button_down dari Mister Anggi) --
    imagebutton:
        xalign 0.5 yalign 0.75
        idle "button_down"
        hover Transform("button_down", matrixcolor=BrightnessMatrix(0.2)) # Efek terang saat disorot
        action Function(lp.click)
    
    text "TEKAN [[SPACE] ATAU TOMBOL DI ATAS!" size 25 color "#cccccc" xalign 0.5 yalign 0.95
    
    # Deteksi Keyboard
    key "K_SPACE" action Function(lp.click)


# ==========================================
# LABEL PEMICU SCENE & MINIGAME (CUTSCENES)
# ==========================================
label play_mg_chap06a:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    scene cg_mg06a_awal with fade
    play music "bgm_03_bayang_petunjuk.ogg" fadein 2.0
    play sound "sfx_angin_malam_kencang.ogg" loop fadein 1.0
    
    "Malam semakin larut. Balai Desa berdiri megah namun memancarkan aura kelam dari luar."
    
    show raka_berpikir at left with dissolve
    r "Balai desa ini dijaga ketat. Ada dua satpam patroli di depan."

    show citra_lelah at right with dissolve
    c "Kepalaku masih berdenyut... Kita harus segera mencari ruang kerja Pak Tirto dan menemukan bukti aliran dananya."

    show bimo_normal at center with dissolve
    b "Aku merasakan energi negatif di sekitar sini. Ada jendela di sisi kanan balai desa yang kuncinya berkarat. Kita bisa masuk lewat sana."
    
    hide bimo_normal
    hide citra_lelah
    hide raka_berpikir
    
    scene bg_jendela_balai_16bit with transisi_asap
    stop sound fadeout 1.0
    
    show raka_berpikir at center with dissolve
    r "Kuncinya keras dan tua. Gue harus congkel perlahan pakai kawat ini. Kalau sampai bunyi keras, satpam bakal dengar."
    hide raka_berpikir

    stop music fadeout 1.0
    "Raka mengambil napas panjang, memasukkan ujung kawat ke dalam lubang kunci jendela..."
    
    # -- Memanggil Minigame --
    call screen mg_lockpicking

    # -- Cutscene Hasil Minigame --
    if _return == True:
        play sound "sfx_creaky_door_open.ogg"
        scene cg_mg06a_menang with flash_hijau
        play music "bgm_tense_chase.ogg" fadein 1.0
        
        "Klak! Suara pelan terdengar, dan pengait jendela berhasil terlepas. Udara dingin dan pengap langsung menyergap dari dalam lorong."
        
        r "Bagus. Kebuka juga. Ayo masuk, geraknya pelan-pelan."
        
        scene bg_lorong_gelap_16bit with dorong_atas
        "Ketiga remaja itu menyelinap masuk ke dalam Balai Desa yang gelap dan sunyi. Investigasi sesungguhnya dimulai."
        $ point_investigasi += 1
        return True

    else:
        play sound "sfx_treng_besi.ogg"
        scene bg_jendela_balai_16bit with hpunch
        
        show raka_kaget at center
        r "Sial! Kawatnya nyangkut dan suaranya nyaring banget!"
        hide raka_kaget
        
        play sound "sfx_door_slammed.ogg"
        "Suara benturan logam itu bergema di keheningan malam."
        
        stop music
        play sound "sfx_footsteps_fast.ogg"
        "Terdengar langkah kaki berat berlari ke arah jendela tempat mereka berada."
        
        scene cg_mg06a_kalah with flashbang
        play sound "sfx_teriakan_takut.ogg" 
        
        "Cahaya senter yang menyilaukan tiba-tiba menyorot wajah mereka. Satpam memergoki mereka!"
        
        scene black with pingsan
        "Rencana penyusupan hancur berantakan sebelum sempat dimulai. Mereka tertangkap basah."
        
        play sound "sfx_game_over.ogg"
        centered "{size=+20}GAME OVER{/size}\n\nKebisingan memancing perhatian penjaga."
        
        return False