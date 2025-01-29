import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import os

# Filväg
file_path = r"C:\Users\Book\OneDrive - TUC Sweden\Skola\Data-visualizion\Grupp-arbete\paid_unemployment_benefit_fund_year (2).csv"

# Steg 1: Kontrollera om filen finns
if os.path.exists(file_path):
    print("Filen finns!")
else:
    print(f"Filen kunde inte hittas på vägen: {file_path}")
    exit()

# Steg 2: Läs in datasetet från CSV-filen
try:
    df = pd.read_csv(file_path)
    print("CSV-filen har lästs in!")
except Exception as e:
    print(f"Ett fel uppstod när filen skulle läsas in: {e}")
    exit()

# Steg 3: Kontrollera kolumnnamn och datatyper
print("\nKolumnnamn i datasetet:")
print(df.columns)

print("\nDatatyper i datasetet:")
print(df.dtypes)

# Steg 4: Fyll saknade värden
df['days'] = pd.to_numeric(df['days'], errors='coerce')  # Omvandla till numeriska värden
df['amount_sek'] = pd.to_numeric(df['amount_sek'], errors='coerce')

df['days'] = df['days'].fillna(df['days'].median())  # Fyll med median om saknade värden
df['amount_sek'] = df['amount_sek'].fillna(df['amount_sek'].median())  # Samma för amount_sek

# Steg 5: Skapa en ny kolumn: ersättning per dag
df['amount_per_day'] = df['amount_sek'] / df['days']

# Visa de första raderna i data för att kontrollera
print("\nFörsta 5 raderna efter transformation:")
print(df.head())

# Kontrollera saknade värden efter transformation
print("\nSaknade värden efter transformation:")
print(df.isnull().sum())

# Steg 6: Gruppdata och sammanfattning
grouped_data = df.groupby(['year', 'gender']).agg(
    total_amount=('amount_sek', 'sum'),
    avg_amount=('amount_sek', 'mean'),
    median_daily=('amount_per_day', 'median'),
    case_count=('days', 'count')
).reset_index()
print("\nSammanfattad data:")
print(grouped_data.head())

# Steg 7: Ladda Data (Exportera till Excel)
output_path = r'processed_data.xlsx'
grouped_data.to_excel(output_path, index=False)
print(f"\nData har exporterats till: {output_path}")

# Steg 8: Visualisering av Data (8 grafer) #Kumulativ utbetalning över tid (Stacked Area Chart)
# 1. **Linjeplot: Totala utbetalningar över tid per kön**
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='year', y='amount_sek', hue='gender', marker='o', palette='muted', linewidth=2)
plt.title('Totala utbetalningar per år och kön', fontsize=16)
plt.xlabel('År', fontsize=14)
plt.ylabel('Totala utbetalningar (SEK)', fontsize=14)
plt.legend(title='Kön', title_fontsize='13', loc='upper left')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

# Denna linjeplot visar utvecklingen av de totala utbetalningarna (i SEK) över åren för både män och kvinnor. Den visualiserar hur utbetalningarna har förändrats och om det finns några skillnader mellan könen genom åren.

# 2. **Stapelgraf: Utbetalningar per kön under 2020**
plt.figure(figsize=(12, 6))
sns.barplot(data=df[df['year'] == 2020], x='gender', y='amount_sek', palette='coolwarm')
plt.title('Utbetalningar per kön under 2020', fontsize=16)
plt.xlabel('Kön', fontsize=14)
plt.ylabel('Utbetalning (SEK)', fontsize=14)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Denna stapelgraf visar utbetalningarna för män och kvinnor under året 2020. Den hjälper oss att jämföra beloppen som betalades ut till de två könen under detta specifika år.

# 3. **Histogram: Fördelning av utbetalningar**
plt.figure(figsize=(12, 6))
sns.histplot(df['amount_sek'], kde=True, bins=25, color='teal', stat='density', linewidth=0)
plt.title('Fördelning av utbetalningar', fontsize=16)
plt.xlabel('Utbetalning (SEK)', fontsize=14)
plt.ylabel('Densitet', fontsize=14)
plt.tight_layout()
plt.show()

# Histogrammet visar hur utbetalningarna är fördelade. Med hjälp av densitetslinjen (KDE) kan vi också se om utbetalningarna följer en viss fördelning och identifiera eventuella avvikelser (t.ex. extremt höga eller låga utbetalningar).

# 4. **Boxplot: Fördelning av ersättning per dag per kön**
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='gender', y='amount_per_day', palette='Set2')
plt.title('Fördelning av ersättning per dag per kön', fontsize=16)
plt.xlabel('Kön', fontsize=14)
plt.ylabel('Ersättning per dag (SEK)', fontsize=14)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Denna boxplot visualiserar fördelningen av ersättning per dag för män och kvinnor. Den visar medianen, kvartilerna och eventuella avvikelser (outliers) i data. Boxplotten ger en bra förståelse för hur stor variationen är i ersättningen per dag mellan könen.

# 5. **Scatterplot: Korrelation mellan dagar och utbetalning**
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='days', y='amount_sek', hue='gender', size='year', sizes=(50, 200), palette='coolwarm', alpha=0.7)
plt.title('Korrelation mellan dagar och utbetalning', fontsize=16)
plt.xlabel('Antal dagar', fontsize=14)
plt.ylabel('Utbetalning (SEK)', fontsize=14)
plt.tight_layout()
plt.show()

# Denna scatterplot visar sambandet mellan antalet dagar och utbetalningarna. Större prickar representerar senare år, och färgen på prickarna skiljer mellan könen. Det hjälper oss att se om det finns någon linjär relation mellan antalet dagar och beloppet som betalats ut.

# 6. **Violinplot: Fördelning av ersättning per dag per kön**
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='gender', y='amount_per_day', palette='Set3', inner='quart')
plt.title('Fördelning av ersättning per dag per kön', fontsize=16)
plt.xlabel('Kön', fontsize=14)
plt.ylabel('Ersättning per dag (SEK)', fontsize=14)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# Denna violinplot ger en mer detaljerad bild av hur ersättningarna per dag fördelas mellan män och kvinnor. Den visar både fördelningens form och kvartilerna, vilket ger oss en förståelse för variationen i ersättningarna.

# 7. **Heatmap: Korrelation mellan antal dagar och utbetalningar**
corr = df[['days', 'amount_sek', 'amount_per_day']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, cbar_kws={'label': 'Korrelationskoefficient'})
plt.title('Korrelation mellan dagar och utbetalningar', fontsize=16)
plt.tight_layout()
plt.show()

# Denna heatmap visar sambandet mellan antal dagar, total utbetalning och ersättning per dag. En positiv korrelation innebär att ökad varaktighet leder till högre utbetalningar, medan en negativ korrelation skulle innebära motsatsen.

# 8. **Stacked Bar Chart: Jämförelse av utbetalningar per kön**
df_grouped = df.groupby(['year', 'gender'])['amount_sek'].sum().unstack()
df_grouped.plot(kind='bar', stacked=True, figsize=(12, 6), cmap='coolwarm')
plt.title('Jämförelse av utbetalningar per kön över åren', fontsize=16)
plt.xlabel('År', fontsize=14)
plt.ylabel('Totala utbetalningar (SEK)', fontsize=14)
plt.legend(title='Kön', title_fontsize='13')
plt.tight_layout()
plt.show()


# Denna stapelgraf jämför de totala utbetalningarna för män och kvinnor över åren. Grafen gör det enkelt att se hur könsfördelningen har förändrats över tid och om det finns några mönster eller skillnader.


"""
# Steg 8: Visualisering av Data (8 grafer) #Kumulativ utbetalning över tid (Stacked Area Chart)
plt.figure(figsize=(12,6))
df_pivot = df.pivot_table(index='year', columns='gender', values='amount_sek', aggfunc='sum').fillna(0)
df_pivot.plot.area(alpha=0.8)
plt.title('Kumulativ totalutbetalning över tid per kön')
plt.xlabel('År')
plt.ylabel('Kumulativ utbetalning (SEK)')
plt.grid(True)
plt.show()


# 1. Linjeplot: Totala utbetalningar över tid per kön
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='year', y='amount_sek', hue='gender')
plt.title('Totala utbetalningar över tid per kön')
plt.xlabel('År')
plt.ylabel('Utbetalning (SEK)')
plt.grid(True)
plt.show()

# 2. Stapelgraf: Utbetalning per kön 2020
plt.figure(figsize=(12, 6))
sns.barplot(data=df[df['year'] == 2020], x='gender', y='amount_sek')
plt.title('Utbetalning per kön 2020')
plt.xlabel('Kön')
plt.ylabel('Utbetalning (SEK)')
plt.xticks(rotation=45)
plt.show()

# 3. Histogram: Fördela utbetalningar
plt.figure(figsize=(12, 6))
sns.histplot(df['amount_sek'], kde=True, bins=20)
plt.title('Fördela utbetalningar')
plt.xlabel('Utbetalning (SEK)')
plt.ylabel('Frekvens')
plt.show()

# 4. Boxplot: Fördelning av ersättning per dag per kön
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='gender', y='amount_per_day')
plt.title('Fördelning av ersättning per dag per kön')
plt.xlabel('Kön')
plt.ylabel('SEK/dag')
plt.xticks(rotation=45)
plt.show()

# 5. Scatterplot: Korrelation mellan dagar och utbetalning
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='days', y='amount_sek', hue='gender', size='year', sizes=(50, 200))
plt.title('Korrelation mellan dagar och utbetalning')
plt.xlabel('Dagar')
plt.ylabel('Utbetalning (SEK)')
plt.show()

# 6. Violinplot: Fördelning av ersättning per dag per kön
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x='gender', y='amount_per_day')
plt.title('Violinplot för ersättning per dag per kön')
plt.xlabel('Kön')
plt.ylabel('SEK/dag')
plt.xticks(rotation=45)
plt.show()

# 7. Heatmap: Korrelation mellan antal dagar och utbetalningar
corr = df[['days', 'amount_sek', 'amount_per_day']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Korrelation mellan antal dagar och utbetalningar')
plt.show()

# 8. Stacked bar chart: Jämförelse av utbetalningar per kön
df_grouped = df.groupby(['year', 'gender'])['amount_sek'].sum().unstack()
df_grouped.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Jämförelse av utbetalningar per kön')
plt.xlabel('År')
plt.ylabel('Utbetalning (SEK)')
plt.legend(title='Kön')
plt.show()
"""
# Steg 9: Maskininlärning - Regression (Förutsäga utbetalning)
print("\n=== Steg 9: Maskininlärning - Regression ===")
X = df[['year', 'days']]  # Funktioner
y = df['amount_sek']  # Målvariabel

# Dela upp data i tränings- och testset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Skapa och träna modellen
model = LinearRegression()
model.fit(X_train, y_train)

# Gör förutsägelser

y_pred = model.predict(X_test)

# Utvärdera modellen
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R2 Score: {r2}')

# Visualisera resultatet av förutsägelsen
plt.figure(figsize=(12, 6))
plt.scatter(y_test, y_pred)
plt.title('Förutsägelse av utbetalning vs verklig utbetalning')
plt.xlabel('Verklig utbetalning (SEK)')
plt.ylabel('Förutsagd utbetalning (SEK)')
plt.show()

print("\nProcessen är klar!")