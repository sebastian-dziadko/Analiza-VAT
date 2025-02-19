import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Wczytanie danych
file_path = r"C:\Users\48690\Downloads\skup.xlsx"
df = pd.read_excel(file_path)

# Założenie: pierwsza kolumna to nazwy krajów
countries = df.iloc[:, 0]  
data = df.iloc[:, 1:]  # Wybór tylko zmiennych numerycznych

# Normalizacja danych
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Tworzenie macierzy połączeń metodą Ward'a
linkage_matrix = linkage(data_scaled, method='ward')

# Określenie liczby skupień
num_clusters = 5  
skupienia = fcluster(linkage_matrix, num_clusters, criterion='maxclust')

# Rysowanie dendrogramu
plt.figure(figsize=(12, 6))
dendrogram(
    linkage_matrix,
    labels=countries.values,
    leaf_rotation=90,
    leaf_font_size=10,
    color_threshold=linkage_matrix[-(num_clusters - 1), 2]  # Poprawiony błąd składniowy
)
plt.title("Dendrogram - Analiza Skupień luki VAT")
plt.xlabel("Kraje")
plt.ylabel("Odległość")
plt.axhline(y=linkage_matrix[-(num_clusters - 1), 2], color='r', linestyle='--', label="Podział na grupy")
plt.legend()
plt.show()

# Dodanie informacji o skupieniach do ramki danych
df['Skupienie'] = skupienia

# Obliczenie średnich wartości w skupieniach
grouped_means = grouped_means = df.groupby('Skupienie').mean(numeric_only=True)

print("Średnie wartości zmiennych w skupieniach:")
print(grouped_means)

# Wizualizacja rozkładu zmiennych dla poszczególnych skupień
plt.figure(figsize=(12, 6))
sns.boxplot(x=df['Skupienie'], y=df['Luka VAT - 2022'])
plt.title("Rozkład Luki VAT - 2022 w poszczególnych skupieniach")
plt.show()

# Analiza PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(data_scaled)
pca_df = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
pca_df['Skupienie'] = skupienia
pca_df['Kraj'] = countries

# Wykres PCA
plt.figure(figsize=(10, 6))
sns.scatterplot(x='PC1', y='PC2', hue='Skupienie', data=pca_df, palette='viridis', s=100)
plt.title("Analiza PCA - Skupienia krajów")
plt.xlabel("Główna składowa 1")
plt.ylabel("Główna składowa 2")
plt.legend(title='Skupienie')
plt.show()
