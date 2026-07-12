# ==========================================
# FILE: mg_chap02c.rpy
# MINIGAME: Keseimbangan Mental (Fokus Raka & Citra)
# MEKANIK: Slider Balancing
# ==========================================

init python:
    import random

    class MentalBalanceGame:
        def __init__(self):
            self.slider = 50.0
            self.time_left = 10.0
            self.red_timer = 0.0
            self.max_red = 3.0 
            self.status = "playing"

        def update(self):
            if self.status != "playing":
                return
                
            drift = random.uniform(1.0, 4.0)
            if self.slider >= 50:
                self.slider += drift 
            else:
                self.slider -= drift 
                
            self.slider += random.uniform(-6.0, 6.0)
            self.slider = max(0.0, min(100.0, self.slider))
            
            if self.slider < 30.0 or self.slider > 70.0:
                self.red_timer += 0.1
            else:
                self.red_timer = max(0.0, self.red_timer - 0.05)
                
            self.time_left -= 0.1
            
            if self.red_timer >= self.max_red:
                self.status = "lose"
            elif self.time_left <= 0:
                self.status = "win"

        def push_left(self):
            self.slider = max(0.0, self.slider - 12.0)
            
        def push_right(self):
            self.slider = min(100.0, self.slider + 12.0)


# ==========================================
# 1. Tampilan Antarmuka (UI) Minigame
# ==========================================
screen mg_keseimbangan_mental():
    modal True
    
    default game = MentalBalanceGame()
    timer 0.1 action Function(game.update) repeat True
    
    # --- BACKGROUND SAAT MINIGAME ---
    add "bg_mg02c_keseimbangan"
    
    $ bg_alpha = hex(int(min(255, (game.red_timer / game.max_red) * 200)))[2:].zfill(2)
    add "#ff0000" + bg_alpha

    key "K_LEFT" action Function(game.push_left)
    key "K_RIGHT" action Function(game.push_right)

    frame:
        xalign 0.5 yalign 0.5
        xpadding 50 ypadding 50
        background Solid("#111111e6")
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "KESEIMBANGAN MENTAL CITRA" size 32 color "#ff00ff" xalign 0.5 bold True
            text "Tahan indikator di ZONA TENGAH! Jangan biarkan energi gaib merobek pertahanannya!" size 16 color "#cccccc" xalign 0.5
            
            null height 10
            
            hbox:
                xalign 0.5
                spacing 50
                text "Waktu Bertahan: [int(game.time_left)] dtk" size 24 color "#55ffff"
                if game.red_timer > 0:
                    text "BAHAYA: [int(game.red_timer * 100 / game.max_red)]%" size 24 color "#ff3333" bold True
                else:
                    text "BAHAYA: 0%" size 24 color "#55ff55"
            
            null height 20
            
            frame:
                xalign 0.5
                xysize (600, 60)
                background Solid("#330000") 
                
                frame:
                    xpos 180 
                    ypos 0
                    xysize (240, 60) 
                    background Solid("#005500") 
                
                frame:
                    xpos int((game.slider / 100.0) * 580) 
                    ypos -10
                    xysize (20, 80)
                    background Solid("#ffffff")
            
            null height 20
            
            hbox:
                spacing 100
                xalign 0.5
                textbutton "◄◄ TARIK KIRI":
                    text_size 28
                    action Function(game.push_left)
                textbutton "TARIK KANAN ►►":
                    text_size 28
                    action Function(game.push_right)

    if game.status == "win":
        timer 0.1 action Return("win")
    elif game.status == "lose":
        timer 0.1 action Return("lose")


# ==========================================
# 2. Label Pemicu Minigame
# ==========================================
label play_mg_chap02c:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    play sound "sfx_heartbeat_fast.ogg" loop
    play music "bgm_06_panggilan_arwah.ogg" fadein 1.0
    
    show citra_marah at center with tv_rusak
    c "ARGH! SUARANYA TERLALU BISING! MEREKA MARAH! MEREKA SAKIT!"
    hide citra_marah
    
    show raka_panik at center
    r "Citra, sadar! Jangan dengerin suaranya! Fokus ke suara gue!"
    hide raka_panik
    
    "Citra berada di ambang kesurupan total. Kamu harus membantunya menjaga keseimbangan rasionalitasnya!"
    
    window hide
    call screen mg_keseimbangan_mental
    
    stop sound fadeout 1.0
    
    if _return == "win":
        # --- POIN RESONANSI DITAMBAHKAN ---
        $ citra_resonansi_gaib += 1 
        
        # --- CUT SCENE: Raka Azan ---
        scene cg_mg02c_raka_azan with flashbang
        play sound "sfx_magic_spell.ogg"
        
        "Melihat Citra semakin histeris, Raka yang kehabisan akal langsung menutup telinganya dan mengumandangkan azan dengan suara lantang."
        "Mendengar gema azan Raka, mata Citra seketika terbelalak kaget. Hawa negatif di sekitarnya mendadak memudar."
        
        # --- CUT SCENE: Citra Tertawa, Duo Melongo ---
        stop music fadeout 1.0
        play music "bgm_02_canda_trio.ogg" fadein 1.0
        scene cg_mg02c_citra_tertawa with dissolve_lambat
        
        c "Bwahahaha! Kak Raka suaranya fals banget, ya ampun!"
        
        r "Hah...? Lu... nggak kesurupan? Kok malah ketawa?!"
        b "Alhamdulillah kau sadar, Citra. Tapi... ada apa ini?"
        
        c "Hihihi, arwahnya pada kabur denger suara Kak Raka. Lagian, ternyata mereka nggak marah ke kita kok."
        c "Mereka cuma usil ngajak bercanda saking senengnya akhirnya ada yang mau nyamperin ke sini."
        
        "Raka dan Bimo hanya bisa saling pandang dan melongo tak percaya. Ketegangan horor barusan hancur lebur oleh selera humor para arwah."
        
    elif _return == "lose":
        # --- CUT SCENE: Citra Pingsan ---
        play sound "sfx_bone_crack.ogg"
        scene cg_mg02c_citra_pingsan with hpunch
        
        c "Ukh... sakit..."
        
        r "Citra! Sial, dia pingsan! Bimo, mundur dulu, kita tarik dia menjauh dari noda darah ini!"
        
        "Pertahanan mental Citra hancur dan ia jatuh pingsan karena kelelahan luar biasa."
        "Raka terpaksa menangkapnya dan menyeretnya menjauh. Kalian gagal mendapatkan koneksi lebih dalam dengan entitas di TKP ini."


    # --- INJEKSI CHECKPOINT (SYSTEM) ---
    call tawarkan_save("PLAY_MG_CHAP02C SELESAI")
    # -----------------------------------
    return