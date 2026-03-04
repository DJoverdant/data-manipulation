import pandas as pd
from ucimlrepo import fetch_ucirepo

# Wine quality
dataset = fetch_ucirepo(id=186)

CATEGORIC = dataset.data.targets
NUMERIC = dataset.data.features

def get_categoric(target: any):
    freq_abs = target.value_counts()
    freq_rel = target.value_counts(normalize=True) * 100

    return pd.DataFrame({
        'Frequência Absoluta': freq_abs,
        'Frequência Relativa (%)': freq_rel
    })

def get_numeric(feature: any) -> str:
    coluna = feature['sepallength']
    classes = 5

    tabela_num = pd.cut(coluna, bins=classes).value_counts().sort_index()

def main():
    get_categoric(CATEGORIC)
    get_numeric(NUMERIC)

if __name__ == '__main__':
    main()