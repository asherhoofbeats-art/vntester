# ==========================================
# FILE: mg_chap04c.rpy
# MINIGAME: Adu Kekuatan Citra vs Ki Renggo
# ==========================================

# ------------------------------------------
# DEFINISI GAMBAR MINIGAME 04C
# ------------------------------------------
image citra_kesurupan = "images/chars/citra_kesurupan.webp"
image at_book_throw = "images/item/at_book_throw.webp"
image bg_mg04c_padepokan_chaos = "images/cg/bg_mg04c_padepokan_chaos.webp"
image cg_mg04c_renggo_serang = "images/cg/cg_mg04c_renggo_serang.webp"
image cg_mg04c_citra_menang = "images/cg/cg_mg04c_citra_menang.webp"
image cg_mg04c_raka_hajar = "images/cg/cg_mg04c_raka_hajar.webp"
image it_koin_kuno = "images/item/it_koin_kuno.webp"
image cg_chap04_citra_kena_buku = "images/cg/cg_chap04_citra_kena_buku.webp"

# ------------------------------------------
# TRANSFORM ANIMASI GERAK CEPAT
# ------------------------------------------
transform gerak_acak_lemparan(target_x, target_y):
    ease 0.3 xalign target_x yalign target_y

# ------------------------------------------
# SCREEN UI MINIGAME ADU KEKUATAN
# ------------------------------------------
screen mg_adu_dukun():
    modal True
    
    add "bg_mg04c_padepokan_chaos"
    add "#000000aa"

    # Waktu batas permainan: 7 Detik (Cukup menantang untuk 6 target)
    default time_limit = 7.0

    # Status 6 proyektil (False = melayang, True = hancur)
    default proj1 = False
    default proj2 = False
    default proj3 = False
    default proj4 = False
    default proj5 = False
    default proj6 = False

    # Titik kemunculan awal
    default p1_x = renpy.random.uniform(0.1, 0.9)
    default p1_y = renpy.random.uniform(0.2, 0.8)
    default p2_x = renpy.random.uniform(0.1, 0.9)
    default p2_y = renpy.random.uniform(0.2, 0.8)
    default p3_x = renpy.random.uniform(0.1, 0.9)
    default p3_y = renpy.random.uniform(0.2, 0.8)
    default p4_x = renpy.random.uniform(0.1, 0.9)
    default p4_y = renpy.random.uniform(0.2, 0.8)
    default p5_x = renpy.random.uniform(0.1, 0.9)
    default p5_y = renpy.random.uniform(0.2, 0.8)
    default p6_x = renpy.random.uniform(0.1, 0.9)
    default p6_y = renpy.random.uniform(0.2, 0.8)

    # Pergerakan dinamis setiap 0.3 detik (sangat gesit)
    timer 0.3 repeat True action [
        SetScreenVariable("p1_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p1_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p2_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p2_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p3_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p3_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p4_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p4_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p5_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p5_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p6_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p6_y", renpy.random.uniform(0.2, 0.9))
    ]

    timer time_limit action Return(False)
    
    if proj1 and proj2 and proj3 and proj4 and proj5 and proj6:
        timer 0.2 action Return(True)

    # UI Indikator Waktu
    vbox:
        xalign 0.5
        yalign 0.05
        spacing 10
        
        text "HANCURKAN SERANGAN BUKU MANTRA! (7 Detik)" size 28 color "#a020f0" xalign 0.5 bold True
        
        bar:
            value AnimatedValue(0, time_limit, time_limit) 
            range time_limit 
            xsize 600 
            ysize 25
            xalign 0.5
            left_bar Solid("#a020f0")
            right_bar Solid("#555555")

    # ===============================================
    # RENDER PROYEKTIL BUKU MANTRA
    # ===============================================
    if not proj1:
        imagebutton:
            idle "at_book_throw"
            at gerak_acak_lemparan(p1_x, p1_y)
            action [SetScreenVariable("proj1", True), Play("sound", "sfx_magic_spell.ogg")]

    if not proj2:
        imagebutton:
            idle "at_book_throw"
            at gerak_acak_lemparan(p2_x, p2_y)
            action [SetScreenVariable("proj2", True), Play("sound", "sfx_magic_spell.ogg")]

    if not proj3:
        imagebutton:
            idle "at_book_throw"
            at gerak_acak_lemparan(p3_x, p3_y)
            action [SetScreenVariable("proj3", True), Play("sound", "sfx_magic_spell.ogg")]

    if not proj4:
        imagebutton:
            idle "at_book_throw"
            at gerak_acak_lemparan(p4_x, p4_y)
            action [SetScreenVariable("proj4", True), Play("sound", "sfx_magic_spell.ogg")]

    if not proj5:
        imagebutton:
            idle "at_book_throw"
            at gerak_acak_lemparan(p5_x, p5_y)
            action [SetScreenVariable("proj5", True), Play("sound", "sfx_magic_spell.ogg")]

    if not proj6:
        imagebutton:
            idle "at_book_throw"
            at gerak_acak_lemparan(p6_x, p6_y)
            action [SetScreenVariable("proj6", True), Play("sound", "sfx_magic_spell.ogg")]


# ==========================================
# LABEL PEMICU MINIGAME ADU KEKUATAN
# ==========================================
label play_mg_chap04_dukun:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    stop music fadeout 1.0
    play music "bgm_boss_ritual.ogg" fadein 1.0

    scene cg_mg04c_renggo_serang with flashmerah
    "Ki Renggo yang terpojok tiba-tiba meraung. Ia meraih setumpuk buku mantra kuno dari mejanya dan melemparkannya ke arah kami dengan kekuatan yang tak wajar!"
    kr "Rasakan kutukan padepokan ini, bocah sialan!!"

    scene bg_padepokan_dalam with vpunch
    show citra_kesurupan at center with dissolve_kilat
    play sound "sfx_glitch_kesurupan.ogg"
    
    c "..."
    "Aura gaib berwarna keunguan tiba-tiba memancar kuat dari tubuh Citra. Matanya berubah putih bersinar saat ia melangkah maju menutupi Raka dan Bimo."
    c "{b}Trik rendahan.{/b}"

    "Klik semua buku mantra yang melayang cepat untuk menghancurkannya!"

    # Panggil Minigame
    call screen mg_adu_dukun

    # Evaluasi Hasil
    if _return == True:
        # --- JIKA MENANG ---
        $ citra_resonansi_gaib = getattr(store, "citra_resonansi_gaib", 0) + 2
        $ ch4_dapat_koin = True
        $ item_koin_kuno = True
        
        stop music fadeout 0.5
        play sound "sfx_explosion.ogg"
        scene cg_mg04c_citra_menang with flashbang
        
        "Dengan ayunan tangannya, Citra memancarkan gelombang energi spiritual yang menghancurkan semua proyektil buku tersebut menjadi serpihan debu!"
        
        play sound "sfx_barang_berat_jatuh.ogg"
        "Ledakan energi itu melempar Ki Renggo hingga menabrak dinding dan jatuh tak sadarkan diri."
        
        scene bg_padepokan_dalam with dissolve
        show citra_lelah at center with dissolve_kilat
        c "Hah... hah... kekuatan apa itu tadi...?"
        hide citra_lelah
        
        play sound "sfx_coin_jatuh.ogg"
        show it_koin_kuno at truecenter with dissolve_kilat
        "Dari kantong Ki Renggo yang robek, sekeping Koin Kuno Berkarat menggelinding ke lantai. Koin itu memancarkan hawa dingin yang sama dengan aura Citra tadi."
        
        r "Biar gue yang simpen. Lumayan buat jimat."
        hide it_koin_kuno with dissolve
        
    else:
        # --- JIKA KALAH ---
        $ ch4_dapat_koin = False
        $ item_koin_kuno = False
        $ citra_resonansi_gaib = getattr(store, "citra_resonansi_gaib", 0) - 1
        stop music fadeout 0.5
        play sound "sfx_benda_dipukul.ogg"
        scene cg_chap04_citra_kena_buku with hpunch
        
        "Buku-buku itu menghantam Citra bertubi-tubi. Auranya meredup, dan ia hampir terjatuh."
        c "Kyaaa!"
        
        play music "bgm_05_otot_kawat.ogg" fadein 1.0
        scene cg_mg04c_raka_hajar with hpunch
        play sound "sfx_punch.ogg"
        
        "Sebelum serangan berikutnya mengenai Citra, Raka melompat ke depan dengan kemarahan memuncak dan mendaratkan pukulan telak ke rahang Ki Renggo!"
        r "Beraninya lu nyakitin Citra, dukun keparat!!"
        
        play sound "sfx_barang_berat_jatuh.ogg"
        "Ki Renggo terpelanting dan langsung pingsan di tempat."
        
        scene bg_padepokan_dalam with dissolve
        show raka_marah at center with dissolve_kilat
        r "Duh, lu gapapa Cit? Lain kali nggak usah sok jadi tameng, biar gue aja yang ngurus ginian."
        hide raka_marah
        
        show citra_lelah at center with mata_mengerjap
        c "M-maaf Kak Raka. Tadi badanku kayak gerak sendiri..."
        hide citra_lelah
        

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP04_DUKUN SELESAI")
    # -----------------------------------
    return