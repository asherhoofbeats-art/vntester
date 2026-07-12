# ==========================================
# FILE: chapter02.rpy
# TEMA: Lendir, Bau Anyir, dan Penampakan
# ==========================================

label chapter_02:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------

    # Inisialisasi variabel petunjuk khusus untuk chapter ini
    $ ch2_lendir_kimia = False

    # Tampilan Judul Chapter di awal
    scene black with bangun_tidur
    play music "bgm_04_teror_tak_kasatmata.ogg" fadein 2.0
    centered "{size=+20}CHAPTER 02{/size}\n\nLendir, Bau Anyir, dan Penampakan" with dissolve_lambat
    pause 2.0
    
    # Scene 1: Masuk ke bagian dalam Dapur MBG
    play sound "sfx_creaky_door_open.ogg"
    scene bg_dalam_dapur with dorong_atas
    show kabut_tipis
    
    "Pintu utama Dapur MBG berderit keras saat Raka mendorongnya. Bau busuk sisa makanan bercampur anyir darah langsung menusuk hidung."
    "Panci-panci besar berserakan di lantai, dan sayuran busuk bertebaran di mana-mana."

    play sound "sfx_fast_swoosh.ogg"
    
    # --- CUT SCENE: Bayangan Buto di Ventilasi ---
    scene cg_ch02_bayangan_buto with dissolve_kilat
    pause 1.5
    
    scene bg_dalam_dapur with dissolve
    show citra_panik at center with mata_mengerjap
    c "Ya ampun... baunya nyengat banget! Dan... Kak Bimo, aku lihat bayangan gede banget lewat di dekat ventilasi tadi!"
    hide citra_panik

    show bimo_berpikir at center with dissolve_kilat
    b "Aku juga merasakannya, Citra. Ada energi yang sangat purba dan marah di ruangan ini. Tetap berada di belakangku."
    hide bimo_berpikir

    show raka_normal at center with dissolve_kilat
    r "Kalian ini parnoan banget. Bayangan gede itu paling cuma tikus got atau kucing yang kena pantulan senter."
    hide raka_normal

    play sound "sfx_benda_jatuh.ogg"
    "Tiba-tiba, terdengar suara gemerisik dari balik tumpukan karung kentang. Raka langsung memasang kuda-kuda karatenya."

    play sound "sfx_serangan_cepat.ogg"
    show raka_marah at center with dorong_kanan
    r "Siapa di sana?! Keluar atau gue tendang karung ini!"
    hide raka_marah

    play sound "sfx_gasp.ogg"
    "Seorang wanita tua dengan seragam dapur yang kotor merangkak keluar sambil gemetar hebat."

    show darmi_panik at center with dissolve_kilat
    md "A-ampun... ampun Den! Jangan makan kulo! Kulo mboten nderek-nderek urusane Pak Kades!"
    hide darmi_panik

    show bimo_normal at center with dissolve_kilat
    b "Tenang, Bu. Kami bukan makhluk jahat. Kami ke sini untuk menyelidiki kasus ini. Ibu siapa?"
    hide bimo_normal

    show darmi_normal at center with dissolve_kilat
    md "K-kulo Mbok Darmi, Den. Koki di sini. Kulo ndelik (sembunyi) pas kejadian... Mengerikan, Den! Genderuwo gede banget ngerobek weteng (perut) temen-temen kulo!"
    hide darmi_normal

    show raka_berpikir at center with dissolve_kilat
    r "Mbok lihat sendiri Genderuwo-nya? Atau cuma lihat hasil akhirnya aja?"
    hide raka_berpikir

    show darmi_panik at center with mata_mengerjap
    md "Kulo mboten wani lihat langsung, Den! Tapi ada lendir hijau bau banget di pojokan sana! Itu pasti ludahnya Genderuwo! Tolong Den, kulo mau pulang!"
    hide darmi_panik

    # ==========================================
    # PANGGIL MINIGAME 02B: CITRA MENGANTAR DARMI
    # ==========================================
    show citra_lelah at center with dissolve_kilat
    c "Kasihan Mbok Darmi, Kak... Dia trauma berat. Biar aku antar dia keluar garis polisi dulu melewati area depan."
    hide citra_lelah

    "Citra memapah Mbok Darmi, berusaha membawanya keluar dari dapur yang dipenuhi aura menekan."
    
  
    call play_mg_chap02b
    
    if _return == "win":
        # Jika berhasil mengantar tanpa membuat Darmi lebih panik
        $ darmi_trust = True
        $ citra_resonansi_gaib += 1
        c "Udah Beres.. Aku berhasil Antar Mbok Darmi sampai keluar gerbang"
        "Citra berhasil membangun kepercayaan yang kuat dengan Mbok Darmi."
    else:
        # Jika gagal / Darmi ketakutan
        $ darmi_trust = False
        
        md "LEPASKAN!! Kulo mau lari sendiri!! Menjauh dari kulo!!"
        "Mbok Darmi meronta ketakutan dan berlari tak tentu arah ke luar balai desa, meninggalkan Citra yang kebingungan."
    # ... kode setelahnya ...

    play sound "sfx_footsteps_fast.ogg"
    "Setelah urusan dengan Mbok Darmi selesai, Trio Investigator melangkah lebih dalam menuju pusat TKP."

    # Scene 2: Lokasi Penemuan Mayat
    stop music fadeout 2.0
    scene bg_tkp_mayat with wipe_kanan
    show kabut_area
    play music "bgm_03_bayang_petunjuk.ogg" fadein 2.0

    "Mereka tiba di area belakang dapur. Garis polisi melingkari sebuah noda gelap di lantai yang sudah mengering."
    
    play sound "sfx_splat.ogg"
    "Di sekitarnya, terdapat genangan cairan kental berwarna hijau yang memancarkan bau menyengat."

    show bimo_marah at center with dissolve_kilat
    b "Astaghfirullah... Arwah-arwah penasaran korban masih berkumpul di sini. Hawanya sangat panas. Aku harus mulai merapal doa pembersih."
    hide bimo_marah

    # ==========================================
    # PANGGIL MINIGAME 02A: BIMO MENGHALAU ARWAH
    # ==========================================
    "Bimo duduk bersila, memejamkan mata, dan mulai menetralkan hawa negatif TKP!"
    
    call play_mg_chap02a
    
    if _return == False:
        # Jika Bimo gagal menetralkan aura
        scene black with flashmerah
        "Energi negatif terlalu kuat! Arwah penasaran merasuki Bimo dan membuatnya lepas kendali!"
        centered "{size=+20}GAME OVER{/size}\n\nGagal menetralkan aura negatif di TKP."
        return
        
    play sound "sfx_magic_spell.ogg"
    "Bimo berhasil menyelesaikan mantranya, membuat udara di ruangan itu terasa sedikit lebih ringan. Kini mereka bisa menyelidiki TKP dengan lebih aman."
    $ citra_resonansi_gaib += 1
    "Raka menyalakan senternya dan mendekati genangan tersebut."

    show raka_berpikir at center with transisi_senter
    r "Lendir hijau ya... Mbok Darmi bilang ini ludah Genderuwo. Tapi baunya familiar. Nggak kayak bau amis makhluk gaib."
    hide raka_berpikir

    # Pilihan interaktif yang mempengaruhi ending chapter
    menu:
        "Gunakan senter untuk menginspeksi tong di sudut ruangan":
            $ ch2_lendir_kimia = True
            stop sound fadeout 1.0
            play sound "sfx_petunjuk_datang.ogg"
            $ poin_investigasi += 2
            $ item_lendir_hijau = True
            # --- CUT SCENE: Raka Mengambil Sampel Kimia ---
            scene cg_ch02_raka_ziplock with transisi_senter
            r "Bingo! Coba lihat ini. Ada tong bekas bahan kimia pabrik di pojokan sini yang sengaja ditutupi kardus."
            r "Lendir hijau ini bukan ludah monster. Ini campuran lem industri dan zat pewarna! Sengaja disebar biar mitos Genderuwo makin dipercaya!"
            
            # Menampilkan ITEM Sampel Kimia
            scene bg_tkp_mayat with dissolve
            show item_lendir_kimia at truecenter with dissolve_kilat
            pause 1.5
            hide item_lendir_kimia with dissolve

            show citra_normal at center with dissolve_kilat
            c "Wah, Kak Raka pinter juga! Berarti tebakanmu benar, ada manusia yang memalsukan TKP ini."
            hide citra_normal

            show bimo_normal at center with dissolve_kilat
            b "Bagus sekali, Raka. Simpan sedikit sampel itu di plastik ziplock. Ini bukti krusial."
            hide bimo_normal

        "Fokus menenangkan Citra yang mulai ketakutan":
            $ ch2_lendir_kimia = False
            $ poin_investigasi -=1
            stop sound fadeout 1.0
            play sound "sfx_gema_suara_hantu.ogg"
            
            scene bg_tkp_mayat with dissolve
            show citra_panik at center with tv_rusak
            c "Kak Raka... kepalaku pusing banget... Suara tangisan mereka kenceng banget di telingaku!"
            hide citra_panik
            
            # ==========================================
            # PANGGIL MINIGAME 02C: KESEIMBANGAN MENTAL CITRA
            # ==========================================
            "Citra kewalahan oleh suara gaib! Bantu Citra menyeimbangkan frekuensi mentalnya!"
            
            call play_mg_chap02c
            
            if _return == False:
                $ citra_resonansi_gaib -=1
                scene cg_ch02_citra_pusing with flashmerah
                with vpunch
                "Pikiran Citra hancur oleh bisikan gelap arwah penasaran!"
                scene black with pingsan
                centered "{size=+20}GAME OVER{/size}\n\nMental Citra terguncang hebat."
                return

           
            b "Eh, Citra! Tahan, jangan pingsan di sini dong! Lantainya kotor banyak lendir!"
            r "Udah, biarin aja lendirnya. Bahaya kalau kita sentuh sembarangan, mending kita fokus jagain lu aja."
            hide raka_panik
            $ citra_resonansi_gaib += 3
            show bimo_lelah at center with dissolve_kilat
            b "Untung kamu berhasil menahannya, Citra. Tapi karena ini, kita kehilangan waktu untuk mencari petunjuk fisik di ruangan ini."
            hide bimo_lelah

    # Penutup Chapter & Kesimpulan Dinamis
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with pingsan
    centered "{size=+15}END OF CHAPTER 02{/size}" with dissolve_lambat
    pause 1.5

    # Teks Teaser/Kesimpulan berdasarkan pilihan pemain
    if ch2_lendir_kimia:
        "KESIMPULAN CHAPTER:\nInsting tajam Raka membuahkan hasil. Mereka mengantongi 'Sampel Lendir Kimia', bukti tak terbantahkan bahwa teror Genderuwo hanyalah rekayasa untuk menutupi pembunuhan keji. Namun, jika ini murni rekayasa manusia, mengapa Bimo dan Citra merasakan entitas yang sangat gelap di sekitar mereka? Penyelidikan baru saja dimulai."
    else:
        "KESIMPULAN CHAPTER:\nFokus Raka terpecah karena harus menjaga Citra yang kelelahan secara spiritual. Alhasil, Trio Investigator melewatkan petunjuk krusial mengenai asal-usul lendir hijau tersebut. Mereka meninggalkan TKP dengan asumsi buta, membuat langkah mereka selanjutnya penuh dengan tebakan berbahaya. Siapakah yang akan menyerang mereka lebih dulu, sang mafia atau sang iblis?"
    
    pause 3.0

    # Lanjut ke Chapter berikutnya

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("CHAPTER_02 SELESAI")
    # -----------------------------------
    jump chapter_03