# ==========================================
# AUTO-GENERATED PROLOG / SPLASHSCREEN
# ==========================================
init python:
    if persistent.has_seen_prolog is None:
        persistent.has_seen_prolog = False

# --- DEKLARASI ASET GAMBAR ---
image it_kertas_segel_hantu_1 = "images/prolog/it_kertas_segel_hantu_1.webp"

# --- SCREEN KHUSUS TEKS PROLOG ---
screen teks_prolog(pesan, warna="#ffffff"):
    text pesan size 40 color warna bold True outlines [(2, "#000", 0, 0)] align (0.5, 0.5) text_align 0.5

# --- SCREEN KLIK UNTUK SKIP ---
screen skip_prolog_btn():
    zorder 100
    button:
        xysize (1920, 1080)
        action Return()
    text _("Klik layar untuk melewati...") size 20 color "#888888" align (0.98, 0.98)

# --- PUSTAKA ANIMASI ATL ---
transform scroll_lambat:
    xalign 0.0
    linear 25.0 xalign 1.0
    repeat
transform scroll_sedang:
    xalign 0.0
    linear 12.0 xalign 1.0
    repeat
transform scroll_maju:
    xalign 1.0
    linear 2.5 xalign 0.0
    repeat
transform mobil_getar:
    xalign 0.5 yalign 0.85
    choice:
        yoffset 0
    choice:
        yoffset -4
    choice:
        yoffset 3
    choice:
        yoffset -2
    pause 0.05
    repeat

label splashscreen:
    # Bypass saat mode Developer
    if config.developer:
        return

    scene black
    pause 1.0
    play music "audio/bgm_01_jejak_misteri.ogg" fadein 2.0
    play sound "audio/sfx_angin_besar.ogg" loop volume 0.6
    # Munculkan overlay skip jika pemain sudah tamat
    if persistent.has_seen_prolog:
        show screen skip_prolog_btn

    with dissolve

    show it_kertas_segel_hantu_1 at mobil_getar
    show screen teks_prolog(_("""Ketik teks bahasa Indonesia..."""), warna="#FFFFFF") with dissolve
    pause 3.0
    hide screen teks_prolog with dissolve

    # --- KELUAR MENUJU MAIN MENU ---
    hide screen skip_prolog_btn
    stop sound fadeout 3.0
    stop music fadeout 3.0
    scene black with dissolve
    pause 1.0

    $ persistent.has_seen_prolog = True
    return