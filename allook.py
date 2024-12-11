import pandas as pd

# Excel-Datei laden
file_path = "deine_datei.xlsx"  # Bitte den Pfad zur Datei hier einfügen
df = pd.read_excel(file_path)

# Filtern der Zeilen, bei denen LGXSTRUU gleich 1 ist
filtered_df = df[df['LGXSTRUU'] == 1]

# Gruppieren nach BCLASS3 (Sektoren) und ISS_Sust, Summieren der Gewichte
grouped = filtered_df.groupby(['BCLASS3', 'ISS_Sust'])['LGXSTRUU_MV_pct'].sum().reset_index()

# Pivot-Tabelle erstellen, um die Werte übersichtlich darzustellen
pivot_table = grouped.pivot(index='BCLASS3', columns='ISS_Sust', values='LGXSTRUU_MV_pct').fillna(0)

# Ausgabe der Ergebnisse
print("Prozentuale Verteilung in den verschiedenen Sektoren:")
print(pivot_table)

# Optional: Ergebnisse in eine neue Excel-Datei speichern
output_path = "ergebnisse.xlsx"  # Optional: Pfad für die Ausgabe
pivot_table.to_excel(output_path) 
