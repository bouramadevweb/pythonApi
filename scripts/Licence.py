from django.core.management.base import BaseCommand
from app.models import ODS_lic, DGeographie, Federation, FLicence, TrancheAge

def handle(*args, **kwargs):
    for ods_entry in ODS_lic.objects.all():
        tranche_age = f"{ods_entry.f_1_4_ans} {ods_entry.f_5_9_ans} {ods_entry.f_10_14_ans} {ods_entry.f_15_19_ans} {ods_entry.f_20_24_ans} {ods_entry.f_25_29_ans} {ods_entry.f_30_34_ans} {ods_entry.f_35_39_ans} {ods_entry.f_40_44_ans} {ods_entry.f_45_49_ans} {ods_entry.f_50_54_ans} {ods_entry.f_55_59_ans} {ods_entry.f_60_64_ans} {ods_entry.f_65_69_ans} {ods_entry.f_70_74_ans} {ods_entry.f_75_79_ans} {ods_entry.f_80_99_ans} {ods_entry.f_nr} {ods_entry.h_1_4_ans} {ods_entry.h_5_9_ans} {ods_entry.h_10_14_ans} {ods_entry.h_15_19_ans} {ods_entry.h_20_24_ans} {ods_entry.h_25_29_ans} {ods_entry.h_30_34_ans} {ods_entry.h_35_39_ans} {ods_entry.h_40_44_ans} {ods_entry.h_45_49_ans} {ods_entry.h_50_54_ans} {ods_entry.h_55_59_ans} {ods_entry.h_60_64_ans} {ods_entry.h_65_69_ans} {ods_entry.h_70_74_ans} {ods_entry.h_75_79_ans} {ods_entry.h_80_99_ans} {ods_entry.h_nr} {ods_entry.nr_nr}"
        tranche_age_instance, _ = TrancheAge.objects.get_or_create(code_age=tranche_age, defaults={'label_age': tranche_age})

        code_commune = ods_entry.code_commune
        code_qpv = ods_entry.code_qpv
        code_commune_geo = f"{code_commune}-{code_qpv}"
        code_commune_instance = DGeographie.objects.filter(code_commune_geo=code_commune_geo).first()
        
        if code_commune_instance is not None:
            flicence_instance = FLicence(
                tranche_age_licence=tranche_age_instance.label_age,
                code_commune_geo=code_commune_instance.code_commune_geo,
                code_federation=Federation.objects.get(code_federation=ods_entry.code),
            )
            flicence_instance.save()
            print(f"Insertion réussie pour {code_commune_geo}")
        else:
            print(f" non trouver code_commune_geo: {code_commune_geo}")

    print('Fin d\'insertion des données de la table FLicence')

# Appel de la fonction handle
handle()
