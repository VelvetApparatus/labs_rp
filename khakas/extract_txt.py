import os
import pandas as pd

def txt_folder_to_csv(txt_dir, out_csv):
    """
    Собирает все .txt из папки txt_dir в один CSV-файл out_csv.
    Одна строка txt -> одна строка CSV, колонка text.
    """
    rows = []

    for filename in os.listdir(txt_dir):
        if not filename.lower().endswith(".txt"):
            continue

        path = os.path.join(txt_dir, filename)
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue  # пропускаем пустые строки
                rows.append({"text": line})

    df = pd.DataFrame(rows)
    df.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"Готово! Записей: {len(df)} → {out_csv}")


# пример использования
# в папке txt_files лежат твои File.txt, File_3000.txt, File_1000_more.txt и т.п.
txt_folder_to_csv("./", "khakas_real.csv")
