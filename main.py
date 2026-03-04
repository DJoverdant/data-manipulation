import pandas as pd
from ucimlrepo import fetch_ucirepo

# Wine quality
dataset = fetch_ucirepo(id=186)

X = dataset.data.features
y = dataset.data.targets

print(X.head())
