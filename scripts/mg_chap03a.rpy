# ==========================================
# FILE: mg_chap03a.rpy
# MINIGAME: Mencari Petunjuk Kalung (Grid Acak)
# ==========================================

# ------------------------------------------
# DEFINISI GAMBAR MINIGAME 03A
# ------------------------------------------
image cg_mg03a_start = "images/cg/cg_mg03a_start.webp"
image bg_mg03a_grid = "images/cg/bg_mg03a_grid.webp"
image cg_mg03a_win = "images/cg/cg_mg03a_win.webp"
image cg_mg03a_lose = "images/cg/cg_mg03a_lose.webp"

# ------------------------------------------
# 1. INISIALISASI PYTHON LOGIC
# ------------------------------------------
init python:
    import random

    def setup_mg_cari():
        # Daftar 16 kotak (Grid 4x4)
        store.mg_cari_grid = []
        for i in range(16):
            # Status awal: "tutup" = belum diklik
            store.mg_cari_grid.append({"isi": "kosong", "status": "tutup", "emoji": "📦"})
        
        # Taruh 1 Kalung (Kunci Kemenangan)
        idx_kalung = random.randint(0, 15)
        store.mg_cari_grid[idx_kalung]["isi"] = "kalung"
        
        # Taruh 4 Tikus Got (Mengurangi Nyawa)
        tikus_count = 0
        while tikus_count < 4:
            idx = random.randint(0, 15)
            if store.mg_cari_grid[idx]["isi"] == "kosong":
                store.mg_cari_grid[idx]["isi"] = "tikus"
                tikus_count += 1
                
        # Status Pemain
        store.mg_cari_nyawa = 5
        store.mg_cari_pesan = "Bongkar tumpukan karung untuk mencari petunjuk!"
        store.mg_cari_status = "main" # main, menang, kalah

    def klik_kotak(idx):
        if store.mg_cari_status != "main":
            return
            
        kotak = store.mg_cari_grid[idx]
        
        if kotak["status"] == "buka":
            return # Cegah klik dua kali pada kotak yang sama
            
        kotak["status"] = "buka"
        
        if kotak["isi"] == "kalung":
            kotak["emoji"] = "📿"
            store.mg_cari_pesan = "KETEMU! Itu kalung milik Galih!"
            renpy.play("sfx_correct.ogg", channel="sound")
            store.mg_cari_status = "menang"
            
        elif kotak["isi"] == "tikus":
            kotak["emoji"] = "🐭"
            store.mg_cari_nyawa -= 1
            store.mg_cari_pesan = "Sial! Digigit tikus got! Kesempatan berkurang."
            renpy.play("sfx_benda_jatuh.ogg", channel="sound")
            
        else: # kosong
            kotak["emoji"] = "💨"
            store.mg_cari_nyawa -= 1
            store.mg_cari_pesan = "Hanya tumpukan debu dan beras busuk..."
            renpy.play("sfx_taruh_benda.ogg", channel="sound")
            
        if store.mg_cari_nyawa <= 0 and store.mg_cari_status != "menang":
            store.mg_cari_pesan = "Kehabisan waktu! Gatot mulai curiga!"
            renpy.play("sfx_error_win.ogg", channel="sound")
            store.mg_cari_status = "kalah"

# ------------------------------------------
# 2. TAMPILAN LAYAR UI (GRID 4x4)
# ------------------------------------------
screen mg_cari_kalung():
    modal True
    
    # Latar Belakang Minigame
    add "bg_mg03a_grid"

    # Frame semi-transparan agar UI tetap terbaca
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 40
        background Solid("#1a1a1acc") # Warna gelap dengan transparansi (cc)
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "MENCARI PETUNJUK" size 30 color "#ffaa00" xalign 0.5 bold True
            
            hbox:
                spacing 50
                xalign 0.5
                text "Kesempatan: [mg_cari_nyawa]/5" size 24 color "#ffffff"
            
            text "[mg_cari_pesan]" size 20 color "#00ccff" xalign 0.5
            
            null height 15
            
            # GRID 4x4 menggunakan vpgrid
            vpgrid:
                cols 4
                spacing 15
                xalign 0.5
                
                for i in range(16):
                    textbutton "[mg_cari_grid[i]['emoji']]":
                        text_size 40
                        xysize (90, 90)
                        background Solid("#3d3d3d")
                        hover_background Solid("#555555")
                        action If(mg_cari_status == "main", 
                            true=Function(klik_kotak, i), 
                            false=None)
            
            null height 20
            
            # Tombol kembali hanya muncul jika menang atau kalah
            if mg_cari_status == "menang":
                textbutton "AMBIL KALUNG & KEMBALI":
                    xalign 0.5
                    text_size 24
                    action Return(True)
            elif mg_cari_status == "kalah":
                textbutton "MENYERAH & KEMBALI":
                    xalign 0.5
                    text_size 24
                    action Return(False)

# ==========================================
# 3. LABEL PEMICU MINIGAME MENCARI KALUNG
# ==========================================
label play_mg_chap03_cari:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Menampilkan Cutscene Awal Minigame
    scene cg_mg03a_start with transisi_senter
    "Raka berjongkok dalam kegelapan, mengarahkan senternya ke tumpukan barang rongsok dan karung beras."
    "Waktu kita tidak banyak sebelum Gatot menyadari keberadaan kita."

    # Jalankan inisialisasi Python
    $ setup_mg_cari()
    play sound "sfx_kelereng_jatuh.ogg"
    
    # Tampilkan layar minigame dan tunggu return dari screen
    call screen mg_cari_kalung
    
    # Evaluasi hasil Return (Menang/Kalah) dan tampilkan Cutscene Resolusi
    if _return == True:
        scene cg_mg03a_win with flashbang
        play sound "sfx_horray.ogg"
        $ poin_investigasi +=1
        $ item_kalung_galih = True
        "Kerja bagus! Di balik tumpukan karung yang berdebu itu, Raka berhasil menemukan sebuah kalung perak."
    else:
        scene cg_mg03a_lose with hpunch
        $ poin_investigasi -=1
        "Kehabisan waktu! Seekor tikus got besar melompat melewati tangan Raka, membuatnya mundur."
        "Raka tidak bisa membongkar area ini lebih lama lagi."
        

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP03_CARI SELESAI")
    # -----------------------------------
    return