import pandas as pd
import glob

import re

def clean_corpus_line(s: str) -> str:
    if not isinstance(s, str):
        return ""
    s = s.strip()
    if not s:
        return ""

    # убрать метки вида [sjt1964f], [abc123], [META] и т.п.
    s = re.sub(r'\[[^\]]*?\]', '', s)

    # убрать тройные и одиночные кавычки по краям
    s = s.strip()
    s = re.sub(r'^"+', '', s)
    s = re.sub(r'"+$', '', s)

    # ещё раз подчистить пробелы
    s = s.strip()

    return s


def merge_csv_files(csv_pattern, out_csv):
    """
    Объединяет несколько CSV в один по строкам.
    csv_pattern может быть типа 'data/*.csv'.
    """
    files = glob.glob(csv_pattern)
    print("Нашёл файлов:", len(files))
    if not files:
        print("Ничего не найдено по шаблону:", csv_pattern)
        return

    dfs = []
    for path in files:
        df = pd.read_csv(path, encoding="utf-8")
        dfs.append(df)

    merged = pd.concat(dfs, ignore_index=True)


    merged['text'] = merged['text'].apply(clean_corpus_line)
    # при желании можно убрать дубликаты по text:
    merged = merged.drop_duplicates(subset=["text"])

    merged.to_csv(out_csv, index=False, encoding="utf-8")
    print(f"Готово! Итоговых строк: {len(merged)} → {out_csv}")


# пример использования
# склеиваем все csv из папки data в один
merge_csv_files("./khakas*.csv", "khakas_merged.csv")
