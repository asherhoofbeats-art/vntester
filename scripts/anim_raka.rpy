# ==========================================
# FILE: anim_raka.rpy
# KUMPULAN ANIMASI & TRANSFORMASI RAKA (FINAL BOSS)
# ==========================================

# ------------------------------------------
# 1. EFEK TRANSFORMASI (PERGERAKAN)
# ------------------------------------------

# Efek napas (naik turun halus saat idle)
transform napas_tempur:
    yoffset 0
    easein 0.8 yoffset 3
    easeout 0.8 yoffset 0
    repeat

# Efek pindah jalur (meluncur mulus ke kiri/kanan)
transform raka_dash_move(target_x):
    # Anchor x=0.5 (tengah), y=1.0 (bawah) agar telapak kaki selalu rata!
    xanchor 0.5 yanchor 1.0 
    ease 0.15 xalign target_x


# ------------------------------------------
# 2. ANIMASI IDLE (BERSIAP MENGHADAP BOS)
# ------------------------------------------
image raka_back_idle:
    # Mengunci titik jangkar di telapak kaki
    align (0.5, 1.0)
    
    "images/sprites/sp_raka_back_ready.webp"
    0.4
    "images/sprites/sp_raka_back_ready_1.webp"
    0.4
    "images/sprites/sp_raka_back_ready_2.webp"
    0.4
    "images/sprites/sp_raka_back_ready_1.webp"
    0.4
    repeat


# ------------------------------------------
# 3. ANIMASI DASH (MENGHINDAR KE KANAN)
# ------------------------------------------
image raka_dash_kanan:
    align (0.5, 1.0)
    
    "images/sprites/sp_raka_dash_1.webp"
    0.05
    "images/sprites/sp_raka_run.webp"
    0.05
    "images/sprites/sp_raka_jump03.webp"
    0.15
    "images/sprites/sp_raka_dash_2.webp"
    0.15
    
    # Setelah mendarat, otomatis kembali ke posisi stand by
    "raka_back_idle"


# ------------------------------------------
# 4. ANIMASI DASH (MENGHINDAR KE KIRI)
# ------------------------------------------
image raka_dash_kiri:
    align (0.5, 1.0)
    
    "images/sprites/sp_raka_dash_left.webp"
    0.05
    "images/sprites/sp_raka_dash_2left.webp"
    0.10
    "images/sprites/sp_raka_dash_3left.webp"
    0.10
    "images/sprites/sp_raka_jump_landing_left.webp"
    0.15
    
    # Setelah mendarat, otomatis kembali ke posisi stand by
    "raka_back_idle"