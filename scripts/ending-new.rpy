# ==========================================
# FILE: ending.rpy
# KUMPULAN 6 ENDING BERDASARKAN NASIB TIRTO
# ==========================================

# ==========================================
# MESIN EVALUASI ENDING (PENENTU NASIB TIRTO)
# ==========================================
label evaluasi_ending_utama:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # 1. CEK ABSOLUTE TRUE ENDING
    if (poin_investigasi > 8 and citra_resonansi_gaib > 8 and item_jenglot == True and 
        (item_gembok_berlendir == True or item_gembok_rusak == True) and item_lendir_hijau == True and 
        item_bukti_otopsi == True and item_rekaman_tirto == True and item_rekaman_renggo == True and 
        item_buku_kas_merah == True and gatot_trust == True and dr_rina_selamat == True and 
        item_speaker_hantu == True and item_koin_kuno == True):
        
        jump ending_tirto_digentayangi

    # 2. CEK GOOD ENDING (STARTUP DETEKTIF)
    elif poin_investigasi >= 6 and item_buku_kas_merah == True and item_rekaman_tirto == True and darmi_trust == True:
        jump ending_startup_trio

    # 3. CEK BAD KARMA ENDING (PENERUS RENGGO)
    elif item_boneka_jerami == True and item_kristal_merah == False:
        jump ending_penerus_renggo

    # 4. CEK DARK COMEDY ENDING (TIRTO GILA KABUR)
    elif gatot_trust == False and item_kalung_galih == True:
        jump ending_tirto_gila

    # 5. CEK BAD INVESTIGATION ENDING (TIRTO BEBAS)
    elif poin_investigasi < 4 and item_buku_kas_merah == False and item_rekaman_tirto == False:
        jump ending_tirto_bebas

    # 6. DEFAULT / NORMAL ENDING (TIRTO DAPAT REMISI)
    else:
        jump ending_tirto_remisi

# ==========================================
# ENDING 1: KORUPTOR BANYAK DISKON (Tirto Dipenjara tapi Dapat Remisi)
# ==========================================
label ending_tirto_remisi:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    stop music fadeout 2.0
    scene black with dissolve_lambat
    
    play music "bgm_11_senyum_koruptor.ogg" fadein 1.0
    "Kematian Ki Renggo mengakhiri teror gaib di desa. Esok harinya, Pak Tirto diseret ke meja hijau."
    
    scene cg_end1_tirto_sidang with dissolve
    "Berkat sebagian bukti yang dikumpulkan Trio, Tirto tertunduk lesu di kursi terdakwa. Hakim mengetukkan palu, memvonisnya 5 tahun penjara atas penggelapan sebagian dana desa."
    
    r "Akhirnya bangkotan itu kena batunya."
    c "Semoga dia sadar di dalam sana."
    
    scene cg_end1_tirto_nonton_tv with fade
    "Namun, keadilan di negeri ini terkadang seperti lelucon."
    "Hanya satu setengah tahun kemudian, Trio melihat berita di televisi. Tirto terlihat segar bugar, bersantai di sel fasilitas khusus."
    "Ia mendapat rentetan remisi berkelakuan baik karena koneksi politiknya yang belum sepenuhnya mati."
    
    b "Astaghfirullah... Dia bahkan tersenyum ke arah kamera."
    "Meski desa sudah aman, ada rasa pahit yang tertinggal di benak Trio Investigator."
    
    scene black with dissolve_lambat
    centered "{size=+30}ENDING 1{/size}\n\nKeadilan yang Diskon"

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("ENDING_TIRTO_REMISI SELESAI")
    # -----------------------------------
    return


# ==========================================
# ENDING 2: HUKUM TUMPUL KE ATAS (Tirto Diperiksa Lalu Bebas)
# ==========================================
label ending_tirto_bebas:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    stop music fadeout 2.0
    scene black with dissolve_lambat
    
    play music "bgm_12_keadilan_mati.ogg" fadein 1.0
    "Trio selamat dan Ki Renggo musnah. Namun, penegakan hukum di dunia nyata butuh lebih dari sekadar cerita mistis."
    
    scene cg_end2_tirto_konferensi with kaca_pecah
    play sound "sfx_camera_shutter.ogg"
    "Karena kurangnya bukti fisik seperti buku kas dan rekaman yang sah, polisi kesulitan menjerat Tirto."
    "Dengan pengacara mahal, Kades licik itu berbalik memposisikan dirinya sebagai korban."
    
    t "Saya ini korban fitnah! Warga dibodohi oleh tiga pemuda ini!"
    
    scene cg_end2_tirto_mobil_mewah with dissolve
    play sound "sfx_car_start.ogg"
    "Pak Tirto bebas tak bersyarat. Sebelum masuk ke dalam mobil mewahnya untuk pindah kota, ia menatap Raka, Bimo, dan Citra dengan senyum meremehkan."
    
    c "Ini nggak adil, Kak! Dia dalang dari semuanya!"
    r "Kita kalah di atas kertas, Cit. Dia lolos."
    
    "Tirto membawa kabur harta simpanannya, meninggalkan desa yang hancur untuk dibangun ulang dari nol oleh warga yang miskin."
    
    scene black with dissolve_lambat
    centered "{size=+30}ENDING 2{/size}\n\nLolos dari Jerat Hukum"

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("ENDING_TIRTO_BEBAS SELESAI")
    # -----------------------------------
    return


# ==========================================
# ENDING 3: KARMA SANG PENUNGGU (ABSOLUTE TRUE ENDING)
# ==========================================
label ending_tirto_digentayangi:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    stop music fadeout 2.0
    scene black with dissolve_lambat
    
    play music "bgm_08_fajar_keadilan.ogg" fadein 1.0
    "Keadilan akhirnya ditegakkan secara mutlak."
    
    scene cg_end3_tirto_vonis with hpunch
    "Tumpukan bukti tak terbantahkan—Buku Kas Merah, Rekaman, hingga kesaksian Gatot dan Mbok Darmi—membuat Tirto tak bisa berkutik."
    "Hakim menjatuhkan hukuman seumur hidup tanpa kemungkinan remisi. Wajah arogan sang Kades seketika pucat pasi."
    
    "Tapi, hukuman dunianya belumlah seberapa dibandingkan hutang darahnya."
    
    stop music fadeout 1.0
    scene cg_end3_tirto_diteror_sel with flashmerah
    play music "bgm_04_teror_tak_kasatmata.ogg" fadein 1.0
    play sound "sfx_demonic_growl.ogg"
    
    "Malam demi malam, sel penjaranya menjadi neraka. Bayangan Jenglot, wujud Genderuwo Renggo, dan roh-roh korban penumbangan mendatangi sudut selnya."
    
    t "TIDAAAK! JANGAN DEKATI AKU! AKU KEMBALIKAN UANGNYA! AMPUUUN!"
    
    "Sipir penjara menemukan Pak Tirto meringkuk dengan tangan mencakar lantai hingga berdarah. Ia akan menghabiskan sisa umurnya dihantui oleh ketamakan dan iblis yang ia pelihara sendiri."
    
    scene black with dissolve_lambat
    centered "{size=+30}ENDING 3 (ABSOLUTE TRUE ENDING){/size}\n\nPenjara Fisik dan Batin"

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("ENDING_TIRTO_DIGENTAYANGI SELESAI")
    # -----------------------------------
    return


# ==========================================
# ENDING 4: AKAL YANG PUTUS (Tirto Kabur dan Menjadi Gila)
# ==========================================
label ending_tirto_gila:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    stop music fadeout 2.0
    scene black with dissolve_lambat
    
    play music "bgm_creepy_ambient.ogg" fadein 1.0
    "Memanfaatkan kekacauan saat Ki Renggo berubah wujud, Pak Tirto berhasil melepaskan ikatannya karena Gatot lengah."
    
    scene cg_end4_tirto_kabur_hutan with vpunch
    play sound "sfx_running_leaves.ogg"
    "Ia lari terbirit-birit menembus gelapnya hutan, tersandung akar, bajunya robek terkena duri belukar."
    "Ia berhasil lolos dari amukan warga maupun jerat polisi. Namun, ia membawa Kalung Galih yang memancarkan aura negatif..."
    
    scene cg_end4_tirto_gelandangan with fade
    "Bulan berganti tahun. Trauma malam itu dan energi gelap kalung yang terus ia genggam menghancurkan kewarasannya."
    "Seseorang yang mirip mantan Kades kaya itu kini terlihat menggelandang di bawah jembatan ibu kota. Wajahnya cemong, matanya liar."
    
    t "Hehehe... Mbah Renggo minta tumbal... Jangan bakar uangku... Panas... Panas!"
    
    "Ia memakan sampah dan tertawa sendiri. Tirto telah kehilangan harta dan akalnya, sebuah hukuman yang lebih kejam dari penjara."
    
    scene black with dissolve_lambat
    centered "{size=+30}ENDING 4{/size}\n\nHarta Tak Dibawa Mati"

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("ENDING_TIRTO_GILA SELESAI")
    # -----------------------------------
    return


# ==========================================
# ENDING 5: STARTUP DETEKTIF MISTIS (GOOD ENDING)
# ==========================================
label ending_startup_trio:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    stop music fadeout 2.0
    scene black with dissolve_lambat
    
    play music "bgm_good_ending.ogg" fadein 1.0
    "Badai telah berlalu. Semua aset Pak Tirto disita oleh negara dan dikembalikan untuk pembangunan desa."
    
    scene cg_end5_tirto_baju_oranye with kaca_pecah
    play sound "sfx_camera_shutter.ogg"
    "Kades korup itu digelandang memakai baju tahanan oranye, menunduk malu disorot puluhan kamera wartawan nasional."
    
    "Sementara itu, reputasi Trio Investigator meroket tajam!"
    "Warga yang diselamatkan mengumpulkan dana donasi, dan stasiun TV membayar mahal hak siar kisah epik mereka menumpas ilmu hitam."
    
    scene cg_end5_trio_kantor_baru with dissolve
    r "Waktunya ekspansi bisnis, kawan-kawan!"
    c "Sistem database hantu Nusantara sudah online, Kak!"
    b "Alhamdulillah, semoga jalan ini selalu membawa manfaat."
    
    "Raka, Bimo, dan Citra akhirnya menyewa ruko besar dan meresmikan agensi detektif supranatural mereka. Dengan peralatan canggih, mereka siap membasmi misteri berikutnya!"
    
    scene black with dissolve_lambat
    centered "{size=+30}ENDING 5 (GOOD ENDING){/size}\n\nAgensi Mistis Era Digital"

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("ENDING_STARTUP_TRIO SELESAI")
    # -----------------------------------
    return


# ==========================================
# ENDING 6: SIKLUS YANG TAK TERPUTUS (Tirto Mewarisi Ilmu Hitam)
# ==========================================
label ending_penerus_renggo:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    stop music fadeout 2.0
    scene black with dissolve_lambat
    
    play music "bgm_boss_ritual.ogg" fadein 1.0
    "Trio berhasil memusnahkan wujud Genderuwo Ki Renggo, tapi absennya bukti hukum membuat Tirto bisa melarikan diri."
    "Semua orang mengira teror di desa tersebut telah benar-benar berakhir."
    
    scene cg_end6_tirto_ngorek_puing with dissolve
    "Beberapa malam kemudian, sesosok pria tambun mengendap-endap di antara puing-puing balai desa yang hangus."
    "Tirto menyingkirkan balok kayu hitam, mencari di ruang bawah tanah rahasianya. Benda itu ada di sana, lolos dari api."
    
    scene cg_end6_tirto_mata_hijau with dissolve_kilat
    play sound "sfx_demonic_growl.ogg"
    
    "Tirto menggenggam Kristal Merah peninggalan Ki Renggo. Seketika, energi gelap merambat ke lengannya."
    "Mata sang mantan Kades berkilat hijau terang. Seringai mengerikan yang sangat familiar terbentuk di wajahnya."
    
    t "Mereka mengambil hartaku... tapi mereka memberiku sesuatu yang jauh lebih berkuasa."
    
    "Ki Renggo mungkin telah mati. Namun, kelicikan Tirto kini dipersenjatai dengan ilmu hitam purba. Mimpi buruk yang baru saja lahir."
    
    scene black with hpunch
    centered "{size=+30}ENDING 6{/size}\n\nLahirnya Dukun Baru"

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("ENDING_PENERUS_RENGGO SELESAI")
    # -----------------------------------
    return