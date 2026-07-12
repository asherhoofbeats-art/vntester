# ==========================================
# FILE: mg_chap05d.rpy
# MINIGAME: Keseimbangan Trance (Bimo & Citra)
# MEKANIK: Slider Balancing
# ==========================================

# ------------------------------------------
# DEFINISI PROMPT & GAMBAR MINIGAME 05D
# ------------------------------------------
# 1. CG Awal - Citra Masuk
# Prompt: 16-bit SNES pixel art style, visual novel CG. A young woman with a simple white bandage around her head stands at the doorway of a cold clinic room. She looks exhausted and is holding her head in pain. Eerie atmosphere.
image cg_mg05d_citra_masuk = "images/cg/cg_mg05d_citra_masuk.webp"
image cg_ch05_citra_mencekik = "images/cg/cg_ch05_citra_mencekik.webp"

# 2. CG Puncak Kesurupan - Mencekik
# Prompt: 16-bit SNES pixel art style, visual novel CG. A young woman surrounded by a dark purple magical aura, floating slightly, reaching her hands aggressively toward a shocked female doctor in a white coat. Dramatic supernatural confrontation.
image cg_mg05d_citra_mencekik = "images/cg/cg_mg05d_citra_mencekik.webp"

# 3. BG Gameplay - Alam Bawah Sadar
# Prompt: 16-bit SNES pixel art style, visual novel BG. Abstract supernatural background representing a chaotic mind. Swirling dark purple and bright cyan magical energies clashing together. Intense mystical atmosphere.
image bg_mg05d_trance = "images/cg/bg_mg05d_trance.webp"

# 4. CG Menang - Menstabilkan
# Prompt: 16-bit SNES pixel art style, visual novel CG. A young man places his softly glowing bright blue magical thumb gently on the forehead of a young woman. The dark purple aura around her is fading into a calm blue light. Peaceful purification spell.
image cg_mg05d_bimo_stabil = "images/cg/cg_mg05d_bimo_stabil.webp"

# 5. CG Kalah - Tamparan Segel Paksa
# Prompt: 16-bit SNES pixel art style, visual novel CG. A young man forcefully hits the forehead of a possessed young woman with his glowing bright blue magical palm. A violent burst of magical sparks and dark smoke colliding. High-action supernatural exorcism.
image cg_mg05d_bimo_tampar = "images/cg/cg_mg05d_bimo_tampar.webp"


# ------------------------------------------
# FUNGSI PYTHON LOGIKA SLIDER BALANCING
# ------------------------------------------
init python:
    import random

    class TranceBalanceGame:
        def __init__(self):
            self.pos = 50.0  # Posisi indikator (0 sampai 100), mulai di tengah
            self.velocity = 0.0
            self.safe_time = 0.0
            self.target_time = 5.0 # Harus bertahan di zona aman selama 5 detik
            self.status = "playing"
            
            # Energi arwah yang acak (menarik ke kiri/kanan)
            self.chaos = random.choice([-1.0, 1.0])

        def update(self):
            if self.status != "playing":
                return

            # Perubahan arah tarikan secara acak setiap saat
            if random.random() < 0.05:
                self.chaos = random.uniform(-2.5, 2.5)

            # Tambahkan tarikan gaib ke kecepatan
            self.velocity += self.chaos
            
            # Gesekan agar tidak terlalu melesat liar
            self.velocity *= 0.85
            
            # Terapkan kecepatan ke posisi
            self.pos += self.velocity

            # Cek Kondisi Kalah (Indikator menyentuh ujung kiri atau kanan)
            if self.pos <= 0 or self.pos >= 100:
                self.status = "lose"

            # Cek Zona Aman (Antara posisi 35 sampai 65)
            if 35 <= self.pos <= 65:
                self.safe_time += 0.05 # Menambah waktu progres (asumsi 20fps timer)
                if self.safe_time >= self.target_time:
                    self.status = "win"
            else:
                # Waktu progres berkurang cepat jika keluar dari zona aman
                self.safe_time = max(0.0, self.safe_time - 0.1)

        def push(self, amount):
            # Tarikan/Dorongan dari pemain
            if self.status == "playing":
                self.velocity += amount


# ------------------------------------------
# SCREEN UI MINIGAME BALANCING
# ------------------------------------------
screen mg_trance_keseimbangan():
    modal True
    
    default game = TranceBalanceGame()
    
    # Timer utama berjalan sekitar 20fps
    timer 0.05 action Function(game.update) repeat True

    # Background mistis & efek partikel
    add "bg_mg05d_trance"
    add "debu_melayang"
    add "#00000066"

    # ==========================
    # HUD & INFORMASI
    # ==========================
    vbox:
        xalign 0.5 ypos 50
        spacing 10
        
        text "STABILKAN ENERGI ARWAH!" size 36 color "#00ffcc" xalign 0.5 bold True
        text "Jaga indikator tetap di ZONA BIRU tengah!" size 24 color "#ffffff" xalign 0.5
        
        # Bar Progres Kemenangan
        bar:
            value AnimatedValue(game.safe_time, game.target_time, 0.5) 
            range game.target_time 
            xsize 600 ysize 25 xalign 0.5
            left_bar Solid("#00ffcc")
            right_bar Solid("#333333")

    # ==========================
    # AREA SLIDER KESEIMBANGAN
    # ==========================
    # Latar Belakang Bar Keseimbangan
    frame:
        background Solid("#333333cc")
        xalign 0.5 yalign 0.5
        xsize 800 ysize 60
        
        # ZONA AMAN (Tengah)
        frame:
            background Solid("#0044ff88")
            xalign 0.5 yalign 0.5
            xsize 240 ysize 60 # Lebar zona aman 30% dari total (dari 35 ke 65)
        
        # Indikator Posisi Saat Ini
        text "🔥":
            size 50
            yalign 0.5
            xpos (game.pos / 100.0)
            xanchor 0.5

    # ==========================
    # KONTROL PEMAIN
    # ==========================
    hbox:
        xalign 0.5 yalign 0.85
        spacing 100
        
        textbutton "⬅️ TAHAN KIRI":
            text_size 30
            xysize (300, 100)
            background Solid("#882222ee")
            hover_background Solid("#ff4444ee")
            action Function(game.push, -4.0)
            
        textbutton "TAHAN KANAN ➡️":
            text_size 30
            xysize (300, 100)
            background Solid("#222288ee")
            hover_background Solid("#4444ffee")
            action Function(game.push, 4.0)

    # Keyboard Binds
    key "K_LEFT" action Function(game.push, -4.0)
    key "K_RIGHT" action Function(game.push, 4.0)

    # Cek Kondisi
    if game.status == "win":
        timer 0.1 action Return("win")
    elif game.status == "lose":
        timer 0.1 action Return("lose")


# ------------------------------------------
# LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap05d:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # 1. CG INTRO: Citra Masuk
    stop music fadeout 1.5
    play sound "sfx_buzz_listrik.ogg"
    
    scene cg_mg05d_citra_masuk with transisi_asap
    "Tiba-tiba, lampu neon di ruang autopsi berkedip cepat. Suhu ruangan anjlok drastis."
    
    play music "bgm_06_panggilan_arwah.ogg" fadein 1.0
    play sound "sfx_heartbeat_fast.ogg" loop
    
    "Pintu terbuka. Citra melangkah masuk sambil memegangi kepalanya yang diperban. Auranya terasa sangat pekat dan kelam."
    
    c "Kak Bimo... h-hawanya... sakit... leherku sakit..."
    
    # 2. CG KESURUPAN
    play sound "sfx_glitch_kesurupan.ogg"
    scene cg_mg05d_citra_mencekik with tv_rusak
    
    c "{b}KENAPA KAU BIARKAN KAMI MATI?! PENGECUT!!{/b}"
    
    play sound "sfx_fast_swish.ogg"
    scene cg_ch05_citra_mencekik with blood_splatter
    "Dengan kecepatan luar biasa, Citra melompat, mencekik leher dr. Rina, dan mengangkat tubuhnya secara gaib."
    
    play sound "sfx_gasp.ogg"
    dr "AARGHH... L-lepaskan... t-tolong...!"
    
    b "Energi arwah ini sangat tidak stabil! Aku harus menahannya agar Citra bisa mengendalikannya dan bicara!"
    
    # MULAI MINIGAME
    window hide
    call screen mg_trance_keseimbangan
    
    if _return == "win":
        # 3. CG MENANG
        stop sound fadeout 1.0
        play sound "sfx_magic_spell.ogg" loop
        
        scene cg_mg05d_bimo_stabil with dissolve_lambat
        "Bimo berhasil menempelkan ibu jarinya di dahi Citra, merapal mantra penstabil jiwa."
        "Aura kelam itu memudar. Arwah di dalam tubuh Citra kini cukup tenang untuk berbicara melalui mulutnya."
        
        scene bg_ruang_autopsi with dissolve_kilat
        c "{b}KAU TAHU KAMI DIBERIKAN ARSENIK! KAU TAHU PERUT KAMI DIROBEK SETELAH KAMI MATI! KATAKAN YANG SEBENARNYA!{/b}"
        
        show rina_lelah at center with dorong_bawah
        dr "I-IYA! S-SAYA MENGAKU! MEREKA DIRACUN ARSENIK OLEH PAK TIRTO! Tolong lepaskan saya!"
        hide rina_lelah
        
        stop sound fadeout 0.5
        play sound "sfx_wuzz_menghilang.ogg"
        "Bimo menarik paksa sisa arwah itu keluar. Citra terbatuk dan melepaskan dr. Rina yang jatuh terduduk lemas di kursinya."
        
        return "win"
        
    else:
        # 4. CG KALAH
        play sound "sfx_bone_crack.ogg"
        "Energi arwah itu terlalu buas dan menarik Citra ke arah kegelapan. Cekikannya semakin kuat hingga dr. Rina hampir kehilangan napas."
        
        b "Tidak ada pilihan lain! TOLAK BALA!"
        
        stop sound fadeout 0.5
        play sound "sfx_punch.ogg"
        scene cg_mg05d_bimo_tampar with flashbang
        with hpunch
        
        "Bimo terpaksa menampar dahi Citra dengan segel telapak tangannya. Arwah itu meledak keluar dan terpental."
        
        scene bg_ruang_autopsi with transisi_asap
        "Citra langsung jatuh pingsan tak sadarkan diri di lantai ruang autopsi yang dingin. Dokter Rina jatuh terduduk di kursinya, bernapas sangat tersengal-sengal dan membelalak ketakutan."
        
        return "lose"