# ==========================================
# FILE: mg_chaparwah.rpy
# MINIGAME: Ritual Pengusiran Arwah
# ==========================================

# ------------------------------------------
# DEFINISI ASET MINIGAME RITUAL
# ------------------------------------------
image cg_mg_ritual_bimo_fokus = "images/cg/cg_mg_ritual_bimo_fokus.webp"
image cg_mg_ritual_arya_curiga = "images/cg/cg_mg_ritual_arya_curiga.webp"
image cg_mg_ritual_sukses = "images/cg/cg_mg_ritual_sukses.webp"
image cg_mg_ritual_gagal = "images/cg/cg_mg_ritual_gagal.webp"

screen mg_arwah_ritual():
    modal True
    
    # --------------------------------------
    # DEKLARASI VARIABEL (WAJIB DI ATAS)
    # --------------------------------------
    default ritual_meter = 0
    default warning_level = 0
    default timer_val = 12.0

    # Background Utama
    add "bg_gang_sempit"
    
    # Logika Tampilan CG Berdasarkan Tingkat Kecurigaan
    if warning_level >= 75:
        add "cg_mg_ritual_arya_curiga"
    elif ritual_meter == 0:
        add "cg_mg_ritual_bimo_fokus"

    # Overlay Gelap agar UI lebih terbaca
    add "#00000088"

    # Timer Mundur (Jika habis, langsung Game Over / Gagal)
    timer timer_val action Return(False)

    # --------------------------------------
    # UI TAMPILAN ATAS
    # --------------------------------------
    vbox:
        xalign 0.5 yalign 0.1
        text "🕯️ RITUAL PENGUSIRAN 🕯️" size 35 color "#ffff00" bold True
        bar:
            value ritual_meter
            range 5
            xsize 400 ysize 20
        text "⚠️ KECURIGAAN ARYA: [warning_level]%" size 25 color "#ff0000" xalign 0.5 bold True

    # --------------------------------------
    # TOMBOL AKSI
    # --------------------------------------
    grid 3 1:
        xalign 0.5 yalign 0.7
        spacing 60
        
        # TOMBOL 1: Mantra Aman (Menambah Progres Ritual)
        textbutton "📿":
            text_size 80
            action [SetScreenVariable("ritual_meter", ritual_meter + 1), Play("sound", "sfx_mantra_whisper.ogg")]
            
        # TOMBOL 2: Berisik (Pengecoh! Menambah Kecurigaan Polisi)
        textbutton "🔔":
            text_size 80
            action [SetScreenVariable("warning_level", warning_level + 25), Play("sound", "sfx_error_win.ogg")]
            
        # TOMBOL 3: Mantra Api (Menambah Progres Ritual)
        textbutton "🔥":
            text_size 80
            action [SetScreenVariable("ritual_meter", ritual_meter + 1), Play("sound", "sfx_fire_burst.ogg")]

    # --------------------------------------
    # KONDISI MENANG / KALAH DI DALAM SCREEN
    # --------------------------------------
    if ritual_meter >= 5:
        timer 0.1 action Return(True)
    if warning_level >= 100:
        timer 0.1 action Return(False)

# ==========================================
# LABEL PEMICU & HASIL (DIPANGGIL DARI CHAPTER)
# ==========================================
label play_mg_arwah_ritual:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Set up musik tegang sebelum masuk layar minigame
    stop music fadeout 1.0
    play music "bgm_boss_ritual.ogg" fadein 1.0
    
    call screen mg_arwah_ritual
    
    # Pengecekan Hasil Return
    if _return == True:
        play sound "sfx_hantu_tersedot.ogg"
        scene cg_mg_ritual_sukses with flash_hijau
        "Ritual berhasil! Arwah terlepas dari tubuh Citra dengan tenang sebelum Pak Polisi sempat menyadari apa yang terjadi."
        return True
    else:
        play sound "sfx_door_kick.ogg"
        scene cg_mg_ritual_gagal with flashmerah
        "Ritual gagal! Suasana terlalu berisik atau waktu kehabisan, Pak Polisi curiga dan arwah kabur paksa dari tubuh Citra!"
        return False