# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default poin_investigasi = 0 #Dari Chapter Awal
default citra_resonansi_gaib = 0 #Dari Chapter Awal Setiap MG Gaib
default item_jenglot = False #Dari Chapter Melawan Renggo Pilihan
default item_gembok_berlendir = False #Dari Chapter 01
default item_gembok_rusak = False #Dari Chapter 01
default item_lendir_hijau = False #Dari Chapter 02
default item_bukti_korupsi = False #Dari Chapter Sarah
default item_bukti_otopsi = False #Dari Chapter 05
default item_rekaman_tirto = False #Dari Chapter 05
default item_rekaman_renggo = False #Dari Chapter 04
default item_buku_kas_merah = False #Dari Chapter 07
default item_speaker_hantu = False #Dari Chapter 05
default item_koin_kuno = False #Dari Chapter 04
default item_boneka_jerami = False #Dari Chapter 04
default item_kristal_merah = False #Dari Chapter 04
default item_kalung_galih = False #Dari Chapter 03
default dr_rina_selamat = False #Dari Chapter 05
default gatot_trust = False #Dari Chapter 06
default darmi_trust = False #Dari Chapter 02

# The game starts here.

label start:


    jump chapter_01

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
