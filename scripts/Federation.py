""" Federation """
from app.models import CLUB_ODS, Federation
from django.db import IntegrityError

try:
    for federation_entry in CLUB_ODS.objects.all():
        print(f"insertion des donnée pour {federation_entry.code} - {federation_entry.federation}")

        Federation_instance = Federation(
            code_federation=federation_entry.code,
            nom_federation=federation_entry.federation
        )
        # Enregistrez dans la base de données
        Federation_instance.save()
    print('Fin d\'insertion des données de la table federation')
except IntegrityError as e:
    print(f"IntegrityError: {e}")
else:
    print('Insertion des données de la table federation terminée avec succès.')
