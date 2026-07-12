# ==========================================
# PUSTAKA SCREEN INTRO CHAPTER KUSTOM
# ==========================================

# GAYA 1: Brutal / Pertumpahan Darah
screen intro_brutal(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            text nomor_act:
                size 85 bold True color "#8b0000" # Merah darah gelap
                drop_shadow (3, 3) drop_shadow_color "#000000" xalign 0.5
            text judul_act:
                size 40 italic True color "#ffffff"
                drop_shadow (2, 2) drop_shadow_color "#ff0000" xalign 0.5

# GAYA 2: Klasik Tradisional / Politis
screen intro_klasik(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 25
            text nomor_act:
                size 70 color "#e6e6e6" 
                outlines [ (2, "#000000", 0, 0) ] xalign 0.5
            text judul_act:
                size 45 italic True color "#cccccc"
                xalign 0.5

# GAYA 3: Taktis / Misi Rahasia (Anbu/Root)
screen intro_taktis(nomor_act, judul_act):
    frame:
        background None
        xalign 0.1 yalign 0.8 # Posisi di pojok kiri bawah (seperti log misi)
        vbox:
            spacing 5
            text "[ [nomor_act] ]":
                size 50 bold True color "#00ff00" # Hijau terminal/radar
            text "TARGET LOG: [judul_act]":
                size 30 color "#ffffff"

# GAYA 4: Memori / Tragedi Masa Lalu
screen intro_memori(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.4
        vbox:
            spacing 40
            text nomor_act:
                size 60 color "#ffffff" xalign 0.5
            text judul_act:
                size 35 italic True color "#a9d0f5" # Biru pucat
                xalign 0.5


# ==========================================
# MASTER PUSTAKA SCREEN INTRO MULTI-GENRE
# ==========================================

# ------------------------------------------
# GENRE 1: ACTION & COMBAT (Gaya 1 - 5)
# ------------------------------------------

# Gaya 1: Frontline / Medan Tempur 
screen intro_frontline(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            align (0.5, 0.5)
            text nomor_act:
                size 80 bold True color "#ff6600" # Warna oranye api/ledakan
                outlines [ (3, "#000000", 0, 0) ] xalign 0.5
            text judul_act:
                size 42 bold True color "#ffffff"
                outlines [ (2, "#ff0000", 1, 1) ] xalign 0.5 # Outline merah tegas

# Gaya 2: Cyber Overdrive 
screen intro_cyber(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            align (0.5, 0.5)
            text nomor_act:
                size 75 bold True color "#00ffff" # Cyan elektrik
                drop_shadow (3, 3) drop_shadow_color "#005555" xalign 0.5
            text judul_act:
                size 38 bold True color "#ffffff" xalign 0.5

# Gaya 3: Kinetic Slash 
screen intro_slash(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 5
            align (0.5, 0.5)
            text nomor_act:
                size 90 bold True italic True color "#ffffff" xalign 0.5
            text judul_act:
                size 45 bold True italic True color "#dd2222" xalign 0.5

# Gaya 4: Heavy Impact 
screen intro_impact(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            align (0.5, 0.5)
            text nomor_act:
                size 95 bold True color "#b0b0b0" xalign 0.5
                outlines [ (4, "#111111", 0, 0) ]
            text judul_act:
                size 40 bold True color "#ffffff" xalign 0.5

# Gaya 5: Tactical Drop / Angkatan Udara 
screen intro_tactical_drop(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.3
        vbox:
            spacing 8
            align (0.5, 0.5)
            text "--- DEPLOYMENT PROFILE ---":
                size 24 color "#aaaaaa" xalign 0.5
            text nomor_act:
                size 65 bold True color "#ffffff" xalign 0.5
            text "OPERATION: [judul_act]":
                size 34 color "#ffcc00" xalign 0.5


# ------------------------------------------
# GENRE 2: HORROR & THRILLER (Gaya 6 - 10)
# ------------------------------------------

# Gaya 6: Corrupted / Glitch Jiwa 
screen intro_corrupted(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 30
            align (0.5, 0.5)
            text nomor_act:
                size 70 bold True color "#444444" xalign 0.5 # Abu-abu mati
            text judul_act:
                size 45 color "#990000" xalign 0.5 # Merah tua pekat
                outlines [ (1, "#000000", 2, 2) ]

# Gaya 7: Deep Insanity 
screen intro_insanity(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 12
            align (0.5, 0.5)
            text nomor_act:
                size 65 color "#6a0dad" xalign 0.5 # Ungu aura gelap
                drop_shadow (4, 4) drop_shadow_color "#000000"
            text judul_act:
                size 40 italic True color "#ffffff" xalign 0.5

# Gaya 8: Bleeding Screen 
screen intro_bleeding(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.4
        vbox:
            spacing 10
            align (0.5, 0.5)
            text nomor_act:
                size 80 bold True color "#ffffff" xalign 0.5
                drop_shadow (2, 4) drop_shadow_color "#550000"
            text judul_act:
                size 42 bold True color "#ff0000" xalign 0.5

# Gaya 9: Cursed Relic / Kuno 
screen intro_relic(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            align (0.5, 0.5)
            text nomor_act:
                size 60 color "#cd7f32" xalign 0.5 # Warna perunggu tua
            text judul_act:
                size 38 italic True color "#d2b48c" xalign 0.5 # Warna kertas usang

# Gaya 10: Jump Panic 
screen intro_jump_panic(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 5
            align (0.5, 0.5)
            text nomor_act:
                size 110 bold True color "#ffffff" xalign 0.5
            text judul_act:
                size 50 bold True color "#000000" xalign 0.5
                outlines [ (2, "#ffffff", 0, 0) ]


# ------------------------------------------
# GENRE 3: DETECTIVE & SPIONASE (Gaya 11 - 15)
# ------------------------------------------

# Gaya 11: Classified Docs 
screen intro_classified(nomor_act, judul_act):
    frame:
        background None
        xalign 0.3 yalign 0.4 # Agak ke kiri atas seperti map berkas
        vbox:
            spacing 10
            text "[ CONFIDENTIAL ]":
                size 22 bold True color "#cc3333"
            text nomor_act:
                size 55 bold True color "#ffffff"
            text "CASE FILE: [judul_act]":
                size 32 color "#eeeeee"

# Gaya 12: Surveillance CCTV 
screen intro_surveillance(nomor_act, judul_act):
    frame:
        background None
        xalign 0.05 yalign 0.05 # Pojok kiri atas layar monitor
        vbox:
            spacing 4
            text "• REC OVERLAY 04":
                size 20 color "#ff0000"
            text nomor_act:
                size 45 color "#ffffff"
            text "LOC: [judul_act]":
                size 26 color "#00ff00" # Hijau teks monitor kuno

# Gaya 13: Radar Intelligence 
screen intro_intel_radar(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.75 # Di bawah tengah, menyerupai HUD radar
        vbox:
            spacing 5
            align (0.5, 0.5)
            text "--- SCANNING AREA ---":
                size 18 color "#00aa00" xalign 0.5
            text nomor_act:
                size 50 bold True color "#00ff00" xalign 0.5
            text "INTEL: [judul_act]":
                size 28 color "#ffffff" xalign 0.5

# Gaya 14: Noir Shadow 
screen intro_noir(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 25
            align (0.5, 0.5)
            text nomor_act:
                size 70 bold True color "#ffffff" xalign 0.5
            text judul_act:
                size 36 italic True color "#888888" xalign 0.5 

# Gaya 15: Decrypted Decodes 
screen intro_decrypted(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            align (0.5, 0.5)
            text ">> DECRYPTION SUCCESSFUL <<":
                size 20 color "#00ff00" xalign 0.5
            text nomor_act:
                size 60 bold True color "#ffffff" xalign 0.5
            text judul_act:
                size 35 color "#00ffff" xalign 0.5 


# ==========================================
# MASTER PUSTAKA SCREEN INTRO (PART 2)
# ==========================================

# ------------------------------------------
# GENRE 4: SLICE OF LIFE / KASUAL (Gaya 16 - 20)
# ------------------------------------------

# Gaya 16: Morning Journal (Buku Harian / Santai)
screen intro_journal(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            text nomor_act:
                size 65 italic True color "#5c4033" xalign 0.5 # Warna cokelat tinta
            text judul_act:
                size 35 italic True color "#8b4513" xalign 0.5

# Gaya 17: Spring Breeze (Hangat & Damai)
screen intro_breeze(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.4
        vbox:
            spacing 15
            text nomor_act:
                size 70 color "#ffb7c5" xalign 0.5 # Warna pink sakura
                outlines [ (1, "#ffffff", 0, 0) ]
            text "~ [judul_act] ~":
                size 38 color "#ffffff" xalign 0.5

# Gaya 18: Lazy Afternoon (Matahari Sore / Tidur Siang)
screen intro_afternoon(nomor_act, judul_act):
    frame:
        background None
        xalign 0.8 yalign 0.8 # Agak ke kanan bawah
        vbox:
            spacing 5
            text nomor_act:
                size 50 bold True color "#ffa500" xalign 1.0 # Oranye hangat
            text judul_act:
                size 28 color "#ffffe0" xalign 1.0

# Gaya 19: Bubble Pop (Ceria & Imut)
screen intro_bubble(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            text nomor_act:
                size 75 bold True color "#87ceeb" xalign 0.5 # Biru langit terang
                drop_shadow (2, 2) drop_shadow_color "#ffffff"
            text judul_act:
                size 40 color "#ffffff" xalign 0.5

# Gaya 20: Cozy Room (Malam yang Tenang)
screen intro_cozy(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            text nomor_act:
                size 55 color "#d3d3d3" xalign 0.5
            text judul_act:
                size 32 italic True color "#a9a9a9" xalign 0.5


# ------------------------------------------
# GENRE 5: DRAMA & ROMANCE (Gaya 21 - 25)
# ------------------------------------------

# Gaya 21: Melancholy Tears (Sedih / Patah Hati)
screen intro_melancholy(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 30
            text nomor_act:
                size 60 italic True color "#a4c8e1" xalign 0.5 # Biru pucat
            text judul_act:
                size 45 italic True color "#ffffff" xalign 0.5
                drop_shadow (1, 3) drop_shadow_color "#000033"

# Gaya 22: Fading Promise (Kenangan Memudar)
screen intro_promise(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.4
        vbox:
            spacing 15
            text nomor_act:
                size 70 color "#e0e0e0" xalign 0.5
                outlines [ (1, "#555555", 0, 0) ]
            text judul_act:
                size 35 italic True color "#cccccc" xalign 0.5

# Gaya 23: Shattered Trust (Konflik / Pengkhianatan)
screen intro_shattered(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            text nomor_act:
                size 85 bold True color "#ffffff" xalign 0.5
                drop_shadow (3, 3) drop_shadow_color "#444444"
            text judul_act:
                size 40 bold True italic True color "#888888" xalign 0.5

# Gaya 24: Burning Bridge (Amarah dalam Hubungan)
screen intro_burning_bridge(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            text nomor_act:
                size 75 bold True color "#b22222" xalign 0.5 # Merah bata/api
            text judul_act:
                size 38 italic True color "#ff8c00" xalign 0.5

# Gaya 25: Silent Monologue (Kesepian)
screen intro_monologue(nomor_act, judul_act):
    frame:
        background None
        xalign 0.2 yalign 0.5 # Merapat ke kiri
        vbox:
            spacing 20
            text nomor_act:
                size 50 color "#ffffff" xalign 0.0
            text judul_act:
                size 28 color "#888888" xalign 0.0


# ------------------------------------------
# GENRE 6: COMEDY & PARODY (Gaya 26 - 30)
# ------------------------------------------

# Gaya 26: Anime Episode Title (Ceria & Menggelegar)
screen intro_anime_ep(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            text "EPISODE [nomor_act] !" :
                size 80 bold True color "#ffff00" xalign 0.5 # Kuning terang
                outlines [ (3, "#ff0000", 2, 2) ] # Outline merah tebal
            text judul_act:
                size 45 bold True color "#ffffff" xalign 0.5
                outlines [ (2, "#0000ff", 1, 1) ]

# Gaya 27: Comic Book Pow! (Gaya Pop-art Konyol)
screen intro_comic(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.4
        vbox:
            spacing -5 # Dibuat mepet
            text nomor_act:
                size 90 bold True color "#ff1493" xalign 0.5 # Pink mencolok
                outlines [ (4, "#ffffff", 0, 0), (6, "#000000", 0, 0) ]
            text judul_act:
                size 40 bold True color "#00ff00" xalign 0.5
                outlines [ (2, "#000000", 0, 0) ]

# Gaya 28: System Error / Kekacauan Konyol (Slapstick)
screen intro_error(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            frame:
                background Solid("#ff0000") # Kotak merah diletakkan di frame
                padding (15, 5)
                xalign 0.5
                text "[ [nomor_act] - FATAL ERROR ]":
                    size 60 bold True color "#000000"
            text judul_act:
                size 35 color "#ffffff" xalign 0.5

# Gaya 29: Parody / Flashy (Gaya Ala Sinetron / Lebay)
screen intro_flashy(nomor_act, judul_act):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 25
            text "~ [nomor_act] ~":
                size 70 bold True italic True color "#ff69b4" xalign 0.5 # Hot pink
            text judul_act:
                size 45 bold True color "#00ced1" xalign 0.5

# Gaya 30: 4-Koma / Panel Singkat
screen intro_4koma(nomor_act, judul_act):
    frame:
        background None
        xalign 0.1 yalign 0.1 # Nempel di pojok kiri atas
        vbox:
            spacing 5
            frame:
                background Solid("#ffffff") # Kotak putih diletakkan di frame
                padding (10, 5)
                xalign 0.0
                text "# [nomor_act]":
                    size 40 bold True color "#333333"
            text judul_act:
                size 25 color "#ffffff" xalign 0.0