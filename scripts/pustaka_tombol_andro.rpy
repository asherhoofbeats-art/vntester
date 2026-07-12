# ==========================================
# PUSTAKA TOMBOL ANDROID (160x160 px)
# Lokasi: D:\RENPY\RPY-PROJECT\PantiBerdarah\game\images\button
# ==========================================

# 1. SCREEN D-PAD KONTROL (Modular)
screen dpad_kontrol():
    # Pemetaan Keyboard untuk Navigasi (Arrow Keys atau WASD)
    key "K_UP" action Return("up")
    key "w" action Return("up")
    
    key "K_DOWN" action Return("down")
    key "s" action Return("down")
    
    key "K_LEFT" action Return("left")
    key "a" action Return("left")
    
    key "K_RIGHT" action Return("right")
    key "d" action Return("right")

    frame:
        background None
        xalign 0.05
        yalign 0.95
        
        # Grid 3x3 untuk D-Pad
        grid 3 3:
            spacing 10
            
            # Baris Atas
            null
            imagebutton idle "images/button/button_up.webp" action Return("up")
            null
            
            # Baris Tengah
            imagebutton idle "images/button/button_left.webp" action Return("left")
            null
            imagebutton idle "images/button/button_right.webp" action Return("right")
            
            # Baris Bawah
            null
            imagebutton idle "images/button/button_down.webp" action Return("down")
            null


# 2. SCREEN MODE FIGHT / MINI GAME
screen mode_fight():
    # Memanggil D-Pad
    use dpad_kontrol
    
    # Pemetaan Keyboard untuk A, B, dan Pause
    key "j" action Return("A")
    key "i" action Return("B")
    key "k" action Return("pause") # Tombol tersembunyi untuk Pause
    
    frame:
        background None
        xalign 0.95
        yalign 0.90
        
        hbox:
            spacing 40
            
            # Tombol B (Kiri, lebih rendah)
            vbox:
                yalign 1.0
                null height 80 
                imagebutton idle "images/button/button_bye.webp" action Return("B")
            
            # Tombol A (Kanan, lebih tinggi)
            vbox:
                yalign 1.0
                imagebutton idle "images/button/button_aye.webp" action Return("A")
                null height 80


# 3. SCREEN MODE EXPLORE
screen mode_explore():
    # Memanggil D-Pad
    use dpad_kontrol
    
    # Pemetaan Keyboard untuk Act, Inspect, Talk, dan Pause
    key "j" action Return("act")
    key "i" action Return("inspect")
    key "l" action Return("talk")
    key "k" action Return("pause") # Tombol tersembunyi untuk Pause
    
    frame:
        background None
        xalign 0.95
        yalign 0.95
        
        vbox:
            spacing 20
            xalign 1.0
            
            # Posisi Atas: Talk
            hbox:
                xalign 0.5
                imagebutton idle "images/button/button_talk.webp" action Return("talk")
            
            # Posisi Bawah Kiri & Kanan: Inspect dan Act
            hbox:
                spacing 30
                imagebutton idle "images/button/button_inspect.webp" action Return("inspect")
                imagebutton idle "images/button/button_act.webp" action Return("act")