# ==========================================
# FILE: mg_chap05b.rpy
# MINIGAME: Menuntun Wanita Tersesat (Nita)
# MEKANIK: Dialogue / Direction Puzzle
# ==========================================

# ------------------------------------------
# DEFINISI KARAKTER, SPRITE & GAMBAR MINIGAME
# ------------------------------------------
define nita = Character("Nita", color="#b3d4ff")
image nita_normal = "images/chars/nita_normal.webp"
image cg_mgchap05b_kunti_nyegat = "images/cg/cg_mgchap05b_kunti_nyegat.webp"
image cg_mgchap05b_mobil_hilang = "images/cg/cg_mgchap05b_mobil_hilang.webp"
image cg_mgchap05b_nita_marah = "images/cg/cg_mgchap05b_nita_marah.webp"
image cg_mgchap05b_nita_naik = "images/cg/cg_mgchap05b_nita_naik.webp"
image cg_mgchap05b_simpang_dua = "images/cg/cg_mgchap05b_simpang_dua.webp"
image cg_mgchap05b_simpang_satu = "images/cg/cg_mgchap05b_simpang_satu.webp"
image cg_mgchap05b_simpang_tiga = "images/cg/cg_mgchap05b_simpang_tiga.webp"
image cg_mgchap05b_end_bimo_jemput = "images/cg/cg_mgchap05b_end_bimo_jemput.webp"
image cg_mgchap05b_raka_bingung = "images/cg/cg_mgchap05b_raka_bingung.webp"
image bg_mg05b_persimpangan = "images/cg/bg_mg05b_persimpangan.webp"
image cg_mg05b_mobil_hantu = "images/cg/cg_mg05b_mobil_hantu.webp"
image cg_mg05b_kaca_spion = "images/cg/cg_mg05b_kaca_spion.webp"
image cg_mg05b_gerbang_makam = "images/cg/cg_mg05b_gerbang_makam.webp"
image cg_mg05b_wanita_menjerit = "images/cg/cg_mg05b_wanita_menjerit.webp"
image cg_chap05_mobil_ngebul = "images/cg/cg_chap05_mobil_ngebul.webp"
image cg_chap05b_susuri_jalan_dua = "images/cg/cg_chap05b_susuri_jalan_dua.webp"
image cg_chap05b_susuri_jalan_satu = "images/cg/cg_chap05b_susuri_jalan_satu.webp"
image cg_chap05b_susuri_jalan_tiga = "images/cg/cg_chap05b_susuri_jalan_tiga.webp"
image cg_nita_hilang = "images/cg/cg_nita_hilang.webp"
image cg_sampai_di_makam = "images/cg/cg_sampai_di_makam.webp"
image it_bt_spekaer_hantu = "images/item/it_bt_spekaer_hantu.webp"
# ------------------------------------------
# SCREEN UI MINIGAME ARAH GAIB
# ------------------------------------------
screen mg_arah_gaib(clue_text, opt_kiri, opt_lurus, opt_kanan, correct_ans):
    modal True
    
    add "bg_mg05b_persimpangan"
    add "kabut_tebal"
    add "#000000aa" 
    
    vbox:
        xalign 0.5 ypos 80
        spacing 20
        
        text "PETUNJUK ARAH GAIB" size 32 color "#ff3333" xalign 0.5 bold True
        
        frame:
            background Solid("#000000cc")
            xpadding 40 ypadding 30
            xalign 0.5
            xsize 900
            text "\"[clue_text]\"" size 28 color "#00ffcc" text_align 0.5 italic True

    vbox:
        xalign 0.5 yalign 0.85
        spacing 15
        
        textbutton "⬅️ KIRI: [opt_kiri]":
            text_size 24
            xsize 800
            background Solid("#222222ee")
            hover_background Solid("#555555ee")
            action Return("kiri" == correct_ans)
            
        textbutton "⬆️ LURUS: [opt_lurus]":
            text_size 24
            xsize 800
            background Solid("#222222ee")
            hover_background Solid("#555555ee")
            action Return("lurus" == correct_ans)
            
        textbutton "➡️ KANAN: [opt_kanan]":
            text_size 24
            xsize 800
            background Solid("#222222ee")
            hover_background Solid("#555555ee")
            action Return("kanan" == correct_ans)

# ------------------------------------------
# LABEL PEMICU MINIGAME
# ------------------------------------------
label play_mg_chap05b:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # SETUP CERITA: Berpisah dengan Bimo & Citra
    scene cg_chap05_mobil_ngebul with transisi_asap
    show raka_lelah at center with dissolve_kilat
    r "Sial, radiatornya asepnya ngebul karena ngerem mendadak tadi. Harus didinginin bentar."
    hide raka_lelah
    
    show bimo_berpikir at center with dissolve_kilat
    b "Biar aku dan Citra yang memperbaikinya. Kau uruslah wanita itu, Raka. Jangan sampai dia marah dan mengganggu kita di sini."
    hide bimo_berpikir
    
    stop music fadeout 2.0
    play music "bgm_06_panggilan_arwah.ogg" fadein 1.0 loop
    
    scene cg_mg05b_mobil_hantu with dissolve_lambat
    "Di pinggir jalan berkabut, terparkir sebuah mobil sedan tua yang tampak berkarat dan usang."
    
    show nita_normal at center with transisi_asap
    nita "Permisi... namaku Nita... kakiku kram jadi tidak bisa mengemudi..."
    nita "Bisakah kau menyetirkan mobilku... membawaku pulang?"
    hide nita_normal with dissolve
    
    r "(Gila... mobil rongsokan begini masih bisa jalan? Orang ini juga pucatnya nggak wajar. Ya udahlah, gue anterin aja cepet-cepet biar urusannya kelar.)"
    
    # INTRO CG: Melihat dari Kaca Spion (Raka Solo)
    scene cg_mgchap05b_nita_naik with transisi_asap
    play sound "sfx_angin_malam_kencang.ogg" loop
    
    "Raka duduk di kursi kemudi. Interior mobil ini berbau apak seperti tanah kuburan basah."
    "Melalui pantulan kaca spion, Nita tampak duduk kaku di kursi belakang. Suhunya sedingin es, membuat napas Raka mengeluarkan uap putih."
    
    r "O-oke... Mbak Nita, kita harus lewat mana sekarang? Jalan di depan bercabang tiga."

    # --- PERTANYAAN 1 ---
    play sound "sfx_bisikan_hantu.ogg"
    scene cg_chap05b_susuri_jalan_satu
    nita "Jalankan perlahan... di depan ada persimpangan..."
    scene cg_mgchap05b_simpang_satu
    window hide
    call screen mg_arah_gaib(
        clue_text="Di persimpangan pertama... ikuti dahan beringin yang menangis ke bumi...",
        opt_kiri="Pohon beringin rindang yang menjuntai ke bawah",
        opt_lurus="Jalan aspal mulus menembus kabut",
        opt_kanan="Pohon bambu kering yang berderit",
        correct_ans="kiri"
    )
    
    if _return == False:
        jump .arah_salah
        
    play sound "sfx_suara_berkendara.ogg"
    scene cg_mgchap05b_simpang_satu with wipe_kiri
    "Raka membelokkan setir mobil tua itu ke kiri, melewati pohon beringin besar. Setirnya terasa sangat berat."

    # --- PERTANYAAN 2 ---
    play sound "sfx_eerie.ogg"
    scene cg_chap05b_susuri_jalan_dua
    nita "Tarik napasmu... jalannya semakin gelap..."
    scene cg_mgchap05b_simpang_dua
    window hide
    call screen mg_arah_gaib(
        clue_text="Jangan ikuti cahaya bulan yang palsu... masuklah ke tempat di mana bayangan mati...",
        opt_kiri="Jalan terang benderang disinari lampu desa",
        opt_lurus="Jalan tanah setapak dengan bayangan memanjang",
        opt_kanan="Terowongan pepohonan yang gelap gulita",
        correct_ans="kanan"
    )
    
    if _return == False:
        jump .arah_salah
        
    play sound "sfx_suara_berkendara.ogg"
    scene cg_mgchap05b_simpang_dua with wipe_kanan
    "Raka memberanikan diri masuk ke terowongan pohon yang gelap gulita."

    # --- PERTANYAAN 3 ---
    play sound "sfx_bisikan_hantu.ogg"
    scene cg_chap05b_susuri_jalan_tiga
    nita "Kita hampir sampai... hawanya sudah memanggilku..."
    scene cg_mgchap05b_simpang_tiga
    window hide
    call screen mg_arah_gaib(
        clue_text="Pintunya dijaga oleh penjaga hitam yang tak pernah bersuara...",
        opt_kiri="Patung Monyet Menari yang terus berkoak keras",
        opt_lurus="Patung gagak batu yang diam membisu",
        opt_kanan="Anjing liar yang melolong di kejauhan",
        correct_ans="lurus"
    )
    
    if _return == False:
        jump .arah_salah
        
    play sound "sfx_rem_mendadak.ogg"
    scene bg_jalanan_malam with dorong_bawah
    "Mobil tua itu melaju lurus dan akhirnya keluar dari hutan berkabut."

    # --- JIKA MENANG ---
    stop music fadeout 2.0
    stop sound fadeout 1.0
    
    # WIN CG: Tiba di Makam
    scene cg_sampai_di_makam with transisi_asap
    "Mobil berhenti tepat di depan sebuah gapura makam tua bersimbol gagak batu."
    
    play sound "sfx_suara_transformasi_atau_hilang.ogg"
    scene cg_nita_hilang with transisi_asap
    "Saat Raka menoleh ke belakang, Nita sudah tidak ada. Namun, di atas jok mobil yang kusam, tergeletak sebuah kotak hitam kecil."
    
    play music "bgm_creepy_ambient.ogg"
    show raka_lega at center with dissolve_kilat
    show it_bt_spekaer_hantu at truecenter
    play sound "sfx_dapat_item.ogg"
    r "Speaker Bluetooth? Kenapa benda modern begini ada di mobil hantu... Ah udahlah, mending gue balik ke Bimo sekarang."
    hide raka_lega
    
    scene cg_sampai_di_makam with dissolve
    r "Eh.. Mana itu ya si Nita tadi?"
    scene cg_mgchap05b_mobil_hilang
    r "Astagfirullah mobilnya juga ngilang... Waduh"
    scene bg_jalanan_malam
    "Raka segera berlari menembus kabut kembali menyusuri jalan dimana dia tadi datang"
    "Lalu tidak lama berlari, terlihat mobil SUV di dekat kebun pisang, dan ada siluet seseorang berdiri melambaikan tangan"
    scene cg_mgchap05b_end_bimo_jemput with dissolve
    b "Hoy.. Raka.. Kami disini.."
    show bimo_normal at center with dissolve_kilat
    b "Oh ya Raka, kau beruntung. Tadi saat kau pergi, kebetulan ada beberapa orang suruhan Pak Kades Tirto lewat berpatroli. Mereka sangat ramah dan membantu kami memperbaiki radiator mobil yang jebol."
    b "Makanya tidak lama kamu pergi. kami jejak mobilmu tadi"
    hide bimo_normal
    show raka_berpikir at center with dissolve_kilat
    r "Alhamdulillah.. Kupikir aku akan berjalan mencari kalian semalaman. hehehe"
    r "Eh By The Way Orang suruhan Pak Kades? Malem-malem begini patroli di pinggir hutan berkabut? Rajin bener..."
    hide raka_berpikir

    show citra_lega at center with dissolve_kilat
    c "Iya Kak! Mereka baik banget lho. Untung aja Pak Kades yang ngundang kita ke desa ini emang peduli sama warganya."
    hide citra_lega

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP05B SELESAI")
    # -----------------------------------
    return "win"

    # --- JIKA KALAH ---
    label .arah_salah:
        stop music fadeout 0.1
        stop sound fadeout 0.1
        play sound "sfx_banshee_scream.ogg"
        
        # LOSE CG: Arwah Menjerit
        scene cg_mg05b_wanita_menjerit with flashmerah
        with hpunch
        
        nita "SALAH JALAN!!"
        "Nita tiba-tiba menjerit sangat keras dari kursi belakang! Wajahnya berubah mengerikan sesaat sebelum kabut pekat menelan seluruh mobil."
        
        scene black with pingsan
        play sound "sfx_suara_berputar_mau_pingsan.ogg"
        "Pandangan Raka menggelap seketika..."
        play music "bgm_creepy_ambient.ogg"
        scene cg_mgchap05b_mobil_hilang with bangun_tidur
        show raka_panik at center with dissolve_kilat
        r "Apa yang terjadi?"
        hide raka_panik
        
        show raka_lelah at center with mata_mengerjap
        r "Aduh... kepala gue... Hah? Gue udah di luar mobil? Mobil tuanya si Nita ke mana?!"
        hide raka_lelah
        
        r "Eh.. Mana itu ya si Nita tadi?"
        scene cg_mgchap05b_mobil_hilang
        r "Astagfirullah mobilnya juga ngilang... Waduh"
        scene bg_jalanan_malam
        "Raka segera berlari menembus kabut kembali menyusuri jalan dimana dia tadi datang"
        "Lalu tidak lama berlari, terlihat mobil SUV di dekat kebun pisang, dan ada siluet seseorang berdiri melambaikan tangan"
        scene cg_mgchap05b_end_bimo_jemput with dissolve
        b "Hoy.. Raka.. Kami disini.."
        show bimo_normal at center with dissolve_kilat
        b "Oh ya Raka, kau beruntung. Tadi saat kau pergi, kebetulan ada beberapa orang suruhan Pak Kades Tirto lewat berpatroli. Mereka sangat ramah dan membantu kami memperbaiki radiator mobil yang jebol."
        b "Makanya tidak lama kamu pergi. kami jejak mobilmu tadi"
        hide bimo_normal
        show raka_berpikir at center with dissolve_kilat
        r "Alhamdulillah.. Kupikir aku akan berjalan mencari kalian semalaman. hehehe"
        r "Eh By The Way Orang suruhan Pak Kades? Malem-malem begini patroli di pinggir hutan berkabut? Rajin bener..."
        hide raka_berpikir

        show citra_lega at center with dissolve_kilat
        c "Iya Kak! Mereka baik banget lho. Untung aja Pak Kades yang ngundang kita ke desa ini emang peduli sama warganya."
        hide citra_lega
        return "lose"