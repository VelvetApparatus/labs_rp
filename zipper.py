import shutil

folder_path = "./data/khakas/audio"
zip_path = "./data/khakas_audio"  # без .zip — модуль сам добавит

shutil.make_archive(zip_path, 'zip', folder_path)

print("Готово! Архив создан:", zip_path + ".zip")
