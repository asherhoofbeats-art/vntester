# ==========================================
# PUSTAKA KAMERA (CAMLIB)
# Simpan sebagai: pustaka_kamera.rpy
# ==========================================

# --- WAJIB ---
transform cam_reset:
    ease 0.5 zoom 1.0 xalign 0.5 yalign 0.5 rotate 0 xoffset 0 yoffset 0

# --- ZOOM & FOKUS ---
transform cam_zoom_in:
    ease 1.5 zoom 1.3 xalign 0.5 yalign 0.5

transform cam_zoom_out:
    ease 1.5 zoom 1.0 xalign 0.5 yalign 0.5

transform cam_zoom_kaget:
    easein 0.15 zoom 1.6 yalign 0.3 xalign 0.5

# --- PANNING & TILTING ---
transform cam_pan_kanan:
    zoom 1.2 xalign 0.0 yalign 0.5
    ease 3.0 xalign 1.0

transform cam_pan_kiri:
    zoom 1.2 xalign 1.0 yalign 0.5
    ease 3.0 xalign 0.0

transform cam_tilt_up:
    zoom 1.2 xalign 0.5 yalign 1.0
    ease 3.0 yalign 0.0

transform cam_tilt_down:
    zoom 1.2 xalign 0.5 yalign 0.0
    ease 3.0 yalign 1.0

# --- DRAMATIS & EFEK KHUSUS ---
transform cam_miring_kanan:
    ease 1.0 zoom 1.2 rotate 10 xalign 0.5 yalign 0.5

transform cam_miring_kiri:
    ease 1.0 zoom 1.2 rotate -10 xalign 0.5 yalign 0.5

transform cam_mabuk:
    zoom 1.1 xalign 0.5 yalign 0.5
    ease 1.5 rotate 3 xoffset 15
    ease 1.5 rotate -3 xoffset -15
    repeat

transform cam_gempa:
    zoom 1.05 xalign 0.5 yalign 0.5
    linear 0.05 xoffset 15 yoffset 15
    linear 0.05 xoffset -15 yoffset -15
    linear 0.05 xoffset 0 yoffset 0
    repeat

# --- POV (SUDUT PANDANG PEMAIN) ---
transform cam_pov_angguk:
    zoom 1.1 xalign 0.5
    easein 0.2 yalign 0.8
    easeout 0.2 yalign 0.5
    easein 0.2 yalign 0.8
    easeout 0.2 yalign 0.5

transform cam_pov_geleng:
    zoom 1.1 yalign 0.5
    easein 0.15 xalign 0.2
    easeout 0.15 xalign 0.8
    easein 0.15 xalign 0.2
    easeout 0.15 xalign 0.5

transform cam_pov_pingsan:
    easein 0.4 yalign 1.0 rotate 90 zoom 1.2

transform cam_tengok_panik:
    zoom 1.1 yalign 0.5
    ease 0.2 xalign 0.0
    pause 0.2
    ease 0.2 xalign 1.0
    pause 0.2
    ease 0.2 xalign 0.5

# --- EFEK LANJUTAN ---
transform cam_jantung_berdebar:
    zoom 1.05 xalign 0.5 yalign 0.5
    easein 0.1 zoom 1.08
    easeout 0.1 zoom 1.05
    pause 0.8
    repeat

transform cam_vertigo:
    xalign 0.5 yalign 0.5
    ease 4.0 zoom 1.3 rotate 5
    ease 4.0 zoom 1.05 rotate -5
    repeat

transform cam_hero_shot:
    zoom 1.25 xalign 0.5 yalign 1.0
    ease 4.0 yalign 0.8

transform cam_terpukul_mundur:
    zoom 1.3 xalign 0.5 yalign 0.5
    easeout 0.3 zoom 1.0 yalign 0.4 rotate -5
    easein 0.5 rotate 0 yalign 0.5