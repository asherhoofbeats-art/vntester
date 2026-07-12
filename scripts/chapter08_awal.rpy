# ==========================================
# FILE: chapter08a.rpy
# TEMA: Pelarian dari Balai Desa yang Terbakar
# ==========================================
image cg_chap08_pahlawan_raka = "images/cg/cg_chap08_pahlawan_raka.webp"
image cg_chap08_pahlawan_bimo = "images/cg/cg_chap08_pahlawan_bimo.webp"
image cg_chap08_pahlawan_citra = "images/cg/cg_chap08_pahlawan_citra.webp"
image cg_chap08_tirto_tong_sampah = "images/cg/cg_chap08_tirto_tong_sampah.webp"
image cg_chap08_renggo_boss = "images/cg/cg_chap08_renggo_boss.webp"
image cg_chap08_raka_terjebak_balkon = "images/cg/cg_chap08_raka_terjebak_balkon.webp"
image cg_chap08_api_balkon_padam = "images/cg/cg_chap08_api_balkon_padam.webp"
image cg_chap08_balkon_kebakaran_game_over = "images/cg/cg_chap08_balkon_kebakaran_game_over.webp"
image bg_final_boss_area = "images/cg/bg_final_boss_area.webp"
image bg_kebakaran_usai = "images/cg/bg_kebakaran_usai.webp"
image bg_kebakaran_usai_raka_gatot_keluar = "images/cg/bg_kebakaran_usai_raka_gatot_keluar.webp"
image cg_balai_desa_api_padam_drone = "images/cg/cg_balai_desa_api_padam_drone.webp"
image cg_balai_desa_terbakar_parah = "images/cg/cg_balai_desa_terbakar_parah.webp"
image cg_chap08_bimo_citra_lihat_kebakaran = "images/cg/cg_chap08_bimo_citra_lihat_kebakaran.webp"
image bg_lapangan_balai_kosong = "images/cg/bg_lapangan_balai_kosong.webp"
image cg_chap08_end_renggo_jadi_abu = "images/cg/cg_chap08_end_renggo_jadi_abu.webp"
image cg_chap08_nita_hantu_menolong = "images/cg/cg_chap08_nita_hantu_menolong.webp"
image cg_chap08_renggo_jadi_abu_mulai = "images/cg/cg_chap08_renggo_jadi_abu_mulai.webp"
image cg_chap08_renggo_jadi_abu_setengah = "images/cg/cg_chap08_renggo_jadi_abu_setengah.webp"
image cg_chap08_rina_damkar = "images/cg/cg_chap08_rina_damkar.webp"
image cg_chap08_rina_siram_air = "images/cg/cg_chap08_rina_siram_air.webp"
image cg_chap08_citra_bimo_kabur = "images/cg/cg_chap08_citra_bimo_kabur.webp"
image cg_bimo_citra_bersiap = "images/cg/siap_minigame08b.webp"
image cg_mg_chap08_pelindung_berhasil = "images/cg/cg_mg_chap08_pelindung_berhasil.webp"
image cg_mg_chap08_pelindung_gagal = "images/cg/cg_mg_chap08_pelindung_gagal.webp"
image cg_chap07_warga_ngamuk = "images/cg/cg_chap07_warga_ngamuk.webp"
image cg_warga_didatangi_buto_bayangan = "images/cg/cg_warga_didatangi_buto_bayangan.webp"
image cg_warga_didatangi_buto_jelas = "images/cg/cg_warga_didatangi_buto_jelas.webp"
image cg_chap08_bimo_diangkat_warga = "images/cg/cg_chap08_bimo_diangkat_warga.webp"
image cg_chap08_citra_diangkat_warga = "images/cg/cg_chap08_citra_diangkat_warga.webp"
image cg_chap08_raka_diangkat_warga = "images/cg/cg_chap08_raka_diangkat_warga.webp"
image bg_lorong_gedung_kades_terbakar = "images/cg/bg_lorong_gedung_kades_terbakar.webp"

label chapter_08_awal:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # ==========================================
    # CHEAT CODE TESTER (Hapus/Komentari saat rilis)
    # ==========================================
    # $ dr_rina_selamat = True
    # $ item_speaker_nita = True
    # $ citra_resonansi_gaib = 5
    # $ ch4_menyan_jafaron = True
    # $ darmi_trust = True
    # ==========================================

    # 1. INTRO CHAPTER
    scene black with bangun_tidur
    play music "bgm_04_teror_tak_kasatmata.ogg" fadein 2.0
    centered "{size=+20}CHAPTER 08 - BAGIAN 1{/size}\n\nApi di Balai Desa" with dissolve_lambat
    pause 1.0
    
    # 2. AWAL KEBAKARAN
    scene cg_balai_desa_terbakar_parah with hpunch
    play sound "sfx_fire_crackling.ogg"
    "Suasana di luar Balai Desa sudah benar-benar tidak terkendali."
    "Warga yang tersulut emosi telah membakar lantai satu. Asap tebal mulai naik menyelimuti lantai dua tempat Trio, Gatot, dan Pak Tirto berada."

    scene bg_lorong_gedung_kades_terbakar with transisi_asap
    show bimo_panik at center with dissolve_kilat
    b "Kita terkepung! Asapnya semakin tebal, api mulai menjalar naik ke sini!"
    
    scene cg_chap07_warga_ngamuk with dissolve
    "Bimo mengintip dari balik tirai jendela. Pemandangan di bawah sana seperti lautan manusia yang dikuasai kemarahan iblis."
    b "Kita harus berpencar. Jika kita semua keluar dari satu titik, kita akan langsung dikeroyok!"
    
    show raka_marah at right with dorong_kiri
    r "Ide bagus. Bimo, lu bawa Citra cari jalan keluar dari jendela samping. Biar gue yang urus dua bangkotan ini."
    
    show gatot_panik at left with dissolve_kilat
    g "Mas Raka! Kita bisa kabur lewat pintu balkon belakang! Apinya belum sampai sana!"
    
    r "Oke, Gatot! Lu seret Pak Kades ke balkon sekarang! Bimo, Citra, semoga beruntung!"

    # ==========================================
    # 3. RUTE BIMO & CITRA (MG_CHAP08B)
    # ==========================================
    scene cg_bimo_citra_bersiap with dissolve
    play sound "sfx_fire_burst.ogg"
    with vpunch
    "Bimo dan Citra berlari menuju ruang kerja rahasia Tirto. Namun naas, api dari lantai bawah tiba-tiba membesar dan memblokir jalan!"
    
    c "Kak Bimo! Apinya terlalu besar! Kita nggak bisa lompat ke jendela!"
    b "Aku akan merapal doa perisai pelindung! Citra, tetap di dekatku!"
    
    # Panggil Minigame Perisai Bimo
    call play_mg_chap08b
    
    if _return == False:
        # GAGAL
        scene cg_mg_chap08_pelindung_gagal with flashmerah
        play sound "sfx_fire_burst.ogg"
        "Api menjilat ruangan tersebut sebelum Bimo selesai merapal doa!"
        scene black with pingsan
        centered "{size=+20}GAME OVER{/size}\n\nBimo dan Citra tewas dalam kobaran api."
        return
        
    # BERHASIL
    scene cg_mg_chap08_pelindung_berhasil with flashbang
    play sound "sfx_magic_spell.ogg"
    "Sebuah pendaran cahaya kebiruan menyelimuti tubuh Bimo dan Citra, menahan hawa panas dari kobaran api!"
    
    scene cg_chap08_citra_bimo_kabur with kaca_pecah
    play sound "sfx_glass_shatter.ogg"
    "Dengan perlindungan gaib tersebut, Bimo menarik Citra dan mereka melompat menerjang kaca jendela, mendarat dengan aman."

    # ==========================================
    # 4. RUTE RAKA, GATOT, TIRTO (MG_CHAP08A - LORONG)
    # ==========================================
    scene bg_lorong_gedung_kades_terbakar with wipe_kanan
    play music "bgm_05_otot_kawat.ogg" fadein 1.0
    "Sementara itu, Raka, Gatot, dan Pak Tirto berlari menyusuri lorong utama yang sudah dipenuhi asap pekat."
    
    scene cg_chap08_rgt_susuri_lorong_terbakar with dissolve
    play sound "sfx_fire_crackling.ogg"
    with hpunch
    g "Uhuk... uhuk... Mas Raka! Kayu atapnya mulai berjatuhan!"
    r "Jangan berhenti! Terus lari ke arah ujung lorong!"
    
    # Panggil Minigame Menembus Lorong
    call play_mg_chap08a
    
    if _return == False:
        # GAGAL
        scene cg_chap08_game_over_mg_raka01 with flashmerah
        play sound "sfx_benda_jatuh.ogg"
        with vpunch
        "Raka terlambat menangkis reruntuhan api. Sebuah balok kayu besar yang terbakar jatuh menimpa mereka bertiga!"
        scene black with pingsan
        centered "{size=+20}GAME OVER{/size}\n\nRaka, Gatot, dan Tirto tertimpa reruntuhan berapi."
        return

    # BERHASIL
    scene cg_chap08_game_win_mg_raka01 with flashbang
    play sound "sfx_serangan_cepat.ogg"
    "HIAAT! Raka menendang dan meninju habis semua proyektil api yang menghalangi jalan, membuka jalur aman untuk mereka lewati."

    # ==========================================
    # 5. RUTE RAKA DI BALKON (MG_CHAP08C)
    # ==========================================
    scene cg_chap08_rgt_win_masuk_balkon with dissolve
    play sound "sfx_strong_kick.ogg"
    "Dengan napas tersengal, mereka mendobrak pintu besi menuju balkon belakang."
    
    "Namun warga ternyata sudah mengepung bagian belakang bangunan. Mereka melihat Raka dan mulai melempar obor ke arah balkon!"
    scene bg_start_mg_obor with vpunch
    r "Sialan! Mereka mau memanggang kita hidup-hidup di sini!"

    # Panggil Minigame Menangkis Obor
    call play_mg_chap08c
    
    if _return == False:
        # GAGAL
        scene cg_chap08_balkon_kebakaran_game_over with flashmerah
        play sound "sfx_fire_burst.ogg"
        with vpunch
        "Sebuah obor lolos dan mengenai tumpukan kayu kering di balkon. Api membesar seketika dan menjebak mereka bertiga!"
        scene black with pingsan
        centered "{size=+20}GAME OVER{/size}\n\nRaka, Gatot, dan Tirto hangus terbakar."
        return

    # BERHASIL
    scene cg_chap08_raka_terjebak_balkon with flashbang
    "Raka berhasil menendang jatuh semua obor yang dilempar warga. Tapi kondisi mereka terkunci."
    "Balkon terlalu tinggi untuk dilompati dengan aman, dan api dari dalam bangunan mulai menjilat pintu balkon."

    # ==========================================
    # 6. RESOLUSI KEBAKARAN (CEK VARIABEL)
    # ==========================================
    if dr_rina_selamat == True:
        # Jika Rina Hidup
        play music "bgm_tense_chase.ogg"
        play sound "sfx_sirine_damkar.ogg"
        "Tiba-tiba, suara sirine meraung memecah keributan massa!"
        
        scene cg_chap08_rina_damkar with dorong_kanan
        "Sebuah truk pemadam kebakaran menerobos masuk ke halaman balai desa. Di kursi penumpang depan, terlihat sosok Dokter Rina!"
        
        scene cg_chap08_rina_siram_air with dissolve_kilat
        play sound "sfx_water_burst.ogg"
        "Ia memimpin tim pemadam untuk langsung menyemprotkan air bertekanan tinggi ke arah balai desa!"
        
        scene cg_chap08_api_balkon_padam with flashbang
        play sound "sfx_water_splash.ogg" # Suara guyuran air kencang
        "Air membasahi sekujur bangunan, mematikan kobaran api yang menjebak Raka di balkon!"
        
    else:
        # Jika Rina Mati
        "Raka merogoh sakunya dengan panik, mencari ponsel untuk memanggil bantuan."
        
        if item_speaker_hantu = True:
            # Punya Speaker Hantu Nita
            play sound "sfx_benda_jatuh.ogg"
            "Karena panik, tangan Raka malah menjatuhkan sebuah benda kotak hitam kecil. Tombol powernya tertekan saat membentur lantai."
            show raka_panik at center
            r "Lah? Ini kan speaker bluetooth bekas Si Hantu Nita?!"
            hide raka_panik
            scene cg_chap08_nita_hantu_menolong with transisi_asap
            play sound "sfx_banshee_scream.ogg"
            "Suhu udara di sekitar balkon mendadak turun drastis. Sosok transparan Nita muncul melayang di udara."
            "Ia meniupkan embusan angin sedingin es yang menyelimuti seluruh bangunan!"
            
            scene cg_chap08_api_balkon_padam with flashbang
            play sound "sfx_water_splash.ogg"
            "Dalam hitungan detik, api yang berkobar padam sepenuhnya, menyisakan kepulan uap dingin di udara."
            
        else:
            # Tidak punya bantuan apa-apa
            scene cg_chap08_balkon_kebakaran_game_over with flashmerah
            play sound "sfx_fire_burst.ogg"
            with hpunch
            
            "Raka mencari-cari ponselnya, namun ia teringat benda itu tertinggal di mobil."
            "Tanpa ada bantuan dari luar, api dari dalam gedung akhirnya menjebol pintu balkon."
            scene black with pingsan
            play music "bgm_12_keadilan_mati.ogg"
            "Ini adalah hukuman karena mereka abai pada keselamatan orang lain."
            centered "{size=+20}GAME OVER{/size}\n\nKarma yang tak termaafkan. Trio tewas terbakar."
            return

    # ==========================================
    # 7. PENUTUP BAGIAN 1
    # ==========================================
    scene cg_chap08_bimo_citra_lihat_kebakaran with dissolve_lambat
    "Api telah berhasil dipadamkan. Trio akhirnya berhasil turun dan berkumpul kembali di lapangan depan balai desa yang kini basah kuyup."
    
    "Mereka mengatur napas, namun ketegangan di udara belum sepenuhnya hilang. Bahaya yang sesungguhnya baru saja dimulai..."
    
    # Lanjut ke Chapter 08 Bagian 2

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_08_AWAL SELESAI")
    # -----------------------------------
    jump chapter_08_akhir