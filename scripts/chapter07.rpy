# ==========================================
# FILE: chapter07.rpy
# TEMA: Murka Gaib dan Teriakan Massa
# STYLE: 16-Bit Retro Horror
# ==========================================

# ------------------------------------------
# DEFINISI ASET CG STORY (CHAPTER 07)
# ------------------------------------------
image cg_chap07_tirto_dicekik_hantu = "images/cg/cg_chap07_tirto_dicekik_hantu.webp"
image cg_chap07_warga_ngamuk = "images/cg/cg_chap07_warga_ngamuk.webp"
image cg_chap07_bimo_persiapan_segel = "images/cg/cg_chap07_bimo_persiapan_segel.webp"
image bg_ruang_tirto_hancur = "images/bg/bg_ruang_tirto_hancur.webp"


default ch7_menang_segel = False

label chapter_07:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Tampilan Judul Chapter di awal
    scene black with bangun_tidur
    play music "bgm_05_otot_kawat.ogg" fadein 2.0
    centered "{size=+20}CHAPTER 07{/size}\n\nMurka Gaib dan Teriakan Massa" with dissolve_lambat
    pause 2.0
    
    # ------------------------------------------
    # SCENE 1: PERTARUNGAN 4 VS 4 (MINIGAME A)
    # ------------------------------------------
    scene bg_ruang_tirto with hpunch
    
    show tirto_marah at center with dorong_bawah
    t "Bodoh! Kenapa kalian diam saja?! Habisi anak-anak ingusan ini dan si pengkhianat Gatot! Bunuh mereka!"
    hide tirto_marah

    play sound "sfx_serangan_cepat.ogg"
    "Ketiga preman bertubuh kekar bayaran Pak Tirto mencabut parang dan rantai besi, merangsek maju ke arah mereka."

    show raka_marah at left with dissolve_kilat
    r "Gatot, lu ambil yang kiri sama tengah! Gue yang kanan!"
    
    show gatot_marah at right with dissolve_kilat
    g "Sip! Biar gue patahin leher anjing-anjing peliharaan Tirto ini!"
    hide raka_marah
    hide gatot_marah

    # ==========================================
    # PANGGIL MINIGAME 7A: BRAWL 4v4 (QTE)
    # ==========================================
    "Pertarungan sengit tak terhindarkan. Raka dan Gatot harus berkoordinasi menangkis serangan mematikan para preman!"
    
    call play_mg_chap07a
    
    if _return == False:
        # Jika game over di MG 7A
        return

    # ------------------------------------------
    # SCENE 2: KEMUNCULAN ENTITAS & RESONANSI CITRA
    # ------------------------------------------
    stop music fadeout 1.5
    play sound "sfx_angin_besar.ogg" loop fadein 1.0
    
    show citra_panik at center with tv_rusak
    c "Tunggu! Semuanya berhenti! Hawanya... hawanya tiba-tiba berubah! Jauh lebih pekat dari yang di dapur tadi!"
    hide citra_panik

    play sound "sfx_glass_shatter.ogg"
    "Suhu di ruangan anjlok drastis. Niat membunuh dari Gatot dan ketakutan ekstrem Tirto seolah memancing sesuatu dari kegelapan."
    "Lampu ruangan berkedip-kedip sebelum akhirnya meledak, menyisakan cahaya temaram dari bulan."

    play music "bgm_07_murka_penjaga.ogg" fadein 1.0
    
    show bimo_panik at right with dorong_kiri
    b "Astaga... Energi dari amarah dan dendam tumbal-tumbal itu berkumpul! Ada entitas sungguhan yang datang memanifestasikan diri!"

    # Menggunakan CG Tirto Dicekik Hantu
    play sound "sfx_demon_roar.ogg"
    scene cg_chap07_tirto_dicekik_hantu with vpunch
    "Sesosok bayangan raksasa bermata merah muncul di sudut ruangan yang berantakan, mencengkeram leher Tirto yang berteriak histeris."

    t "AAARGH! T-Tolong! Jauhkan monster ini!"

    # Kembali ke layar normal untuk dialog
    
    show bimo_marah at right with dissolve_kilat
    b "Kalau dia dibunuh oleh arwah, kita kehilangan saksi! Hukum duniawi butuh dia hidup-hidup! Citra, tahan energi spiritualnya! Aku butuh waktu untuk merapal segel!"

    show citra_marah at left with flash_biru
    c "A-aku akan coba meresonansikan auraku dengan mereka... Kumohon, tenanglah!"

    # ==========================================
    # PANGGIL MINIGAME 7B: RESONANSI CITRA
    # ==========================================
    call play_mg_chap07b
    
    if _return == False:
        # Jika game over di MG 7B
        return
        
    # ------------------------------------------
    # SCENE 3: SEGEL BIMO (MINIGAME C)
    # ------------------------------------------
    scene cg_chap07_bimo_persiapan_segel with transisi_asap
    play sound "sfx_mantra_whisper.ogg" loop
    show bimo_fokus at center
    b "Citra berhasil menahan energinya! Sekarang giliranku!"
    b "Tolong lindungi punggungku, Raka! Aku tidak boleh kehilangan konsentrasi!"
    hide bimo_fokus
    show raka_marah
    r "Siap! Lu fokus aja sama komat-kamit lu, monster itu biar gue yang halau kalau mendekat!"

    # ==========================================
    # PANGGIL MINIGAME 7C: SEGEL MANTRA (PUZZLE)
    # ==========================================
    call play_mg_chap07c
    
    if _return == False:
        # Jika kalah game over di MG 7C
        return
        
    # Jika Menang:
    $ ch7_menang_segel = True
    $ citra_resonansi_gaib +=1
    stop music fadeout 2.0
    play music "bgm_03_bayang_petunjuk.ogg" fadein 2.0

    scene bg_ruang_tirto_hancur with dissolve_lambat
    show bimo_lega at center with dissolve_lambat
    b "Hah... hah... Berhasil. Ancaman gaibnya sudah netral."
    hide bimo_lega

    show raka_lega at left with dissolve_kilat
    r "Aman! Sini lu, koruptor botak!"
    hide raka_lega

    play sound "sfx_merobek_plasik.ogg"
    "Raka langsung menarik kerah Pak Tirto yang masih gemetar ketakutan dan mengikat tangannya menggunakan kabel telepon di kursi."


    # ------------------------------------------
    # SCENE 4: AMUK MASSA & PROVOKASI MBOK DARMI
    # ------------------------------------------
    show tirto_panik at center with mata_mengerjap
    t "S-saya menyerah... Tolong bawa saya pergi ke kantor polisi. T-tempat ini dikutuk!"
    hide tirto_panik

    show citra_lelah at left with dissolve_kilat
    c "Syukurlah... Kita udah punya bukti kuat. Aku akan telepon markas sekarang—"
    hide citra_lelah

    stop music fadeout 1.0
    play sound "sfx_gemuruh_gua.ogg" fadein 1.0
    "Namun, sebelum Citra sempat memutar nomor, terdengar suara gemuruh yang sangat bising dari arah luar gedung."
    
    play sound "sfx_glass_shatter.ogg"
    "Suara ratusan langkah kaki, teriakan beringas, pecahan kaca lantai bawah, dan cahaya terang berwarna oranye menyinari ruangan dari luar jendela."

    show raka_panik at center with dorong_bawah
    r "Suara apa itu?!"
    hide raka_panik

    play sound "sfx_footsteps_fast.ogg"
    "Gatot berjalan cepat ke arah jendela dan mengintip ke bawah. Matanya terbelalak kaget."

    # Menggunakan CG Warga Ngamuk
    play music "bgm_12_keadilan_mati.ogg" fadein 1.0
    scene cg_chap07_warga_ngamuk with flashmerah
    show gatot_normal at left
    play sound "sfx_warga_ngamuk"
    g "Gila... Balai desa dikepung warga! Ratusan orang bawa obor, parang, sama jerigen bensin!"
    hide gatot_normal
    show raka_marah at left
    r "Apa?! Gimana warga bisa tahu kita di sini?!"
    hide raka_marah
    show gatot_normal at left
    g "Tunggu... Liat di barisan paling depan! Itu... Mbok Darmi?!"
    hide gatot_normal
    play sound "sfx_warga_marah.ogg" loop
    show darmi_marah at left
    md "(Berteriak dari bawah) ITU DIA! TIRTO SI KADES KEPARAT! DIA YANG BIKIN DESA KITA KENA KUTUK PESUGIHAN!"
    
    play sound "sfx_fire_crackling.ogg" loop
    md "HANCURKAN BALAI DESA! BAKAR DIA HIDUP-HIDUP SEBELUM DIA MENGORBANKAN ANAK CUCU KITA!"
    hide darmi_marah
    "Warga yang terbakar amarah bersorak menyetujui ucapan Mbok Darmi. Mereka mulai melemparkan obor ke arah pintu masuk."

    # Kembali ke layar normal
    scene bg_ruang_tirto_hancur with dissolve_kilat
    
    show raka_marah at left with flashmerah
    r "Sial! Nenek tua itu bukannya dia yang ngeracunin orang-orang?! Sekarang dia malah mutarbalikkan fakta buat nyelamatin dirinya sendiri!"
    
    show citra_panik at right with vpunch
    c "Kak Raka... Mereka benar-benar mulai menyiram bensin ke pintu utama! Api mulai membesar!"

    show gatot_marah at center with hpunch
    g "Sialan! Kalau lantai bawah dibakar, kita ikut mati terpanggang di lantai dua ini!"
    hide gatot_marah
    hide raka_marah
    hide citra_panik

    # Penutup Chapter & Kesimpulan Dinamis
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with pingsan
    centered "{size=+15}END OF CHAPTER 07{/size}" with dissolve_lambat
    pause 1.5

    "KESIMPULAN CHAPTER:\nPertarungan brutal melawan preman dan entitas gaib berhasil dimenangkan oleh Trio Investigator. Pak Tirto akhirnya tertangkap basah. Namun, kemenangan ini berumur pendek. Hasutan licik Mbok Darmi memicu dendam warga desa meledak menjadi amuk massa yang buta. Balai Desa kini dikepung lautan api. Terjebak di lantai dua bersama sang dalang kejahatan, malam ini berubah menjadi perjuangan absolut untuk bertahan hidup dari murka manusia."

    pause 3.0

    # Lanjut ke Chapter 08

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_07 SELESAI")
    # -----------------------------------
    jump chapter_08_awal