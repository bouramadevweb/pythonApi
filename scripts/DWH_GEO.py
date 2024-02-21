"""Module import python"""
from app.models import CLUB_ODS
from app.models import DGeographie
from django.db import IntegrityError

try:
    for club_ods_entry in CLUB_ODS.objects.all():
        print(f"insertion des donnée pour {club_ods_entry.code_commune} - {club_ods_entry.commune}")
       
        geographie_instance = DGeographie(
           
            code_commune_geo=club_ods_entry.code_commune,
            code_qpv_geo=club_ods_entry.code_qpv,
            commune_geo=club_ods_entry.commune,
            departement_geo=club_ods_entry.departement,
            region_geo=club_ods_entry.region,
            statut_geo=club_ods_entry.statut_geo,
        )

        # Enregistrez dans la base de données
        geographie_instance.save()

    print('Fin d\'insertion des données de la table DGeographie')
except IntegrityError as e:
    print(f"IntegrityError: {e}")
else:
    print('Insertion des données de la table DGeographie terminée avec succès.')

