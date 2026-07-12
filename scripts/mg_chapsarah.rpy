# ==========================================
# FILE: mg_chapsarah.rpy
# MINIGAME: Cyber-Hack (20 Teka-Teki Plesetan)
# ==========================================

screen mg_sarah_hack():
    modal True
    add "cg_sarah_monitor_data"
    add "#000000dd"

    default questions = [
        ("Lemari apa yang bisa masuk kantong?", "🚪", "🧥", "B"),
        ("Soto apa yang paling bisa dipercaya?", "🥣", "🧪", "A"),
        ("Kenapa pohon kelapa di depan rumah harus ditebang?", "🌴", "🪓", "B"),
        ("Telor apa yang garing?", "🍳", "🥚", "A"),
        ("Huruf apa yang paling kedinginan?", "🥶", "🌡️", "A"),
        ("Sayur apa yang jago nyanyi?", "🥦", "🎤", "B"),
        ("Kenapa air laut asin?", "🌊", "🧂", "B"),
        ("Benda apa yang kalau ditekan malah keluar orangnya?", "🔔", "🚪", "B"),
        ("Ikan apa yang berhenti?", "🛑", "🐟", "A"),
        ("Apa bahasa Jepangnya saya tidak tahu?", "🤷", "🇯🇵", "A"),
        ("Kutu apa yang paling panjang?", "🐜", "🚂", "B"),
        ("Sapi apa yang bisa nempel di tembok?", "🐮", "🕷️", "B"),
        ("Kenapa matahari tenggelam?", "☀️", "📉", "A"),
        ("Kenapa zombie kalau nyerang bareng-bareng?", "🧟", "👥", "B"),
        ("Apa yang punya kaki enam dan bisa terbang?", "🦟", "🚁", "A"),
        ("Buah apa yang pernah menjajah Indonesia?", "🍎", "🍐", "B"),
        ("Kenapa kucing kalau dikejar anjing selalu lari?", "🐱", "🏃", "A"),
        ("Apa yang bikin mobil nggak bisa jalan?", "🚗", "🔧", "B"),
        ("Ikan apa yang paling kaya?", "🐟", "💰", "B"),
        ("Kenapa burung terbang ke selatan saat musim dingin?", "🐦", "🧭", "A")
    ]
    
    # Ambil 5 soal acak dari 20 soal
    default current_game = renpy.random.sample(questions, 5)
    default idx = 0
    default score = 0
    default q_data = current_game[idx]

    vbox:
        xalign 0.5 yalign 0.2
        text "💻 HACKING: TEBAK PLESETAN [idx+1]/5" size 35 color "#00ff00" xalign 0.5
        text "[q_data[0]]" size 40 color "#ffffff" xalign 0.5

    # Grid Pilihan Emoji
    grid 2 1:
        xalign 0.5 yalign 0.6
        spacing 100
        
        # TOMBOL A (Pilihan Kiri)
        textbutton "[q_data[1]]":
            text_size 80
            action [
                If(q_data[3] == "A", SetScreenVariable("score", score + 1)),
                If(idx < 4, 
                    [SetScreenVariable("idx", idx + 1), SetScreenVariable("q_data", current_game[min(idx+1, 4)])], 
                    Return(score + 1 if q_data[3] == "A" else score)
                )
            ]
            
        # TOMBOL B (Pilihan Kanan)
        textbutton "[q_data[2]]":
            text_size 80
            action [
                If(q_data[3] == "B", SetScreenVariable("score", score + 1)),
                If(idx < 4, 
                    [SetScreenVariable("idx", idx + 1), SetScreenVariable("q_data", current_game[min(idx+1, 4)])], 
                    Return(score + 1 if q_data[3] == "B" else score)
                )
            ]

label play_mg_sarah_hack:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    stop music fadeout 1.0
    play music "bgm_10_fokus_spiritual.ogg" fadein 1.0
    
    show sarah_fokus at center with dissolve_kilat
    s "Pak Tirto memakai firewall berbasis plesetan? Benar-benar tidak habis pikir!"
    
    call screen mg_sarah_hack
    $ final_score = _return
    
    if final_score >= 5:
        play sound "sfx_correct.ogg"
        scene black with flash_hijau
        show it_bukti_korupsi at truecenter
        
        "Sarah berhasil menjawab 5 teka-teki! Poin investigasi +1."
        $ point_investigasi = +1
        return True
    elif final_score >= 3:
        show it_bukti_korupsi at truecenter
        "Sarah berhasil menjawab [final_score] teka-teki. Akses terbuka, tapi tidak ada poin investigasi penuh."
        $ point_investigasi = +0
        return True
    else:
        play sound "sfx_static_aggresive.ogg"
        scene cg_sarah_connection_cut with flashmerah
        "Sarah gagal menjawab cukup pertanyaan (Skor: [final_score]). Akses ditolak!"
        return False