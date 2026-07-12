# ==========================================
# FILE: mg_chap04a.rpy
# MINIGAME: Labirin Hutan Bambu Berhantu
# ==========================================

# ------------------------------------------
# DEFINISI GAMBAR & CUTSCENE MINIGAME 04A
# ------------------------------------------
image bg_mg04a_bambu = "images/cg/bg_mg04a_bambu.webp"
image cg_mg04a_raka_senter = "images/cg/cg_mg04a_raka_senter.webp"
image it_boneka_penyesat = "images/item/it_boneka_penyesat.webp"
image cg_mg04a_kuntilanak = "images/cg/cg_mg04a_kuntilanak.webp"
image cg_mg04a_bimo_waspada = "images/cg/cg_mg04a_bimo_waspada.webp"

# ------------------------------------------
# SCREEN UI MINIGAME LABIRIN
# ------------------------------------------
screen mg_maze_bambu(nyasar_meter):
    modal True
    
    # Latar belakang hutan bambu utama
    add "bg_mg04a_bambu"
    
    # Efek Senter: Layar digelapkan secara signifikan untuk memberi kesan pandangan terbatas
    add "#000000e6" # Hitam dengan transparansi 90%
    
    # UI Bagian Atas: Meteran Nyasar (Maksimal 2 sekarang)
    vbox:
        xalign 0.5
        yalign 0.1
        spacing 10
        
        text "LABIRIN HUTAN BAMBU" size 35 color "#ff3333" bold True xalign 0.5
        text "Batas Kesalahan: [nyasar_meter] / 2" size 25 color "#ffffff" xalign 0.5
        
        bar:
            value nyasar_meter
            range 2
            xsize 400
            ysize 25
            xalign 0.5
            left_bar Solid("#ff0000")
            right_bar Solid("#555555")
            
        text "Jangan sampai tersesat dua kali..." size 18 color "#aaaaaa" xalign 0.5 italic True

    # UI Bagian Bawah: Pilihan Navigasi Senter
    vbox:
        xalign 0.5
        yalign 0.8
        spacing 30
        
        text "Arahkan senter dan pilih jalan:" size 24 color "#00ffcc" xalign 0.5 bold True
        
        hbox:
            spacing 50
            xalign 0.5
            
            # Tombol Kiri
            textbutton "⬅️ KIRI":
                text_size 35
                text_color "#ffffff"
                background Solid("#333333")
                hover_background Solid("#555555")
                action Return("kiri")
                
            # Tombol Lurus
            textbutton "⬆️ LURUS":
                text_size 35
                text_color "#ffffff"
                background Solid("#333333")
                hover_background Solid("#555555")
                action Return("lurus")
                
            # Tombol Kanan
            textbutton "➡️ KANAN":
                text_size 35
                text_color "#ffffff"
                background Solid("#333333")
                hover_background Solid("#555555")
                action Return("kanan")

# ==========================================
# LABEL PEMICU MINIGAME LABIRIN
# ==========================================
label play_mg_chap04_maze:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Inisialisasi Jalur dan Status
    # Jalur yang benar untuk keluar dari labirin: Kanan, Lurus, Kiri
    $ correct_path = ["kanan", "lurus", "kiri"]
    $ current_step = 0
    $ nyasar_meter = 0
    
    # BGM Suasana Seram
    play music "bgm_creepy_ambient.ogg" fadein 2.0 loop 

    # Tampilkan CG Raka menyenter jalan sebagai intro labirin
    scene cg_mg04a_raka_senter with transisi_senter
    "Raka menyalakan senternya. Jarak pandang sangat terbatas. Kabut tebal membuat semua batang bambu terlihat sama."
    
    label .maze_loop:
        
        # Kondisi Menang: Jika pemain berhasil menebak semua urutan
        if current_step >= len(correct_path):
            jump .maze_win
            
        # Panggil Screen Minigame
        call screen mg_maze_bambu(nyasar_meter)
        
        # Tangkap pilihan arah pemain
        $ chosen_direction = _return
        
        # Evaluasi Pilihan
        if chosen_direction == correct_path[current_step]:
            # JIKA BENAR
            play sound "sfx_footsteps_approach.ogg"
            scene cg_mg04a_raka_senter with transisi_senter
            "Kalian terus melangkah ke arah [chosen_direction]..."
            "Jalan ini terasa benar. Hawa di sekitar sedikit lebih ringan."
            $ current_step += 1
            $ citra_resonansi_gaib +=1
            jump .maze_loop
            
        else:
            # JIKA SALAH
            $ nyasar_meter += 1
            
            if nyasar_meter == 1:
                # KESALAHAN PERTAMA (Peringatan & Item Jimat)
                play sound "sfx_patah_ranting.ogg"
                scene black with hpunch
                "KRAK!"
                "Ranting bambu patah diinjak. Hawa dingin seketika berhembus kuat meniup wajah kalian."
                
                # Tampilkan item jimat penyesat
                $ citra_resonansi_gaib = getattr(store, "citra_resonansi_gaib", 0) - 1
                show it_boneka_penyesat at truecenter with dissolve_kilat
                $ item_boneka_jerami = True
                play sound "sfx_eerie.ogg"
                "Senter Raka menyorot sebuah boneka jerami usang yang terikat pada batang bambu."
                "Ini jalan buntu yang disiapkan untuk menyesatkan manusia. Kalian harus segera berbalik arah!"
                hide it_boneka_penyesat with dissolve
                jump .maze_loop
                
            elif nyasar_meter >= 2:
                # KESALAHAN KEDUA (GAME OVER JUMPSCARE)
                stop music fadeout 0.1
                play sound "sfx_banshee_scream.ogg"
                
                # Jumpscare Kuntilanak
                scene cg_mg04a_kuntilanak with flashmerah
                with hpunch
                
                "{b}HIHIHIHIHIHI...!!!{/b}"
                "Sebuah wajah pucat mengintip dari balik bambu! Kalian tersesat terlalu dalam dan tidak akan pernah bisa keluar lagi!"
                
                play sound "sfx_game_over.ogg"
                scene black with tv_rusak
                pause 1.0
                
                centered "{color=#ff0000}{size=50}GAME OVER{/size}{/color}"
                pause 2.0
                
                # Return paksa ke Main Menu
                $ MainMenu(confirm=False)()

    label .maze_win:
        stop music fadeout 2.0
        play sound "sfx_angin_malam_kencang.ogg"
        $ citra_resonansi_gaib +=1
        # Tampilkan CG Bimo Waspada saat keluar dari labirin
        scene cg_mg04a_bimo_waspada with dissolve_lambat
        "Kalian berhasil! Jarak pandang perlahan terbuka."
        "Hutan bambu menipis, namun Bimo tiba-tiba merentangkan tangannya, menghentikan langkah kalian."
        "Di ujung jalan, terlihat sebuah gubuk tua... beserta sosok gaib yang menjaganya."
        
        return