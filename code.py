import pandas as pd
import matplotlib.pyplot as plt

# 1 Lecture du csv
df = pd.read_csv("./ventes.csv")
                                            



# 2 Calcul du Chiffre d’Affaires Brut
df["CA_Brut"] = df["Prix"] * df["Quantite"]

# 3 Application des remises
df["CA_Net"] = df["CA_Brut"] * (1 - df["Remise"] / 100)

# 4  Calcul de la TVA 
df["TVA"] = df["CA_Net"] * 0.20

# 5  CA Total de l’entreprise
ca_total = df["CA_Net"].sum()
print(f"CA Total de l’entreprise : {ca_total:.2f} ")

# 6  Produit le plus rentable
id_max = df.loc[df["CA_Net"].idxmax(), "ID"]
print(f"Produit le plus rentable : ID {id_max}")

# 7 nouveau csv avec les résultats
df.to_csv("resultats_final.csv", index=False)





# Graphique du CA par produit
plt.bar(df["ID"], df["CA_Net"], color="pink")
plt.xlabel("ID Produit")
plt.ylabel("CA Net")
plt.title("Chiffre d’Affaires Net par Produit")
plt.savefig("ca_par_produit.png")
plt.show()
