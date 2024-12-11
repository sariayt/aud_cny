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

# Gesamte Gewichte für jeden Sektor unter Berücksichtigung aller ISS_Sust-Werte
pivot_table['Total_Sektor_Gewicht_mit_ISS_Sust'] = pivot_table.sum(axis=1)

# Gesamte Gewichte pro Sektor, unabhängig von ISS_Sust
total_gewichte = filtered_df.groupby('BCLASS3')['LGXSTRUU_MV_pct'].sum().reset_index()
total_gewichte = total_gewichte.rename(columns={'LGXSTRUU_MV_pct': 'Total_Sektor_Gewicht_ohne_ISS_Sust'})

# Pivot-Tabelle mit den sektorspezifischen Gesamtgewichten zusammenführen
final_table = pivot_table.merge(total_gewichte, on='BCLASS3', how='left')

# Ausgabe der Ergebnisse
print("Ergebnisse mit und ohne Berücksichtigung von ISS_Sust:")
print(final_table)

# Optional: Ergebnisse in eine neue Excel-Datei speichern
output_path = "ergebnisse_mit_und_ohne_iss_sust.xlsx"  # Optional: Pfad für die Ausgabe
final_table.to_excel(output_path)
