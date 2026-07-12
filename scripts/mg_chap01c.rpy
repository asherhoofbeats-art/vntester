# ==========================================
# FILE: mg_chap01c.rpy
# MINIGAME: Analisis Residu Kimia Gembok
# ==========================================

screen mg_analisis_kimia():
    modal True
    
    # Nilai target yang harus dicapai pemain untuk menang
    default target_ph = 3       # Asam kuat (cairan pemotong besi)
    default target_visc = 8     # Viskositas kental
    default target_dens = 5     # Kepadatan medium
    
    # Nilai saat ini (yang bisa diubah pemain)
    default current_ph = 7
    default current_visc = 1
    default current_dens = 1
    
    default status_msg = "SINKRONISASI POLA MOLEKUL..."

    # Latar gelap transparan
    add "#000000cc"

    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40
        background Solid("#002200") # Warna hijau gelap ala layar terminal CRT retro
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "SCANNER RESIDU PORTABEL v1.0" size 30 color "#00ff00" xalign 0.5 bold True
            text "Target Pola: pH: 3 | Viskositas: 8 | Kepadatan: 5" size 18 color "#00cc00" xalign 0.5
            
            null height 15
            
            # --- BARIS 1: Tingkat pH ---
            hbox:
                spacing 30
                xalign 0.5
                text "Tingkat pH   :" size 24 color "#ffffff" yalign 0.5
                textbutton "<":
                    action If(current_ph > 0, [Play("sound", "sfx_mencet_tombol.ogg"), SetScreenVariable("current_ph", current_ph - 1)])
                    text_size 30 text_color "#00ff00"
                text "[current_ph]" size 28 color "#ffff00" yalign 0.5
                textbutton ">":
                    action If(current_ph < 14, [Play("sound", "sfx_mencet_tombol.ogg"), SetScreenVariable("current_ph", current_ph + 1)])
                    text_size 30 text_color "#00ff00"

            # --- BARIS 2: Viskositas ---
            hbox:
                spacing 30
                xalign 0.5
                text "Viskositas   :" size 24 color "#ffffff" yalign 0.5
                textbutton "<":
                    action If(current_visc > 0, [Play("sound", "sfx_mencet_tombol.ogg"), SetScreenVariable("current_visc", current_visc - 1)])
                    text_size 30 text_color "#00ff00"
                text "[current_visc]" size 28 color "#ffff00" yalign 0.5
                textbutton ">":
                    action If(current_visc < 10, [Play("sound", "sfx_mencet_tombol.ogg"), SetScreenVariable("current_visc", current_visc + 1)])
                    text_size 30 text_color "#00ff00"

            # --- BARIS 3: Kepadatan ---
            hbox:
                spacing 30
                xalign 0.5
                text "Kepadatan    :" size 24 color "#ffffff" yalign 0.5
                textbutton "<":
                    action If(current_dens > 0, [Play("sound", "sfx_mencet_tombol.ogg"), SetScreenVariable("current_dens", current_dens - 1)])
                    text_size 30 text_color "#00ff00"
                text "[current_dens]" size 28 color "#ffff00" yalign 0.5
                textbutton ">":
                    action If(current_dens < 10, [Play("sound", "sfx_mencet_tombol.ogg"), SetScreenVariable("current_dens", current_dens + 1)])
                    text_size 30 text_color "#00ff00"

            null height 20
            
            text status_msg size 20 color "#ffaa00" xalign 0.5
            
            null height 10

            textbutton "ANALISIS SAMPEL":
                xalign 0.5
                text_size 24
                action [
                    If(current_ph == target_ph and current_visc == target_visc and current_dens == target_dens,
                        [Play("sound", "sfx_correct.ogg"), Return(True)],
                        [Play("sound", "sfx_error_win.ogg"), SetScreenVariable("status_msg", "ERROR: POLA TIDAK COCOK!")]
                    )
                ]

# ==========================================
# Label Pemicu Minigame Analisis Kimia
# ==========================================
label play_mg_chap01c:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    play sound "sfx_kamera_digital.ogg"
    "Raka mengeluarkan alat scanner portabelnya dan meneteskan sampel residu dari gembok."
    "Sesuaikan parameter di layar agar cocok dengan target pola kimia industri."
    
    call screen mg_analisis_kimia
    
    play sound "sfx_level_up.ogg"
    "BEEP! Analisis Selesai: 99.8% Korosif Industri."
    

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP01C SELESAI")
    # -----------------------------------
    return