# ==========================================
# FILE: anim_renggo.rpy
# KUMPULAN ANIMASI & TRANSFORMASI FINAL BOSS (KI RENGGO / GENDERUWO)
# ==========================================

# ------------------------------------------
# 1. EFEK TRANSFORMASI DASAR (GERAKAN)
# ------------------------------------------

# Efek Napas Berat untuk Boss Raksasa
transform napas_boss:
    yoffset 0
    easein 1.2 yoffset 5
    easeout 1.2 yoffset 0
    repeat

# Efek bergetar saat terkena ledakan (Damage/Hit)
transform boss_kena_hit:
    ease 0.05 xoffset -15
    ease 0.05 xoffset 15
    ease 0.05 xoffset -15
    ease 0.05 xoffset 15
    ease 0.05 xoffset 0

# ------------------------------------------
# 2. WUJUD AWAL & POSISI IDLE
# ------------------------------------------

# Transisi Ki Renggo komat-kamit memanggil roh
image renggo_transforming:
    align (0.5, 1.0)
    "images/sprites/renggo_genderuwo.webp"

# Posisi siaga/idle (tangan mengepal)
image genderuwo_idle:
    align (0.5, 1.0)
    "images/sprites/edited_sp_genderuwo_warcry.webp"

# ------------------------------------------
# 3. ANIMASI WARCRY (MENGAUM)
# ------------------------------------------
image genderuwo_warcry_anim:
    align (0.5, 1.0)
    "images/sprites/edited_sp_genderuwo_warcry.webp"
    0.15
    "images/sprites/edited_sp_genderuwo_warcry_1.webp"
    0.15
    "images/sprites/sp_genderuwo_warcry.webp"
    1.2 # Puncak auman
    "images/sprites/edited_sp_genderuwo_warcry_1.webp"
    0.15
    "genderuwo_idle"

# ------------------------------------------
# 4. ANIMASI SERANGAN (HANTAMAN TELAPAK)
# ------------------------------------------
image genderuwo_attack_anim:
    align (0.5, 1.0)
    # Ancang-ancang (Wind-up)
    "images/sprites/edited_sp_genderuwo_attack_1.webp"
    0.4 
    # Hantaman terbuka (Berhenti di sini untuk mekanik tahan)
    "images/sprites/edited_sp_genderuwo_attack.webp"

# ------------------------------------------
# 5. MEKANIK CITRA (TERLILIT & LEPAS IKATAN)
# ------------------------------------------

# Terlilit dengan efek meronta-ronta (Getar)
image genderuwo_terlilit_loop:
    align (0.5, 1.0)
    "images/sprites/edited_sp_genderuwo_terlilit.webp"
    ease 0.05 xoffset 3
    ease 0.05 xoffset -3
    ease 0.05 xoffset 2
    ease 0.05 xoffset -2
    ease 0.05 xoffset 0
    pause 0.2
    repeat

# Telat menyerang: Hantu terpental, Boss lepas dan mengaum
image genderuwo_lepas_ikatan:
    align (0.5, 1.0)
    "images/sprites/edited_sp_genderuwo_terlilit_1.webp"
    0.3
    "genderuwo_warcry_anim"

# ------------------------------------------
# 6. ANIMASI SERANGAN MASUK (SUKSES)
# ------------------------------------------
image genderuwo_terkena_ledakan:
    align (0.5, 1.0)
    "images/sprites/edited_sp_genderuwo_terlilit.webp"
    0.1
    # Ledakan mengenai Boss yang sedang terlilit
    "images/sprites/edited_sp_genderuwo_terkena_ledakan_lilit.webp"
    0.3
    # Jatuh berlutut kesakitan (Stun sementara)
    "images/sprites/edited_sp_genderuwo_terkena_ledakan_lilit_1.webp"
    1.5 
    # Bangkit dan membuang sisa api
    "images/sprites/edited_sp_genderuwo_warcry_1.webp"
    1.0
    "genderuwo_idle"

# ------------------------------------------
# 7. ANIMASI KEKALAHAN BOSS (GAME OVER BOSS)
# ------------------------------------------
image genderuwo_kalah_anim:
    align (0.5, 1.0)
    "images/sprites/edited_sp_genderuwo_terlilit.webp"
    0.2
    
    # Rentetan Ledakan Pembuka
    "images/sprites/edited_sp_genderuwo_terkena_ledakan_lilit_2.webp"
    0.3
    
    # Rentetan Ledakan Dada & Bahu
    "images/sprites/edited_sp_genderuwo_terkena_ledakan.webp"
    0.2
    "images/sprites/edited_sp_genderuwo_terkena_ledakan_1.webp"
    0.2
    
    # Ledakan Final di Lutut (Stun parah)
    "images/sprites/edited_sp_genderuwo_terkena_ledakan_2.webp"
    0.8
    
    # Menyusut kembali ke wujud asli yang berlutut kalah
    "images/sprites/edited_sp_genderuwo_renggo_jatuh_1.webp"
    2.0 
    
    # Tersungkur di lantai (Gambar diam sebagai background penutup)
    "images/sprites/edited_sp_genderuwo_renggo_jatuh_2.webp"