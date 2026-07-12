# ==========================================
# FILE: mg_chap01a.rpy
# MINIGAME: Menyetel Frekuensi Sinyal Video Call
# ==========================================

# 1. Tampilan Antarmuka (UI) Minigame
screen mg_radio_tuning():
    modal True
    
    # Variabel lokal layar (nilai awal slider saat minigame dimulai)
    default current_freq = 20
    default current_noise = 80
    
    # Target nilai rahasia yang harus dicapai pemain
    default target_freq = 75
    default target_noise = 30
    
    # Pesan petunjuk/error
    default error_msg = "Geser slider untuk mencari sinyal."

    # ------------------------------------------
    # LOGIKA INDIKATOR DINAMIS (REAL-TIME)
    # ------------------------------------------
    # Hitung jarak absolut antara posisi pemain dan target
    $ dist_freq = abs(current_freq - target_freq)
    $ dist_noise = abs(current_noise - target_noise)

    # Status Frekuensi (Gunakan [[ agar Ren'Py tidak menganggapnya variabel)
    if dist_freq <= 5:
        $ f_text = "[[TERKUNCI]"
        $ f_color = "#00ff00" # Hijau
    elif dist_freq <= 20:
        $ f_text = "[[MENGHAMPIRI SINYAL...]"
        $ f_color = "#ffff00" # Kuning
    else:
        $ f_text = "[[SINYAL HILANG]"
        $ f_color = "#ff3333" # Merah

    # Status Noise
    if dist_noise <= 5:
        $ n_text = "[[SUARA BERSIH]"
        $ n_color = "#00ff00" # Hijau
    elif dist_noise <= 20:
        $ n_text = "[[MULAI JELAS...]"
        $ n_color = "#ffff00" # Kuning
    else:
        $ n_text = "[[TERLALU BISING]"
        $ n_color = "#ff3333" # Merah
    # ------------------------------------------

    # Latar belakang gelap transparan untuk fokus ke minigame
    add "#000000cc"

    # Frame utama minigame
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 50
        ypadding 40
        background Solid("#1a1a1a") # Warna kotak abu-abu gelap retro
        
        vbox:
            spacing 25
            xalign 0.5
            
            text "MENERIMA PANGGILAN VIDEO..." size 28 color "#00ff00" xalign 0.5 bold True
            
            # Area Pesan Kesalahan Utama
            text error_msg size 18 color "#ff3333" xalign 0.5
            
            null height 10
            
            # SLIDER 1: Frekuensi
            vbox:
                spacing 5
                # Hbox ini menampilkan Judul Slider dan Indikator Dinamis secara bersebelahan
                hbox:
                    spacing 10
                    text "FREKUENSI (MHz)" color "#ffffff" size 20
                    text f_text color f_color size 20 bold True
                
                bar:
                    value ScreenVariableValue("current_freq", 100)
                    xsize 400
                    ysize 30
            
            # SLIDER 2: Pengurang Noise
            vbox:
                spacing 5
                # Hbox untuk Judul dan Indikator Dinamis
                hbox:
                    spacing 10
                    text "FILTER NOISE (%)" color "#ffffff" size 20
                    text n_text color n_color size 20 bold True
                
                bar:
                    value ScreenVariableValue("current_noise", 100)
                    xsize 400
                    ysize 30
            
            null height 20
            
            # Tombol Eksekusi
            textbutton "HUBUNGKAN":
                xalign 0.5
                text_size 26
                # Logika Kemenangan: Nilai slider harus berada di jarak +/- 5 dari target
                action [
                    If(abs(current_freq - target_freq) <= 5 and abs(current_noise - target_noise) <= 5,
                        # Jika Benar: Mainkan SFX benar, lalu tutup screen dan lanjutkan game
                        [Play("sound", "sfx_correct.ogg"), Return(True)],
                        
                        # Jika Salah: Mainkan suara rusak, update pesan error
                        [Play("sound", "sfx_static_noise.ogg"), SetScreenVariable("error_msg", "Gagal! Sinyal belum sinkron sepenuhnya. Coba lagi.")]
                    )
                ]

# ==========================================
# 2. Label Pemicu Minigame
# ==========================================
label play_mg_chap01a:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Mainkan suara static radio saat minigame dimulai
    play sound "sfx_static_noise.ogg" loop
    
    # Memanggil screen minigame dan menunggu hingga pemain menang (Return True)
    call screen mg_radio_tuning
    
    # Eksekusi setelah pemain berhasil menyelesaikan minigame
    stop sound fadeout 1.0
    play sound "sfx_bip.ogg"
    

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP01A SELESAI")
    # -----------------------------------
    return