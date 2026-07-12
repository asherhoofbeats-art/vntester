# ==========================================
# FILE: chapter04.rpy
# TEMA: Jejak Sang Dukun
# ==========================================

# ------------------------------------------
# DEFINISI CG BARU CHAPTER 04
# ------------------------------------------
image cg_ch04_hutan_bambu = "images/cg/cg_ch04_hutan_bambu.webp"
image cg_ch04_penjaga_gaib = "images/cg/cg_ch04_penjaga_gaib.webp"
image cg_ch04_raka_dobrak = "images/cg/cg_ch04_raka_dobrak.webp"
image cg_ch04_jenglot_tua = "images/cg/cg_ch04_jenglot_tua.webp"
image cg_ch04_renggo_dicekik = "images/cg/cg_ch04_renggo_dicekik.webp"
image cg_ch04_renggo_terkulai = "images/cg/cg_ch04_renggo_terkulai.webp"
image cg_chap04_raka_banting_renggo = "images/cg/cg_chap04_raka_banting_renggo.webp"
image cg_chap04_bimo_kalahkan_hantu = "images/cg/cg_chap04_bimo_kalahkan_hantu.webp"

# ------------------------------------------
# MAIN STORY CHAPTER 04
# ------------------------------------------
label chapter_04:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Inisialisasi variabel untuk chapter ini
    $ ch4_jenglot_tua = False
    $ ch4_menyan_jafaron = False

    # Tampilan Judul Chapter di awal
    scene black with bangun_tidur
    play music "bgm_04_teror_tak_kasatmata.ogg" fadein 2.0
    centered "{size=+20}CHAPTER 04{/size}\n\nJejak Sang Dukun" with dissolve_lambat
    pause 2.0
    
    # Scene 1: Tiba di luar Padepokan
    scene bg_padepokan_luar with transisi_asap
    show kabut_tipis
    show daun_gugur
    play sound "sfx_angin_malam_kencang.ogg" loop fadein 1.0
    
    "Berdasarkan informasi dari satpam Joko, Trio Investigator menyusuri jalan setapak di pinggir desa menuju padepokan Ki Renggo."
    "Bangunan kayu beraura suram itu berdiri di tengah pepohonan bambu yang berderit ditiup angin malam."

    # --- CUT SCENE 1: Menembus Hutan Bambu Berhantu ---
    scene cg_ch04_hutan_bambu with dissolve_lambat
    "Langkah mereka melambat seiring pekatnya kabut yang mendadak mengepung. Gesekan batang-batang bambu terdengar seolah sedang saling berbisik memperingatkan kedatangan mereka."

    # ==========================================
    # [PANGGIL MINIGAME 04A: LABIRIN BAMBU]
    # ==========================================
    call play_mg_chap04_maze

    scene bg_padepokan_luar with dissolve
    play sound "sfx_dengung_insting_bahaya.ogg"
    play music "bgm_creepy_ambient.ogg"
    show bimo_berpikir at center with dissolve_kilat
    b "Berhenti sebentar. Padepokan ini dilindungi oleh pagar gaib. Ada sosok hitam besar yang menjaga pintu depan."
    hide bimo_berpikir

    show citra_panik at center with mata_mengerjap
    c "I-iya Kak Bimo... Matanya merah terang ngeliatin kita dari tadi. Aku nggak berani maju."
    hide citra_panik

    scene cg_ch04_penjaga_gaib with dissolve_lambat
    "Di bawah kegelapan malam, sesosok entitas bayangan hitam pekat dengan sepasang mata merah menyala berdiri kokoh di depan pintu gubuk, memancarkan hawa kebencian yang menusuk tulang."

    scene bg_padepokan_luar with dissolve
    show raka_lega at center with dissolve_kilat
    r "Halah, halusinasi kalian berdua aja itu. Di mata gue, ini cuma gubuk bambu reot yang digembok."
    hide raka_lega

    show raka_marah at center with dorong_kanan
    r "Udah, biar gue yang muter lewat pintu belakang dan dobrak masuk. Kalian tunggu di sini."
    hide raka_marah

    show bimo_normal at center with dissolve_kilat
    b "Silakan, Raka. Sementara kau mendobrak, aku akan menetralisir penjaga gaib di depan ini agar Citra bisa aman masuk."
    hide bimo_normal

    # ==========================================
    # [PANGGIL MINIGAME 04B: SEGEL BIMO]
    # ==========================================
    call play_mg_chap04_segel

    # Scene 2: Di dalam Padepokan
    stop sound fadeout 0.5
    play sound "sfx_door_kick.ogg"
    
    # --- CUT SCENE 4: Dobrakan Maut Raka ---
    scene cg_ch04_raka_dobrak with flashbang
    "BRAAAAKK!"
    "Pintu belakang padepokan hancur berantakan menjadi serpihan kayu akibat tendangan keras Raka yang tanpa basa-basi."

    scene bg_padepokan_dalam with dissolve
    show debu_melayang
    play music "bgm_05_otot_kawat.ogg" fadein 1.0
    "Raka mendobrak pintu belakang hingga engselnya lepas. Di tengah ruangan yang dipenuhi asap kemenyan, Ki Renggo terkejut bukan main."

    show renggo_marah at center with dorong_kiri
    kr "Siapa kalian?! Berani-beraninya mendobrak padepokan suci saya! Saya tidak tahu menahu urusan kalian!"
    hide renggo_marah

    show raka_marah at center with dissolve_kilat
    r "Nggak usah sok suci lu, dukun palsu! Kita tahu lu yang naruh barang bukti palsu di TKP Dapur MBG!"
    hide raka_marah
    
    show renggo_marah at center with dissolve_kilat
    kr "Tuduhan macam apa itu?! Kalian cari mati berurusan dengan Ki Renggo!"
    hide renggo_marah

    # ==========================================
    # [PANGGIL MINIGAME 04C: ADU KEKUATAN DUKUN]
    # ==========================================
    call play_mg_chap04_dukun

    # Setelah adu kekuatan, Renggo ditangkap.
    stop music fadeout 2.0
    play music "bgm_03_bayang_petunjuk.ogg" fadein 2.0

    "Raka dan Bimo segera mengikat Ki Renggo yang kini sudah kehilangan daya perlawanannya akibat serangan balik Citra."

    show renggo_panik at center with dorong_bawah
    kr "A-ampun, Den! Aduh, ampun! S-saya ngaku... Saya ini cuma disuruh!"
    hide renggo_panik

    show raka_berpikir at center with dissolve_kilat
    r "Disuruh siapa?! Dan kenapa lu bikin perut mayat-mayat itu robek, hah?!"
    hide raka_berpikir

    show renggo_panik at center with mata_mengerjap
    kr "Sumpah demi Tuhan, Den! Bukan saya yang ngerobek perutnya! Waktu saya datang ke TKP, mayat-mayat itu perutnya sudah robek duluan!"
    kr "Saya cuma dibayar buat nyiram lendir hijau sama naruh kalung aja biar dikira ulah Genderuwo!"
    hide renggo_panik
    
    show bimo_berpikir at center with dissolve_kilat
    b "Bukan kau? Lalu siapa yang membayar jasamu untuk memalsukan TKP mengerikan itu?"
    hide bimo_berpikir
    
    show renggo_panik at center with mata_mengerjap
    kr "Sumpah saya mboten ngertos (tidak tahu), Den! Saya cuma dapat pesan dari orang suruhan yang nggak saya kenal!"
    hide renggo_panik

    # --- CUT SCENE: Raka Membanting Ki Renggo ---
    play sound "sfx_bashing.ogg"
    scene cg_chap04_raka_banting_renggo with hpunch
    play sound "sfx_strong_punch.ogg"
    "Karena kesal mendengar Ki Renggo yang berbelit-belit dan mencoba berbohong, Raka langsung mencengkeram kerahnya dan membanting dukun tua itu ke lantai kayu dengan keras!"
    
    r "Jangan main-main sama gue! Sekali lagi lu bohong, gue patahin leher lu! Siapa yang nyuruh?!"
    
    scene bg_padepokan_dalam with dissolve
    show renggo_panik at center with vpunch
    kr "Aduh, ampun Den! Iya, iya saya ngaku! Sama Bu Dokter dari Puskesmas, Den! Dokter Rina! Dia bayar saya mahal banget!"
    hide renggo_panik

    show raka_berpikir at center with dissolve_kilat
    r "Dokter Puskesmas? Buat apa seorang dokter medis repot-repot nyewa dukun buat bikin teror klenik?"
    hide raka_berpikir

    show bimo_berpikir at center with dissolve_kilat
    b "Pasti ada sesuatu yang sangat fatal yang sengaja disembunyikan Dokter Rina dalam laporan hasil autopsinya..."
    hide bimo_berpikir

    play sound "sfx_menggigil.ogg"
    "Sementara Raka dan Bimo sibuk mencerna pengakuan tersebut, Citra berdiri kaku di sudut ruangan. Pandangannya terpaku pada sebuah kotak kayu usang di bawah meja ritual."

    show citra_berpikir at center with dissolve_lambat
    c "(Hawa di sudut ini beda... Dingin, pekat, dan bau anyir darah... Sangat berbeda dengan trik murahan Ki Renggo ini.)"
    hide citra_berpikir

    # Pilihan interaktif: Penentu Syarat Secret Ending / Lore Jenglot
    menu:
        "Cek kotak kayu yang memancarkan hawa dingin tersebut":
            # ==========================================
            # [PANGGIL MINIGAME 04D: RHYTHM RADAR JENGLOT]
            # ==========================================
            call play_mg_chap04_jenglot
            
            if _return == "win":
                $ ch4_jenglot_tua = True
                $ citra_resonansi_gaib +=3
                $ item_jenglot = True
                play sound "sfx_creaky_door_open.ogg"
                "Citra perlahan membongkar papan kayu yang berdebu tersebut..."
                
                # --- CUT SCENE 6: Boneka Jenglot Tua ---
                scene cg_ch04_jenglot_tua with transisi_asap
                play sound "sfx_eerie.ogg"
                "Boneka Jenglot ini nampaknya merupakan barang terkutuk yang harus disingkirkan"

                scene bg_padepokan_dalam with dissolve
                show renggo_panik at center with tv_rusak
                kr "Jangan dibawa neng. itu sangat berbahaya. Saya ga tahu itu titipan orang"
                hide renggo_panik

                show bimo_normal at center with dissolve_kilat
                b "Benda ini adalah benda untuk pesugihan yang berbahaya. Kita sebaiknya menyimpannya untuk kemudian kita netralkan nanti. Berikan padaku Citra"
                hide bimo_normal
            else:
                $ ch4_jenglot_tua = False
                $ citra_resonansi_gaib -=2
                $ item_jenglot = False
                "Karena insting Citra buyar akibat gangguan entitas gaib, kalian akhirnya meninggalkan sudut ruangan itu tanpa menyadari adanya benda celaka di bawah sana."

        "Abaikan hawanya dan bersiap meringkus Ki Renggo":
            $ ch4_jenglot_tua = False
            play sound "sfx_fast_swoosh.ogg"
            show citra_lelah at center with dissolve_kilat
            c "(Ah, mungkin perasaanku aja. Daripada aku nemu hal aneh lagi, mending aku bantuin Kak Bimo melucuti barang bawaan dukun ini.)"
            hide citra_lelah
            
            # ==========================================
            # [PANGGIL MINIGAME 04E: KOTAK JIMAT MENYAN]
            # ==========================================
            call play_mg_chap04e

    scene bg_padepokan_dalam with dissolve
    show raka_lega at center with dissolve_kilat
    r "Oke, pengakuan lu udah gue rekam. Sekarang bangun, kita bawa lu ke kantor polisi!"
    hide raka_lega

    # --- KLIMAKS CHAPTER: SERANGAN MAHLUK GAIB ---
    stop music fadeout 1.0
    play sound "sfx_angin_besar.ogg" loop fadein 1.0
    "Namun, saat Raka menarik kerah baju Ki Renggo untuk berdiri, suhu ruangan mendadak anjlok drastis. Lampu minyak di padepokan seketika padam."

    show renggo_panik at center with mata_mengerjap
    kr "U-ugh... t-tolong... ukh!"
    hide renggo_panik

    play music "bgm_12_keadilan_mati.ogg" fadein 1.0
    scene cg_ch04_renggo_dicekik with vpunch
    play sound "sfx_bone_crack.ogg"
    
    "Tiba-tiba, sesosok lengan bayangan raksasa yang sangat hitam dan berotot bermanifestasi dari balik dinding, mencekik leher Ki Renggo hingga tubuh rentanya terangkat dari lantai!"
    
    scene bg_padepokan_dalam with flashmerah
    show citra_panik at center with hpunch
    c "KAK BIMO! ADA YANG NYEKIK DIA!"
    hide citra_panik

    show bimo_marah at center with dissolve_kilat
    b "Entitas pesugihannya marah karena rahasianya dibongkar! ALLAHU AKBAR!"
    hide bimo_marah
    
    scene cg_chap04_bimo_kalahkan_hantu with vpunch
    play sound "sfx_magic_spell.ogg"
    "Bimo melemparkan sisa garam Ruqyah miliknya. Bayangan raksasa itu menggeram marah lalu menghilang, menjatuhkan Ki Renggo dengan keras ke lantai."
    
    scene cg_ch04_renggo_terkulai with hpunch
    play sound "sfx_barang_berat_jatuh.ogg"
    "Tubuh Ki Renggo mengelepar sebentar sebelum akhirnya tak sadarkan diri. Wajahnya sangat pucat dan napasnya tersengal."
    
    scene bg_padepokan_dalam with dissolve
    show raka_panik at center with dissolve_kilat
    r "Sialan! Denyut nadinya lemah banget! Kalau dia mati, kita kehilangan saksi kunci!"
    hide raka_panik
    $ item_rekaman_renggo = True
    show bimo_panik at center with dissolve_kilat
    b "Kita harus melarikannya ke Puskesmas desa sekarang juga untuk menyelamatkan nyawanya! Sekalian kita minta pertanggungjawaban dari Dokter Rina!"
    hide bimo_panik

    # Penutup Chapter & Kesimpulan Dinamis
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with pingsan
    centered "{size=+15}END OF CHAPTER 04{/size}" with dissolve_lambat
    pause 1.5

    # Teks Teaser/Kesimpulan berdasarkan pilihan pemain
    if ch4_jenglot_tua:
        "KESIMPULAN CHAPTER:\nPenggerebekan padepokan menguak fakta tak terduga. Sang dukun palsu membantah melakukan mutilasi dan menunjuk Dokter Rina dari Puskesmas sebagai penyewa jasanya. Penemuan 'Boneka Jenglot Tua' oleh Citra serta serangan gaib raksasa yang mencekik Ki Renggo membuktikan satu hal mengerikan: konspirasi ini dimanfaatkan untuk praktik pesugihan maut."
    elif ch4_menyan_jafaron:
        "KESIMPULAN CHAPTER:\nSang dukun palsu menunjuk Dokter Rina sebagai penyewa jasanya. Meski Citra gagal mengungkap tabir gaib di sudut ruangan, ia berhasil membuka teka-teki kotak dan mengamankan 'Menyan Jafaron' yang sangat berguna untuk perlindungan. Serangan mendadak bayangan raksasa memastikan bahwa nyawa Trio Investigator kini menjadi incaran kekuatan gelap."
    else:
        "KESIMPULAN CHAPTER:\nSang dukun palsu membantah melakukan mutilasi dan mengarahkan kecurigaan pada Dokter Rina dari Puskesmas. Serangan tiba-tiba dari bayangan gaib raksasa yang membuat Ki Renggo sekarat membuktikan campur tangan kekuatan mistis. Citra gagal menemukan petunjuk atau perlindungan apa pun, membuat mereka melangkah ke Puskesmas dengan tangan kosong."
    
    pause 3.0

    # Lanjut ke Chapter berikutnya

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_04 SELESAI")
    # -----------------------------------
    jump chapter_05