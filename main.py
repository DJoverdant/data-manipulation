from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
import pandas as pd
import subprocess

# Wine quality
dataset = fetch_ucirepo(id=186)
NUMERIC = dataset.data.features


def plot_data(feature: pd.DataFrame):
    ph_values = feature["pH"]

    binned = pd.cut(ph_values, bins=5)
    freq = binned.value_counts().sort_index()

    freq.plot(
        kind="bar",
        color="teal",
        rot=45,
        title="Distribuição do pH do Vinho",
        xlabel="Intervalos de pH",
        ylabel="Frequência",
    )


def main():
    subprocess.run("clear")
    plot_data(NUMERIC)
    plt.show()


if __name__ == "__main__":
    main()
