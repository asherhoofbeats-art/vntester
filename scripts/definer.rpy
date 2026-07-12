# ==========================================
# DEFINISI KARAKTER & WARNA NAMA
# ==========================================

# Trio Investigator
define r = Character("Raka", color="#d32f2f")   # Merah (Kuat, Emosian)
define b = Character("Bimo", color="#1976d2")   # Biru (Tenang, Spiritual)
define c = Character("Citra", color="#9c27b0")  # Ungu (Indigo, Misterius)

# Tokoh Pendukung (Termasuk Sarah di awal cerita)
define s = Character("Sarah", color="#ff9800")  # Oranye (Ceria, Tomboy)
define t = Character("Pak Tirto", color="#388e3c") # Hijau Gelap (Pejabat Korup)
define kr = Character("Ki Renggo", color="#795548") # Cokelat (Dukun)
define g = Character("Gatot", color="#607d8b")  # Abu-abu (Preman)

# Tokoh NPC
define md = Character("Mbok Darmi", color="#8d6e63")
define j = Character("Joko", color="#5c6bc0")
define dr = Character("dr. Rina", color="#00bcd4")

# ==========================================
# DEFINISI BACKGROUND (Total 14 BG)
# ==========================================

image bg_balai_desa = "images/bg/bg_balai_desa.webp"
image bg_dalam_dapur = "images/bg/bg_dalam_dapur.webp"
image bg_gudang_beras = "images/bg/bg_gudang_beras.webp"
image bg_jalan_desa = "images/bg/bg_jalan_desa.webp"
image bg_luar_dapur = "images/bg/bg_luar_dapur.webp"
image bg_mobil_trio = "images/bg/bg_mobil_trio.webp"
image bg_padepokan_dalam = "images/bg/bg_padepokan_dalam.webp"
image bg_padepokan_luar = "images/bg/bg_padepokan_luar.webp"
image bg_pos_satpam = "images/bg/bg_pos_satpam.webp"
image bg_puskesmas_depan = "images/bg/bg_puskesmas_depan.webp"
image bg_ruang_autopsi = "images/bg/bg_ruang_autopsi.webp"
image bg_ruang_tirto = "images/bg/bg_ruang_tirto.webp"
image bg_sel_tahanan = "images/bg/bg_sel_tahanan.webp"
image bg_tkp_mayat = "images/bg/bg_tkp_mayat.webp"
image bg_jalanan_malam = "images/bg/bg_jalanan_malam.webp"
image it_kertas_segel_hantu = "images/item/it_kertas_segel_hantu_1.webp"
image it_obor_terlempar = "images/item/it_obor_terlempar_1.webp"
image it_projectile_fireball_katon = "images/item/it_projectile_fireball_katon.webp"
# ==========================================
# DEFINISI SPRITE POSE KARAKTER
# ==========================================

# -----------------------------------
# TRIO INVESTIGATOR (Max 6 Pose)
# -----------------------------------
# Raka (Skeptis, Tukang Pukul)
image raka_normal = "images/chars/raka_normal.webp"
image raka_marah = "images/chars/raka_marah.webp"
image raka_berpikir = "images/chars/raka_berpikir.webp"
image raka_lega = "images/chars/raka_lega.webp"
image raka_lelah = "images/chars/raka_lelah.webp"
image raka_panik = "images/chars/raka_panik.webp"
image it_rekaman_renggo = "images/item/it_rekaman_renggo"
image it_catatan_dukun = "images/item/it_catatan_renggo"
image it_projectile_banana_peel = "images/item/it_projectile_banana_peel.webp"
image it_projectile_empty_can = "images/item/it_projectile_empty_can.webp"
image it_projectile_rubber_chicken = "images/item/it_projectile_rubber_chicken.webp"

# Bimo (Spiritual, Bijak)
image bimo_normal = "images/chars/bimo_normal.webp"
image bimo_marah = "images/chars/bimo_marah.webp"
image bimo_berpikir = "images/chars/bimo_berpikir.webp"
image bimo_lega = "images/chars/bimo_lega.webp"
image bimo_lelah = "images/chars/bimo_lelah.webp"
image bimo_panik = "images/chars/bimo_panik.webp"
image bimo_fokus = "images/chars/bimo_siap_tarung.webp"
image button_act = "images/button/desktop/button_act.webp"
image button_aye = "images/button/desktop/button_aye.webp"
image button_bye = "images/button/desktop/button_bye.webp"
image button_down = "images/button/desktop/button_down.webp"
image button_inspect = "images/button/desktop/button_inspect.webp"
image button_left = "images/button/desktop/button_left.webp"
image button_right = "images/button/desktop/button_right.webp"
image button_talk = "images/button/desktop/button_talk.webp"
image button_up = "images/button/desktop/button_up.webp"

# Citra (Indigo, Penakut / Kesurupan)
image citra_normal = "images/chars/citra_normal.webp"
image citra_marah = "images/chars/citra_marah.webp"      # Pose saat kesurupan/mengamuk
image citra_berpikir = "images/chars/citra_berpikir.webp"
image citra_lega = "images/chars/citra_lega.webp"
image citra_lelah = "images/chars/citra_lelah.webp"     # Pose pasca-kesurupan
image citra_panik = "images/chars/citra_panik.webp"     # Pose takut hantu

# -----------------------------------
# TOKOH PENDUKUNG (Max 3 Pose)
# -----------------------------------
# Sarah (Cameo Chat/Video Call dari Luar Negeri)
image sarah_normal = "images/chars/sarah_normal.webp"
image sarah_marah = "images/chars/sarah_marah.webp"     # Ngomel-ngomel
image sarah_lega = "images/chars/sarah_lega.webp"       # Senyum/Kocak

# Pak Tirto (Villain - Pejabat Korup)
image tirto_normal = "images/chars/tirto_normal.webp"   # Senyum licik
image tirto_marah = "images/chars/tirto_marah.webp"
image tirto_panik = "images/chars/tirto_panik.webp"     # Saat hantu betulan muncul

# Ki Renggo (Anti-Villain - Dukun Bayaran)
image renggo_normal = "images/chars/renggo_normal.webp"
image renggo_marah = "images/chars/renggo_marah.webp"   # Merapal mantra tempur
image renggo_panik = "images/chars/renggo_panik.webp"   # Ketahuan nipu

# Gatot (Anti-Hero - Preman Balas Dendam)
image gatot_normal = "images/chars/gatot_normal.webp"   # Pegang senjata
image gatot_marah = "images/chars/gatot_marah.webp"     # Menyerang
image gatot_lelah = "images/chars/gatot_lelah.webp"     # Kalah duel sama Raka

# -----------------------------------
# TOKOH NPC (Max 2 Pose)
# -----------------------------------
# Mbok Darmi (Koki Takhayul)
image darmi_normal = "images/chars/darmi_normal.webp"
image darmi_panik = "images/chars/darmi_panik.webp"     # Ketakutan liat lendir

# Joko (Satpam Dapur)
image joko_normal = "images/chars/joko_normal.webp"
image joko_panik = "images/chars/joko_panik.webp"       # Saat disekap Gatot

# dr. Rina (Dokter Tertekan)
image rina_normal = "images/chars/rina_normal.webp"
image rina_lelah = "images/chars/rina_lelah.webp"       # Stres diancam Pemda
image rina_panik = "images/chars/rina_panik.webp" 
# ==========================================
# DEFINISI TOKOH TAMBAHAN
# ==========================================

# Polisi & Warga
define ar = Character("Bripka Arya", color="#3f51b5") # Biru Tua (Polisi jujur tapi lelah)
define km = Character("Kang Maman", color="#ff5722")  # Oranye Terang (Provokator massa/warga)

# Entitas Gaib
define sp = Character("Sang Penjaga", color="#b71c1c") # Merah Darah (Entitas raksasa pelindung tanah)
define at = Character("Arwah Tumbal", color="#009688") # Hijau Pucat (Gabungan arwah staf dapur yang marah)

# Karakter Ekstra (Bisa untuk cameo/subplot)
define ck = Character("Cika", color="#e91e63")        # Pink (Tiktoker/Jurnalis lokal penebar rumor)
define py = Character("Pak Yanto", color="#827717")    # Hijau Lumut (Supplier bahan makanan busuk)

# -----------------------------------
# TOKOH TAMBAHAN (Pose Normal)
# -----------------------------------
image arya_normal = "images/chars/arya_normal.webp"
image maman_normal = "images/chars/maman_normal.webp"
image arwah_normal = "images/chars/arwah_normal.webp"
image cika_normal = "images/chars/cika_normal.webp"
image yanto_normal = "images/chars/yanto_normal.webp"
image maman_panik = "images/chars/maman_panik.webp"
image arya_normal = "images/chars/arya_normal.webp"
image maman_normal = "images/chars/maman_normal.webp"
image arwah_normal = "images/chars/arwah_normal.webp"
image buto_normal = "images/chars/buto_normal.webp"
image cika_normal = "images/chars/cika_normal.webp"
image yanto_normal = "images/chars/yanto_normal.webp"
image raka_aura_hitam = "images/chars/raka_aura_hitam.webp"
image raka_siap_tarung = "images/chars/raka_siap_tarung.webp"
image bimo_siap_tarung = "images/chars/bimo_siap_tarung.webp"
image citra_siap_tarung = "images/chars/citra_siap_tarung.webp"
image citra_tertawa = "images/chars/citra_tertawa.webp"
image citra_kesurupan = "images/chars/citra_kesurupan.webp"
image renggo_mantra = "images/chars/renggo_mantra.webp"

# ==========================================
# DEFINISI CG & ITEM (Tambahkan ke definer.rpy)
# ==========================================
image cg_ch01_canda_di_mobil = "images/cg/cg_ch01_canda_di_mobil.webp"
image cg_mg01a_alat_komunikasi = "images/cg/cg_mg01a_alat_komunikasi.webp"
image cg_mg01a_sarah_vcall = "images/cg/cg_mg01a_sarah_vcall.webp"
image cg_ch01_pagar_gaib = "images/cg/cg_ch01_pagar_gaib.webp"
image cg_ch01_raka_skeptis = "images/cg/cg_ch01_raka_skeptis.webp"
image cg_mg01b_jejak_gembok = "images/cg/cg_mg01b_jejak_gembok.webp"
image cg_mg01b_dobrak_masuk = "images/cg/cg_mg01b_dobrak_masuk.webp"
image cg_mg01c_ambil_sampel = "images/cg/cg_mg01c_ambil_sampel.webp"
image cg_mg01c_hasil_scanner = "images/cg/cg_mg01c_hasil_scanner.webp"
image cg_ch01_masuk_gerbang = "images/cg/cg_ch01_masuk_gerbang.webp"
image item_broken_padlock = "images/item/item_broken_padlock.webp"

# ==========================================
# DEFINISI CG & ITEM CHAPTER 02
# ==========================================
image cg_ch02_bayangan_buto = "images/cg/cg_ch02_bayangan_buto.webp"
image cg_ch02_citra_darmi = "images/cg/cg_ch02_citra_darmi.webp"
image cg_ch02_bimo_mantra = "images/cg/cg_ch02_bimo_mantra.webp"
image cg_ch02_raka_ziplock = "images/cg/cg_ch02_raka_ziplock.webp"
image cg_ch02_citra_pusing = "images/cg/cg_ch02_citra_pusing.webp"

image item_lendir_kimia = "images/item/item_lendir_kimia.webp"
image cg_mg02a_setan_datang = "images/cg/cg_mg02a_setan_datang.webp"
image bg_mg02a_segel_bimo = "images/cg/bg_mg02a_segel_bimo.webp"
image cg_mg02a_bimo_terpental = "images/cg/cg_mg02a_bimo_terpental.webp"
image cg_mg02a_bimo_berhasil = "images/cg/cg_mg02a_bimo_berhasil.webp"
image bg_mg02b_maze_dapur = "images/cg/bg_mg02b_maze_dapur.webp"
image cg_mg02b_darmi_terimakasih = "images/cg/cg_mg02b_darmi_terimakasih.webp"
image cg_mg02b_citra_kembali = "images/cg/cg_mg02b_citra_kembali.webp"
image cg_mg02b_darmi_kabur = "images/cg/cg_mg02b_darmi_kabur.webp"
image bg_mg02c_keseimbangan = "images/cg/bg_mg02c_keseimbangan.webp"
image cg_mg02c_raka_azan = "images/cg/cg_mg02c_raka_azan.webp"
image cg_mg02c_citra_tertawa = "images/cg/cg_mg02c_citra_tertawa.webp"
image cg_mg02c_citra_pingsan = "images/cg/cg_mg02c_citra_pingsan.webp"