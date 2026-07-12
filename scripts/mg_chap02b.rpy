# ==========================================
# FILE: mg_chap02b.rpy
# MINIGAME: Mengantar Mbok Darmi (Fokus Citra)
# MEKANIK: Stealth Maze 2D Turn-Based
# ==========================================

init python:
    import random

    class StealthMazeGame:
        def __init__(self):
            # Ukuran grid 6x6 (0-5)
            self.grid_size = 6
            # Titik awal Citra & Mbok Darmi
            self.player = [0, 0]
            # Titik Pintu Keluar
            self.exit = [5, 5]
            # Koordinat tembok/rintangan
            self.walls = [[1,0], [1,1], [1,2], [3,3], [3,4], [3,5], [4,1], [5,1]]
            # Koordinat awal roh
            self.ghosts = [[0, 5], [5, 0], [2, 3]]
            
            self.panic = 0
            self.max_panic = 3
            self.status = "playing"

        def move_player(self, dx, dy):
            if self.status != "playing":
                return
                
            nx, ny = self.player[0] + dx, self.player[1] + dy
            # Pastikan tidak keluar batas dan tidak menabrak tembok
            if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                if [nx, ny] not in self.walls:
                    self.player = [nx, ny]
                    self.check_collision()
                    
                    if self.status == "playing":
                        self.move_ghosts()
                        self.check_collision()
                        
                    # Cek kemenangan
                    if self.player == self.exit and self.status == "playing":
                        self.status = "win"

        def move_ghosts(self):
            for g in self.ghosts:
                moves = [[0,1], [0,-1], [1,0], [-1,0]]
                random.shuffle(moves)
                for dx, dy in moves:
                    nx, ny = g[0] + dx, g[1] + dy
                    if 0 <= nx < self.grid_size and 0 <= ny < self.grid_size:
                        if [nx, ny] not in self.walls and [nx, ny] != self.exit:
                            g[0], g[1] = nx, ny
                            break

        def check_collision(self):
            if self.player in self.ghosts:
                self.panic += 1
                renpy.play("sfx_gema_suara_hantu.ogg")
                if self.panic >= self.max_panic:
                    self.status = "lose"
                else:
                    self.player = [0, 0]
                    self.ghosts = [[0, 5], [5, 0], [2, 3]]


# ==========================================
# 1. Tampilan Antarmuka (UI) Minigame
# ==========================================
screen mg_stealth_maze(maze):
    modal True
    
    # --- MENGGUNAKAN BACKGROUND BARU ---
    add "bg_mg02b_maze_dapur"
    add "#000000dd" # Lapisan gelap agar UI minigame terbaca jelas

    # Pintasan Keyboard PC (Panah / Arrow Keys)
    key "K_UP" action Function(maze.move_player, 0, -1)
    key "K_DOWN" action Function(maze.move_player, 0, 1)
    key "K_LEFT" action Function(maze.move_player, -1, 0)
    key "K_RIGHT" action Function(maze.move_player, 1, 0)

    # Pintasan Keyboard PC Ekstra (W, A, S, D untuk Gamer)
    key "w" action Function(maze.move_player, 0, -1)
    key "W" action Function(maze.move_player, 0, -1)
    key "s" action Function(maze.move_player, 0, 1)
    key "S" action Function(maze.move_player, 0, 1)
    key "a" action Function(maze.move_player, -1, 0)
    key "A" action Function(maze.move_player, -1, 0)
    key "d" action Function(maze.move_player, 1, 0)
    key "D" action Function(maze.move_player, 1, 0)

    frame:
        xalign 0.5 yalign 0.5
        xpadding 40 ypadding 40
        background Solid("#111111ee")
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "EVAKUASI MBOK DARMI" size 32 color "#00ffcc" xalign 0.5 bold True
            text "Gunakan Panah Navigasi untuk bergerak ke Pintu Keluar.\nJangan sampai menyentuh Roh Hitam!" size 16 color "#cccccc" text_align 0.5 xalign 0.5
            
            # Panic Meter Bar
            hbox:
                spacing 10
                xalign 0.5
                text "PANIC METER:" size 20 color "#ff5555" yalign 0.5
                bar value maze.panic range maze.max_panic xsize 300 ysize 25 left_bar "#ff0000" right_bar "#550000" yalign 0.5
            
            null height 10
            
            # Menggambar Grid 6x6
            grid maze.grid_size maze.grid_size:
                xalign 0.5
                spacing 5
                
                for y in range(maze.grid_size):
                    for x in range(maze.grid_size):
                        frame:
                            xysize (60, 60)
                            
                            if [x, y] == maze.player:
                                background Solid("#00aaff") 
                                text "🚶‍♀️" xalign 0.5 yalign 0.5 size 30
                            elif [x, y] in maze.ghosts:
                                background Solid("#550000") 
                                text "👻" xalign 0.5 yalign 0.5 size 30
                            elif [x, y] == maze.exit:
                                background Solid("#00ff00") 
                                text "EXIT" xalign 0.5 yalign 0.5 size 16 color "#000000" bold True
                            elif [x, y] in maze.walls:
                                background Solid("#444444") 
                            else:
                                background Solid("#222222") 

            null height 20
            
            # Menggunakan grid 3x2 untuk D-Pad Virtual Smartphone
            grid 3 2:
                xalign 0.5
                spacing 15
                
                null
                # TOMBOL ATAS
                textbutton "⬆️":
                    xysize (120, 120) 
                    text_xalign 0.5 
                    text_yalign 0.5 
                    text_size 80
                    action Function(maze.move_player, 0, -1)
                null
                
                # TOMBOL KIRI
                textbutton "⬅️":
                    xysize (120, 120) 
                    text_xalign 0.5 
                    text_yalign 0.5 
                    text_size 80
                    action Function(maze.move_player, -1, 0)
                    
                # TOMBOL BAWAH
                textbutton "⬇️":
                    xysize (120, 120) 
                    text_xalign 0.5 
                    text_yalign 0.5 
                    text_size 80
                    action Function(maze.move_player, 0, 1)
                    
                # TOMBOL KANAN
                textbutton "➡️":
                    xysize (120, 120) 
                    text_xalign 0.5 
                    text_yalign 0.5 
                    text_size 80
                    action Function(maze.move_player, 1, 0)

    # Deteksi Menang/Kalah
    if maze.status == "win":
        timer 0.5 action Return("win")
    elif maze.status == "lose":
        timer 0.5 action Return("lose")


# ==========================================
# 2. Label Pemicu Minigame
# ==========================================
label play_mg_chap02b:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    $ current_maze = StealthMazeGame()
    
    label .retry_maze:
        window hide
        call screen mg_stealth_maze(current_maze)
        
        if _return == "win":
            # --- PENAMBAHAN POIN STAT ---
            $ citra_resonansi_gaib += 1
            $ darmi_trust = True
            
            # --- CUT SCENE 2: Terima Kasih ---
            play sound "sfx_creaky_door_open.ogg"
            scene cg_mg02b_darmi_terimakasih with dissolve_lambat
            
            c "Fiuh... Kita berhasil keluar, Mbok. Mbok Darmi aman sekarang."
            md "Matur nuwun sanget, Neng... Kulo wangsul riyin nggih (Terima kasih banyak Neng, saya pulang dulu ya)."
            
            "Citra melihat Mbok Darmi berlari menjauh dari area dapur."
            
            # --- CUT SCENE 3: Citra Kembali ---
            scene cg_mg02b_citra_kembali with transisi_asap
            play sound "sfx_footsteps_approach.ogg"
            "Citra memantapkan keberaniannya, ia segera kembali ke dalam kegelapan untuk menyusul Raka dan Bimo."
            return "win"
            
        elif _return == "lose":
            # --- CUT SCENE 4: Darmi Kabur ---
            play sound "sfx_teriakan_takut.ogg"
            scene cg_mg02b_darmi_kabur with hpunch
            
            c "Kak Raka! Kak Bimo! Bayangannya mendekat!"
            md "TULUNG!!! BUTO IJO!!"
            
            "Kepanikan Mbok Darmi memuncak. Roh jahat itu nyaris menangkap mereka."
            "Citra harus memandu Mbok Darmi mencari jalan lain dan mengulang dari titik awal."
            
            $ current_maze = StealthMazeGame()
            jump .retry_maze