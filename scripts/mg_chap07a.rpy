# ==========================================
# FILE: mg_chap07a.rpy
# MINIGAME: Brawl 4v4 (Tag-Team QTE)
# STYLE: 16-Bit Retro Arcade Beat 'em Up
# ==========================================

# ------------------------------------------
# DEFINISI GAMBAR KHUSUS MINIGAME 7A
# ------------------------------------------
image cg_chap07_raka_tendang_penjahat = "images/cg/cg_chap07_raka_tendang_penjahat.webp"
image cg_mg_chap07a_combo_winning = "images/cg/cg_mg_chap07a_combo_winning.webp"
image cg_mg_chap07a_kalah = "images/cg/cg_mg_chap07a_kalah.webp"
image cg_mg_chap07a_menang = "images/cg/cg_mg_chap07a_menang.webp"
image cg_mg_chap07a_pov_gatot = "images/cg/cg_mg_chap07a_pov_gatot.webp"
image cg_mg_chap07a_pov_raka = "images/cg/cg_mg_chap07a_pov_raka.webp"

# ------------------------------------------
# LOGIKA MESIN MINIGAME (PYTHON)
# ------------------------------------------
init python:
    class MgBrawlQTE:
        def __init__(self):
            self.rounds = 5 # Total serangan yang harus dihindari/dibalas
            self.current_round = 1
            
            # Waktu perlahan akan semakin cepat setiap ronde
            self.max_time = 3.0
            self.time_left = 3.0
            self.state = "playing" # "playing", "win", atau "lose"
            
            # Daftar kemungkinan serangan (Instruksi, ID Tombol, Ikon Tombol, Gambar BG Dinamis)
            self.prompts = [
                ("PREMAN MENGAYUNKAN PARANG!\nMENGHINDAR KE BAWAH!", "down", "button_down", "cg_mg_chap07a_pov_raka"),
                ("SERANGAN RANTAI DARI SAMPING!\nTANGKIS KE KIRI!", "left", "button_left", "cg_mg_chap07a_pov_raka"),
                ("PREMAN MENENDANG!\nMENGHINDAR KE KANAN!", "right", "button_right", "cg_mg_chap07a_pov_gatot"),
                ("CELAH TERBUKA!\nLOMPAT KE ATAS!", "up", "button_up", "cg_mg_chap07a_pov_gatot"),
                ("GATOT MENAHAN PREMAN!\nTENDANG SEKARANG!", "act", "button_act", "cg_chap07_raka_tendang_penjahat")
            ]
            
            # Mengacak urutan serangan setiap kali main
            renpy.random.shuffle(self.prompts)
            
            # Mengambil serangan pertama
            self.current_prompt = self.prompts[0][0]
            self.current_target = self.prompts[0][1]
            self.current_icon = self.prompts[0][2]
            self.current_bg = self.prompts[0][3]

        def update_time(self):
            if self.state == "playing":
                self.time_left -= 0.05
                if self.time_left <= 0:
                    self.state = "lose"
                    renpy.play("sfx_flesh_tear.ogg", channel="sound")
                renpy.restart_interaction()

        def click_btn(self, btn):
            if self.state != "playing": 
                return
                
            if btn == self.current_target:
                # Jika BENAR: Lanjut ronde
                renpy.play("sfx_punch.ogg", channel="sound")
                
                # Opsional: Bunyi swoosh tanda adegan berganti
                renpy.play("sfx_fast_swoosh.ogg", channel="audio")
                
                self.current_round += 1
                
                if self.current_round > self.rounds:
                    self.state = "win"
                else:
                    # Mempercepat waktu setiap ronde agar makin menantang
                    self.max_time = max(1.0, 3.0 - (self.current_round * 0.4))
                    self.time_left = self.max_time
                    
                    # Memuat serangan berikutnya dan mengganti Background
                    self.current_prompt = self.prompts[self.current_round - 1][0]
                    self.current_target = self.prompts[self.current_round - 1][1]
                    self.current_icon = self.prompts[self.current_round - 1][2]
                    self.current_bg = self.prompts[self.current_round - 1][3]
            else:
                # Jika SALAH TEKAN: Langsung kalah
                self.state = "lose"
                renpy.play("sfx_flesh_tear_heavy.ogg", channel="sound")
                
            renpy.restart_interaction()


# ------------------------------------------
# SCREEN MINIGAME BRAWL QTE
# ------------------------------------------
screen mg_chap07a_brawl():
    modal True

    # Membuat instance logika minigame
    default brawl = MgBrawlQTE()

    # -- Timer Utama --
    timer 0.05 repeat True action Function(brawl.update_time)

    # -- Pengecekan Menang/Kalah Otomatis --
    if brawl.state == "win":
        timer 0.2 action Return(True)
    elif brawl.state == "lose":
        timer 0.2 action Return(False)

    # Background yang berubah-ubah secara dinamis sesuai aksi (POV Gatot/Raka)
    add brawl.current_bg
    add "#ff000033" # Overlay merah tipis agar terasa tegang

    # -- HUD INSTRUKSI & TIMER --
    vbox:
        xalign 0.5 yalign 0.15 spacing 15
        
        # Teks Status
        text "RONDE: [brawl.current_round] / [brawl.rounds]" size 35 color "#00ff00" bold True xalign 0.5 outlines [ (2, "#000000", 0, 0) ]
        
        # Teks Instruksi Serangan (Otomatis berubah)
        text "[brawl.current_prompt]" size 45 color "#ffffff" bold True text_align 0.5 xalign 0.5 outlines [ (3, "#000000", 0, 0) ]
        
        # Ikon Bantuan Visual
        add brawl.current_icon zoom 0.4 xalign 0.5
        
        # Bar Timer Bergerak
        frame:
            xalign 0.5
            xsize 600 ysize 30
            background "#333333"
            frame:
                xsize int((brawl.time_left / brawl.max_time) * 600) ysize 30
                background "#ff0000"

    # -- VIRTUAL GAMEPAD (TOMBOL KONTROL) --
    hbox:
        xalign 0.5 yalign 0.85 spacing 100
        
        # D-PAD (Kiri, Atas, Bawah, Kanan)
        grid 3 3:
            spacing 10
            null
            imagebutton:
                idle Transform("button_up", zoom=0.5)
                hover Transform("button_up", zoom=0.5, matrixcolor=BrightnessMatrix(0.3))
                action Function(brawl.click_btn, "up")
            null
            
            imagebutton:
                idle Transform("button_left", zoom=0.5)
                hover Transform("button_left", zoom=0.5, matrixcolor=BrightnessMatrix(0.3))
                action Function(brawl.click_btn, "left")
            null
            imagebutton:
                idle Transform("button_right", zoom=0.5)
                hover Transform("button_right", zoom=0.5, matrixcolor=BrightnessMatrix(0.3))
                action Function(brawl.click_btn, "right")
                
            null
            imagebutton:
                idle Transform("button_down", zoom=0.5)
                hover Transform("button_down", zoom=0.5, matrixcolor=BrightnessMatrix(0.3))
                action Function(brawl.click_btn, "down")
            null

        # TOMBOL AKSI (Pukul/Tendang)
        vbox:
            yalign 0.5
            imagebutton:
                idle Transform("button_act", zoom=0.55)
                hover Transform("button_act", zoom=0.55, matrixcolor=BrightnessMatrix(0.3))
                action Function(brawl.click_btn, "act")
                
    text "TEKAN TOMBOL DI LAYAR ATAU ARAH KEYBOARD!" size 25 color "#cccccc" xalign 0.5 yalign 0.98 outlines [ (2, "#000000", 0, 0) ]

    # -- DUKUNGAN KEYBOARD --
    key "K_UP" action Function(brawl.click_btn, "up")
    key "K_DOWN" action Function(brawl.click_btn, "down")
    key "K_LEFT" action Function(brawl.click_btn, "left")
    key "K_RIGHT" action Function(brawl.click_btn, "right")
    key "K_SPACE" action Function(brawl.click_btn, "act")


# ==========================================
# LABEL PEMICU SCENE BRAWL 4v4
# ==========================================
label play_mg_chap07a:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Memanggil Minigame
    call screen mg_chap07a_brawl
    
    if _return == False:
        # KALAH MINIGAME (Waktu Habis / Salah Tombol)
        stop music fadeout 0.5
        play sound "sfx_flesh_tear_heavy.ogg"
        scene cg_mg_chap07a_kalah with flashmerah
        with hpunch
        
        "Raka salah memperhitungkan serangan. Rantai besi preman itu menghantam keras rahangnya dan Gatot secara bersamaan!"
        
        scene black with pingsan
        "Keduanya tersungkur tak berdaya dengan wajah bersimbah darah. Tanpa perlawanan mereka, Bimo dan Citra dengan cepat dihabisi oleh anak buah Tirto."
        
        play sound "sfx_game_over_hancur_8bit.ogg"
        centered "{size=+20}GAME OVER{/size}\n\nGagal menangkis serangan preman bayaran Tirto."
        return False
        
    # MENANG MINIGAME
    play sound "sfx_punch.ogg"
    play sound "sfx_barang_berat_jatuh.ogg"
    
    # Transisi aksi combo yang mulus
    scene cg_mg_chap07a_combo_winning with transisi_tebasan
    pause 0.5
    
    scene cg_mg_chap07a_menang with flash_hijau
    with vpunch
    
    "BAK! BUK!"
    "Kombinasi pukulan telak Gatot dan tendangan memutar Raka berhasil menumbangkan ketiga preman tersebut hingga terkapar tak sadarkan diri."

    show raka_lega at left with dissolve_kilat
    r "Hah... hah... Selesai juga kroco-kroconya."

    show tirto_panik at right with vpunch
    t "M-mundur kalian! Saya ini Kepala Desa! Aparat akan menghukum kalian!"
    $ poin_investigasi += 1
    show gatot_marah at left with hpunch
    g "Hukum kepala bapak kau! Malam ini lu mati, Tirto!"
    
    hide gatot_marah
    hide raka_lega
    hide tirto_panik
    

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP07A SELESAI")
    # -----------------------------------
    return True