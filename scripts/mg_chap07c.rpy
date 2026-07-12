# ==========================================
# FILE: mg_chap07c.rpy
# MINIGAME: Segel Bimo (Mantra Sequence / Combo)
# STYLE: 16-Bit Retro RPG Magic Cast
# ==========================================

# ------------------------------------------
# ASET GAMBAR KHUSUS MINIGAME 7C
# ------------------------------------------
image cg_mg_chap07c_starting_game = "images/cg/cg_mg_chap07c_starting_game.webp"
image bg_mg_chap07c = "images/bg/bg_mg_chap07c.webp"
image cg_mg_chap07c_bimo_menang = "images/cg/cg_mg_chap07c_bimo_menang.webp"
image cg_mg_chap07c_bimo_kalah = "images/cg/cg_mg_chap07c_bimo_kalah.webp"

# ------------------------------------------
# LOGIKA MESIN MINIGAME (PYTHON)
# ------------------------------------------
init python:
    import random

    class MgSegelMantra:
        def __init__(self):
            self.buttons = ["up", "down", "left", "right", "act"]
            self.total_stages = 3
            self.current_stage = 1
            
            # Waktu batas merapal mantra (total)
            self.time_left = 15.0
            self.state = "playing" # "playing", "win", "lose"
            
            # Target urutan mantra (Kombinasi tombol)
            self.target_sequence = []
            self.player_sequence = []
            
            self.generate_sequence()

        def generate_sequence(self):
            # Tingkat kesulitan bertambah: Tahap 1 (4 tombol), Tahap 2 (5 tombol), Tahap 3 (6 tombol)
            seq_length = 3 + self.current_stage
            self.target_sequence = [random.choice(self.buttons) for _ in range(seq_length)]
            self.player_sequence = []

        def update(self):
            if self.state != "playing": 
                return
            
            # Timer berjalan terus
            self.time_left -= 0.05
            if self.time_left <= 0:
                self.state = "lose"
            
            renpy.restart_interaction()

        def press(self, btn_id):
            if self.state != "playing": 
                return
            
            # Index tombol yang sedang ditekan
            current_index = len(self.player_sequence)
            
            # Mengecek apakah tombol yang ditekan sesuai urutan target
            if btn_id == self.target_sequence[current_index]:
                renpy.play("sfx_suara_ting.ogg", channel="sound")
                self.player_sequence.append(btn_id)
                
                # Cek apakah seluruh urutan di stage ini sudah selesai
                if len(self.player_sequence) == len(self.target_sequence):
                    renpy.play("sfx_correct.ogg", channel="sound")
                    self.current_stage += 1
                    
                    if self.current_stage > self.total_stages:
                        self.state = "win"
                    else:
                        # Tambah sedikit waktu bonus dan buat urutan baru
                        self.time_left += 3.0
                        self.generate_sequence()
            else:
                # Jika SALAH TEKAN: Mantra gagal, harus ulang dari awal urutan stage ini!
                renpy.play("sfx_insting_salah.ogg", channel="sound")
                self.player_sequence = []
                
            renpy.restart_interaction()


# ------------------------------------------
# SCREEN MINIGAME SEGEL MANTRA
# ------------------------------------------
screen mg_chap07c_segel():
    modal True

    # Instance mesin minigame
    default segel = MgSegelMantra()

    # Timer utama
    timer 0.05 repeat True action Function(segel.update)

    # Deteksi menang/kalah
    if segel.state == "win":
        timer 0.2 action Return(True)
    elif segel.state == "lose":
        timer 0.2 action Return(False)

    # Background menggunakan aset asli
    add "bg_mg_chap07c"
    add "#0000ff22" # Overlay biru aura magis yang sangat tipis agar membaur dengan BG

    # -- UI Tampilan Atas --
    vbox:
        xalign 0.5 yalign 0.1 spacing 15
        text "MINIGAME: SEGEL GAIB" size 40 color "#00ffff" bold True xalign 0.5 outlines [ (2, "#000000", 0, 0) ]
        text "TEKAN TOMBOL SESUAI URUTAN MANTRA!" size 25 color "#ffffff" bold True xalign 0.5 outlines [ (2, "#000000", 0, 0) ]
        
        hbox:
            spacing 50 xalign 0.5
            text "TAHAP: [segel.current_stage]/[segel.total_stages]" size 35 color "#00ff00" bold True outlines [ (2, "#000000", 0, 0) ]
            text "WAKTU: [segel.time_left:.1f]s" size 35 color "#ff0000" bold True outlines [ (2, "#000000", 0, 0) ]

    # -- TAMPILAN URUTAN MANTRA (TARGET & PROGRESS) --
    vbox:
        xalign 0.5 yalign 0.35 spacing 20
        
        # Baris Urutan yang harus ditekan
        hbox:
            spacing 15 xalign 0.5
            for i, btn in enumerate(segel.target_sequence):
                # Membedakan tampilan: sudah ditekan vs belum ditekan
                if i < len(segel.player_sequence):
                    # Sudah ditekan (Menyala / Terang)
                    add "button_" + btn zoom 0.5 matrixcolor BrightnessMatrix(0.5)
                else:
                    # Belum ditekan (Gelap / Normal)
                    add "button_" + btn zoom 0.5 matrixcolor BrightnessMatrix(-0.3)

    # -- VIRTUAL GAMEPAD (TOMBOL KONTROL) --
    hbox:
        xalign 0.5 yalign 0.8 spacing 100
        
        # D-PAD (Kiri, Atas, Bawah, Kanan)
        grid 3 3:
            spacing 10
            null
            imagebutton:
                idle Transform("button_up", zoom=0.5)
                hover Transform("button_up", zoom=0.5, matrixcolor=BrightnessMatrix(0.3))
                action Function(segel.press, "up")
            null
            
            imagebutton:
                idle Transform("button_left", zoom=0.5)
                hover Transform("button_left", zoom=0.5, matrixcolor=BrightnessMatrix(0.3))
                action Function(segel.press, "left")
            null
            imagebutton:
                idle Transform("button_right", zoom=0.5)
                hover Transform("button_right", zoom=0.5, matrixcolor=BrightnessMatrix(0.3))
                action Function(segel.press, "right")
                
            null
            imagebutton:
                idle Transform("button_down", zoom=0.5)
                hover Transform("button_down", zoom=0.5, matrixcolor=BrightnessMatrix(0.3))
                action Function(segel.press, "down")
            null

        # TOMBOL AKSI (Pukul/Rapal)
        vbox:
            yalign 0.5
            imagebutton:
                idle Transform("button_act", zoom=0.55)
                hover Transform("button_act", zoom=0.55, matrixcolor=BrightnessMatrix(0.3))
                action Function(segel.press, "act")
                
    text "JIKA SALAH TEKAN, MANTRA AKAN DIULANG DARI AWAL!" size 20 color "#ffaaaa" xalign 0.5 yalign 0.98 outlines [ (2, "#000000", 0, 0) ]

    # -- DUKUNGAN KEYBOARD --
    key "K_UP" action Function(segel.press, "up")
    key "K_DOWN" action Function(segel.press, "down")
    key "K_LEFT" action Function(segel.press, "left")
    key "K_RIGHT" action Function(segel.press, "right")
    key "K_SPACE" action Function(segel.press, "act")


# ==========================================
# LABEL PEMICU SCENE SEGEL MANTRA
# ==========================================
label play_mg_chap07c:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Intro Scene
    scene cg_mg_chap07c_starting_game with flash_biru
        
    "Bimo memutar tasbih kayunya dan mulai menyusun simbol-simbol gaib di udara. Ia harus merangkai urutan mantra gaib tanpa celah."

    # Panggil Minigame
    call screen mg_chap07c_segel
    
    if _return == True:
        # MENANG
        stop sound fadeout 0.5
        play sound "sfx_massive_energy_show.ogg"
        
        scene cg_mg_chap07c_bimo_menang with flashbang
        with hpunch
        
        b "{i}DENGAN NAMA ALLAH PENCIPTA ALAM SEMESTA DAN NUR MUHAMMAD SANG PENERANG, KEMBALILAH KAU KE TEMPAT ASALMU! SEGEL CAHAYA!!{/i}"
        
        play sound "sfx_demonic_roar.ogg"
        "Cahaya biru terang berpendar dari tangan Bimo, membentuk perisai energi yang menghantam wujud raksasa gaib tersebut."
        "Entitas itu menjerit memekakkan telinga sebelum akhirnya terdorong mundur dan lenyap tertiup angin, menyisakan kepulan asap berbau menyan."
        
        return True
        
    else:
        # KALAH
        stop sound fadeout 0.5
        
        b "{i}KEMBALILAH... Ukh! Sial, konsentrasiku pecah!{/i}"
        
        play sound "sfx_glass_shatter.ogg"
        scene cg_mg_chap07c_bimo_kalah with flashmerah
        with vpunch
        
        "Segel pelindung Bimo retak dan hancur berantakan. Entitas itu mengamuk, menghempaskan Bimo dan Citra dengan kekuatan penuh hingga membentur dinding."
        
        with hpunch
        play sound "sfx_flesh_tear_heavy.ogg"
        "Bimo memuntahkan darah segar, tasbihnya terputus dan berhamburan ke lantai. Pertahanan terakhir mereka telah rubuh."
        
        scene black with pingsan
        play sound "sfx_game_over.ogg"
        centered "{size=+20}GAME OVER{/size}\n\nGagal merangkai urutan mantra gaib, berujung pada Kematian Bimo"
        return False