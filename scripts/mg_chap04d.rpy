# ==========================================
# FILE: mg_chap04d.rpy
# MINIGAME: Menahan Bisikan Kematian (Fokus Citra)
# MEKANIK: Rhythm Focus / Timing Tapping
# ==========================================

# ------------------------------------------
# ASET GAMBAR MINIGAME
# ------------------------------------------
# Catatan: Siapkan dua gambar lingkaran transparan (format PNG/WEBP) di folder images/item/
image mg_ring_base = "images/item/ring_base.webp"     # Cincin target (diam)
image mg_ring_moving = "images/item/ring_moving.webp" # Cincin gelombang yang mengecil

init python:
    class JenglotRadarGame:
        def __init__(self):
            self.hits_needed = 3
            self.current_hits = 0
            self.sanity = 3 # Kesempatan salah / nyawa Citra
            
            self.ring_scale = 3.5 # Ukuran awal gelombang merah (sangat besar)
            self.shrink_speed = 0.04 # Kecepatan mengecil (makin tinggi makin cepat)
            
            self.status = "playing"
            self.msg = "FOKUS! Tahan bisikan itu!"
            self.msg_color = "#ffffff"

        def update(self):
            if self.status != "playing":
                return
                
            # Mengecilkan cincin secara bertahap
            self.ring_scale -= self.shrink_speed
            
            # Jika cincin terlewat mengecil (kurang dari ukuran 0.6) = GAGAL / MISS
            if self.ring_scale < 0.6:
                self.miss("TERLEWAT!")

        def tap(self):
            if self.status != "playing":
                return
                
            # Area Timing yang Pas (Toleransi skala 0.85 sampai 1.25)
            if 0.85 <= self.ring_scale <= 1.35:
                self.hit()
            else:
                self.miss("TIMING SALAH!")

        def hit(self):
            # Berhasil menekan tepat waktu
            renpy.play("sfx_chime_one.ogg")
            self.current_hits += 1
            self.ring_scale = 3.5 # Reset ke ukuran awal
            
            # Setiap berhasil, kecepatan akan sedikit bertambah (makin sulit)
            self.shrink_speed += 0.005
            
            self.msg = "TEPAT!"
            self.msg_color = "#00ffcc"
            
            if self.current_hits >= self.hits_needed:
                self.status = "win"

        def miss(self, reason):
            # Gagal menahan fokus
            renpy.play("sfx_glitch_mumble.ogg")
            renpy.play("sfx_insting_salah.ogg")
            self.sanity -= 1
            self.ring_scale = 3.5 # Reset ke ukuran awal
            
            self.msg = reason
            self.msg_color = "#ff3333"
            
            if self.sanity <= 0:
                self.status = "lose"


# ------------------------------------------
# SCREEN UI MINIGAME RHYTHM
# ------------------------------------------
screen mg_jenglot_radar():
    modal True
    
    default game = JenglotRadarGame()
    
    # Timer utama untuk pergerakan cincin (berjalan 60 fps / 0.016 detik)
    timer 0.016 action Function(game.update) repeat True
    
    # Background gelap dengan efek kabut untuk suasana mistis
    add "bg_padepokan_dalam"
    add "kabut_tipis" # Dari pustaka cuaca
    add "#220000bb"   # Lapisan merah gelap berdarah
    
    # Tombol raksasa memenuhi layar agar mudah ditap di HP
    button:
        xysize (config.screen_width, config.screen_height)
        action Function(game.tap)
        
    # Pintasan keyboard PC
    key "K_SPACE" action Function(game.tap)
    key "K_RETURN" action Function(game.tap)

    # ==========================
    # HUD & INFORMASI
    # ==========================
    vbox:
        xalign 0.5 ypos 50
        spacing 15
        
        text "FOKUS BATIN CITRA" size 36 color "#ffcc00" xalign 0.5 bold True
        text "Ketuk Layar / Tekan SPASI tepat saat Cincin Merah menyentuh Garis Putih!" size 18 color "#cccccc" xalign 0.5
        text game.msg size 28 color game.msg_color xalign 0.5 bold True
        
        null height 20
        
        hbox:
            xalign 0.5 spacing 100
            # Indikator Sukses
            vbox:
                xalign 0.5
                text "KONSENTRASI" size 16 color "#ffffff" xalign 0.5
                text "[game.current_hits] / [game.hits_needed]" size 32 color "#00ffcc" xalign 0.5 bold True
            
            # Indikator Nyawa / Kewarasan
            vbox:
                xalign 0.5
                text "KEWARASAN" size 16 color "#ffffff" xalign 0.5
                text "[game.sanity]" size 32 color "#ff3333" xalign 0.5 bold True

    # ==========================
    # AREA VISUAL CINCIN TARGET
    # ==========================
    # Cincin Diam (Target putih)
    add "mg_ring_base":
        xalign 0.5 yalign 0.5
        zoom 1.0
        
    # Cincin Mengecil (Gelombang merah yang datang)
    add "mg_ring_moving":
        xalign 0.5 yalign 0.5
        # Transformasi dinamis ukurannya berdasarkan variabel game.ring_scale
        zoom game.ring_scale

    # Cek Kondisi Menang/Kalah
    if game.status == "win":
        timer 0.1 action Return("win")
    elif game.status == "lose":
        timer 0.1 action Return("lose")


# ------------------------------------------
# LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap04_jenglot:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Transisi Masuk ke Pikiran Citra
    stop music fadeout 2.0
    play sound "sfx_tinnitus.ogg"
    scene black with transisi_asap
    
    play music "bgm_10_fokus_spiritual.ogg" fadein 1.5 loop
    play sound "sfx_detak_jantung.ogg" loop
    
    show citra_lelah at center with dissolve_kilat
    c "Ukh... bau anyir ini... kepalaku mulai pusing..."
    c "(Ada suara bisikan yang kuat sekali dari arah lantai kayu itu. Aku harus fokus untuk membongkar ilusi ini!)"
    hide citra_lelah

    # Memanggil screen minigame
    window hide
    call screen mg_jenglot_radar
    
    # Hentikan suara tegang
    stop sound fadeout 1.0
    
    if _return == "win":
        # JIKA BERHASIL MENEKAN RITME
        $ citra_resonansi_gaib = getattr(store, "citra_resonansi_gaib", 0) + 1
        play sound "sfx_petunjuk_datang.ogg"
        scene bg_padepokan_dalam with flashbang
        
        show citra_lega at center with dissolve_kilat
        c "Dapat! Sumber hawanya ada di balik papan kayu yang ini!"
        hide citra_lega
        
        "Citra berhasil menembus ilusi pelindung gaib yang menutupi kotak rahasia Ki Renggo."
        $ ch4_jenglot_tua = True
        play sound "sfx_creaky_door_open.ogg"
        "Citra perlahan membongkar papan kayu yang berdebu tersebut..."
                
                # --- CUT SCENE 6: Boneka Jenglot Tua ---
        scene cg_ch04_jenglot_tua with transisi_asap
        play sound "sfx_eerie.ogg"
        "Di dalamnya terdapat sebuah Boneka Jenglot berambut panjang yang sudah sangat tua dan mengering. Mata boneka itu seolah menatap tajam ke arah Citra, memancarkan hawa pembunuhan yang pekat."

        scene bg_padepokan_dalam with dissolve
        show renggo_panik at center with tv_rusak
        kr "J-jangan sentuh itu, Neng! Itu bukan punya saya! Itu benda celaka peninggalan orang yang nyuruh Bu Dokter!"
        hide renggo_panik
        return "win"
        
    elif _return == "lose":
        # JIKA GAGAL DAN KEHILANGAN KEWARASAN
        $ citra_resonansi_gaib = getattr(store, "citra_resonansi_gaib", 0) - 1
        stop music fadeout 1.0
        play sound "sfx_game_over_2.ogg"
        
        # Efek visual Citra kesakitan / Horor
        scene bg_padepokan_dalam with tv_rusak
        show citra_panik at center with mata_mengerjap
        play sound "sfx_teriakan_takut.ogg"
        
        c "KYAAA! SUARANYA TERLALU JELAS!"
        
        show raka_panik at center with dorong_kiri
        r "Citra?! Lu kenapa? Tiba-tiba teriak!"
        hide raka_panik
        
        show citra_lelah at center with dissolve_kilat
        c "M-maaf Kak... Kepalaku mendadak pusing banget. Aku ngerasa ada hawa jahat, tapi pas aku coba fokus, bisikannya malah nyerang balik."
        hide citra_lelah
        
        "Pikiran Citra terlalu lelah untuk menembus pertahanan gaib benda tersebut. Trio Investigator kehilangan kesempatan untuk menemukan benda rahasia yang dikubur Ki Renggo."
        

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP04_JENGLOT SELESAI")
    # -----------------------------------
    return