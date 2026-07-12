# ==========================================
# FILE: mg_chap01b.rpy
# MINIGAME: Investigasi Area (Point & Click)
# ==========================================

screen mg_investigasi_gerbang():
    # modal True memastikan pemain harus menyelesaikan minigame ini
    modal True
    
    # Tooltip untuk menampilkan teks saat kursor diarahkan ke objek
    default ttip = Tooltip("Arahkan kursor mouse untuk mencari petunjuk...")
    
    # Tampilan teks instruksi/tooltip di atas layar
    frame:
        xalign 0.5
        ypos 50
        background Solid("#000000cc")
        xpadding 30 ypadding 15
        text ttip.value size 24 color "#ffffff"

    # =======================================
    # OBJEK 1: GEMBOK (Jalur Investigasi Teliti)
    # =======================================
    # Catatan: Sesuaikan angka xpos dan ypos dengan posisi gembok di gambar BG Anda
    button:
        xpos 550 ypos 450 
        xysize (150, 150)
        action Return("gembok")
        hovered ttip.Action("Periksa Gembok Besi yang Rusak")
        
        # Latar transparan saat idle, dan kuning samar saat disorot (hover)
        idle_background Solid("#00000000")
        hover_background Solid("#ffff0044")

    # =======================================
    # OBJEK 2: GARIS POLISI (Jalur Terobos Masuk)
    # =======================================
    button:
        xpos 200 ypos 300 
        xysize (400, 150)
        action Return("garis_polisi")
        hovered ttip.Action("Abaikan dan Terobos Garis Polisi")
        
        idle_background Solid("#00000000")
        hover_background Solid("#ff000044")

    # Tombol Darurat untuk pemain yang bingung / ingin langsung lewat
    textbutton "Abaikan Semua & Masuk":
        xalign 0.95
        yalign 0.95
        action Return("garis_polisi")
        text_size 20

# ==========================================
# Label Pemicu Minigame & Resolusi Cerita
# ==========================================
label play_mg_chap01b:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # Memanggil screen investigasi
    call screen mg_investigasi_gerbang
    
    # Mengeksekusi cerita berdasarkan objek apa yang di-klik pemain
    if _return == "gembok":
        $ ch1_jejak_gembok = True
        play sound "sfx_ding_idea.ogg"
        show raka_normal at center with transisi_senter
        r "Gemboknya dipotong pakai alat pemotong besi hidrolik, dan ada noda bahan kimia di sini."
        r "Jelas banget ini bukan ulah hantu. Buto ijo mana yang bawa-bawa tang potong industri?"
        hide raka_normal
        
        show bimo_lega at center with dissolve_kilat
        b "Pengamatan yang tajam, Raka. Setidaknya kita punya bukti awal adanya campur tangan manusia."
        hide bimo_lega

    elif _return == "garis_polisi":
        $ ch1_jejak_gembok = False
        play sound "sfx_fast_swoosh.ogg"
        show raka_marah at center with dorong_kanan
        r "Ah udahlah, buang waktu mikirin gembok. Mending kita langsung dobrak aja pintu utamanya!"
        hide raka_marah
        
        show citra_panik at center with mata_mengerjap
        c "K-kak Raka, jangan buru-buru dong! Gimana kalau ada jebakan di dalam?"
        hide citra_panik


    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP01B SELESAI")
    # -----------------------------------
    return