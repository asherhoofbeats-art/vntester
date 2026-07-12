# ==========================================
# FILE: mg_chap02a.rpy
# MINIGAME: Menghalau Roh di TKP (Fokus Bimo)
# ==========================================

init python:
    import random
    
    # Fungsi untuk membuat urutan segel acak setiap kali minigame dimainkan
    def generate_segel_seq():
        symbols = ["SEGEL UTARA", "SEGEL SELATAN", "SEGEL BARAT", "SEGEL TIMUR"]
        return [random.choice(symbols) for _ in range(5)]

# 1. Tampilan Antarmuka (UI) Minigame
screen mg_halau_roh(target_seq, memory_time, input_time):
    modal True
    
    default phase = "MEMORIZE"
    default timer_val = memory_time
    default current_input = []
    default status_msg = "HAFALKAN URUTAN SEGEL INI!"
    
    # Latar belakang gelap transparan
    add "bg_mg02a_segel_bimo"
    add "#000000aa" # Tambahkan lapisan gelap sedikit agar teks minigame tetap terbaca
    
    # Logika Timer (Berjalan setiap 1 detik)
    timer 1.0 action [
        If(timer_val > 0,
            SetScreenVariable("timer_val", timer_val - 1),
            # Jika waktu habis
            If(phase == "MEMORIZE",
                # Ganti ke fase input
                [SetScreenVariable("phase", "INPUT"), SetScreenVariable("timer_val", input_time), SetScreenVariable("status_msg", "MASUKKAN URUTAN SEGEL DENGAN CEPAT!")],
                # Jika fase input habis waktu
                Return("timeout")
            )
        )
    ] repeat True
    
    # Frame utama
    frame:
        xalign 0.5 yalign 0.5
        xpadding 50 ypadding 50
        background Solid("#1a0000") # Warna merah gelap mencerminkan hawa panas roh
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "MANTRA PENOLAK BALA" size 32 color "#ff5555" xalign 0.5 bold True
            text status_msg size 20 color "#ffffff" xalign 0.5
            
            # Indikator Waktu
            if phase == "MEMORIZE":
                text "Waktu Menghafal: [timer_val] detik" size 24 color "#55ffff" xalign 0.5
            else:
                text "Sisa Waktu: [timer_val] detik" size 24 color "#ffaa00" xalign 0.5
            
            null height 20
            
            # Area Display Urutan
            hbox:
                spacing 15
                xalign 0.5
                if phase == "MEMORIZE":
                    # Tampilkan urutan yang harus dihafal
                    for s in target_seq:
                        frame:
                            background Solid("#330000")
                            padding (10, 10)
                            text s size 20 color "#ffcccc"
                else:
                    # Tampilkan tombol yang sudah ditekan pemain
                    for s in current_input:
                        frame:
                            background Solid("#003300")
                            padding (10, 10)
                            text s size 20 color "#55ff55"
                    # Sisa slot yang belum ditekan
                    for i in range(len(target_seq) - len(current_input)):
                        frame:
                            background Solid("#222222")
                            padding (10, 10)
                            text "???" size 20 color "#777777"
            
            null height 30
            
            # Area Tombol Input (Hanya muncul saat fase INPUT)
            if phase == "INPUT":
                grid 2 2:
                    xalign 0.5
                    spacing 20
                    for sym in ["SEGEL UTARA", "SEGEL SELATAN", "SEGEL BARAT", "SEGEL TIMUR"]:
                        textbutton sym:
                            text_size 24
                            action [
                                Play("sound", "sfx_mencet_tombol.ogg"),
                                SetScreenVariable("current_input", current_input + [sym]),
                                
                                # Cek kebenaran urutan
                                If(current_input + [sym] == target_seq[:len(current_input)+1],
                                    # JIKA BENAR: Cek apakah ini tombol terakhir
                                    If(len(current_input) + 1 == len(target_seq),
                                        Return("win")
                                    ),
                                    # JIKA SALAH: Kembalikan status kalah ke label
                                    Return("wrong")
                                )
                            ]

# ==========================================
# 2. Label Pemicu Minigame
# ==========================================
# ==========================================
# 2. Label Pemicu Minigame
# ==========================================
label play_mg_chap02a:
    # --- INJEKSI AUTO-LOCK (SYSTEM) ---
    $ renpy.block_rollback()
    $ _rollback = False
    $ _save = False
    # ----------------------------------
    
    # --- CUT SCENE: Arwah Menyerang ---
    scene cg_mg02a_setan_datang with dissolve_kilat
    play sound "sfx_gema_suara_hantu.ogg"
    b "Mereka menyerang! Bersiaplah!"
    
    # Buat urutan baru saat minigame dimulai
    $ current_target_seq = generate_segel_seq()
    $ mg_input_time = 15 # Waktu awal 15 detik
    
    label .retry_loop:
        # Panggil screen dengan membawa variabel urutan dan waktu
        window hide
        call screen mg_halau_roh(current_target_seq, 4, mg_input_time)
        
        # Evaluasi Hasil Minigame
        if _return == "win":
            # --- CUT SCENE: Bimo Berhasil ---
            play sound "sfx_magic_spell.ogg"
            scene cg_mg02a_bimo_berhasil with flashbang
            pause 2.0
            
            # Kembali ke BG biasa
            scene bg_tkp_mayat with dissolve
            show bimo_normal at center with dissolve_kilat
            "Bimo menyelesaikan mantranya dengan sempurna. Hawa panas di ruangan perlahan menghilang dan TKP kembali netral."
            hide bimo_normal
            return
            
        elif _return == "wrong" or _return == "timeout":
            # --- CUT SCENE: Bimo Terpental (Kalah/Timeout) ---
            play sound "sfx_benda_dipukul.ogg"
            scene cg_mg02a_bimo_terpental with hpunch
            pause 1.5
            
            scene bg_tkp_mayat with dissolve
            
            if _return == "timeout":
                show bimo_panik at center with dissolve_kilat
                b "Terlambat! Hawa negatifnya kembali menyebar!"
                hide bimo_panik
            else:
                show bimo_lelah at center with dissolve_kilat
                b "Ukh! Konsentrasiku pecah! Arwah-arwah ini mencoba melawan!"
                hide bimo_lelah
            
            # Penalti waktu
            $ mg_input_time -= 3 
            
            if mg_input_time <= 0:
                show bimo_panik at center with dissolve_kilat
                b "Energinya terlalu besar! Aku harus memaksakan segel ini!"
                hide bimo_panik
                
                play sound "sfx_magic_spell.ogg"
                scene cg_mg02a_bimo_berhasil with flashbang
                pause 1.5
                
                scene bg_tkp_mayat with dissolve
                show bimo_lelah at center with dissolve_kilat
                "Dengan sisa tenaga, Bimo memaksakan mantranya. TKP berhasil dibersihkan, meski Bimo kini sangat kelelahan."
                hide bimo_lelah
                return
            else:
                "Sial! Kamu kehilangan fokus. Waktu inputmu kini berkurang menjadi [mg_input_time] detik. Hafalkan ulang!"
                jump .retry_loop