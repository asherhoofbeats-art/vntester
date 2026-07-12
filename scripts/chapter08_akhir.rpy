# ==========================================
# FILE: chapter_08_akhir.rpy
# TEMA: Murka Ki Renggo & Genderuwo Purba
# ==========================================
image cg_chap08_trio_dikepung_warga = "images/cg/cg_chap08_trio_dikepung_warga.webp"
image cg_chap08_buto_hancurkan_desa = "images/cg/cg_chap08_buto_hancurkan_desa.webp"
image cg_chap08_buto_makan_sajen = "images/cg/cg_chap08_buto_makan_sajen.webp"
image cg_chap08_buto_makan_warga = "images/cg/cg_chap08_buto_makan_warga.webp"
image cg_chap08_buto_mengamuk = "images/cg/cg_chap08_buto_mengamuk.webp"
image cg_chap08_buto_menghilang = "images/cg/cg_chap08_buto_menghilang.webp"
image cg_chap08_citra_beri_sajen = "images/cg/cg_chap08_citra_beri_sajen.webp"
image cg_chap08_tirto_merasa_aman = "images/cg/cg_chap08_tirto_merasa_aman.webp"
image cg_chap08_trio_dikejar_warga = "images/cg/cg_chap08_trio_dikejar_warga.webp"
image cg_end1_tirto_nonton_tv = "images/cg/cg_end1_tirto_nonton_tv.webp"
image cg_end1_tirto_sidang = "images/cg/cg_end1_tirto_sidang.webp"
image cg_end2_tirto_mobil_mewah = "images/cg/cg_end2_tirto_mobil_mewah.webp"
image cg_end2_tirto_konferensi = "images/cg/cg_end2_tirto_konferensi.webp"
image cg_end3_tirto_diteror_sel = "images/cg/cg_end3_tirto_diteror_sel.webp"
image cg_end3_tirto_vonis = "images/cg/cg_end3_tirto_vonis.webp"
image cg_end4_tirto_gelandangan = "images/cg/cg_end4_tirto_gelandangan.webp"
image cg_end4_tirto_kabur_hutan = "images/cg/cg_end4_tirto_kabur_hutan.webp"
image cg_end5_tirto_baju_oranye = "images/cg/cg_end5_tirto_baju_oranye.webp"
image cg_end5_trio_kantor_baru = "images/cg/cg_end5_trio_kantor_baru.webp"
image cg_end6_tirto_ngorek_puing = "images/cg/cg_end6_tirto_ngorek_puing.webp"
image cg_end6_tirto_mata_hijau = "images/cg/cg_end6_tirto_mata_hijau.webp"
image cg_chap08_tirto_nyungsep = "images/cg/cg_chap08_tirto_nyungsep.webp"
image cg_chap08_tirto_dihempaskan = "images/cg/cg_chap08_tirto_dihempaskan.webp"
image cg_chap08_tirto_minta_tolong = "images/cg/cg_chap08_tirto_minta_tolong.webp"

label chapter_08_akhir:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # 1. TRANSISI KE BAGIAN AKHIR
    scene black with dissolve_lambat
    play music "bgm_04_teror_tak_kasatmata.ogg" fadein 2.0
    centered "{size=+20}CHAPTER 08 - BAGIAN 2{/size}\n\nMurka sang Penunggu"
    pause 1.0

    # 2. AWAL KETEGANGAN PASCA KEBAKARAN
    scene cg_balai_desa_api_padam_drone with dissolve
    "Api telah padam, baik oleh air maupun hawa gaib. Namun, bahaya sesungguhnya belum berakhir."
    
    scene cg_chap08_wg_bingung_hujan with dissolve
    "Warga memang kebingungan melihat api yang padam tiba-tiba, namun kemarahan di mata mereka tidak surut."
    
    scene bg_kebakaran_usai with dissolve
    show darmi_panik at center
    md "Jangan biarkan mereka kabur! Seret Kades dan antek-anteknya!"
    hide darmi_panik
    
    "Massa kembali merangsek maju. Dari kejauhan, Citra melihat Raka, Gatot, dan Tirto yang sudah terpojok setelah turun dari balkon."

    # ==========================================
    # 3. EVENT BUTO IJO (PEMICU & RESOLUSI)
    # ==========================================
    if citra_resonansi_gaib < 5:
        # Gagal Syarat Resonansi
        c "Aku... aku harus memanggil sesuatu! Apapun itu!"
        "Citra memejamkan matanya, berusaha memanggil arwah. Namun energi spiritualnya terlalu lemah."
        scene cg_chap08_trio_dikepung_warga with flashmerah
        play sound "sfx_stab.ogg"
        with vpunch
        "Massa berhasil mendobrak masuk. Tanpa belas kasihan, mereka menyeret Trio dan Gatot menuju amukan massa."
        centered "{size=+20}GAME OVER{/size}\n\nKekuatan Citra tidak mencukupi."
        return
        
    # Jika Resonansi Cukup (>= 5)
    scene bg_kebakaran_usai with vpunch
    play sound "sfx_whuz_gaib.ogg"
    show citra_kesurupan at truecenter
    "Mata Citra berubah putih seluruhnya. Energi spiritual meledak dari tubuhnya, menciptakan pusaran angin di halaman balai desa!"
    
    scene cg_warga_didatangi_buto_bayangan with dissolve_kilat
    "Sebuah siluet raksasa setinggi bangunan dua lantai merobek dimensi dan berdiri di tengah-tengah massa!"
    
    scene cg_warga_didatangi_buto_jelas with flashbang
    play sound "sfx_demonic_roar.ogg"
    with hpunch
    "Itu Buto Ijo yang sesungguhnya! Monster itu mengaum memekakkan telinga!"
    
    scene cg_chap07_warga_ketakutan_buto with hpunch
    play sound "sfx_warga_ketakutan.ogg"
    "Warga yang tadinya beringas, kini lari kocar-kacir, terinjak-injak satu sama lain dalam ketakutan yang absolut!"
    
    scene bg_kebakaran_usai_raka_gatot_keluar with dissolve
    "Kekacauan itu memberikan celah. Raka, Gatot, dan Pak Tirto berhasil menyusul dan berkumpul kembali dengan Bimo dan Citra."
    
    r "Gila lu Cit! Lu beneran bisa manggil Hulk versi Indo?!"
    
# Penanganan Buto Ijo (Pengecekan Item Persembahan)
    if ch4_menyan_jafaron == True:
        # OPSI 1: Punya Menyan Jafaron
        c "Sekarang waktunya mengembalikan dia! Kak Bimo, berikan Menyan Jafaron yang kita temukan!"
        scene cg_chap08_citra_beri_sajen with dissolve
        "Citra melemparkan bungkus Menyan Jafaron yang mereka dapatkan sebelumnya ke arah monster Buto Ijo."
        
        scene cg_chap08_buto_makan_sajen with dissolve
        "Buto Ijo itu menangkap sajen tersebut dan memakannya dengan rakus."
        
        play sound "sfx_fast_swoosh.ogg"
        scene cg_chap08_buto_menghilang with dissolve
        "Setelah menerima persembahannya, raksasa itu menghilang tertiup angin hitam, mengembalikan ketenangan di balai desa."
        
    elif item_kristal_merah == True:
        # OPSI 2: Tidak punya Menyan, tapi punya Kristal Darah
        c "A-aku nggak punya sajen! Tunggu, Kak Bimo, lemparkan Kristal Darah yang kita temukan!"
        scene cg_chap08_citra_beri_sajen with dissolve
        "Sebagai ganti sajen, Citra mengambil Kristal Darah yang memancarkan aura magis pekat dan melemparkannya ke udara."
        
        scene cg_chap08_buto_makan_sajen with dissolve
        "Buto Ijo itu mengendus energi kuat dari kristal tersebut, menangkapnya, dan menelannya bulat-bulat."
        
        play sound "sfx_fast_swoosh.ogg"
        scene cg_chap08_buto_menghilang with dissolve
        "Energi gelap kristal itu memuaskan rasa laparnya. Raksasa tersebut memudar menjadi asap hitam dan pergi meninggalkan balai desa."

    else:
        # OPSI 3: Tidak Punya Keduanya (Bad Ending Branch)
        c "A-aku nggak bisa mengendalikannya! Dia kelaparan dan kita tidak punya persembahan apa-apa!"
        
        scene cg_chap08_buto_makan_warga
        play sound "sfx_demonic_roar.ogg"
        "Buto Ijo itu menatap beringas ke arah warga yang berlarian. Trio menyadari mereka telah melepaskan monster yang tak bisa mereka jinakkan."
        
        b "Kita harus lari sekarang! Tinggalkan saja si Tirto itu!"
        
        scene cg_chap08_trio_dikejar_warga with pingsan
        play sound "sfx_warga_ketakutan.ogg"
        "Trio bersama Gatot lari menembus gelapnya malam seraya dikejar warga yang marah."
        "Membiarkan desa tersebut dikuasai amarah monster yang dipanggil Citra, mungkin opsi terbaik saat ini."
        
        centered "{size=+20}MISSION FAILED{/size}\n\nKeputusan yang membawa malapetaka."
        return

    # ==========================================
    # 4. RESOLUSI WARGA: DARMI TRUST
    # ==========================================
    "Buto Ijo telah pergi. Beberapa warga yang tersisa kembali berkumpul, masih memegang senjata tajam."
    
    if darmi_trust == True:
        # Darmi Percaya
        scene cg_chap08_trio_dikepung_warga with dissolve
        play sound "sfx_warga_marah.ogg"
        show darmi_normal at center
        md "Lho... Non Citra to ini?!"
        "Mbok Darmi menerobos barisan warga dan merentangkan tangannya di depan Trio."
        md "Tahan kabeh! Mereka ini orang baik! Non ini yang nyelamatin kulo dari Setan palsu di dapur!"
        
        show gatot_normal at right
        g "Benar! Trio Investigator ini yang membongkar semua kebusukan Pak Kades! Kades inilah yang selama ini memeras desa kita!"
        
        "Mendengar kesaksian dari Mbok Darmi dan Gatot, senjata di tangan warga perlahan turun. Tatapan marah mereka berubah menjadi rasa syukur yang luar biasa."
        
        # Momen Pahlawan
        stop music fadeout 1.0
        play music "bgm_08_fajar_keadilan.ogg"
        
        scene cg_chap08_bimo_diangkat_warga with dissolve_kilat
        "Warga bersorak. Mereka mengangkat Bimo tinggi-tinggi."
        
        scene cg_chap08_citra_diangkat_warga with dissolve_kilat
        "Citra tertawa lepas saat ibu-ibu memeluknya dan mengangkatnya bersorak."
        
        scene cg_chap08_raka_diangkat_warga with dissolve_kilat
        "Raka yang salah tingkah ikut diangkat ke udara, merasa canggung dengan status pahlawan dadakan ini."
        
    else:
        # Darmi Tidak Percaya (Bad Ending Branch)
        "Meskipun monster itu sudah hilang, warga yang masih marah dan trauma menatap Trio dengan penuh kebencian."
        "Mereka menganggap Trio adalah dukun ilmu hitam yang membawa monster tersebut ke desa mereka."
        play sound "sfx_warga_ngamuk.ogg"
        scene cg_chap08_trio_dikepung_warga with pingsan
        "Tanpa ada pembelaan dari warga desa, Trio terpaksa melarikan diri, meninggalkan misi mereka tak terselesaikan."
        scene cg_chap08_trio_dikejar_warga
        centered "{size=+20}MISSION FAILED{/size}\n\nDianggap sebagai musuh masyarakat."
        return

    # ==========================================
    # 5. FINAL BOSS ENTRANCE: KI RENGGO
    # ==========================================
    scene bg_lapangan_balai_kosong with dissolve_lambat
    play music "bgm_07_murka_penjaga.ogg"
    "Saat Trio berpikir malam panjang ini akhirnya usai..."
    
    play sound "sfx_demonic_roar.ogg"
    with hpunch
    "Sebuah ledakan energi hijau gelap menghantam halaman balai desa, menghempaskan warga yang sedang bersorak!"
    
    show renggo_transforming at napas_boss 
    
    play music "bgm_05_otot_kawat.ogg" fadein 1.0
    
    kr "HAAHAAHAA! JANGAN SENANG DULU KALIAN, BOCAH-BOCAH SIALAN!"
    kr "Kalian pikir kalian jagoan di tanah kekuasaanku?!"
    
    "Ki Renggo, dukun sesat yang menjadi dalang di balik segalanya, berdiri di sana. Matanya menyala hijau terang."
    
    "Pak Tirto yang sedari tadi terikat, tiba-tiba tersenyum lebar."
    scene cg_chap08_tirto_merasa_aman
    t "Mbah Renggo! Mbah datang menyelamatkan saya! Habisi mereka, Mbah!"

    scene cg_chap08_tirto_minta_tolong
    t "Tolong saya mbah.. Nanti akan Ku Bangunkan Pondok yang baru"
    scene cg_chap08_tirto_dihempaskan
    kr "Dasar pejabat tak berguna. Kau Pikir ini urusan Pondok!"
    
    play sound "sfx_magic_trick.ogg"
    "Ki Renggo mengayunkan tongkatnya. Sebuah kekuatan kasatmata mengangkat tubuh gemuk Pak Tirto ke udara, lalu menghempaskannya..."
    
    
    play sound "sfx_benda_jatuh.ogg"
    with vpunch
    play sound "sfx_towewew.ogg"
    scene cg_chap08_tirto_nyungsep
    "...Tepat masuk ke dalam tong sampah besar berbahan seng di sudut balai desa!"
    
    kr "Sekarang... Rasakan wujud asliku!"
    
    scene bg_lapangan_balai_kosong with flashmerah
    play sound "sfx_monster_died.ogg"
    with hpunch
    "Ki Renggo merapal mantra terlarang. Tubuh tuanya membesar, merobek kulit manusiawinya, dan berubah menjadi sosok Genderuwo purba yang sangat mengerikan!"
    
    # PANGGIL FINAL BOSS MINIGAME
    call play_final_boss
    
    # Jika Menang dari minigame, label `play_final_boss` sudah otomatis melompat ke `ending_true`.
    # Jika kalah, akan berujung pada Game Over yang sudah diset di dalam minigame.

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_08_AKHIR SELESAI")
    # -----------------------------------
    return