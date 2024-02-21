from app.models import CLUB_ODS, Federation, DGeographie, Club
from django.db import IntegrityError

def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

try:
    for club_ods_entry in CLUB_ODS.objects.all():
        print(f"Vérification pour {club_ods_entry.code} - {club_ods_entry.federation}")
        code_commune_geo = get_or_none(
            DGeographie,
            code_commune_geo=f"{club_ods_entry.code_commune}-{club_ods_entry.code_qpv}"
        )
        federation = get_or_none(Federation, code_federation=club_ods_entry.code)

        if code_commune_geo and federation:
            # Créer une instance Club
            club_instance = Club(
                code_commune_geo=code_commune_geo,
                code_federation=federation,
                nombre_club=club_ods_entry.clubs,
                nombre_epa=club_ods_entry.epa
            )

            # Enregistrez l'instance dans la base de données
            club_instance.save()

            print(f"Insertion réussie pour {club_ods_entry.code_commune} - {club_ods_entry.federation}")
        else:
            print(f"Échec de l'insertion pour {club_ods_entry.code_commune} - {club_ods_entry.federation}")

    print('Fin d\'insertion des données de la table Club à partir de CLUB_ODS')
except IntegrityError as e:
    print(f"IntegrityError: {e}")
else:
    print('Insertion des données de la table Club à partir de CLUB_ODS terminée avec succès.')
