import pdfplumber
import pandas as pd
import regex as re

def extract_sentences_from_pdf(pdf_path):
    all_text = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                all_text.append(text)

    full_text = "\n".join(all_text)

    # --- Разбиваем на предложения ---
    # Разбивает по точкам, восклицательным и вопросительным знакам
    sentences = re.split(r'[.!?]\s+', full_text)

    cleaned = []
    for s in sentences:
        s = s.strip()
        if not s:
            continue

        # ставим точку в конце, если ее нет
        if not s.endswith("."):
            s += "."

        # первая буква заглавная
        s = s[0].upper() + s[1:]

        cleaned.append(s)

    return cleaned


def pdf_to_sentence_csv(pdf_path, csv_path):
    sentences = extract_sentences_from_pdf(pdf_path)

    df = pd.DataFrame({"text": sentences})
    df.to_csv(csv_path, index=False, encoding="utf-8")

    print(f"Готово! {len(df)} предложений сохранено в {csv_path}")


# Пример вызова:
pdf_to_sentence_csv("./khakas/mal.pdf", "./khakas/sentences_mal.csv")
