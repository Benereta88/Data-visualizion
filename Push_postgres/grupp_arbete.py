import numpy as np
import os
import pandas as pd
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt

# EXTRACT:
# Steg 1: Importera CSV-filen
csv_file_path = "C:\\Users\\Book\\OneDrive - TUC Sweden\\Skrivbordet\\inlämnnings-uppgift\\paid_unemployment_benefit_fund__year.csv"
df = pd.read_csv(csv_file_path)
print("Steg 1: Importera CSV-filen")
print(df.head())

# TRANSFORM:
# Steg 2: Hantera saknade värden
# Här antar vi att saknade värden fylls med 0 där det är meningsfullt.
df.fillna(0, inplace=True)
print("Steg 2: Hantera saknade värden")
print(df.head())

# Steg 3: Skapa nya kolumner baserat på beräkningar
# Vi skapar en kolumn för 'amount_per_day' som är amount_sek dividerat med days
if 'amount_sek' in df.columns and 'days' in df.columns:
    df['amount_per_day'] = df['amount_sek'] / df['days'].replace(0, np.nan)  # Undvik division med 0
else:
    print("Kolumnerna 'amount_sek' och/eller 'days' saknas i CSV-filen.")
print("Steg 3: Skapa nya kolumner")
print(df.head())

# Steg 4: Filtrera datan
# Filtrera för att endast inkludera data från år 2005 och framåt.
# Exempel på en fråga kan vara: "Hur har antalet betalningar förändrats över tid?"
if 'year' in df.columns:
    df_filtered = df[df['year'] >= 2005]
else:
    print("Kolumnen 'year' saknas i CSV-filen.")
    df_filtered = df
print("Steg 4: Filtrera datan")
print(df_filtered.head())

# Steg 5: Använd groupby() och agg() för att summera och analysera nyckeltal
# Vi kan svara på frågor som: "Hur mycket har betalats ut totalt per år?" genom att gruppera efter år och summera
summary = df_filtered.groupby('year').agg({
    'amount_sek': 'sum',
    'days': 'sum'
})
print("Steg 5: Använd groupby() och agg()")
print(summary)

# Steg 6: Lägg till summering av 'amount_per_day' (om relevant)
summary['amount_per_day'] = summary['amount_sek'] / summary['days'].replace(0, np.nan)  # Undvik division med 0
print("Steg 6: Lägg till summering av 'amount_per_day'")
print(summary)

# Steg 7: Besvara frågor genom att analysera och visualisera datan

# Fråga 1: Hur mycket har betalats ut per år?
plt.figure(figsize=(10, 6))
sns.lineplot(data=summary, x=summary.index, y='amount_sek')
plt.title("Total Betalning per År")
plt.xlabel("År")
plt.ylabel("Total Betalning (SEK)")
plt.show()

# Fråga 2: Hur har antalet dagar förändrats över tid?
plt.figure(figsize=(10, 6))
sns.lineplot(data=summary, x=summary.index, y='days')
plt.title("Totala Dagar per År")
plt.xlabel("År")
plt.ylabel("Totala Dagar")
plt.show()

# Fråga 3: Vad är det genomsnittliga beloppet per dag för varje år?
plt.figure(figsize=(10, 6))
sns.lineplot(data=summary, x=summary.index, y='amount_per_day')
plt.title("Genomsnittligt Belopp per Dag per År")
plt.xlabel("År")
plt.ylabel("Belopp per Dag (SEK)")
plt.show()

# Fråga 4: Finns det någon skillnad i beloppet beroende på kön? (Generell analys baserat på kolumnen 'gener')
if 'gener' in df.columns:
    gender_summary = df.groupby(['year', 'gener']).agg({'amount_sek': 'sum'}).unstack()
    gender_summary.columns = gender_summary.columns.droplevel()
    gender_summary.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title("Totala Betalningar per Kön och År")
    plt.xlabel("År")
    plt.ylabel("Totala Betalningar (SEK)")
    plt.show()

# Fråga 5: Vilken åldersgrupp har fått mest i ersättning varje år? (Basera på 'age_range_year')
if 'age_range_year' in df.columns:
    age_group_summary = df.groupby(['year', 'age_range_year']).agg({'amount_sek': 'sum'}).unstack()
    age_group_summary.columns = age_group_summary.columns.droplevel()
    age_group_summary.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title("Totala Betalningar per Åldersgrupp och År")
    plt.xlabel("År")
    plt.ylabel("Totala Betalningar (SEK)")
    plt.show()

# Fråga 6: Vad är den största betalningen som gjorts under ett år? (Beräknat per år)
max_payment_per_year = df.groupby('year')['amount_sek'].max()
print("Fråga 6: Största betalning per år")
print(max_payment_per_year)

# Fråga 7: Hur många dagar har betalats totalt per år?
total_days_per_year = df.groupby('year')['days'].sum()
print("Fråga 7: Totalt antal dagar per år")
print(total_days_per_year)

# Fråga 8: Vilken är den genomsnittliga betalningen per dag?
avg_amount_per_day = summary['amount_per_day'].mean()
print(f"Fråga 8: Genomsnittlig betalning per dag: {avg_amount_per_day:.2f} SEK")

# Fråga 9: Vad är den totala summan för alla år?
total_amount_all_years = df['amount_sek'].sum()
print(f"Fråga 9: Totalt belopp för alla år: {total_amount_all_years:.2f} SEK")

# LOAD:
# Steg 8: Exportera den bearbetade datan till en Excel-fil
summary.to_excel("C:\\Users\\Book\\OneDrive - TUC Sweden\\Skrivbordet\\inlämnnings-uppgift\\processed_data.xlsx", engine='openpyxl')

# Kontrollera om Excel-filen har skapats korrekt
excel_file_path = "C:\\Users\\Book\\OneDrive - TUC Sweden\\Skrivbordet\\inlämnnings-uppgift\\processed_data.xlsx"
if os.path.exists(excel_file_path):
    print(f"Excel-filen har skapats korrekt: {excel_file_path}")
else:
    print("Något gick fel, Excel-filen skapades inte.")
