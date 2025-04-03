import os

def rename_txt_files(folder_path, prefix="yeni_dosya"):
    
    # Klasördeki tüm dosyaları listele
    for count, filename in enumerate(os.listdir(folder_path)):
        # Sadece .txt uzantılı dosyaları işle
        if filename.endswith(".txt"):
            # Eski dosya yolu
            old_file = os.path.join(folder_path, filename)
            # Yeni dosya adı
            new_name = f"{prefix}_{count + 1}.txt"
            # Yeni dosya yolu
            new_file = os.path.join(folder_path, new_name)
            
            try:
                # Dosyayı yeniden adlandır
                os.rename(old_file, new_file)
                print(f"Dosya adı değiştirildi: {filename} -> {new_name}")
            except Exception as e:
                print(f"Hata oluştu ({filename}): {str(e)}")

# Kullanım örneği
klasor_yolu = "/Users/smlmrt/Desktop/Örnek Resimler label"  # Kendi klasör yolunuzu buraya yazın
rename_txt_files(klasor_yolu, prefix="metin")