# ==========================================
# PUSTAKA TRANSISI KUSTOM
# Simpan sebagai: pustaka_transisi.rpy
# ==========================================

# 1. Flashbang (Layar kilat putih menyilaukan, cocok untuk ledakan/foto)
define flashbang = Fade(0.1, 0.0, 0.5, color="#ffffff")
# Flash Status
define flash_hijau = Fade(0.1, 0.0, 0.5, color="#00ff00") # Cocok saat terkena racun / efek heal
define flash_biru = Fade(0.1, 0.0, 0.5, color="#0044ff")  # Cocok untuk masuk menu sistem / kena sihir air

# 2. Flash Merah (Kilat merah, cocok untuk adegan terkena serangan)
define flashmerah = Fade(0.1, 0.0, 0.5, color="#ff0000")

# 3. Kedip Bangun Tidur (Gelap lama, lalu perlahan terang)
define bangun_tidur = Fade(1.5, 1.0, 2.0, color="#000000")
# Dissolve Kustom
define dissolve_lambat = Dissolve(2.0) # Cocok untuk adegan sedih / romantis
define dissolve_kilat = Dissolve(0.2)  # Cocok untuk adegan buru-buru / tegang

# 4. Wipe/Usap Layar (Bawaan Ren'Py)
define wipe_kiri = CropMove(0.5, "wipeleft")
define wipe_kanan = CropMove(0.5, "wiperight")
# Melengkapi arah Push
define dorong_bawah = PushMove(0.3, "pushdown")

# Slide (Gambar baru meluncur di atas gambar lama)
define slide_kiri = CropMove(0.5, "slideleft")
define slide_kanan = CropMove(0.5, "slideright")
define slide_atas = CropMove(0.5, "slideup")
define slide_bawah = CropMove(0.5, "slidedown")

# 5. ImageDissolve (Transisi menggunakan pola gambar)
# Catatan: Siapkan gambar hitam-putih (.png atau .jpg) di folder 'images/transisi/'
# Area putih akan muncul lebih dulu, area hitam belakangan.
define blinds = ImageDissolve("images/transisi/garis_tirai.png", 1.0, 8)
define blood_splatter = ImageDissolve("images/transisi/cipratan_darah.webp", 1.5, 8)
define kaca_pecah = ImageDissolve("images/transisi/kaca_pecah.webp", 1.0, 8)
define transisi_asap = ImageDissolve("images/transisi/mask_asap.webp", 1.5, 8)
define transisi_radar = ImageDissolve("images/transisi/mask_radar.webp", 1.0, 16)
define transisi_matrix = ImageDissolve("images/transisi/mask_matrix.webp", 0.8, 32)
define transisi_tebasan = ImageDissolve("images/transisi/mask_tebas.webp", 0.5, 8)
define transisi_tinta = ImageDissolve("images/transisi/mask_tinta.webp", 1.5, 16)
define transisi_air = ImageDissolve("images/transisi/mask_riak_air.webp", 2.0, 16)
define transisi_terbakar = ImageDissolve("images/transisi/mask_terbakar.webp", 1.2, 8)
define transisi_hex = ImageDissolve("images/transisi/mask_hex.webp", 1.0, 16)
define transisi_kuas = ImageDissolve("images/transisi/mask_kuas.webp", 1.0, 8)
define transisi_tirai = ImageDissolve("images/transisi/mask_tirai.webp", 1.5, 16)
define transisi_tembakan = ImageDissolve("images/transisi/mask_peluru.webp", 0.3, 4) 
define transisi_senter = ImageDissolve("images/transisi/mask_senter.webp", 1.5, 16)
define transisi_teropong = ImageDissolve("images/transisi/mask_teropong.webp", 1.0, 8)
define transisi_pintubesi = ImageDissolve("images/transisi/mask_pintubesi.webp", 1.0, 4)
define transisi_camo = ImageDissolve("images/transisi/mask_camo.webp", 1.2, 16)
define transisi_cctv = ImageDissolve("images/transisi/mask_cctv.webp", 0.5, 16)
define transisi_sniper = ImageDissolve("images/transisi/mask_sniper.webp", 1.0, 8)
define transisi_darah = ImageDissolve("images/transisi/mask_darah.webp", 2.0, 16)
define transisi_retak = ImageDissolve("images/transisi/mask_retak.webp", 0.8, 8)
define transisi_radio = ImageDissolve("images/transisi/mask_radio.webp", 0.5, 32)


# 6. Pixellate (Efek memecah jadi piksel kotak-kotak)
# Angka 5 adalah tingkat kebesaran pikselnya.
define efek_piksel = Pixellate(1.0, 5)
# 7. Iris Kamera / Fokus Mata
define fokus_tutup = CropMove(1.0, "irisout")
define fokus_buka = CropMove(1.0, "irisin")
# Pingsan (Terang perlahan menuju gelap gulita total)
define pingsan = Fade(2.0, 1.0, 0.0, color="#000000")

# 8. Push / Dorongan Kasar
define dorong_kiri = PushMove(0.3, "pushleft")
define dorong_kanan = PushMove(0.3, "pushright")
define dorong_atas = PushMove(0.3, "pushup")
# 9. Mata Mengerjap / Pusing (Layar berkedip gelap beberapa kali)
define mata_mengerjap = MultipleTransition([
    False, Fade(0.2, 0.0, 0.2, color="#000000"),
    True, Fade(0.2, 0.0, 0.2, color="#000000"),
    False, Fade(0.2, 0.0, 0.5, color="#000000"),
    True])
# 10. Transisi Glitch TV / Horor
# Catatan: Siapkan gambar bintik hitam-putih acak bernama 'glitch_noise.png'
define tv_rusak = ImageDissolve("images/transisi/tv_rusak.webp", 0.3, 32)
