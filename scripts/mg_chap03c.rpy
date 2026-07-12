# ==========================================
# FILE: mg_chap03c.rpy
# MINIGAME: Introgasi Joko (Ilusi Gaib Citra)
# ==========================================

# ------------------------------------------
# DEFINISI GAMBAR MINIGAME 03C
# ------------------------------------------
image at_severed_demonic_head = "images/item/at_severed_demonic_head.webp"
image at_red_spot = "images/item/at_red_spot.webp"
image bg_mg03c_joko_aura = "images/cg/bg_mg03c_joko_aura.webp"
image cg_mg03c_citra_intimidasi = "images/cg/cg_mg03c_citra_intimidasi.webp"
image cg_mg03c_raka_jotos = "images/cg/cg_mg03c_raka_jotos.webp"

# ------------------------------------------
# TRANSFORM ANIMASI GERAK MULUS
# ------------------------------------------
transform gerak_acak_introgasi(target_x, target_y):
    ease 0.4 xalign target_x yalign target_y

# ------------------------------------------
# SCREEN UI MINIGAME INTROGASI
# ------------------------------------------
screen mg_introgasi_joko():
    modal True
    
    # Latar Belakang (Joko yang ketakutan dengan aura gelap)
    add "bg_mg03c_joko_aura"

    # Waktu batas permainan: 10 Detik
    default time_limit = 10.0

    # Status 8 titik penempatan (False = Merah melayang, True = Kepala Iblis diam)
    default spot1 = False
    default spot2 = False
    default spot3 = False
    default spot4 = False
    default spot5 = False
    default spot6 = False
    default spot7 = False
    default spot8 = False

    # Titik kemunculan awal untuk 8 proyektil titik merah
    default p1_x = renpy.random.uniform(0.1, 0.9)
    default p1_y = renpy.random.uniform(0.2, 0.8)
    default p2_x = renpy.random.uniform(0.1, 0.9)
    default p2_y = renpy.random.uniform(0.2, 0.8)
    default p3_x = renpy.random.uniform(0.1, 0.9)
    default p3_y = renpy.random.uniform(0.2, 0.8)
    default p4_x = renpy.random.uniform(0.1, 0.9)
    default p4_y = renpy.random.uniform(0.2, 0.8)
    default p5_x = renpy.random.uniform(0.1, 0.9)
    default p5_y = renpy.random.uniform(0.2, 0.8)
    default p6_x = renpy.random.uniform(0.1, 0.9)
    default p6_y = renpy.random.uniform(0.2, 0.8)
    default p7_x = renpy.random.uniform(0.1, 0.9)
    default p7_y = renpy.random.uniform(0.2, 0.8)
    default p8_x = renpy.random.uniform(0.1, 0.9)
    default p8_y = renpy.random.uniform(0.2, 0.8)

    # Sistem Pergerakan Dinamis (Mengacak posisi setiap 0.4 detik)
    timer 0.4 repeat True action [
        SetScreenVariable("p1_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p1_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p2_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p2_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p3_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p3_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p4_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p4_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p5_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p5_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p6_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p6_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p7_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p7_y", renpy.random.uniform(0.2, 0.9)),
        SetScreenVariable("p8_x", renpy.random.uniform(0.1, 0.9)),
        SetScreenVariable("p8_y", renpy.random.uniform(0.2, 0.9))
    ]

    # Timer kegagalan
    timer time_limit action Return(False)
    
    # Timer keberhasilan (Mengecek apakah semua 8 titik sudah diisi)
    if spot1 and spot2 and spot3 and spot4 and spot5 and spot6 and spot7 and spot8:
        timer 0.2 action Return(True)

    # UI Indikator Waktu Berjalan
    vbox:
        xalign 0.5
        yalign 0.05
        spacing 10
        
        text "TANGKAP 8 TITIK MERAH UNTUK MEMANGGIL IBLIS! (10 Detik)" size 28 color "#ff3333" xalign 0.5 bold True
        
        bar:
            value AnimatedValue(0, time_limit, time_limit) 
            range time_limit 
            xsize 600 
            ysize 25
            xalign 0.5

# ===============================================
    # TITIK 1
    # ===============================================
    if not spot1:
        imagebutton:
            idle "at_red_spot"
            at gerak_acak_introgasi(p1_x, p1_y)
            action [SetScreenVariable("spot1", True), Play("sound", "<vol=0.3>sfx_demonic_roar.ogg")]
    else:
        add "at_severed_demonic_head" xpos 350 ypos 200

    # ===============================================
    # TITIK 2
    # ===============================================
    if not spot2:
        imagebutton:
            idle "at_red_spot"
            at gerak_acak_introgasi(p2_x, p2_y)
            action [SetScreenVariable("spot2", True), Play("sound", "<vol=0.3>sfx_demonic_roar.ogg")]
    else:
        add "at_severed_demonic_head" xpos 850 ypos 200

    # ===============================================
    # TITIK 3
    # ===============================================
    if not spot3:
        imagebutton:
            idle "at_red_spot"
            at gerak_acak_introgasi(p3_x, p3_y)
            action [SetScreenVariable("spot3", True), Play("sound", "<vol=0.3>sfx_demonic_roar.ogg")]
    else:
        add "at_severed_demonic_head" xpos 200 ypos 400

    # ===============================================
    # TITIK 4
    # ===============================================
    if not spot4:
        imagebutton:
            idle "at_red_spot"
            at gerak_acak_introgasi(p4_x, p4_y)
            action [SetScreenVariable("spot4", True), Play("sound", "<vol=0.3>sfx_demonic_roar.ogg")]
    else:
        add "at_severed_demonic_head" xpos 1000 ypos 400

    # ===============================================
    # TITIK 5
    # ===============================================
    if not spot5:
        imagebutton:
            idle "at_red_spot"
            at gerak_acak_introgasi(p5_x, p5_y)
            action [SetScreenVariable("spot5", True), Play("sound", "<vol=0.3>sfx_demonic_roar.ogg")]
    else:
        add "at_severed_demonic_head" xpos 300 ypos 600

    # ===============================================
    # TITIK 6
    # ===============================================
    if not spot6:
        imagebutton:
            idle "at_red_spot"
            at gerak_acak_introgasi(p6_x, p6_y)
            action [SetScreenVariable("spot6", True), Play("sound", "<vol=0.3>sfx_demonic_roar.ogg")]
    else:
        add "at_severed_demonic_head" xpos 900 ypos 600

    # ===============================================
    # TITIK 7
    # ===============================================
    if not spot7:
        imagebutton:
            idle "at_red_spot"
            at gerak_acak_introgasi(p7_x, p7_y)
            action [SetScreenVariable("spot7", True), Play("sound", "<vol=0.3>sfx_demonic_roar.ogg")]
    else:
        add "at_severed_demonic_head" xpos 500 ypos 100

    # ===============================================
    # TITIK 8
    # ===============================================
    if not spot8:
        imagebutton:
            idle "at_red_spot"
            at gerak_acak_introgasi(p8_x, p8_y)
            action [SetScreenVariable("spot8", True), Play("sound", "<vol=0.3>sfx_demonic_roar.ogg")]
    else:
        add "at_severed_demonic_head" xpos 700 ypos 100
# ==========================================
# 3. LABEL PEMICU MINIGAME INTROGASI
# ==========================================
label play_mg_chap03_introgasi:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    stop music fadeout 1.0
    play music "bgm_06_panggilan_arwah.ogg" fadein 1.0

    # Cutscene Intro Minigame
    scene cg_mg03c_citra_intimidasi with flashmerah
    play sound "sfx_glitch_kesurupan.ogg"
    
    c "{b}Beri tahu kami di mana Ki Renggo, atau teman-temanku dari alam bawah akan menemanimu di gudang ini selamanya!{/b}"
    
    "Tangkap 8 titik merah yang melayang di layar dengan cepat untuk memanggil ilusi Kepala Iblis!"
    
    # Memanggil screen minigame
    call screen mg_introgasi_joko
    
    # Evaluasi Hasil (Menang/Kalah)
    if _return == True:
        # Jika Menang: Citra dapat poin gaib
        $ citra_resonansi_gaib = getattr(store, "citra_resonansi_gaib", 0) + 1
        
        play sound "sfx_teriakan_wanita.ogg"
        scene bg_gudang_beras with flashmerah
        show debu_melayang
        
        show joko_panik at center with hpunch
        j "KYAAAAAAA!!! Ampun Neng! Jauhkan wajah-wajah iblis itu dari saya! Ini... ini petanya!"
        hide joko_panik
        
        show citra_lega at center with dissolve_kilat
        c "(Tersenyum miring) Kerja bagus. Hantu-hantu itu lumayan nurut ternyata."
        hide citra_lega
        
    else:
        # Jika Kalah: Raka pakai kekerasan
        stop music fadeout 0.5
        play music "bgm_05_otot_kawat.ogg" fadein 1.0
        $ citra_resonansi_gaib -=1
        play sound "sfx_punch.ogg"
        scene cg_mg03c_raka_jotos with hpunch
        
        "BAM!! Beras berhamburan ke udara saat kepalan tangan Raka menghancurkan karung tepat di sebelah kepala Joko."
        
        r "Kelamaan mikir lu! Kalo lu nggak ngasih tau, kepala lu gue bikin kayak karung beras ini!"
        
        scene bg_gudang_beras with hpunch
        show debu_melayang
        show joko_panik at center with mata_mengerjap
        j "A-ampun Bang! Jangan pukul saya! Ini petanya!"
        hide joko_panik

    # Transisi pemberian peta
   # Transisi pemberian peta
    play sound "sfx_merobek_plasik.ogg"
    scene cg_ch3_peta_renggo with dissolve_lambat
    "Joko merogoh kantong seragamnya yang kotor dengan tangan bergetar, menyerahkan secarik kertas berisi coretan rute menuju padepokan Ki Renggo."
    

    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP03_INTROGASI SELESAI")
    # -----------------------------------
    return