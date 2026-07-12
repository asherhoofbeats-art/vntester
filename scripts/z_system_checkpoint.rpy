# ==========================================
# AUTO-GENERATED CHECKPOINT SYSTEM
# ==========================================
label tawarkan_save(checkpoint_name="Checkpoint"):
    # Buka sementara akses save dan rollback agar pemain bisa save
    $ _save = True
    $ _rollback = True
    
    # Efek transisi ringan (Opsional)
    scene black with dissolve
    
    menu:
        "Pencapaian: [checkpoint_name]\nApakah Anda ingin menyimpan permainan sekarang?"
        
        "Ya, Buka Menu Save":
            call screen save
            
        "Tidak, Lanjutkan Cerita":
            pass

    # Kunci kembali fitur save sebelum lanjut ke label berikutnya
    $ _save = False
    $ _rollback = False
    
    return
