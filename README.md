# Analiza Skupień dla Luki VAT w Krajach UE

W ramach tego projektu przeprowadzona została analiza skupień krajów Unii Europejskiej na podstawie danych dotyczących luki VAT w latach 2012, 2016 i 2022, PKB per capita, VAT jako procent PKB oraz szarej strefy jako procent PKB. Celem analizy było zidentyfikowanie grup krajów o podobnych cechach podatkowych i gospodarczych.

## Instrukcja

1. Pobierz wszystkie pliki projektu.
2. Załaduj dane z pliku `.xlsx` zawierającego dane o krajach UE oraz wskaźniki ekonomiczne.
3. Uruchom skrypt w Pythonie, który przeprowadzi analizę skupień oraz analizę głównych składowych (PCA).
4. Sprawdź wyniki w postaci wizualizacji, które przedstawiają wyniki analizy skupień oraz rozkłady zmiennych w poszczególnych grupach.
5. Zajrzyj do raportu o wynikach analizy, aby poznać główne wnioski z przeprowadzonego badania.

## Wymagania

Aby uruchomić ten projekt, upewnij się, że masz zainstalowane poniższe pakiety Python:

- pandas
- numpy
- matplotlib
- seaborn
- scipy
- sklearn

## Dane

Dane do analizy zostały zebrane z różnych źródeł, w tym z raportów dotyczących luki VAT i wskaźników ekonomicznych. Plik Excel zawiera następujące kolumny:

- **Kraj** - Nazwa kraju
- **Luka VAT - 2022** - Wartość luki VAT w 2022 roku
- **Luka VAT - 2016** - Wartość luki VAT w 2016 roku
- **Luka VAT - 2012** - Wartość luki VAT w 2012 roku
- **PKB per capita** - Produkt krajowy brutto na osobę
- **VAT jako % PKB** - Procent wpływów VAT w stosunku do PKB
- **Szara strefa jako % PKB** - Procent szarej strefy w stosunku do PKB

## Analiza

Przeprowadzona analiza obejmuje:

1. **Analizę Skupień**: Na podstawie danych dotyczących luki VAT oraz wskaźników gospodarczych, kraje UE zostały podzielone na grupy o podobnych cechach przy użyciu metody analizy skupień (hierarchiczne grupowanie metodą Ward'a). 
   
2. **Analizę Głównych Składowych (PCA)**: W celu zredukowania wymiarów danych i lepszego zobrazowania wyników, przeprowadzono analizę PCA, co pozwoliło na zrozumienie głównych czynników, które wpływają na podobieństwa między krajami.

## Wizualizacje

Projekt generuje następujące wizualizacje:

- **Dendrogram**: Wizualizacja hierarchicznej analizy skupień, która przedstawia, jak kraje zostały pogrupowane na podstawie podobieństw w zmiennych ekonomicznych.
- **Wykres pudełkowy**: Rozkład wartości luki VAT w 2022 roku w poszczególnych grupach krajów.
- **Wykres PCA**: Wizualizacja wyników analizy głównych składowych, pokazująca, jak kraje zostały rozdzielone w przestrzeni dwóch głównych komponentów.

## Wnioski

Dzięki analizie skupień i PCA udało się zidentyfikować grupy krajów o podobnych cechach związanych z luką VAT oraz innymi wskaźnikami ekonomicznymi. Na tej podstawie można dostrzec istotne różnice między krajami UE, które mogą wynikać z różnorodnych polityk podatkowych.
