# ==========================================
# FILE: mg_chap04e.rpy
# MINIGAME: Membuka Kunci Kotak Jimat (Fokus Citra)
# MEKANIK: Memory Sequence (Simon Says)
# ==========================================

# ------------------------------------------
# DEFINISI CG & BACKGROUND MINIGAME 04E
# ------------------------------------------
# 1. Permainan Dimulai (Citra menemukan kotak)
# PROMPT AI: 16-bit SNES pixel art style. Close-up of a young woman's hands (Citra) holding a small, old, intricately carved wooden puzzle box. The box looks mysterious. Blurry background of a dark shaman hut. Visual novel CG.
image cg_mg04e_kotak_ditemukan = "images/cg/cg_mg04e_kotak_ditemukan.webp"

# 2. Latar Permainan (Permainan Berlangsung)
# PROMPT AI: 16-bit SNES pixel art style. Top-down close-up view of an ancient wooden puzzle box. The box has four distinct square wooden buttons carved with mysterious Javanese symbols. Magical and mysterious atmosphere. Game UI background.
image bg_mg04e_kotak_puzzle = "images/cg/bg_mg04e_kotak_puzzle.webp"

# 3. Jika Menang (Menyan Jafaron Terbuka)
# PROMPT AI: 16-bit SNES pixel art style. The ancient wooden puzzle box is now open. Inside, resting on dark velvet, is a chunk of glowing, deep blood-red mystical incense resin (Menyan Jafaron). It emits a soft, magical red aura. Visual novel item CG.
image cg_mg04e_menyan_jafaron = "images/cg/cg_mg04e_menyan_jafaron.webp"

# 4. Jika Kalah (Kotak Macet)
# PROMPT AI: 16-bit SNES pixel art style. The ancient wooden puzzle box looks jammed and slightly broken, with small wooden splinters sticking out. A young woman's hands are pulling away in disappointment. Visual novel CG.
image cg_mg04e_kotak_macet = "images/cg/cg_mg04e_kotak_macet.webp"


init python:
    import random
    
    # Fungsi untuk membuat urutan aksara acak (4 langkah agar ramah mobile)
    def generate_aksara_seq():
        symbols = ["AKSARA UTARA", "AKSARA SELATAN", "AKSARA BARAT", "AKSARA TIMUR"]
        return [random.choice(symbols) for _ in range(4)]

# ------------------------------------------
# SCREEN UI MINIGAME MEMORY
# ------------------------------------------
screen mg_buka_kotak_jimat(target_seq, memory_time, input_time):
    modal True
    
    default phase = "MEMORIZE"
    default timer_val = memory_time
    default current_input = []
    default status_msg = "HAFALKAN URUTAN KUNCI INI!"
    
    # Latar Belakang Kotak Kayu (Permainan Berlangsung)
    add "bg_mg04e_kotak_puzzle"
    add "#000000aa" # Lapisan gelap agar teks terbaca
    
    timer 1.0 action [
        If(timer_val > 0,
            SetScreenVariable("timer_val", timer_val - 1),
            If(phase == "MEMORIZE",
                [SetScreenVariable("phase", "INPUT"), SetScreenVariable("timer_val", input_time), SetScreenVariable("status_msg", "TEKAN TOMBOL SESUAI URUTAN!")],
                Return("timeout")
            )
        )
    ] repeat True
    
    frame:
        xalign 0.5 yalign 0.5
        xpadding 50 ypadding 50
        background Solid("#2a1b12e6") # Warna cokelat kayu gelap
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "TEKA-TEKI KOTAK JIMAT" size 32 color "#ffcc00" xalign 0.5 bold True
            text status_msg size 20 color "#ffffff" xalign 0.5
            
            if phase == "MEMORIZE":
                text "Waktu Menghafal: [timer_val] detik" size 24 color "#55ffff" xalign 0.5
            else:
                text "Sisa Waktu: [timer_val] detik" size 24 color "#ffaa00" xalign 0.5
            
            null height 20
            
            # Area Display Urutan
            hbox:
                spacing 15
                xalign 0.5
                if phase == "MEMORIZE":
                    for s in target_seq:
                        frame:
                            background Solid("#4a3219")
                            padding (10, 10)
                            text s size 20 color "#ffcccc"
                else:
                    for s in current_input:
                        frame:
                            background Solid("#3a5f2b") # Hijau saat ditekan
                            padding (10, 10)
                            text s size 20 color "#55ff55"
                    for i in range(len(target_seq) - len(current_input)):
                        frame:
                            background Solid("#222222")
                            padding (10, 10)
                            text "???" size 20 color "#777777"
            
            null height 30
            
            # Tombol Input (Hanya di fase INPUT)
            if phase == "INPUT":
                grid 2 2:
                    xalign 0.5
                    spacing 20
                    for sym in ["AKSARA UTARA", "AKSARA SELATAN", "AKSARA BARAT", "AKSARA TIMUR"]:
                        textbutton sym:
                            text_size 24
                            action [
                                Play("sound", "sfx_stone_grind_pencet.ogg"),
                                SetScreenVariable("current_input", current_input + [sym]),
                                
                                If(current_input + [sym] == target_seq[:len(current_input)+1],
                                    If(len(current_input) + 1 == len(target_seq),
                                        Return("win")
                                    ),
                                    Return("wrong")
                                )
                            ]

# ------------------------------------------
# LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap04e:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # CUT SCENE 1: Menemukan Kotak
    scene cg_mg04e_kotak_ditemukan with transisi_asap
    play sound "sfx_barang_berjatuhan_dari_kantong.ogg"
    
    "Saat melucuti sabuk Ki Renggo, Citra menemukan sebuah kotak kayu kecil dengan ukiran yang rumit. Kotak itu tidak memiliki lubang kunci, melainkan empat tombol tuas."
    
    c "(Wah, kelihatannya ini kotak rahasia. Aku harus menekan ukirannya dengan urutan yang benar untuk membukanya.)"
    
    $ current_target_seq = generate_aksara_seq()
    $ mg_input_time = 10 
    $ nyawa_kotak = 3 # Kesempatan salah 2 kali sebelum kotak macet
    
    play music "bgm_10_fokus_spiritual.ogg" fadein 1.0
    
    label .retry_kotak:
        window hide
        call screen mg_buka_kotak_jimat(current_target_seq, 4, mg_input_time)
        
        if _return == "win":
            # CUT SCENE 3: MENANG (DAPAT MENYAN JAFARON)
            $ ch4_menyan_jafaron = True
            $ citra_resonansi_gaib = getattr(store, "citra_resonansi_gaib", 0) + 1
            $ poin_investigasi +=2
            stop music fadeout 1.0
            play sound "sfx_creaky_door_open.ogg"
            scene cg_mg04e_menyan_jafaron with flashbang
            play sound "sfx_zing_muncul_pamer.ogg"
            
            "KLIK! Penutup kotak kayu itu terbuka."
            "Di dalamnya terdapat sebongkah resin berwarna merah darah pekat yang memancarkan aroma mistis yang sangat kuat."
            
            scene bg_padepokan_dalam with dissolve
            show citra_lega at center with dissolve_kilat
            c "Kak Bimo, lihat! Aku nemu sesuatu di kantong Ki Renggo."
            hide citra_lega
            
            show bimo_normal at center with dissolve_kilat
            b "Astaga... Itu Menyan Jafaron kualitas tinggi. Ini benda yang sangat langka dan memiliki energi penolak bala yang luar biasa kuat."
            b "Simpan baik-baik, Citra. Benda ini akan sangat berguna untuk melindungi kita dari serangan gaib yang lebih besar nanti."
            hide bimo_normal
            
            return
            
        elif _return == "wrong" or _return == "timeout":
            # JIKA SALAH TEKAN / WAKTU HABIS
            $ nyawa_kotak -= 1
            play sound "sfx_sudden_crack.ogg"
            scene bg_mg04e_kotak_puzzle with hpunch
            
            if nyawa_kotak > 0:
                c "Duh! Tombolnya agak keras... Salah urutan nih. Aku harus coba lagi, tapi kayanya mekanismenya makin ringkih."
                jump .retry_kotak
            else:
                # CUT SCENE 4: KALAH (KOTAK MACET)
                $ citra_resonansi_gaib = getattr(store, "citra_resonansi_gaib", 0) - 1
                $ ch4_menyan_jafaron = False
                $ poin_investigasi -=1
                stop music fadeout 1.0
                play sound "sfx_wooden_crate_break.ogg"
                scene cg_mg04e_kotak_macet with vpunch
                
                "KRAK!"
                "Karena terlalu sering salah menekan, mekanisme kunci kuno di dalam kotak itu patah. Tombol-tombolnya kini tersangkut dan tidak bisa ditekan lagi."
                
                scene bg_padepokan_dalam with dissolve
                show citra_lelah at center with dissolve_kilat
                c "Yah... rusak deh. Susah banget sih teka-tekinya."
                hide citra_lelah
                
                show raka_normal at center with dissolve_kilat
                r "Udah, biarin aja Cit. Paling isinya cuma jimat pelet atau apalah. Sini bantuin gue ngiket si dukun."
                hide raka_normal
                
                return