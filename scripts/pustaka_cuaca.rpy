# ==========================================
# PUSTAKA CUACA & PARTIKEL
# Simpan sebagai: pustaka_cuaca.rpy
# ==========================================

# Catatan: Siapkan gambar kecil berformat .webp di folder 'images/partikel/'

# 1. Salju Lembut (Turun lurus perlahan)
image salju_lembut = SnowBlossom("images/partikel/salju.webp", count=100, xspeed=(0, 0), yspeed=(50, 100), start=0)

# 2. Hujan Deras (Turun cepat dan miring)
image hujan_deras = SnowBlossom("images/partikel/hujan.webp", count=250, xspeed=(-50, -100), yspeed=(600, 800), start=0, fast=True)

# 3. Kelopak Sakura (Gugur meliuk-liuk tertiup angin)
image sakura_gugur = SnowBlossom("images/partikel/sakura.webp", count=75, xspeed=(100, 150), yspeed=(100, 150), start=0)

# 4. Debu Ruangan Tua (Melayang lambat ke atas/samping)
image debu_melayang = SnowBlossom("images/partikel/debu.webp", count=40, xspeed=(-10, 10), yspeed=(-15, 15), start=0)

# 5. Bara Api / Sparks (Naik ke atas)
image bara_api = SnowBlossom("images/partikel/bara.webp", count=50, xspeed=(-20, 20), yspeed=(-100, -200), start=0)

# 6. Daun Kering (Jatuh melayang acak)
image daun_gugur = SnowBlossom("images/partikel/daun.webp", count=30, xspeed=(-50, 50), yspeed=(150, 250), start=2)

# 7. Awan Kabut Melayang (Bergerak horizontal sangat lambat)
# PERBAIKAN: yspeed diturunkan drastis agar tidak jatuh seperti hujan, xspeed dibuat searah.
image kabut_tipis = SnowBlossom("images/partikel/awan.webp", count=15, xspeed=(20, 40), yspeed=(-5, 5), border=100, start=0)

image kabut_area:
    contains:
        # Gunakan yspeed sangat rendah agar tidak terlihat jatuh seperti hujan
        # xspeed dibuat searah agar kabut terlihat tertiup angin pelan
        SnowBlossom("images/partikel/awan.webp", count=20, xspeed=(30, 60), yspeed=(-5, 5), border=100, start=2)
        
        # Logika Muncul - Diam - Hilang
        alpha 0.0
        linear 10.0 alpha 0.5  # Muncul perlahan dalam 10 detik
        pause 15.0             # Menetap selama 15 detik
        linear 10.0 alpha 0.0  # Menghilang perlahan dalam 10 detik
        pause 5.0              # Jeda kosong sebelum muncul lagi
        repeat

# Versi yang lebih tebal (Layer Ganda)
image kabut_tebal:
    contains:
        SnowBlossom("images/partikel/awan.webp", count=15, xspeed=(20, 40), yspeed=(-2, 2), border=100)
        alpha 0.0
        linear 8.0 alpha 0.6
        pause 10.0
        linear 8.0 alpha 0.0
        repeat
    contains:
        SnowBlossom("images/partikel/awan.webp", count=15, xspeed=(-20, -40), yspeed=(-2, 2), border=100)
        alpha 0.0
        pause 5.0 # Jeda agar layer kedua muncul tidak berbarengan
        linear 12.0 alpha 0.4
        pause 12.0
        linear 12.0 alpha 0.0
        repeat

# 8. Kunang-kunang (Bergerak acak ke segala arah)
image kunang_kunang = SnowBlossom("images/partikel/kunang.webp", count=25, xspeed=(-30, 30), yspeed=(-30, 30), border=50, start=0)

# 9. Gelembung Udara (Naik ke atas dengan kecepatan variatif)
image gelembung_air = SnowBlossom("images/partikel/bubble.webp", count=40, xspeed=(-20, 20), yspeed=(-150, -50), start=0)

# 10. Bulu Melayang (Sangat ringan, jatuh sangat lambat)
image bulu_melayang = SnowBlossom("images/partikel/bulu.webp", count=10, xspeed=(-100, 100), yspeed=(20, 50), start=5)

# 11. Partikel Cahaya (Melayang pelan di bawah sinar matahari)
image partikel_cahaya = SnowBlossom("images/partikel/cahaya.webp", count=20, xspeed=(-20, 20), yspeed=(-10, 20), start=0)

# 12. Badai Pasir (Bergerak cepat ke samping)
image badai_pasir = SnowBlossom("images/partikel/pasir.webp", count=300, xspeed=(-1000, -1500), yspeed=(50, 100), start=0, fast=True)

# 13. Kelopak Mawar (Jatuh meliuk elegan)
image mawar_gugur = SnowBlossom("images/partikel/mawar.webp", count=30, xspeed=(-100, 100), yspeed=(150, 250), start=1)

# 14. Gelembung Sabun (Melayang manja ke atas)
image gelembung_sabun = SnowBlossom("images/partikel/soap_bubble.webp", count=15, xspeed=(-50, 50), yspeed=(-80, -120), start=0)

# 15. Abu Terbakar (Turun pelan dan acak)
image abu_pembakaran = SnowBlossom("images/partikel/abu.webp", count=60, xspeed=(-30, 30), yspeed=(40, 80), start=0)

# 16. Hujan Batu Kerikil (Jatuh cepat, berat, count sedang)
image hujan_kerikil = SnowBlossom("images/partikel/batu.webp", count=80, xspeed=(-20, 20), yspeed=(400, 600), fast=True)