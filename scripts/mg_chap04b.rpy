# ==========================================
# FILE: mg_chap04b.rpy
# MINIGAME: Mematahkan Pagar Gaib (Fokus Bimo)
# ==========================================

# ------------------------------------------
# FUNGSI PYTHON UNTUK MENGACAK POSISI
# ------------------------------------------
init python:
    import random
    
    def shuffle_segel_positions(pos_dict, current_node):
        # Buat salinan dictionary agar layar bisa mendeteksi perubahan
        new_dict = pos_dict.copy()
        
        # Jika tinggal 1 angka (atau sudah selesai semua), tidak perlu diacak
        if current_node >= 5:
            return new_dict
        
        # Cari tahu angka berapa saja yang belum ditekan
        unclicked = [i for i in range(current_node, 6)]
        
        # Ambil slot koordinat dari angka-angka yang belum ditekan
        available_spots = [new_dict[i] for i in unclicked]
        
        # Acak slot koordinat tersebut
        random.shuffle(available_spots)
        
        # Pasangkan kembali ke angkanya
        for idx, node in enumerate(unclicked):
            new_dict[node] = available_spots[idx]
            
        return new_dict

# ------------------------------------------
# DEFINISI GAMBAR MINIGAME 04B
# ------------------------------------------
image bg_mg04b_penjaga = "images/cg/bg_mg04b_penjaga.webp"
image cg_mg04b_bimo_fokus = "images/cg/cg_mg04b_bimo_fokus.webp"
image cg_mg04b_bimo_menang = "images/cg/cg_mg04b_bimo_menang.webp"
image cg_mg04b_bimo_kalah = "images/cg/cg_mg04b_bimo_kalah.webp"
image it_kristal_darah = "images/item/it_kristal_darah.webp"

# ------------------------------------------
# SCREEN UI MINIGAME SEGEL GAIB
# ------------------------------------------
screen mg_segel_bimo():
    modal True
    
    # Latar Belakang Entitas Penjaga
    add "bg_mg04b_penjaga"
    
    # Efek vignette untuk memfokuskan pandangan
    add "#00000088"

    # Waktu batas permainan: 30 Detik
    default time_limit = 15.0

    # Titik yang sedang aktif (1 sampai 5)
    default current_node = 1
    
    # Mapping Angka -> Indeks Koordinat Awal
    default pos_dict = {1:0, 2:1, 3:2, 4:3, 5:4}

    # Kumpulan Koordinat untuk 5 Titik
    $ coords = [
        (600, 150),  # Slot 0 (Atas)
        (850, 550),  # Slot 1 (Kanan Bawah)
        (350, 300),  # Slot 2 (Kiri Atas)
        (850, 300),  # Slot 3 (Kanan Atas)
        (350, 550)   # Slot 4 (Kiri Bawah)
    ]

    # Timer untuk MENGACAK posisi setiap 2 detik
    timer 0.5 repeat True action SetScreenVariable("pos_dict", shuffle_segel_positions(pos_dict, current_node))

    # Timer kegagalan (Habis 30 detik)
    timer time_limit action Return(False)
    
    # Timer keberhasilan (Mengecek jika kelima titik sudah diklik berurutan)
    timer 0.1 repeat True action If(current_node > 5, true=Return(True), false=None)

    # UI Indikator Waktu Berjalan
    vbox:
        xalign 0.5
        yalign 0.05
        spacing 10
        
        text "BENTUK SEGEL GARAM!\nKLIK ANGKA SECARA BERURUTAN (1-5)" size 28 color "#00ccff" xalign 0.5 bold True text_align 0.5
        
        bar:
            value AnimatedValue(0, time_limit, time_limit) 
            range time_limit 
            xsize 600 
            ysize 25
            xalign 0.5
            left_bar Solid("#00ccff")
            right_bar Solid("#333333")


    # Render Node (Tombol)
    for i in range(1, 6):
        # Ambil posisi terkini berdasarkan acakan pos_dict
        $ coord_idx = pos_dict[i]
        $ x_pos = coords[coord_idx][0]
        $ y_pos = coords[coord_idx][1]

        if current_node == i:
            # NODE AKTIF (Bisa diklik, warna cerah)
            textbutton str(i):
                xpos x_pos ypos y_pos
                text_size 60
                text_color "#ffffff"
                text_bold True
                background Solid("#ff0000")
                hover_background Solid("#ffaa00")
                action [SetScreenVariable("current_node", i + 1), Play("sound", "sfx_magic_spell.ogg")]
                
        elif current_node > i:
            # NODE SELESAI (Sudah diklik, berubah jadi tanda centang bersinar, Posisinya FIX karena tidak diacak lagi)
            text "✔️":
                xpos x_pos ypos y_pos
                size 60
                color "#00ffcc"
                
        else:
            # NODE TERKUNCI (Belum gilirannya, transparan)
            text str(i):
                xpos x_pos ypos y_pos
                size 60
                color "#555555"


# ==========================================
# LABEL PEMICU MINIGAME SEGEL
# ==========================================
label play_mg_chap04_segel:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    stop music fadeout 1.0
    play music "bgm_10_fokus_spiritual.ogg" fadein 1.0

    scene cg_mg04b_bimo_fokus with dissolve_lambat
    play sound "sfx_mantra_whisper.ogg" loop
    
    "Bimo memusatkan seluruh energi spiritualnya ke tangannya yang menggenggam garam berkat."
    b "Titik kelemahannya membentuk sebuah pola di dadanya. Jika aku bisa menyerang titik-titik itu secara berurutan..."
    
    "Klik angka 1 sampai 5 secara BERURUTAN sebelum waktunya habis! Hati-hati, titik penjaga ini akan terus berpindah posisi!"
    
    stop sound fadeout 0.5
    
    # Memanggil screen minigame
    call screen mg_segel_bimo
    
    # Evaluasi Hasil (Menang/Kalah)
    if _return == True:
        # --- JIKA MENANG ---
        stop music fadeout 0.5
        play sound "sfx_holy_burn.ogg"
        
        scene cg_mg04b_bimo_menang with flashbang
        "Bimo melempar segenggam garam tersebut secara presisi. Garam itu bereaksi dengan hawa iblis, menciptakan ledakan cahaya putih yang menyilaukan!"
        
        play sound "sfx_monster_died.ogg"
        "Bayangan raksasa bermata merah itu meraung hebat sebelum akhirnya hancur berkeping-keping menjadi abu."
        
        scene bg_padepokan_luar with dissolve
        play sound "sfx_ting_ting.ogg"
        show it_kristal_darah at truecenter with dissolve_kilat
        
        "Di bekas tempat bayangan itu berdiri, tertinggal sebuah kristal kecil yang memancarkan hawa hangat."
        $ ch4_dapat_kristal = True
        $ item_kristal_merah = True
        $ citra_resonansi_gaib +=1
        b "Sisa energi gaib yang mengkristal. Ini bisa berguna nanti."
        hide it_kristal_darah with dissolve
        
        show bimo_lega at center with dissolve_kilat
        b "Jalannya sudah bersih, Citra. Kau aman sekarang."
        hide bimo_lega
        
    else:
        # --- JIKA KALAH ---
        stop music fadeout 0.5
        play sound "sfx_power_surge_monster.ogg"
        $ citra_resonansi_gaib -=1
        scene cg_mg04b_bimo_kalah with flashmerah
        with hpunch
        play sound "sfx_punch.ogg"
        "Terlalu lambat! Bayangan itu menyadari niat Bimo dan melepaskan gelombang energi kelam yang memukul mundur Bimo hingga terjatuh."
        
        b "Argh! Energinya terlalu padat... Pagar ini butuh waktu lama untuk hancur dengan sendirinya."
        $ item_kristal_merah = False
        $ ch4_dapat_kristal = False
        
        scene bg_padepokan_luar with dissolve
        show bimo_lelah at center with mata_mengerjap
        b "Maaf Citra, aku gagal menghancurkannya secara instan. Kita harus menunggu Raka mendobrak dari belakang agar fokus penjaga ini terpecah."
        hide bimo_lelah
    

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP04_SEGEL SELESAI")
    # -----------------------------------
    return