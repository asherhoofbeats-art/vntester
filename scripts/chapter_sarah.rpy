# ==========================================
# FILE: chapter_sarah.rpy
# TEMA: Mata Digital di Luar Negeri
# ==========================================

# ------------------------------------------
# DEFINISI ASET SARAH
# ------------------------------------------
image sarah_normal = "images/chars/sarah_normal.webp"
image sarah_fokus = "images/chars/sarah_berpikir.webp"
image sarah_lelah = "images/chars/sarah_lelah.webp"
image sarah_kaget = "images/chars/sarah_panik.webp"

# ------------------------------------------
# DEFINISI CG & ITEM CHAPTER SARAH
# ------------------------------------------
image cg_sarah_workspace = "images/cg/cg_sarah_workspace.webp"
image cg_sarah_pensive = "images/cg/cg_sarah_pensive.webp"
image cg_sarah_monitor_data = "images/cg/cg_sarah_monitor_data.webp"
image cg_sarah_pesan_raka = "images/cg/cg_sarah_pesan_raka.webp"
image cg_sarah_panik_trace = "images/cg/cg_sarah_panik_trace.webp"
image cg_sarah_relief = "images/cg/cg_sarah_relief.webp"
image cg_sarah_connection_cut = "images/cg/cg_sarah_connection_cut.webp"
image it_kunci_enkripsi = "images/item/it_kunci_enkripsi.webp"
image it_bukti_korupsi = "images/item/it_bukti_korupsi.webp"

# ------------------------------------------
# MAIN STORY CHAPTER SARAH
# ------------------------------------------
label chapter_sarah:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Inisialisasi variabel untuk chapter ini
    $ sarah_hack_success = False

    # Tampilan Judul Chapter
    scene black with bangun_tidur
    play music "bgm_04_teror_tak_kasatmata.ogg" fadein 2.0
    centered "{size=+20}CHAPTER SARAH{/size}\n\nOperasi Senyap di Balik Layar" with dissolve_lambat
    pause 2.0
    
    "Sementara Trio Investigator berjuang di lapangan, di belahan bumi lain, Sarah bekerja tanpa henti."
    "Sebagai mata digital tim, ia memiliki akses ke data yang tidak bisa dijangkau oleh siapapun di Indonesia."

    # Scene 1: Ruang Kerja Sarah
    scene cg_sarah_workspace with dissolve_lambat
    "Lampu ruangan temaram. Hanya cahaya dari tiga monitor besar yang menerangi wajah Sarah yang tampak serius."
    
    play sound "sfx_static_noise.ogg"
    "Ting! Sebuah pesan terenkripsi masuk."
    
    scene cg_sarah_pesan_raka with dissolve_kilat
    "Layar laptop menampilkan antarmuka chat terenkripsi dari Raka yang berisi kode akses untuk data mentah kasus korupsi."
    
    s "Akhirnya... data mentah dari mereka sudah sampai. Saatnya bekerja."
    
    "Sarah menggunakan token enkripsi khusus untuk membobol pertahanan siber lawan."
    play sound "sfx_dapat_item.ogg"
    show it_kunci_enkripsi at truecenter with dissolve_kilat
    "Kunci enkripsi ini akan menjadi akses utama Sarah menuju server pusat Pak Tirto."
    hide it_kunci_enkripsi

    # Memanggil Minigame Hacking
    call play_mg_sarah_hack
    $ sarah_hack_success = _return

    # Scene 2: Penemuan Bukti (Bercabang berdasarkan hasil minigame)
    if sarah_hack_success:
        scene cg_sarah_monitor_data with flashbang
        "Sarah berhasil menembus firewall tingkat tinggi. Terpampang nyata daftar transaksi fiktif yang menghubungkan rekening Pak Tirto dengan Ki Renggo."
        
        scene cg_sarah_relief with dissolve_lambat
        show it_bukti_korupsi at truecenter
        play sound "sfx_dapat_item.ogg"
        $ item_bukti_korupsi = True
        $ poin_investigasi +=3
        s "Dapat kau. Semua bukti aliran dana ini sudah cukup untuk membuat jabatan Pak Tirto tamat."
        
        
        "Sarah segera mengunggah salinan bukti tersebut ke cloud aman yang bisa diakses oleh Bimo dan Raka."
        
    else:
        scene cg_sarah_panik_trace with flashmerah
        "Sistem keamanan Pak Tirto terlalu kuat! Jejak digital Sarah terdeteksi dan mulai dilacak oleh firewall musuh."
        play sound "sfx_alert_alarm.ogg"
        $ poin_investigasi -=3
        scene cg_sarah_pensive with dissolve_lambat
        show sarah_lelah at center with dissolve_kilat
        s "Sial, aku terlalu ceroboh. Tapi... setidaknya aku sempat menyalin sebagian kecil data. Semoga itu cukup buat Bimo."
        hide sarah_lelah

    # Penutup Chapter & Kesimpulan
    stop music fadeout 2.0
    scene black with pingsan
    centered "{size=+15}END OF CHAPTER SARAH{/size}" with dissolve_lambat
    pause 1.5

    if sarah_hack_success:
        "KESIMPULAN CHAPTER:\nSarah berhasil mendapatkan bukti mutlak korupsi Pak Tirto. Dengan data ini, Trio Investigator memiliki 'senjata' yang cukup kuat untuk mengguncang kursi kekuasaan Pak Tirto dari akarnya."
    else:
        "KESIMPULAN CHAPTER:\nMeski gagal mendapatkan semua bukti, Sarah berhasil mengamankan potongan penting data yang bisa dijadikan petunjuk bagi tim lapangan. Perang siber ini baru saja dimulai."
    
    pause 3.0

    # Kembali ke alur utama

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_SARAH SELESAI")
    # -----------------------------------
    jump chapter_06