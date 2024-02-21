import os
import pandas as pd
from app.models import CLUB_ODS
from rugby.settings import DATA_DIR

def run():
    """Lire un fichier CSV, traiter les données et insérer dans le modèle Django ODS."""
    try:
        # Définir le chemin du fichier CSV
        csv_file_path = os.path.join(DATA_DIR, 'clubs-data-2021.csv')

        # Lire le fichier CSV dans un DataFrame pandas
        df = pd.read_csv(csv_file_path, sep=';',dtype=str)
        print(df.head())

        # Créer une liste pour stocker les objets ODS
        my_ods = []

        # Iterer sur les lignes du DataFrame et créer des objets ODS
        for index, row in df.iterrows():
            ods = CLUB_ODS(
                code_commune = row['Code Commune'],
                commune = row['Commune'],
                code_qpv = row['Code QPV'],
                nom_qpv = row['Nom QPV'],
            departement = row['Département'],
                region = row['Région'],
                statut_geo = row['Statut géo'],
                code = row['Code'],
                federation = row['Fédération'],
                clubs = row['Clubs'],
                epa = row['EPA'],
                total = row['Total'],
            )
            my_ods.append(ods)

        CLUB_ODS.objects.bulk_create(my_ods)
        print("Insertion des données réussie.")

    except Exception as e:
        print(f"Une erreur s'est produite: {str(e)}")

if __name__ == "__main__":
    run()

