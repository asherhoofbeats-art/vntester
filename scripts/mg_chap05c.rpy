# ==========================================
# FILE: mg_chap05c.rpy
# MINIGAME: Interogasi Dokter Rina (Visual Evidence)
# MEKANIK: Clue Matching / Objection!
# ==========================================

# ------------------------------------------
# DEFINISI ITEM GAMBAR
# ------------------------------------------
# (Definisi Prompt CG dan BG tetap sama dengan sebelumnya)
image cg_mg05c_rina_mengelak = "images/cg/cg_mg05c_rina_mengelak.webp"
image bg_mg05c_interogasi = "images/cg/bg_mg05c_interogasi.webp"
image cg_mg05c_rina_terpojok = "images/cg/cg_mg05c_rina_terpojok.webp"
image cg_mg05c_raka_diusir = "images/cg/cg_mg05c_raka_diusir.webp"
image it_laporan_autopsi_asli = "images/item/it_laporan_autopsi_asli.webp"

# Item Barang Bukti & Pengecoh
image it_projectile_banana_peel = "images/item/it_projectile_banana_peel.webp"
image it_projectile_empty_can = "images/item/it_projectile_empty_can.webp"
image it_projectile_rubber_chicken = "images/item/it_projectile_rubber_chicken.webp"
image it_rekaman_renggo = "images/item/it_rekaman_renggo.webp"
image item_broken_padlock = "images/item/item_broken_padlock.webp"
image item_lendir_kimia = "images/item/item_lendir_kimia.webp"
image it_catatan_dukun = "images/item/it_catatan_dukun.webp"

# ------------------------------------------
# SCREEN UI MINIGAME INTEROGASI
# ------------------------------------------
screen mg_interogasi_rina(statement, health):
    modal True
    
    # Background Meja Autopsi & Partikel Ruangan Dingin
    add "bg_mg05c_interogasi"
    add "debu_melayang"
    add "#000000aa" # Efek gelap dramatis
    
    # Indikator Kesalahan (Nyawa)
    hbox:
        xalign 0.05 yalign 0.05
        spacing 10
        text "KESEMPATAN: " size 24 color "#ffffff" bold True
        for i in range(health):
            text "❤️" size 24
    
    # Pernyataan Dokter Rina
    frame:
        background Solid("#440000cc")
        xalign 0.5 ypos 80
        xpadding 40 ypadding 30
        xsize 1100
        vbox:
            spacing 10
            text "PERNYATAAN DOKTER RINA:" size 24 color "#ffaaaa" xalign 0.5 bold True
            text "\"[statement]\"" size 30 color "#ffffff" xalign 0.5 text_align 0.5 italic True

    # Pilihan Barang Bukti (Inventory Grid)
    vbox:
        xalign 0.5 yalign 0.95
        spacing 15
        
        text "PILIH BUKTI UNTUK MEMBANTAH:" size 26 color "#00ffcc" xalign 0.5 bold True
        
        # Grid 3 kolom, 2 baris untuk memuat 6 item
        grid 3 2:
            spacing 20
            xalign 0.5
            
            # 1. Lendir Kimia
            button:
                xysize (280, 180)
                background Solid("#225522ee")
                hover_background Solid("#44aa44ee")
                action Return("lendir")
                vbox:
                    xalign 0.5 yalign 0.5 spacing 10
                    add "item_lendir_kimia" fit "contain" xysize (100, 100) xalign 0.5
                    text "Lendir Hijau" size 22 xalign 0.5
                    
            # 2. Catatan Dukun
            button:
                xysize (280, 180)
                background Solid("#552222ee")
                hover_background Solid("#aa4444ee")
                action Return("catatan")
                vbox:
                    xalign 0.5 yalign 0.5 spacing 10
                    add "it_catatan_dukun" fit "contain" xysize (100, 100) xalign 0.5
                    text "Buku Catatan" size 22 xalign 0.5
                    
            # 3. Rekaman Ki Renggo
            button:
                xysize (280, 180)
                background Solid("#222255ee")
                hover_background Solid("#4444aaee")
                action Return("rekaman")
                vbox:
                    xalign 0.5 yalign 0.5 spacing 10
                    add "it_rekaman_renggo" fit "contain" xysize (100, 100) xalign 0.5
                    text "Rekaman Suara" size 22 xalign 0.5

            # 4. PENGECOH: Kulit Pisang
            button:
                xysize (280, 180)
                background Solid("#555522ee")
                hover_background Solid("#aaaa44ee")
                action Return("pisang")
                vbox:
                    xalign 0.5 yalign 0.5 spacing 10
                    add "it_projectile_banana_peel" fit "contain" xysize (100, 100) xalign 0.5
                    text "Kulit Pisang" size 22 xalign 0.5

            # 5. PENGECOH: Ayam Karet
            button:
                xysize (280, 180)
                background Solid("#552255ee")
                hover_background Solid("#aa44aaee")
                action Return("ayam")
                vbox:
                    xalign 0.5 yalign 0.5 spacing 10
                    add "it_projectile_rubber_chicken" fit "contain" xysize (100, 100) xalign 0.5
                    text "Ayam Karet" size 22 xalign 0.5

            # 6. PENGECOH: Gembok Rusak
            button:
                xysize (280, 180)
                background Solid("#333333ee")
                hover_background Solid("#666666ee")
                action Return("gembok")
                vbox:
                    xalign 0.5 yalign 0.5 spacing 10
                    add "item_broken_padlock" fit "contain" xysize (100, 100) xalign 0.5
                    text "Gembok Rusak" size 22 xalign 0.5

# ------------------------------------------
# LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap05c:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    $ mg05c_health = 3
    
    # MUSIK TEGANG DIMULAI
    stop music fadeout 1.0
    play music "bgm_05_otot_kawat.ogg" fadein 1.0 loop
    
    scene cg_mg05c_rina_mengelak with flashbang
    play sound "sfx_gebrak_meja.ogg"
    
    show raka_marah at center with dorong_kanan
    r "Nggak usah pura-pura, Dok! Kita tahu lu yang bayar Ki Renggo buat malsuin TKP biar kelihatan kayak ulah Buto Ijo!"
    hide raka_marah
    
    show rina_normal at center with dorong_kiri
    dr "Tuduhan dari mana itu?! Mana buktinya kalau berani menuduh saya memalsukan hasil autopsi?!"
    hide rina_normal
    
    "Tunjukkan bukti investigasi yang tepat dari ranselmu untuk mematahkan argumen Dokter Rina!"

    # ==========================
    # RONDE 1
    # ==========================
    label .ronde_1:
        window hide
        call screen mg_interogasi_rina("Kalian tidak punya bukti kalau serangan Buto Ijo itu palsu! TKP di dapur dipenuhi oleh lendir monster!", mg05c_health)
        
        if _return == "lendir":
            play sound "sfx_correct.ogg"
            scene bg_mg05c_interogasi with flash_biru
            show raka_lega at center with dissolve_kilat
            r "OBJECTION! Lendir hijau di TKP itu palsu! Bimo udah menganalisisnya, itu cuma campuran bahan kimia dan sabun cuci!"
            hide raka_lega
            jump .ronde_2
        else:
            call .salah_tebak(_return)
            if mg05c_health <= 0:
                jump .kalah_interogasi
            jump .ronde_1

    # ==========================
    # RONDE 2
    # ==========================
    label .ronde_2:
        play sound "sfx_bashing.ogg"
        scene bg_mg05c_interogasi
        show rina_lelah at center with vpunch
        dr "Ugh... L-lalu kenapa kalau lendirnya palsu?! Bisa saja ada warga iseng! Itu tidak membuktikan saya menyewa dukun!"
        hide rina_lelah
        
        window hide
        call screen mg_interogasi_rina("Siapapun bisa menaburkan lendir itu! Kalian tidak punya bukti tertulis kalau saya berhubungan dengan dukun palsu itu!", mg05c_health)
        
        if _return == "catatan":
            play sound "sfx_correct.ogg"
            scene bg_mg05c_interogasi with flash_biru
            show raka_marah at center with dissolve_kilat
            r "OBJECTION! Di Buku Catatan Ki Renggo yang gue temuin, ada nama lu mentransfer uang puluhan juta tepat sehari setelah kematian staf dapur!"
            hide raka_marah
            jump .ronde_3
        else:
            call .salah_tebak(_return)
            if mg05c_health <= 0:
                jump .kalah_interogasi
            jump .ronde_2

    # ==========================
    # RONDE 3 (FINAL)
    # ==========================
    label .ronde_3:
        play sound "sfx_gebrak_meja.ogg"
        scene bg_mg05c_interogasi
        show rina_panik at center with hpunch
        dr "I-itu... itu uang sumbangan puskesmas untuk padepokan! Saya tidak pernah secara eksplisit menyuruh dia memalsukan skenario Buto Ijo!"
        hide rina_panik
        
        window hide
        call screen mg_interogasi_rina("Itu hanya uang sumbangan biasa! Kalian sama sekali tidak memiliki pengakuan langsung tentang konspirasi ini!", mg05c_health)
        
        if _return == "rekaman":
            play sound "sfx_winning_quiz.ogg"
            scene bg_mg05c_interogasi with flashbang
            show raka_lega at center with dissolve_kilat
            r "SKAKMAT, DOKTER RINA! Gue punya rekaman suara Ki Renggo pas kita interogasi tadi. Dia nangis-nangis ngaku kalau Dokter Rina dari Puskesmas yang nyuruh dia nyiram lendir dan ngerobek perut mayat!"
            hide raka_lega
            jump .menang_interogasi
        else:
            call .salah_tebak(_return)
            if mg05c_health <= 0:
                jump .kalah_interogasi
            jump .ronde_3

    # ==========================
    # LABEL KHUSUS: SALAH TEBAK & PENGECOH
    # ==========================
    label .salah_tebak(item_id):
        play sound "sfx_insting_salah.ogg"
        scene bg_mg05c_interogasi with flashmerah
        with hpunch
        
        if item_id == "pisang":
            show raka_berpikir at center with dissolve_kilat
            r "OBJECTION! Buktinya adalah kulit pisang ini! Pasti Ki Renggo kepeleset waktu lagi sibuk malsuin TKP!"
            hide raka_berpikir
            show rina_marah at center with dissolve_kilat
            dr "Apa-apaan itu?! Jangan membawa sampah ke ruang autopsi saya! Kulit pisang busuk tidak membuktikan apa-apa!"
            hide rina_marah
            
        elif item_id == "ayam":
            show raka_lega at center with dissolve_kilat
            r "OBJECTION! Ayam karet ini adalah kuncinya! Dukun itu pasti meremas ayam ini untuk menakut-nakuti warga kan?!"
            hide raka_lega
            show rina_lelah at center with dissolve_kilat
            dr "Kamu ini detektif atau pelawak?! Singkirkan mainan konyol bersuara aneh itu dari meja saya!"
            hide rina_lelah
            
        elif item_id == "gembok":
            show raka_panik at center with dissolve_kilat
            r "OBJECTION! Gembok rusak ini bukti kalau ada pembobolan paksa di area puskesmas!"
            hide raka_panik
            show rina_marah at center with dissolve_kilat
            dr "Itu gembok loker yang baru saja kamu rusak di luar kan?! Saya akan menagih ganti ruginya nanti! Itu tidak ada hubungannya dengan autopsi!"
            hide rina_marah
            
        else:
            # Jika menyodorkan bukti asli tapi di ronde yang salah (misal: menyodorkan rekaman di ronde 1)
            show raka_marah at center with dissolve_kilat
            r "OBJECTION! Coba perhatikan baik-baik barang bukti ini!"
            hide raka_marah
            show rina_marah at center with dissolve_kilat
            dr "Hah! Argumenmu berantakan! Bukti itu sama sekali tidak relevan dengan pernyataan saya barusan!"
            hide rina_marah
            
        $ mg05c_health -= 1
        return

    # ==========================
    # KONDISI MENANG
    # ==========================
    label .menang_interogasi:
        stop music fadeout 0.5
        play sound "sfx_emotional_damage.ogg"
        
        scene cg_mg05c_rina_terpojok with vpunch
        dr "T-TIDAAAKK...!!"
        
        "Dokter Rina berkeringat dingin dan menggebrak meja dengan putus asa. Seluruh kebohongannya telah dihancurkan oleh Raka."
        
        play sound "sfx_taruh_sesuatu.ogg"
        "Dengan tangan gemetar, ia membuka laci mejanya dan melemparkan sebuah map merah ke arah Raka."
        
        scene bg_ruang_autopsi with transisi_asap
        show it_laporan_autopsi_asli at truecenter with dissolve_lambat
        play sound "sfx_dapat_item.ogg"
        dr "I-ini... Laporan Autopsi Asli sebelum saya ubah. Mereka mati karena... racun arsenik."
        
        "Kalian mendapatkan 'Laporan Autopsi Asli'!"
        hide it_laporan_autopsi_asli with dissolve
        
        return "win"

    # ==========================
    # KONDISI KALAH
    # ==========================
    label .kalah_interogasi:
        stop music fadeout 0.5
        play sound "sfx_door_banging_massive.ogg"
        
        scene bg_mg05c_interogasi with hpunch
        show rina_marah at center with dorong_bawah
        dr "CUKUP! Argumen kalian muter-muter dan konyol! SEKURITI!!"
        hide rina_marah
        
        scene cg_mg05c_raka_diusir with slide_bawah
        play sound "sfx_menabrak_kocak.ogg"
        
        "Dua petugas keamanan bertubuh besar menerobos masuk dan langsung menyeret Raka serta Bimo keluar dari ruang autopsi secara paksa."
        
        show raka_marah at center with dissolve_kilat
        r "Woy lepasin! Gue belum selesai interogasi! Argh!"
        hide raka_marah
        
        return "lose"