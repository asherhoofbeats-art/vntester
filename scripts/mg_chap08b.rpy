# ==========================================
# FILE: mg_chap08b.rpy
# MINIGAME: RHYTHM DOA BIMO (GUITAR HERO STYLE)
# LOKASI: Ruang Kerja Tirto yang Terbakar
# ==========================================

# ------------------------------------------
# 1. DEKLARASI ASET GAMBAR LOKAL
# ------------------------------------------


# ------------------------------------------
# 2. LOGIKA MESIN RHYTHM GAME (PYTHON)
# ------------------------------------------
init python:
    class RhythmPrayerGame:
        def __init__(self):
            # Urutan kata doa yang akan jatuh
            self.words = ["YA", "ALLAH", "YA", "MALIK", "YA", "WALIY"]
            self.curr_idx = 0
            
            self.y_pos = 0.0          # Posisi vertikal kata saat ini (0.0 atas, 1.0 bawah)
            self.speed = 0.025        # Kecepatan jatuh (ditambah setiap 0.05 detik)
            
            self.hits = 0             # Jumlah ketukan pas
            self.state = "playing"    # playing, win, lose
            self.message = ""         # Pesan feedback (Sempurna/Terlewat)
            self.msg_timer = 0.0      # Timer untuk menghilangkan pesan feedback

        def tick(self):
            if self.state != "playing":
                return
                
            # Kata jatuh ke bawah
            self.y_pos += self.speed
            
            # Kurangi timer pesan feedback
            if self.msg_timer > 0:
                self.msg_timer -= 0.05
            else:
                self.message = ""

            # Jika kata terlewat batas bawah layar (gagal tangkap)
            if self.y_pos > 1.0:
                self.message = "TERLEWAT!"
                self.msg_timer = 0.5
                renpy.play("sfx_benda_jatuh.ogg", channel="sound")
                self.next_word()
                
            renpy.restart_interaction()

        def hit_action(self):
            if self.state != "playing":
                return
                
            # Cek apakah posisi kata berada di dalam "Hit Zone" (0.70 sampai 0.95)
            if 0.70 <= self.y_pos <= 0.95:
                self.hits += 1
                self.message = "SEMPURNA!"
                self.msg_timer = 0.5
                renpy.play("sfx_magic_charge.ogg", channel="sound")
            else:
                self.message = "TERLALU CEPAT!"
                self.msg_timer = 0.5
                renpy.play("sfx_stab.ogg", channel="sound")
                
            self.next_word()

        def next_word(self):
            self.curr_idx += 1
            self.y_pos = 0.0
            
            # Cek jika semua kata sudah habis
            if self.curr_idx >= len(self.words):
                # Butuh minimal 5 kata benar untuk menang (toleransi 1 meleset)
                if self.hits >= 5:
                    self.state = "win"
                else:
                    self.state = "lose"
            renpy.restart_interaction()

# ------------------------------------------
# 3. SCREEN ANTARMUKA MINIGAME
# ------------------------------------------
screen mg_chap08b_play(game):
    modal True
    
    # Timer Utama Mesin Game (Berjalan 20 frame per detik)
    timer 0.05 action Function(game.tick) repeat True
    
    # Cek Kondisi Berakhir
    if game.state == "win":
        timer 0.5 action Return(True)
    elif game.state == "lose":
        timer 0.5 action Return(False)
    
    # 1. Background
    add "cg_bimo_citra_bersiap"
    
    # Efek panas buatan
    add Solid("#ff000033") 
    
    # 2. UI Status & Target Hitungan
    vbox:
        xalign 0.05 yalign 0.05 spacing 10
        text "RAPALKAN DOA!" size 45 color "#00ffff" bold True outlines [(3, "#000000", 0, 0)]
        text "Lafal Tepat: [game.hits] / 6" size 35 color "#00ffcc" bold True outlines [(2, "#000000", 0, 0)]

    # 3. ZONA TARGET (Hit Zone) - Area di mana pemain harus menekan tombol
    # Area ini melintang di bawah layar (yalign 0.85)
    frame:
        background Solid("#00ffcc44") # Warna area transparan
        xalign 0.5 yalign 0.85
        xsize 800 ysize 100
        
        # Garis pembatas target atas dan bawah
        add Solid("#00ffff") xalign 0.5 yalign 0.0 xsize 800 ysize 5
        add Solid("#00ffff") xalign 0.5 yalign 1.0 xsize 800 ysize 5

    # 4. KATA YANG JATUH DARI ATAS
    if game.state == "playing" and game.curr_idx < len(game.words):
        text game.words[game.curr_idx]:
            size 70 color "#ffffff" bold True outlines [(3, "#000000", 0, 0)]
            xalign 0.5
            yanchor 0.5 ypos game.y_pos # Bergerak vertikal sesuai game.y_pos

    # 5. PESAN FEEDBACK (Sempurna / Terlewat)
    if game.message != "":
        text game.message:
            size 60 color "#ffea00" bold True outlines [(3, "#ff0000", 0, 0)]
            xalign 0.5 yalign 0.4

    # 6. KONTROL PEMAIN (Bisa diklik layar atau tekan SPASI)
    if game.state == "playing":
        key "K_SPACE" action Function(game.hit_action)
        
        # Tombol visual di layar
        textbutton "TEKAN SAAT KATA BERADA DI AREA KOTAK!":
            xalign 0.5 yalign 0.95
            text_size 35 text_color "#ffffff" text_bold True text_outlines [(2, "#000", 0, 0)]
            background Solid("#000000aa") padding (20, 10)
            action Function(game.hit_action)

# ------------------------------------------
# 4. LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap08b:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Inisialisasi Game Rhythm
    $ current_prayer_game = RhythmPrayerGame()
    
    scene cg_bimo_citra_bersiap with dissolve
    play music "bgm_tense_chase.ogg" fadein 1.0
    
    "TUTORIAL: Lafal doa akan jatuh dari atas layar. Tekan tombol SPASI atau KLIK tulisan di bawah layar tepat saat kata masuk ke dalam Kotak Biru!"
    
    # Mulai Minigame
    call screen mg_chap08b_play(current_prayer_game)
    
    # Evaluasi Hasil Game
    if _return == True:
        # Jika berhasil merangkai lafal doa
        stop music fadeout 1.0
        
        # BIMO MENGUCAPKAN DOA PENUH!
        play sound "sfx_magic_spell.ogg"
        b "Allahumma innii a'udzu bika min zawaali ni'matik, wa tahawwuli 'aafiyatik, wa fujaa'ati niqmatik, wa jamii'i sakhathik!"
        
        return True
        
    else:
        # Jika gagal atau terlalu banyak salah (kurang dari 5 kata)
        stop music fadeout 1.0
        return False