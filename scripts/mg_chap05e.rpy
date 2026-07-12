# ==========================================
# FILE: mg_chap05e.rpy
# MINIGAME: Meracik Penawar (Save Dr. Rina)
# MEKANIK: Sequence Click (Waktu Terbatas)
# ==========================================

# ------------------------------------------
# DEFINISI PROMPT & GAMBAR MINIGAME 05E
# ------------------------------------------
# 1. CG Rina Minum
# Prompt: 16-bit SNES pixel art style, visual novel CG. A female doctor in a white coat drinking a glass of green tea, looking very relieved and exhausted. Cold clinic room background.
image cg_mg05e_rina_minum = "images/cg/cg_mg05e_rina_minum.webp"

# 2. CG Rina Keracunan
# Prompt: 16-bit SNES pixel art style, visual novel CG. A female doctor dropping a glass that shatters. She is clutching her chest in extreme sudden dizziness, surrounded by a faint, unnatural green mist. High stakes drama.
image cg_mg05e_rina_keracunan = "images/cg/cg_ch05_rina_keracunan.webp"

# 3. BG Lemari Obat (Minigame)
# Prompt: 16-bit SNES pixel art style, visual novel BG. Close up of an open rusty medical cabinet filled with various colorful glowing chemical vials (Blue, Red, Green, Yellow).
image bg_mg05e_lemari_obat = "images/cg/bg_mg05e_lemari_obat.webp"

# 4. CG Rina Selamat
# Prompt: 16-bit SNES pixel art style, visual novel CG. A female doctor in a white coat sitting on the floor, breathing heavily but looking safe and grateful. A glowing green healing aura surrounds her slightly.
image cg_mg05e_rina_selamat = "images/cg/cg_mg05e_rina_selamat.webp"

# 5. CG Rina Tumbang (Kalah)
# Prompt: 16-bit SNES pixel art style, visual novel CG. A female doctor slumped heavily over her clinic desk, completely incapacitated. A shattered glass is on the floor. Gloomy and tragic aftermath scene.
image cg_mg05e_rina_tumbang = "images/cg/cg_ch05_rina_mati.webp"

# 6. Item: Rekaman Tirto & Penawar
# (Sudah didefinisikan di prompt sebelumnya)
image it_rekaman_tirto = "images/item/it_rekaman_tirto.webp"
image it_obat_penawar = "images/item/it_obat_penawar.webp"


# ------------------------------------------
# FUNGSI PYTHON LOGIKA MERACIK PENAWAR
# ------------------------------------------
init python:
    class AntidoteGame:
        def __init__(self):
            # Urutan yang benar: Biru, Merah, Hijau
            self.target_seq = ["biru", "merah", "hijau"]
            self.current_seq = []
            
            self.time_left = 12.0 # Waktu 12 detik untuk berpikir dan memilih
            self.status = "playing"
            self.msg = "RACIK PENAWAR DENGAN URUTAN YANG TEPAT!"
            self.msg_color = "#ffffff"

        def update(self):
            if self.status == "playing":
                self.time_left -= 0.1
                if self.time_left <= 0:
                    self.status = "lose"

        def click_bottle(self, color):
            if self.status == "playing":
                self.current_seq.append(color)
                renpy.play("sfx_suara_ting.ogg") # Bunyi botol kaca
                
                idx = len(self.current_seq) - 1
                
                # Jika salah pilih botol
                if self.current_seq[idx] != self.target_seq[idx]:
                    self.status = "lose"
                    renpy.play("sfx_error_win.ogg")
                    
                # Jika semua urutan benar
                elif len(self.current_seq) == len(self.target_seq):
                    self.status = "win"
                    self.msg = "PENAWAR BERHASIL DIRACIK!"
                    self.msg_color = "#00ff00"


# ------------------------------------------
# SCREEN UI MINIGAME MERACIK OBAT
# ------------------------------------------
screen mg_racik_penawar():
    modal True
    
    default game = AntidoteGame()
    
    timer 0.1 action Function(game.update) repeat True

    # Background Lemari Obat & Partikel Debu Ruangan
    add "bg_mg05e_lemari_obat"
    add "debu_melayang" 
    add "#000000aa"

    # ==========================
    # HUD & INFORMASI WAKTU
    # ==========================
    vbox:
        xalign 0.5 ypos 50
        spacing 15
        
        text game.msg size 32 color game.msg_color xalign 0.5 bold True
        
        # Timer Bar
        bar:
            value AnimatedValue(game.time_left, 12.0, 0.1)
            range 12.0
            xsize 800 ysize 30 xalign 0.5
            left_bar Solid("#ffcc00")
            right_bar Solid("#ff0000")
            
        text "Waktu: [int(game.time_left)] detik" size 28 color "#ffcc00" xalign 0.5

    # ==========================
    # LOG PEMILIHAN (Visual Feedback)
    # ==========================
    hbox:
        xalign 0.5 ypos 200
        spacing 20
        text "Urutan Mu: " size 28 color "#ffffff"
        for c in game.current_seq:
            if c == "biru":
                text "🔵" size 28
            elif c == "merah":
                text "🔴" size 28
            elif c == "hijau":
                text "🟢" size 28
            elif c == "kuning":
                text "🟡" size 28

    # ==========================
    # TOMBOL BOTOL KIMIA
    # ==========================
    hbox:
        xalign 0.5 yalign 0.75
        spacing 40
        
        textbutton "🧪 Botol Biru":
            text_size 28
            xysize (220, 150)
            background Solid("#0044ffee")
            hover_background Solid("#4488ffee")
            action Function(game.click_bottle, "biru")
            
        textbutton "🧪 Botol Merah":
            text_size 28
            xysize (220, 150)
            background Solid("#ff0000ee")
            hover_background Solid("#ff4444ee")
            action Function(game.click_bottle, "merah")
            
        textbutton "🧪 Botol Hijau":
            text_size 28
            xysize (220, 150)
            background Solid("#00ff00ee")
            hover_background Solid("#44ff44ee")
            action Function(game.click_bottle, "hijau")
            
        textbutton "🧪 Botol Kuning":
            text_size 28
            xysize (220, 150)
            background Solid("#ffcc00ee")
            hover_background Solid("#ffff44ee")
            action Function(game.click_bottle, "kuning")

    if game.status == "win":
        timer 0.5 action Return("win")
    elif game.status == "lose":
        timer 0.5 action Return("lose")


# ------------------------------------------
# LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap05e:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # 1. CG INTRO: Rina Kelelahan & Minum
    stop music fadeout 1.0
    play music "bgm_11_senyum_koruptor.ogg" fadein 1.0
    
    scene cg_mg05e_rina_minum with dissolve_lambat
    
    show rina_lelah at center with mata_mengerjap
    dr "Hah... hah... t-terima kasih... a-air..."
    hide rina_lelah
    
    "Dokter Rina yang masih syok berat mengambil segelas teh hijau di atas mejanya dengan tangan gemetar. Ia meminumnya dengan rakus untuk menenangkan diri."
    "Namun, beberapa detik kemudian..."
    
    # 2. CG KERACUNAN
    play sound "sfx_gelas_pecah.ogg"
    scene cg_mg05e_rina_keracunan with hpunch
    with flashmerah
    
    "PRANG!"
    "Gelas itu jatuh dari tangannya. Dokter Rina tiba-tiba memegang dadanya, pandangannya nanar menahan rasa pusing yang luar biasa."
    
    show rina_panik at center with tv_rusak
    dr "Ukh! D-dada saya... p-panas... tehnya... r-racun..."
    hide rina_panik
    
    show raka_panik at center with dorong_kiri
    r "Dokter! Sial, siapa yang naruh teh itu di situ?!"
    hide raka_panik
    
    "Dari arah ambang pintu, sekilas terlihat siluet Mbok Darmi, petugas kebersihan Puskesmas. Wajahnya pucat pasi menyadari apa yang terjadi, lalu ia berlari menjauh!"
    
    show rina_lelah at center with mata_mengerjap
    dr "T-tolong... lemari obat... c-campurkan karbon {color=#0044ff}BIRU{/color}... l-lalu sulfat {color=#ff0000}MERAH{/color}... t-terakhir klorin {color=#00ff00}HIJAU{/color}..."
    hide rina_lelah
    
    show bimo_panik at center with dissolve_kilat
    b "Raka, cepat ke lemari obat! Ingat urutannya: Biru, Merah, Hijau! Aku akan mencoba menahan sirkulasi darahnya!"
    hide bimo_panik
    
    # MULAI MINIGAME
    window hide
    call screen mg_racik_penawar
    
    if _return == "win":
        # 3. CG MENANG (Sembuh)
        stop music fadeout 1.0
        play sound "sfx_magic_spell.ogg"
        show it_obat_penawar at truecenter
        scene cg_mg05e_rina_selamat with flash_hijau
        
        "Raka dengan cekatan mencampurkan ketiga bahan tersebut dan memasukkannya ke mulut dr. Rina. Ia terbatuk hebat, namun rasa sakitnya perlahan mereda."
        
        show rina_lelah at center with dissolve_kilat
        dr "Hah... hah... Tirto... P-Pak Kades... d-dia mencoba membungkam saya..."
        hide rina_lelah
        
        play music "bgm_08_fajar_keadilan.ogg" fadein 1.0 loop
        show raka_marah at center with dissolve_kilat
        r "Udah jelas, Dok! Kalo lu mati, rahasianya aman. Apalagi tadi anak buah Pak Kades sempat-sempatnya buntutin kita dan pura-pura bantuin benerin mobil!"
        r "Pak Kades memantau kita dari awal. Sekarang lu mau bantu kita jatohin dia, kan?"
        hide raka_marah
        
        play sound "sfx_buka_tong.ogg"
        play sound "sfx_dapat_item.ogg"
        "Dokter Rina mengangguk lemah. Ia merogoh saku jas putihnya dan menyerahkan sebuah Flashdisk Perekam Suara."
        
        show it_rekaman_tirto at truecenter with transisi_senter
        dr "I-ini... rekaman ancaman langsung dari Pak Tirto yang menyuruh saya memanipulasi autopsi bersama Ki Renggo. Ambil ini... hancurkan dia."
        hide it_rekaman_tirto with dissolve
        
        show bimo_lega at center with dissolve_kilat
        b "Saksi kunci dan bukti mutlak. Dengan ini, kita bisa memastikan Pak Tirto membusuk di penjara."
        hide bimo_lega
        $ rina_hidup = True
        return "win"
        
    else:
        # 4. CG KALAH (Tragis)
        stop music fadeout 0.1
        play sound "sfx_game_over_2.ogg"
        
        scene cg_mg05e_rina_tumbang with transisi_darah
        
        "Raka salah mencampurkan bahan medis (atau kehabisan waktu). Reaksi penolakan di tubuh Dokter Rina semakin hebat hingga akhirnya tubuhnya melemas total dan tumbang di atas meja."
        
        scene bg_ruang_autopsi with hpunch
        show raka_marah at center with dorong_kiri
        r "SIAAALL!! DOKTERNYA MATI! SAKSI KUNCI KITA MATI!"
        hide raka_marah
        
        play music "bgm_12_keadilan_mati.ogg" fadein 1.0 loop
        show bimo_marah at center with dissolve_kilat
        b "Tirto... dia telah merencanakan semuanya! Anak buahnya yang pura-pura memperbaiki mobil kita tadi pasti yang memberi tahu Mbok Darmi kapan harus menaruh racunnya!"
        b "Raka, kejar petugas kebersihan tadi! Jangan sampai dia lolos!"
        hide bimo_marah
        
        play sound "sfx_footsteps_fast.ogg"
        "Raka melesat keluar ruangan dan berhasil meringkus Mbok Darmi di lorong belakang."
        scene cg_chap05_darmi_ditangkap with hpunch
        "Mbok Darmi" "Ampun, Den! Ampun! Saya cuma disuruh Pak Kades Tirto nyampurin serbuk putih ke tehnya Bu Dokter! Saya dikasih duit banyak, saya nggak tahu itu racun mematikan!"
        
        show raka_lelah at center with dissolve_kilat
        r "Brengsek lu, Tirto. Sengaja mutus mata rantai kesaksian."
        hide raka_lelah
        
        show bimo_lelah at center with dissolve_kilat
        b "Kita kehilangan kesaksian resmi dan bukti otentik, tapi setidaknya pengakuan lisan Mbok Darmi memastikan bahwa Pak Kades adalah dalang di balik semua ini."
        hide bimo_lelah
        
        return "lose"