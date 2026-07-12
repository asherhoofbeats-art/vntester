# ==========================================
# PUSTAKA SCREEN OUTRO CHAPTER KUSTOM
# Simpan di file: pustaka_outro.rpy
# ==========================================

# ------------------------------------------
# GENRE 1: ACTION / NINJA / TACTICAL
# ------------------------------------------

# Gaya 1: Mission Complete (Gaya Laporan Intel)
screen outro_mission(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            align (0.5, 0.5)
            text "--- [nomor_act] CONCLUDED ---":
                size 50 bold True color "#00ff00" xalign 0.5
            text "STATUS: [pesan_outro]":
                size 30 color "#ffffff" xalign 0.5

# Gaya 2: Blood Spilled (Akhir yang brutal/berdarah)
screen outro_blood(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            align (0.5, 0.5)
            text "[nomor_act]":
                size 70 bold True color "#8b0000" xalign 0.5
                drop_shadow (3, 3) drop_shadow_color "#000000"
            text pesan_outro:
                size 35 italic True color "#ff4444" xalign 0.5

# Gaya 3: Fading Ember (Sisa-sisa pertempuran)
screen outro_ember(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            align (0.5, 0.5)
            text "[nomor_act]":
                size 65 bold True color "#ff8c00" xalign 0.5
                outlines [ (2, "#000000", 0, 0) ]
            text pesan_outro:
                size 30 color "#888888" xalign 0.5

# Gaya 4: Scroll Sealed (Gaya Gulungan Ninja Tradisional)
screen outro_scroll(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            align (0.5, 0.5)
            text "[nomor_act]":
                size 60 color "#d2b48c" xalign 0.5 # Warna perkamen/kertas kuno
            text "- [pesan_outro] -":
                size 35 italic True color "#ffffff" xalign 0.5

# Gaya 5: Cliffhanger Strike (Tebasan di akhir cerita)
screen outro_cliffhanger(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 5
            align (0.5, 0.5)
            text "[nomor_act]":
                size 80 bold True italic True color "#ffffff" xalign 0.5
            text pesan_outro:
                size 45 bold True italic True color "#dd2222" xalign 0.5


# ------------------------------------------
# GENRE 2: HORROR / THRILLER / DARK
# ------------------------------------------

# Gaya 6: Nightmare Pauses (Jeda mimpi buruk)
screen outro_nightmare(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            align (0.5, 0.5)
            text "[nomor_act]":
                size 70 bold True color "#4b0082" xalign 0.5 # Ungu gelap
                drop_shadow (4, 4) drop_shadow_color "#000000"
            text pesan_outro:
                size 35 color "#a9a9a9" xalign 0.5

# Gaya 7: Tape Stopped (Rekaman berakhir)
screen outro_vhs(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.1 yalign 0.9 # Di pojok kiri bawah
        vbox:
            spacing 5
            text "STOP ■":
                size 40 bold True color "#ffffff"
            text "[nomor_act] - [pesan_outro]":
                size 25 color "#cccccc"

# Gaya 8: Dead End (Kematian/Bad Ending)
screen outro_dead_end(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            align (0.5, 0.5)
            text "[nomor_act]":
                size 90 bold True color "#000000" xalign 0.5
                outlines [ (3, "#ff0000", 0, 0) ]
            text pesan_outro:
                size 40 bold True color "#ff0000" xalign 0.5

# Gaya 9: Whispers Fade (Suara-suara menghilang)
screen outro_whispers(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            align (0.5, 0.5)
            text "[nomor_act]":
                size 55 color "#555555" xalign 0.5
            text pesan_outro:
                size 28 italic True color "#333333" xalign 0.5

# Gaya 10: You Survived (Bertahan hidup sementara)
screen outro_survived(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.4
        vbox:
            spacing 25
            align (0.5, 0.5)
            text "[nomor_act]":
                size 65 color "#ffffff" xalign 0.5
                drop_shadow (2, 2) drop_shadow_color "#ffffff"
            text pesan_outro:
                size 30 color "#888888" xalign 0.5


# ------------------------------------------
# GENRE 3: DRAMA / ROMANCE / EMOTIONAL
# ------------------------------------------

# Gaya 11: Tears Dry (Kesedihan yang mereda)
screen outro_tears(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 30
            align (0.5, 0.5)
            text "[nomor_act]":
                size 60 italic True color "#a4c8e1" xalign 0.5
            text pesan_outro:
                size 40 italic True color "#ffffff" xalign 0.5

# Gaya 12: Promise Kept (Harapan/Janji manis)
screen outro_promise(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            align (0.5, 0.5)
            text "[nomor_act]":
                size 70 color "#ffb6c1" xalign 0.5 # Pink lembut
            text pesan_outro:
                size 35 color "#ffffff" xalign 0.5

# Gaya 13: Shattered Bonds (Perpisahan/Konflik)
screen outro_shattered(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            align (0.5, 0.5)
            text "[nomor_act]":
                size 75 bold True color "#ffffff" xalign 0.5
                drop_shadow (2, 2) drop_shadow_color "#555555"
            text pesan_outro:
                size 35 bold True italic True color "#888888" xalign 0.5

# Gaya 14: Sunset Farewell (Matahari terbenam)
screen outro_sunset(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            align (0.5, 0.5)
            text "[nomor_act]":
                size 65 bold True color "#ffa07a" xalign 0.5 
            text pesan_outro:
                size 32 italic True color "#ffffe0" xalign 0.5

# Gaya 15: Diary Closed (Menutup buku harian)
screen outro_diary(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            align (0.5, 0.5)
            text "[nomor_act]":
                size 55 italic True color "#8b4513" xalign 0.5 # Cokelat
            text pesan_outro:
                size 30 italic True color "#a0522d" xalign 0.5


# ------------------------------------------
# GENRE 4: SLICE OF LIFE / COMEDY
# ------------------------------------------

# Gaya 16: See You Next Time (Anime ending yang ceria)
screen outro_anime_end(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 10
            align (0.5, 0.5)
            text "[nomor_act]":
                size 80 bold True color "#ffff00" xalign 0.5
                outlines [ (3, "#0000ff", 1, 1) ]
            text pesan_outro:
                size 45 bold True color "#ffffff" xalign 0.5
                outlines [ (2, "#ff0000", 1, 1) ]

# Gaya 17: Sleepy Time (Waktu tidur yang damai)
screen outro_sleepy(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.8 yalign 0.8 # Pojok kanan bawah
        vbox:
            spacing 5
            text "[nomor_act]":
                size 45 bold True color "#ffebcd" xalign 1.0 
            text "Zzz... [pesan_outro]":
                size 25 italic True color "#aaaaaa" xalign 1.0

# Gaya 18: Comic Bam! (Akhir yang konyol/menggantung ala komik)
screen outro_comic_end(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing -5
            align (0.5, 0.5)
            text "[nomor_act]":
                size 90 bold True color "#32cd32" xalign 0.5 
                outlines [ (4, "#ffffff", 0, 0), (6, "#000000", 0, 0) ]
            text pesan_outro:
                size 45 bold True color "#ff1493" xalign 0.5
                outlines [ (3, "#000000", 0, 0) ]

# Gaya 19: That's a Wrap! (Gaya sutradara film)
screen outro_wrap(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            align (0.5, 0.5)
            frame:
                background Solid("#ffffff")
                padding (10, 5)
                xalign 0.5
                text "[nomor_act]":
                    size 50 bold True color "#000000"
            text pesan_outro:
                size 30 bold True color "#ffffff" xalign 0.5

# Gaya 20: Happy Days (Hari yang cerah)
screen outro_happy(nomor_act, pesan_outro):
    frame:
        background None
        xalign 0.5 yalign 0.5
        vbox:
            spacing 15
            align (0.5, 0.5)
            text "[nomor_act]":
                size 75 bold True color "#87ceeb" xalign 0.5 # Biru langit
                drop_shadow (3, 3) drop_shadow_color "#ffffff"
            text pesan_outro:
                size 35 color "#ffffff" xalign 0.5