# ==========================================
# FILE: mg_chap06c.rpy
# MINIGAME: Retas Brankas Digital
# STYLE: 16-Bit Retro Horror
# ==========================================

# ------------------------------------------
# ASET GAMBAR, BACKGROUND, CG & ITEM
# ------------------------------------------
# Background


# CG Minigame
image cg_mg06c_brankas_rahasia = "images/cg/cg_mg06c_brankas_rahasia.webp"
image cg_mg06c_hacking = "images/cg/cg_mg06c_hacking.webp"
image cg_mg06c_sukses = "images/cg/cg_mg06c_sukses.webp"
image cg_mg06c_gagal = "images/cg/cg_mg06c_gagal.webp"

# Item Bukti Utama


# ------------------------------------------
# SCREEN MINIGAME 3: HACKING KEYPAD
# ------------------------------------------
screen mg_hack_brankas():
    modal True
    
    # -- Deklarasi Variabel Layar --
    default time_left = 20.0
    default entered_pin = ""
    default correct_pin = "3827"
    default status_msg = "MASUKKAN PIN 4 DIGIT"
    default status_color = "#00ff00"

    # Background layar peretasan
    add "cg_mg06c_hacking"
    add "#000000AA" # Gelapkan sedikit agar UI Keypad terbaca jelas

    # -- Timer Hitung Mundur --
    timer 0.1 repeat True action [
        SetScreenVariable("time_left", time_left - 0.1),
        If(time_left <= 0.0, Return(False))
    ]

    # -- UI Tampilan Atas (Petunjuk Hacker) --
    vbox:
        xalign 0.5 yalign 0.05 spacing 5
        text "💻 DECRYPTOR DEVICE v2.1 💻" size 40 color "#00ff00" bold True xalign 0.5
        text "SISA WAKTU: [time_left:.1f] DETIK" size 35 color "#ff0000" bold True xalign 0.5
        null height 10
        
        # Kotak Petunjuk (Riddle)
        frame:
            xalign 0.5
            background "#002200"
            padding (20, 20)
            vbox:
                spacing 5
                text "INTERCEPTED DATA LOG:" size 20 color "#00ff00"
                text "> D1: Angka ganjil di bawah 5, tapi bukan 1." size 22 color "#ffffff"
                text "> D2: Hasil perkalian 2 x 4." size 22 color "#ffffff"
                text "> D3: Angka genap paling pertama (selain 0)." size 22 color "#ffffff"
                text "> D4: Angka keberuntungan sempurna." size 22 color "#ffffff"

    # -- UI Tampilan Layar Brankas (PIN Input) --
    vbox:
        xalign 0.5 yalign 0.45 spacing 15
        
        # Pesan Status
        text "[status_msg]" size 25 color status_color bold True xalign 0.5
        
        # Tampilan Bintang/Angka Input
        frame:
            xalign 0.5
            background "#111111"
            xsize 300 ysize 80
            text "[entered_pin]" size 50 color "#00ff00" bold True xalign 0.5 yalign 0.5 kerning 15.0

    # -- UI Keypad 0-9 --
    grid 3 4:
        xalign 0.5 yalign 0.85
        spacing 15
        
        # Baris 1
        textbutton "1":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "1")]
        textbutton "2":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "2")]
        textbutton "3":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "3")]
            
        # Baris 2
        textbutton "4":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "4")]
        textbutton "5":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "5")]
        textbutton "6":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "6")]
            
        # Baris 3
        textbutton "7":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "7")]
        textbutton "8":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "8")]
        textbutton "9":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "9")]
            
        # Baris 4
        textbutton "CLR":
            text_size 25 xsize 80 ysize 80 text_color "#ff0000"
            action [Play("sound", "sfx_error_win.ogg"), SetScreenVariable("entered_pin", "")]
        textbutton "0":
            text_size 40 xsize 80 ysize 80
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin + "0")]
        textbutton "DEL":
            text_size 25 xsize 80 ysize 80 text_color "#ffff00"
            action [Play("sound", "sfx_bip.ogg"), SetScreenVariable("entered_pin", entered_pin[:-1])]

    # -- Logika Pengecekan PIN Otomatis --
    if len(entered_pin) == 4:
        if entered_pin == correct_pin:
            # Berhasil
            timer 0.1 action Return(True)
        else:
            # Gagal/Salah PIN - Reset input dan kurangi waktu sebagai penalti
            timer 0.1 action [
                Play("sound", "sfx_error_win.ogg"),
                SetScreenVariable("status_msg", "ACCESS DENIED! TIME PENALTY!"),
                SetScreenVariable("status_color", "#ff0000"),
                SetScreenVariable("time_left", time_left - 3.0),
                SetScreenVariable("entered_pin", "")
            ]


# ==========================================
# LABEL PEMICU SCENE & MINIGAME (CUTSCENES)
# ==========================================
label play_mg_chap06c:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # -- Cutscene Menemukan Brankas --
    scene bg_ruang_tirto with transisi_asap
    play music "bgm_03_bayang_petunjuk.ogg" fadein 1.0
    
    show raka_berpikir at right with dissolve_kilat
    r "Kita mencar. Citra, Bimo, cek meja dan laci. Gatot, bantu gue cek dinding, barangkali ada brankas rahasia."

    play sound "sfx_footsteps_fast.ogg"
    "Mereka mulai menggeledah ruangan dengan cepat dan hati-hati."

    play sound "sfx_ding_idea.ogg"
    scene cg_mg06c_brankas_rahasia with transisi_senter
    
    r "Gotcha! Ada brankas tersembunyi di balik lukisan pemandangan ini."
    
    g "Tapi pake kunci kombinasi digital. Lu bisa bobol? Waktu kita nggak banyak, anak buah Tirto lagi patroli."
    
    r "Gue coba sambungin decryptor rakitan gue. Ada log password yang keenkripsi di alat ini."

    # Menghentikan musik sejenak untuk memicu ketegangan
    stop music fadeout 1.0
    "Raka menyambungkan perangkat kecilnya ke panel brankas. Waktu terus berjalan, ia harus memecahkan petunjuk log untuk mendapatkan kombinasi yang pas."
    
    # -- Memanggil Minigame --
    play music "bgm_tense_chase.ogg" fadein 0.5
    call screen mg_hack_brankas
    
    # -- Cutscene Hasil Minigame --
    if _return == True:
        # MENANG: Brankas Terbuka
        play sound "sfx_correct.ogg"
        stop music fadeout 1.0
        
        play sound "sfx_buka_tong.ogg"
        scene cg_mg06c_sukses with flash_hijau
        play music "bgm_08_fajar_keadilan.ogg" fadein 1.0
        
        r "Terbuka! Ini dia, Buku Kas Merah. Isinya lengkap, dari anggaran pakan fiktif, uang tutup mulut dr. Rina, sampai biaya sewa Ki Renggo!"
        
        g "Syukurlah... Akhirnya kebrengsekan Tirto ada buktinya. Pengorbanan temen gue nggak sia-sia."

        # Mendapatkan Item Buku Kas Merah
        play sound "sfx_suara_ting.ogg"
        show item_buku_kas_merah at truecenter with dissolve_kilat
        "Mendapatkan [Buku Kas Merah]!"
        
        # Asumsi variabel ini dideklarasikan di chapter utama
        $ ch6_buku_kas = True
        $ point_investigasi += 1
        
        hide item_buku_kas_merah with dissolve_kilat
        
        return True

    else:
        # KALAH: Waktu Habis / Alarm Berbunyi
        stop music
        play sound "sfx_error_win.ogg"
        scene cg_mg06c_gagal with flashmerah
        
        r "Sial! Sistem pertahanannya kekunci permanen!"
        
        play sound "sfx_buzz_listrik.ogg"
        "Lampu indikator merah menyala terang. Alarm ruangan berbunyi memekakkan telinga."
        
        play sound "sfx_door_kick.ogg"
        "Pintu utama didobrak. Pasukan anak buah Pak Tirto sudah mengepung mereka!"
        
        g "Gawat! Kita ketahuan!"
        
        # Karena ini merupakan rute "Keadilan Pincang" (cerita tetap jalan tapi tidak punya bukti)
        # Kita kembalikan nilai False agar script utama merespons tanpa memberikan buku kas.
        $ ch6_buku_kas = False
        
        return False