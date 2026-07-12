# ==========================================
# FILE: final_boss_renggo.rpy
# MINIGAME FINAL BOSS: MELAWAN GENDERUWO KI RENGGO
# MEKANIK: Lane Dodge (Tracking & Double Attack) -> QTE Bind Zig-Zag -> Attack
# ==========================================

# ------------------------------------------
# 1. DEKLARASI ASET GAMBAR LOKAL & ATL
# ------------------------------------------
image bg_lapangan_final = "images/bg/bg_lapangan_balai_kosong.webp"

image tombol_kiri_idle = "images/button/tombol_dash_kiri.webp"
image tombol_kanan_idle = "images/button/tombol_dash_kanan.webp"

image item_warning = "images/button/warning_sign.webp"
image item_segel_hantu = "images/item/it_kertas_segel_hantu_1.webp"
image item_fireball = "images/item/it_projectile_fireball_katon.webp"

# --- TRANSFORMASI UNTUK ANIMASI PROYEKTIL & UI ---
# ==========================================
# ADEGAN KEMATIAN KI RENGGO (JEMBATAN MENUJU ENDING)
# ==========================================

label adegan_renggo_abu:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    
    scene bg_lapangan_balai_kosong with dissolve_lambat
    
    play sound "sfx_monster_died.ogg"
    
    with hpunch
    "Tebasan dan serangan bertubi-tubi dari Trio akhirnya meruntuhkan pertahanan Genderuwo raksasa itu."
    "Raungan menyayat hati terdengar saat wujud monsternya memudar, menyisakan tubuh ringkih Ki Renggo yang terkapar di tanah."

    play music "bgm_01_jejak_misteri.ogg"
    
    scene cg_chap08_renggo_jadi_abu_mulai with dissolve
    "Tubuh tuanya mulai retak. Cahaya keemasan bercampur abu mulai menguar dari ujung jari-jarinya."
    
    kr "Uhuk... uhuk... Kekuatanku... Ilmu hitam yang kubangun puluhan tahun..."
    
    scene cg_chap08_renggo_jadi_abu_setengah with dissolve
    "Kulitnya perlahan terkelupas menjadi debu yang tertiup angin malam. Di detik-detik terakhirnya, tatapan sombong Ki Renggo berubah menjadi keputusasaan yang amat dalam."
    "Air mata menetes dari sudut matanya yang keriput."
    
    kr "Ya Allah... aku tahu ajalku di depan mata."
    kr "Setelah semua kekejian ini... masihkah pintu tobat-Mu tersedia untukku, hamba-Mu yang musyrik ini?"
    
    scene cg_chap08_end_renggo_jadi_abu with blood_splatter
    play sound "sfx_magic_spell.ogg"
    "Kalimat itu menjadi kata-kata terakhirnya. Tubuh Ki Renggo hancur sepenuhnya menjadi abu, tersapu bersih oleh angin malam yang berhembus melintasi balai desa."

    scene bg_kebakaran_usai with dissolve_lambat
    "Keheningan menyelimuti lapangan."
    "Kutukan yang mengikat desa ini akhirnya terangkat..."
    
    # Setelah Renggo mati, sistem akan langsung lompat ke mesin evaluasi 
    # untuk menentukan nasib Tirto (6 Ending)

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("ADEGAN_RENGGO_ABU SELESAI")
    # -----------------------------------
    jump evaluasi_ending_utama
# 1. Bimo melempar fireball ke arah Boss
transform lempar_fireball:
    xalign 0.5 yalign 1.0 zoom 0.5 alpha 0.0
    parallel:
        ease 0.4 yalign 0.3
    parallel:
        ease 0.4 zoom 1.5
    parallel:
        ease 0.1 alpha 1.0
        pause 0.2
        ease 0.1 alpha 0.0

# 2. Peringatan bahaya berkedip
transform warning_kedip:
    alpha 0.0 zoom 1.5
    ease 0.2 alpha 1.0 zoom 1.0
    pause 0.2
    ease 0.2 alpha 0.0
    repeat

# 3. Fireball Boss jatuh dari langit ke tanah
transform boss_fireball_fall(target_x):
    xalign target_x yalign -0.2 zoom 1.5
    ease 0.4 yalign 0.9

# --- TRANSFORMASI KESULITAN QTE (ZIG-ZAG) ---

# HP Penuh (Mudah - Mengayun horizontal)
transform target_bergerak_easy:
    xalign 0.5 yalign 0.6
    ease 1.0 xalign 0.2
    ease 2.0 xalign 0.8
    ease 1.0 xalign 0.5
    repeat

# HP Sisa 2 (Sulit - Zigzag Medium)
transform target_bergerak_medium:
    xalign 0.5 yalign 0.6
    ease 0.6 xalign 0.2 yalign 0.3
    ease 0.6 xalign 0.8 yalign 0.7
    ease 0.6 xalign 0.2 yalign 0.7
    ease 0.6 xalign 0.8 yalign 0.3
    ease 0.6 xalign 0.5 yalign 0.6
    repeat

# HP Sisa 1 (Sangat Sulit - Zigzag Cepat Pamungkas)
transform target_bergerak_hard:
    xalign 0.5 yalign 0.6
    ease 0.3 xalign 0.1 yalign 0.2
    ease 0.3 xalign 0.9 yalign 0.8
    ease 0.3 xalign 0.1 yalign 0.8
    ease 0.3 xalign 0.9 yalign 0.2
    ease 0.3 xalign 0.5 yalign 0.6
    repeat


# ------------------------------------------
# 2. LOGIKA MESIN MINIGAME (PYTHON)
# ------------------------------------------
init python:
    import random

    class FinalBossGame:
        def __init__(self):
            # Status Nyawa
            self.boss_hp = 3
            self.player_hp = 3
            
            # Posisi Jalur (0: Kiri, 1: Tengah, 2: Kanan)
            self.lane_positions = [0.2, 0.5, 0.8]
            self.raka_lane = 1
            
            # Menggunakan List untuk Target Boss (Bisa 1 atau 2 lane sekaligus)
            self.boss_target_lanes = []
            
            # Pengatur Status & Animasi
            self.state = "tutorial" 
            self.timer = 0.0
            
            # String penyimpan animasi yang sedang aktif
            self.boss_anim = "genderuwo_idle"
            self.raka_anim = "raka_back_idle"

        def start_game(self):
            # Dipanggil saat tombol MULAI di tutorial ditekan
            self.state = "idle"
            self.timer = 2.0
            renpy.restart_interaction()

        def tick(self):
            # Berjalan setiap 0.1 detik
            if self.state in ["win", "lose", "tutorial"]:
                return

            self.timer -= 0.1

            # ALUR LOGIKA BOSS
            if self.state == "idle" and self.timer <= 0:
                # Mulai fase ancang-ancang serangan
                self.boss_anim = "genderuwo_attack_anim" # Boss mulai menarik tangan
                
                # Boss selalu mengincar posisi Raka saat ini!
                if self.boss_hp == 1:
                    # FASE PAMUNGKAS: Serangan Ganda (Posisi Raka + 1 Jalur Random Lainnya)
                    available_lanes = [0, 1, 2]
                    available_lanes.remove(self.raka_lane)
                    second_lane = random.choice(available_lanes)
                    self.boss_target_lanes = [self.raka_lane, second_lane]
                else:
                    # FASE NORMAL: Hanya mengincar posisi Raka
                    self.boss_target_lanes = [self.raka_lane]
                
                self.state = "warning"
                # Waktu peringatan 0.6 detik + Waktu jatuh 0.4 detik = Total 1 Detik!
                self.timer = 0.6 

            elif self.state == "warning" and self.timer <= 0:
                # Waktu peringatan habis, Fireball Boss Jatuh!
                self.state = "boss_attack_fall"
                renpy.play("sfx_fire_burst.ogg", channel="sound")
                self.timer = 0.4 # Waktu fireball melesat turun

            elif self.state == "boss_attack_fall" and self.timer <= 0:
                # Fireball menghantam tanah, cek apakah mengenai Raka
                self.state = "attack_check"
                
                if self.raka_lane in self.boss_target_lanes:
                    # KENA SERANGAN
                    self.state = "player_hit"
                    self.player_hp -= 1
                    renpy.play("sfx_stab.ogg", channel="sound")
                    if self.player_hp <= 0:
                        self.timer = 1.0
                    else:
                        self.boss_anim = "genderuwo_warcry_anim" # Boss mengejek
                        self.timer = 1.5
                else:
                    # BERHASIL MENGHINDAR -> FASE CITRA MENAHAN (BIND)
                    self.state = "bind"
                    self.boss_anim = "genderuwo_terlilit_loop"
                    renpy.play("sfx_gema_suara_hantu.ogg", channel="sound")
                    self.timer = 2.5 # Waktu QTE Bimo melempar segel

            elif self.state == "bind" and self.timer <= 0:
                # GAGAL QTE: Bimo telat menembak, Boss lepas
                self.state = "idle"
                self.boss_anim = "genderuwo_lepas_ikatan"
                renpy.play("sfx_demonic_roar.ogg", channel="sound")
                self.timer = 2.0

            elif self.state == "bimo_attack" and self.timer <= 0:
                # Fireball selesai melesat, boss kena damage
                self.state = "boss_hit"
                self.boss_hp -= 1
                
                if self.boss_hp <= 0:
                    # Rangkaian Suara Kematian Boss (Antrean beruntun)
                    renpy.play("sfx_explosion.ogg", channel="sound")
                    renpy.music.queue("sfx_explosion_one.ogg", channel="sound")
                    renpy.music.queue("sfx_monster_died.ogg", channel="sound")
                    
                    self.boss_anim = "genderuwo_kalah_anim"
                    self.timer = 4.0
                else:
                    # Ledakan Biasa
                    renpy.play("sfx_explosion_one.ogg", channel="sound")
                    self.boss_anim = "genderuwo_terkena_ledakan"
                    self.timer = 3.0

            elif self.state == "boss_hit" and self.timer <= 0:
                if self.boss_hp <= 0:
                    self.state = "win"
                else:
                    # Boss memulihkan diri, kembali idle
                    self.state = "idle"
                    self.boss_anim = "genderuwo_idle"
                    renpy.play("sfx_demonic_growl.ogg", channel="sound")
                    self.timer = 2.0

            elif self.state == "player_hit" and self.timer <= 0:
                if self.player_hp <= 0:
                    self.state = "lose"
                else:
                    self.state = "idle"
                    self.boss_anim = "genderuwo_idle"
                    self.timer = 1.5
                    
            renpy.restart_interaction()

        # AKSI PEMAIN
        def move_left(self):
            if self.state in ["warning", "boss_attack_fall", "idle"] and self.raka_lane > 0:
                self.raka_lane -= 1
                self.raka_anim = "raka_dash_kiri"
                renpy.play("sfx_dashing.ogg", channel="sound")
                renpy.restart_interaction()

        def move_right(self):
            if self.state in ["warning", "boss_attack_fall", "idle"] and self.raka_lane < 2:
                self.raka_lane += 1
                self.raka_anim = "raka_dash_kanan"
                renpy.play("sfx_dashing.ogg", channel="sound")
                renpy.restart_interaction()

        def throw_seal(self):
            if self.state == "bind":
                # Tombol QTE Bimo ditekan
                self.state = "bimo_attack"
                self.timer = 0.5 # Waktu animasi fireball melesat
                renpy.play("sfx_magic_spell.ogg", channel="sound")
                renpy.restart_interaction()

# ------------------------------------------
# 3. SCREEN ANTARMUKA MINIGAME
# ------------------------------------------
screen mg_boss_renggo(game):
    modal True
    
    # Timer Utama Mesin Game
    timer 0.1 repeat True action Function(game.tick)
    
    # Pengecekan Akhir
    if game.state == "win":
        timer 0.5 action Return(True)
    elif game.state == "lose":
        timer 0.5 action Return(False)

    # 1. Background
    add "bg_lapangan_final"
    
    # 2. Sprite Boss (Ditarik ke atas agar tidak tertutup Raka)
    add game.boss_anim at napas_boss:
        xalign 0.5
        yalign 0.65 
    
    # Efek Layar Merah saat pemain terkena serangan
    if game.state == "player_hit":
        add "#ff000044"
        
    # Efek Fireball Bimo Melesat Naik
    if game.state == "bimo_attack":
        add "item_fireball" at lempar_fireball

    # 3. Warning Sign & Fireball Jatuh (Mengakomodasi Serangan Ganda)
    if game.state == "warning":
        for target_lane in game.boss_target_lanes:
            add "item_warning" at warning_kedip:
                xalign game.lane_positions[target_lane]
                yalign 0.5
            
    if game.state == "boss_attack_fall":
        # Proyektil jatuh mengarah ke jalur warning
        for target_lane in game.boss_target_lanes:
            add "item_fireball" at boss_fireball_fall(game.lane_positions[target_lane])

    # 4. Sprite Raka (Di layer depan/bawah, ditambatkan ke jalur posisinya)
    add game.raka_anim at raka_dash_move(game.lane_positions[game.raka_lane]):
        yalign 1.0

    # 5. UI: Indikator HP
    vbox:
        xalign 0.05 yalign 0.05 spacing 10
        text "HP RAKA: [game.player_hp]/3" size 35 color "#00ffcc" bold True outlines [(2, "#000", 0, 0)]
    
    vbox:
        xalign 0.95 yalign 0.05 spacing 10
        text "HP BOSS: [game.boss_hp]/3" size 35 color "#ff3333" bold True outlines [(2, "#000", 0, 0)]

    # 6. KONTROL PEMAIN (TOMBOL ARAH)
    if game.state in ["idle", "warning", "boss_attack_fall"]:
        # Tombol Menghindar Kiri & Kanan
        hbox:
            xalign 0.5 yalign 0.95 spacing 400
            imagebutton:
                idle Transform("tombol_kiri_idle", zoom=0.7)
                hover Transform("tombol_kiri_idle", zoom=0.7, matrixcolor=BrightnessMatrix(0.3))
                action Function(game.move_left)
                
            imagebutton:
                idle Transform("tombol_kanan_idle", zoom=0.7)
                hover Transform("tombol_kanan_idle", zoom=0.7, matrixcolor=BrightnessMatrix(0.3))
                action Function(game.move_right)
                
        # Dukungan Keyboard
        key "K_LEFT" action Function(game.move_left)
        key "K_RIGHT" action Function(game.move_right)

    # 7. QTE TARGET BERGERAK (BIMO & CITRA)
    elif game.state == "bind":
        
        # Logika pembagian kesulitan berdasarkan HP Boss yang tersisa
        if game.boss_hp == 3:
            # Serangan Pertama (Easy/Horizontal)
            vbox at target_bergerak_easy:
                text "LEMPAR SEGEL!" size 40 color "#ffff00" bold True xalign 0.5 outlines [(2, "#000", 0, 0)]
                imagebutton:
                    idle Transform("item_segel_hantu", zoom=1.2)
                    hover Transform("item_segel_hantu", zoom=1.3, matrixcolor=BrightnessMatrix(0.4))
                    action Function(game.throw_seal)
                    xalign 0.5
                    
        elif game.boss_hp == 2:
            # Serangan Kedua (Medium/Zigzag)
            vbox at target_bergerak_medium:
                text "LEMPAR SEGEL!" size 40 color "#ffff00" bold True xalign 0.5 outlines [(2, "#000", 0, 0)]
                imagebutton:
                    idle Transform("item_segel_hantu", zoom=1.2)
                    hover Transform("item_segel_hantu", zoom=1.3, matrixcolor=BrightnessMatrix(0.4))
                    action Function(game.throw_seal)
                    xalign 0.5
                    
        else:
            # Serangan Terakhir (Hard/Zigzag Cepat)
            vbox at target_bergerak_hard:
                text "LEMPAR SEGEL!" size 40 color "#ff0000" bold True xalign 0.5 outlines [(2, "#000", 0, 0)]
                imagebutton:
                    idle Transform("item_segel_hantu", zoom=1.2)
                    hover Transform("item_segel_hantu", zoom=1.3, matrixcolor=BrightnessMatrix(0.4))
                    action Function(game.throw_seal)
                    xalign 0.5

    # 8. LAYAR TUTORIAL (Paling Atas)
    if game.state == "tutorial":
        frame:
            xalign 0.5 yalign 0.5
            xpadding 50 ypadding 40
            background Solid("#000000dd")
            
            vbox:
                spacing 25
                xalign 0.5
                text "TUTORIAL FINAL BOSS" size 50 color "#ffaa00" bold True xalign 0.5
                
                text "{b}1. MENGHINDAR:{/b}\nJangan berdiri di tempat {color=#ff5555}Warning Sign{/color} karena serangan bola api akan jatuh di situ! Pindah jalur menggunakan panah/keyboard." size 28 color "#ffffff" text_align 0.5 xalign 0.5
                
                text "{b}2. MENYERANG:{/b}\nSerang Genderuwo dengan mengeklik/menekan tombol saat posisi hantu kecil ada tepat di atas tubuh Genderuwo!" size 28 color "#ffffff" text_align 0.5 xalign 0.5
                
                null height 20
                
                textbutton "MULAI PERTARUNGAN":
                    xalign 0.5
                    text_size 35 text_bold True text_color "#00ffcc"
                    action Function(game.start_game)

# ------------------------------------------
# 4. LABEL PEMICU
# ------------------------------------------
label play_final_boss:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Inisialisasi status game
    $ current_boss_game = FinalBossGame()
    
    # Memutar BGM Boss dengan SFX Roar pertama kali
    play music "bgm_05_otot_kawat.ogg" fadein 1.0
    play sound "sfx_demonic_roar.ogg"
    
    # Tampilkan UI Minigame
    call screen mg_boss_renggo(current_boss_game)
    
    if _return == True:
        # MENANG - Masuk ke Ending
        scene black with bangun_tidur
        "Tubuh Ki Renggo hancur tak bersisa. Teror di desa ini akhirnya benar-benar berakhir..."
        jump adegan_renggo_abu
    else:
        # KALAH - Game Over
        stop music fadeout 1.0
        scene black with flashmerah
        with vpunch
        "Pertahanan Trio hancur oleh amukan Genderuwo raksasa. Kesadaran mereka perlahan memudar dalam kegelapan..."
        centered "{size=+20}GAME OVER{/size}\n\nTrio Investigator tewas."
        return