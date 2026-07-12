# ==========================================
# FILE: chapter03.rpy
# TEMA: Bentrok di Gudang Beras
# ==========================================

# ------------------------------------------
# DEFINISI CUTSCENES (CG) CHAPTER 03
# ------------------------------------------
image cg_ch3_joko_disekap = "images/cg/cg_ch3_joko_disekap.webp"
image cg_ch3_nemu_kalung = "images/cg/cg_ch3_nemu_kalung.webp"
image cg_ch3_raka_fokus = "images/cg/cg_ch3_raka_fokus.webp"
image cg_ch3_raka_menerjang = "images/cg/cg_ch3_raka_menerjang.webp"
image cg_ch3_gatot_kabur = "images/cg/cg_ch3_gatot_kabur.webp"
image cg_ch3_peta_renggo = "images/cg/cg_ch3_peta_renggo.webp"
image cg_chap03_gatot_dibanting = "images/cg/cg_chap02_gatot_dibanting.webp"
image cg_chap03_gatot_terjerembab = "images/cg/cg_chap02_gatot_terjerembab.webp"


label chapter_03:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Inisialisasi variabel untuk chapter ini
    $ ch3_kalung_gatot = False
    $ ch3_menang_qte = False

    # Tampilan Judul Chapter di awal
    scene black with bangun_tidur
    play music "bgm_03_bayang_petunjuk.ogg" fadein 2.0
    centered "{size=+20}CHAPTER 03{/size}\n\nBentrok di Gudang Beras" with dissolve_lambat
    pause 2.0
    
    # Scene 1: Menyusup ke Gudang Beras
    play sound "sfx_creaky_door_open.ogg"
    scene bg_gudang_beras with transisi_asap
    show debu_melayang
    
    "Trio Investigator mengikuti jejak seretan dan suara rintihan tertahan yang mengarah ke gudang beras di sayap kiri bangunan."
    
    play sound "sfx_footsteps_approach.ogg"
    "Suasananya sangat gelap dan pengap. Dari sela-sela tumpukan karung, mereka mengintip apa yang terjadi."

    # --- CUTSCENE 01: JOKO DISEKAP ---
    scene cg_ch3_joko_disekap with dissolve_kilat
    play sound "sfx_benda_jatuh.ogg"
    
    j "A-ampun Bang Gatot! Sumpah, saya nggak tahu apa-apa soal adiknya Abang! Saya cuma satpam jaga depan!"

    g "Alah, bohong lu! Gua tahu lu disuruh mungutin emas palsu di TKP kan?! Siapa yang nyuruh lu, hah?!"

    # Kembali ke view normal
    scene bg_gudang_beras with dissolve_kilat
    show debu_melayang
    
    show citra_panik at center with dissolve_kilat
    c "Kak... itu ada preman bawa linggis lagi nyekap satpam. Gimana nih? Aku takut dia dibunuh..."
    hide citra_panik

    show bimo_berpikir at center with dissolve_kilat
    b "Pria yang membawa senjata itu... auranya dipenuhi dendam dan kesedihan yang mendalam, bukan niat jahat murni."
    hide bimo_berpikir

    show raka_marah at center with dissolve_kilat
    r "Apapun alasannya, nyekap orang itu tindakan kriminal. Tapi kita dengarkan dulu mereka untuk dapat petunjuk"
    hide raka_marah

    # ==========================================
    # [PANGGIL MINIGAME 01: MENCARI KALUNG]
    # ==========================================
    "Sambil bersembunyi, Raka menyapu area sekitar dengan senternya."
    call play_mg_chap03_cari
    $ ch3_kalung_gatot = _return

    # Kembali ke view normal setelah minigame cari
    scene bg_gudang_beras with dissolve_kilat
    show debu_melayang

    play sound "sfx_ayunan_tongkat.ogg"
    "Tiba-tiba, Gatot mengangkat senjatanya tinggi-tinggi, berniat memukul Joko."

    show joko_panik at center with tv_rusak
    j "TOLONGGG!!!"
    hide joko_panik

    # Transisi ke pertarungan
    stop music fadeout 0.5
    play music "bgm_05_otot_kawat.ogg" fadein 1.0
    play sound "sfx_wuzz_ngebut.ogg"

    # --- CUTSCENE 04: RAKA MENERJANG ---
    scene cg_ch3_raka_menerjang with flashbang
    
    "Tanpa berpikir panjang, Raka melompat keluar dari persembunyiannya."
    r "Heh, badut! Lepasin satpam itu sekarang!"
    g "Siapa lu?! Berani-beraninya ikut campur urusan gua! Sini lu kalau mau mati!"

    play sound "sfx_fast_swish.ogg"
    "Gatot melemparkan senjatanya ke arah Raka dengan brutal."

    # ==========================================
    # [PANGGIL MINIGAME 02: QTE MENANGKIS]
    # ==========================================
    call play_mg_chap03_qte
    $ ch3_menang_qte = _return

    scene bg_gudang_beras with dissolve_kilat
    show debu_melayang

    # Resolusi Pertarungan berdasarkan hasil QTE
    if ch3_menang_qte:
        play sound "sfx_punch.ogg"
        scene cg_chap03_gatot_dibanting with hpunch
        show debu_melayang
        "Dengan refleks karatenya, Raka berhasil mengatasi serangan Gatot, meraih lengannya, dan membantingnya keras ke lantai."
        
        play sound "sfx_barang_berat_jatuh.ogg"
        scene cg_chap03_gatot_dibanting with vpunch
        g "Arghh! Brengsek... lepaskan gua! Adek gua dibunuh, gua cuma mau cari pelakunya!"
        hide gatot_lelah
        
        show raka_lega at left with dissolve_kilat
        r "Gue bilang tenang, ya tenang! Kita di sini juga lagi nyari kebenarannya, bukan cari ribut sama lu!"
        hide raka_lega
    else:
        play sound "sfx_benda_dipukul.ogg"
        scene bg_gudang_beras with flashmerah
        show debu_melayang
        "Raka kewalahan menahan rentetan serangan Gatot."

        show raka_lelah at center with mata_mengerjap
        r "Ugh! Sial... gerakannya lumayan cepet."
        hide raka_lelah

        show gatot_marah at center with dissolve_kilat
        g "Jangan halangin gua! Gua bakal cari bajingan yang bunuh adek gua pakai cara gua sendiri!"
        hide gatot_marah
        
        # --- CUTSCENE 05: GATOT KABUR ---
        play sound "sfx_footsteps_fast.ogg"
        scene cg_ch3_gatot_kabur with transisi_asap
        "Gatot mendorong Raka hingga terjatuh dan bersiap melarikan diri dari gudang menuju kegelapan malam."

    # Resolusi Bercabang Berdasarkan Kalung & Pertarungan
    scene bg_gudang_beras with dissolve_lambat
    show debu_melayang

    if ch3_kalung_gatot and ch3_menang_qte:
        stop music fadeout 2.0
        play music "bgm_09_air_mata_tumbal.ogg" fadein 2.0
        
        show bimo_normal at center with dissolve_lambat
        b "Gatot, kami tahu kau berduka. Adikmu... Galih, bukan? Kami menemukan kalungnya terjatuh di depan."
        hide bimo_normal

        show gatot_lelah at center with dissolve_lambat
        g "Kalung... kalung Galih? Ya Tuhan... dia dibunuh sebelum dibuang ke TKP. Perutnya dirobek buat nutupin racun!"
        g "Gua bakal bantu kalian... asalkan kalian janji jeblosin dalangnya ke penjara."
        hide gatot_lelah

    elif ch3_kalung_gatot and not ch3_menang_qte:
        show bimo_panik at center with dissolve_kilat
        b "Tunggu, Gatot! Kami punya kalung adikmu, Galih!"
        hide bimo_panik

        show gatot_marah at center with dorong_kanan
        g "Kurang ajar, lu nyolong barang adek gua?! Gua nggak percaya sama kalian!"
        hide gatot_marah
        
        play sound "sfx_footsteps_fast.ogg"
        "Gatot merampas kalung itu dari tangan Bimo dan benar-benar lari menghilang."

    elif not ch3_kalung_gatot and ch3_menang_qte:
        show gatot_lelah at center with dissolve_kilat
        g "Lu boleh nahan gua sekarang, tapi gua nggak bakal ngomong apa-apa sama lu pada! Polisi sama aja bohong!"
        hide gatot_lelah
        
        show raka_lelah at center with dissolve_kilat
        r "Batu banget nih orang. Susah diajak kerja sama kalau nggak ada sesuatu yang bisa bikin dia percaya sama kita."
        hide raka_lelah

    else:
        scene cg_ch3_gatot_kabur with dissolve
        "Tanpa kalung dan kalah dalam duel, Trio Investigator terpaksa membiarkan Gatot pergi."

    # Mengamankan Joko
    stop music fadeout 3.0
    play music "bgm_03_bayang_petunjuk.ogg" fadein 2.0
    
    show citra_lega at center with dissolve_kilat
    c "Pak Satpam nggak apa-apa? Tadi Bang Gatot bilang Bapak mungutin emas palsu?"
    hide citra_lega

    show joko_panik at center with mata_mengerjap
    j "S-saya disuruh Ki Renggo, Neng! Dukun bayaran dari desa sebelah! Tolong jangan serahin saya ke polisi!"
    hide joko_panik

    # ==========================================
    # [PANGGIL MINIGAME 03: INTEROGASI JOKO]
    # ==========================================
    call play_mg_chap03_introgasi

    scene bg_gudang_beras with dissolve_kilat
    show debu_melayang

    show bimo_berpikir at center with dissolve_kilat
    b "Ki Renggo... Namanya sering terdengar dalam praktik ilmu hitam komersial. Kita punya petunjuk baru."
    hide bimo_berpikir

    # Penutup Chapter & Kesimpulan Dinamis
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with pingsan
    centered "{size=+15}END OF CHAPTER 03{/size}" with dissolve_lambat
    pause 1.5

    # Teks Teaser/Kesimpulan berdasarkan pilihan pemain
    if ch3_kalung_gatot and ch3_menang_qte:
        "KESIMPULAN CHAPTER:\nRaka berhasil menaklukkan Gatot dalam pertarungan, dan penemuan kalung Galih membuat sang preman mau membuka diri. Gatot kini berpihak pada Trio Investigator. Dengan petunjuk baru berupa peta yang mengarah pada dukun palsu Ki Renggo, jalan menuju kebenaran semakin terbuka."
    else:
        "KESIMPULAN CHAPTER:\nPertarungan di gudang beras berakhir dengan kekacauan. Kegagalan menenangkan Gatot membuat Trio Investigator kehilangan potensi sekutu yang sangat berharga. Meski Joko memberikan peta menuju Ki Renggo sang dukun, mereka kini harus melangkah dengan hati-hati. Gatot yang dibutakan dendam masih berkeliaran di luar sana."
    
    pause 3.0

    # Lanjut ke Chapter berikutnya

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_03 SELESAI")
    # -----------------------------------
    jump chapter_04