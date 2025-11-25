import pandas as pd
import matplotlib.pyplot as plt

# --- Étape 3.1 : Stats numériques ---
print("\nStatistiques descriptives :")
print(df.describe())

# --- Étape 3.2 : Stats catégorielles ---
categorical_cols = ["gender", "country", "contract_type"]

for col in categorical_cols:
    print(f"\nRépartition de {col} :")
    print(df[col].value_counts())

# --- Étape 3.3 : Visualisations ---
df.hist(figsize=(12,6))
plt.tight_layout()
plt.show()

df["gender"].value_counts().plot(kind="bar", title="Gender Count")
plt.show()

df["contract_type"].value_counts().plot(kind="bar", title="Contract Type Count")
plt.show()
