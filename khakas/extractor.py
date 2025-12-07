import pandas as pd




def filter_fn(x):
    if not isinstance(x, str):
        return False
    x = x.strip()
    if not x:
        return False
    words = x.split()  # корректно делит по пробелам
    if len(words) < 7:
        return False
    # if len(words) > 20:
        # return False
    return True



def extract():
    df = pd.read_csv('./khakas/data_oral_khakas_corpus.csv')
    df = df.drop_duplicates(subset=["text"], keep="first")


    df["valid"] = df["text"].apply(filter_fn)

    df = df[df["valid"] == True]

    print("Количество подходящих строк:", len(df))

    # оставить первые 9000 (если столько есть)
    df = df.head(9000)

    # Сохранение в txt (по одному предложению в строке)
 
    df["text"].to_csv(f"texts_oral_corpus_{len(df)}.txt", index=False, header=False)




extract()