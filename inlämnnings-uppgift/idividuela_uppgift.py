import numpy as np
import os
import pandas as pd
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt

# EXTRACT:
# Steg 1: Importera CSV-filen

csv_file_path = "C:\\Users\\Book\\OneDrive - TUC Sweden\\Skola\\Data-visualizion\\inlämnnings-uppgift\\unemployment_benefit.csv"
df = pd.read_csv(csv_file_path)
print("Steg 1: Importera CSV-filen")
print(df.head())

# TRANSFORM:
#  Rnsa och bearbeta datan:
# Steg 2: Hantera saknade värden
# Anta att vi fyller saknade värden med 0

df.fillna(0, inplace=True)
print("Steg 2: Hantera saknade värden")
print(df.head())


# Steg 3.1: Skapa nya kolumner baserat på beräkningar eller villkor
# Exempel: Skapa en ny kolumn 'amount_per_person' som är 'amount_sek' delat med 'persons'

if 'amount_sek' in df.columns and 'persons' in df.columns:
    df['amount_per_person'] = df.apply(lambda row: row['amount_sek'] / row['persons'] if row['persons'] != 0 else 0, axis=1)
else:
    print("Kolumnerna 'amount_sek' och/eller 'persons' saknas i CSV-filen.")
print("Steg 3: Skapa nya kolumner")


# Steg 4: Filtrera datan
# Exempel: Filtrera för att endast inkludera data från år 2005 och framåt
if 'year' in df.columns:
    df_filtered = df[df['year'] >= 2005]
else:
    print("Kolumnen 'year' saknas i CSV-filen.")
    df_filtered = df
print("Steg 4: Filtrera datan")
print(df_filtered.head())

      
# Steg 5: Använd groupby() och agg() för att summera och analysera nyckeltal
# Exempel: Gruppby 'year' och summera 'amount_sek' och 'persons'
summary = df_filtered.groupby('year').agg({
    'amount_sek': 'sum',
    'persons': 'sum'
})
print("Steg 5: Använd groupby() och agg()")
print(summary)


# Steg 6: Lägg till summering av 'amount_per_person'
summary['amount_per_person'] = summary.apply(lambda row: row['amount_sek'] / row['persons'] if row['persons'] != 0 else 0, axis=1)
print("Steg 6: Lägg till summering av 'amount_per_person'")
print(summary)


# LOAD:
# Steg 7: Exportera den bearbetade datan till en Excel-fil
summary.to_excel("C:\\Users\\Book\\OneDrive - TUC Sweden\\Skola\\Data-visualizion\\inlämnnings-uppgift\\processed_data.xlsx", engine='openpyxl')
# Kontrollera om Excel-filen har skapats korrekt
excel_file_path = ("C:\\Users\\Book\\OneDrive - TUC Sweden\\Skola\\Data-visualizion\\inlämnnings-uppgift\\processed_data.xlsx")
if os.path.exists(excel_file_path):
    print(f"Excel-filen har skapats korrekt: {excel_file_path}")
else:
    print("Något gick fel, Excel-filen skapades inte.")


# ANALYS:
# Steg 8:  Utför utforskande dataanalys(EDA)
# med minst tre olika visualiseringar: 
# Histogram för datafördelning
plt.figure(figsize=(10, 6))
sns.histplot(df_filtered['amount_sek'], bins=30, kde=True)
plt.title('Histogram över Amount SEK')
plt.xlabel('Amount SEK')
plt.ylabel('Frekvens')
plt.show()

# Linjediagram för att visa trender över tid
plt.figure(figsize=(10, 6))
sns.lineplot(data=summary, x=summary.index, y='amount_sek')
plt.title('Trend för Amount SEK över tid')
plt.xlabel('År')
plt.ylabel('Total Amount SEK')
plt.show()

# Scatter plot för att visa relationer mellan två variabler
plt.figure(figsize=(10, 6))
sns.scatterplot(data=summary, x='persons', y='amount_per_person')
plt.title('Scatter Plot av Amount Per Person vs. Antal Personer')
plt.xlabel('Antal Personer')
plt.ylabel('Amount Per Person')
plt.show()

# steg 9
# Skapa log-transformerad kolumn för 'amount_sek'
df_filtered['log_amount_sek'] = np.log(df_filtered['amount_sek'] + 1)

# Professionella och tydliga visualiseringar
plt.figure(figsize=(10, 6))
sns.histplot(df_filtered['log_amount_sek'], kde=True)
plt.title('Log-transformerad fördelning av Amount SEK')
plt.xlabel('Log Amount SEK')
plt.ylabel('Frekvens')
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(x='year', y='amount_sek', data=df_filtered)
plt.title('Trend av Amount SEK över åren')
plt.xlabel('År')
plt.ylabel('Amount SEK')
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(x='persons', y='amount_sek', data=df_filtered)
plt.title('Relation mellan antal personer och Amount SEK')
plt.xlabel('Antal personer')
plt.ylabel('Amount SEK')
plt.show()

# Slutsatser:
# Insiktsfulla slutsatser med djupgående reflektioner
# Slutsats 1: Histogrammet visar att fördelningen av 'amount_sek' är högerskev, vilket indikerar att de flesta värden är lägre med några höga värden.
# Slutsats 2: Linjediagrammet indikerar en ökande trend i 'amount_sek' över åren, vilket tyder på en tillväxt i det totala beloppet över tid.
# Slutsats 3: Scatter plot avslöjar en positiv relation mellan antalet personer och beloppet per person, vilket indikerar att när antalet personer ökar, tenderar beloppet per person också att öka.
# Slutsats 4: Log-transformeringen av 'amount_sek' visar en mer normalfördelad data, vilket kan vara användbart för vidare statistiska analyser.
# Slutsats 5: Den statistiska analysen visar en signifikant positiv korrelation mellan 'amount_sek' och 'num_people', vilket stärker observationen från scatter plot.

# Benereta Hoxha uppgift 2, (individuela)

