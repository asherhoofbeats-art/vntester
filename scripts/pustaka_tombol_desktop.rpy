# ==========================================
# PUSTAKA TOMBOL DESKTOP / PC (100x100 px)
# ==========================================

# 1. SCREEN D-PAD KONTROL (Pojok Kiri Bawah)
# Screen dasar ini bisa dipanggil oleh mode lain
screen dpad_kontrol():
    # Pemetaan Keyboard untuk Arah (Arrow Keys atau WASD)
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
            spacing 10 # Jarak antar tombol (proporsional untuk ukuran 100px)
            
            # Baris Atas
            null
            imagebutton idle "images/button/desktop/button_up.webp" action Return("up")
            null
            
            # Baris Tengah
            imagebutton idle "images/button/desktop/button_left.webp" action Return("left")
            null
            imagebutton idle "images/button/desktop/button_right.webp" action Return("right")
            
            # Baris Bawah
            null
            imagebutton idle "images/button/desktop/button_down.webp" action Return("down")
            null


# 2. SCREEN MODE FIGHT / MINI GAME
# Menampilkan D-Pad + Tombol B dan A (Pojok Kanan Bawah)
screen mode_fight():
    # Memanggil screen D-Pad
    use dpad_kontrol
    
    # Pemetaan Keyboard Khusus Mode Fight/Minigame
    key "j" action Return("A")
    key "i" action Return("B")
    key "k" action Return("pause") # Tombol K tersembunyi untuk Pause
    
    frame:
        background None
        xalign 0.95
        yalign 0.95
        
        hbox:
            spacing 20
            
            # Tombol B (Kiri, posisinya sedikit diturunkan)
            vbox:
                yalign 1.0
                null height 50 
                imagebutton idle "images/button/desktop/button_bye.webp" action Return("B")
            
            # Tombol A (Kanan, posisinya sedikit dinaikkan)
            vbox:
                yalign 1.0
                imagebutton idle "images/button/desktop/button_aye.webp" action Return("A")
                null height 50


# 3. SCREEN MODE EXPLORE
# Menampilkan D-Pad + Tombol Talk, Inspect, Act (Pojok Kanan Bawah)
screen mode_explore():
    # Memanggil screen D-Pad
    use dpad_kontrol
    
    # Pemetaan Keyboard Khusus Mode Explore
    key "j" action Return("act")
    key "i" action Return("inspect")
    key "l" action Return("talk")
    key "k" action Return("pause") # Tombol K tersembunyi untuk Pause
    
    frame:
        background None
        xalign 0.95
        yalign 0.95
        
        # Disusun membentuk formasi piramida terbalik/segitiga
        vbox:
            spacing 15
            xalign 1.0
            
            # Posisi Atas: Talk
            hbox:
                xalign 0.5
                imagebutton idle "images/button/desktop/button_talk.webp" action Return("talk")
            
            # Posisi Bawah Kiri & Kanan: Inspect dan Act
            hbox:
                spacing 20
                imagebutton idle "images/button/desktop/button_inspect.webp" action Return("inspect")
                imagebutton idle "images/button/desktop/button_act.webp" action Return("act")