""" """
from django.db import models
from django.db.models import UniqueConstraint


class Player(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name + self.country
    
class Personne(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    nom = models.CharField(max_length=20) 
    prenom = models.CharField(max_length=100) 
    age = models.IntegerField() 
    def pers(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f' {self.nom } {self.prenom} {self.age}'
     
class CLUB_ODS(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    code_commune = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)
    code_qpv = models.CharField(max_length=100)
    nom_qpv = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    statut_geo = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    federation = models.CharField(max_length=100)
    clubs = models.CharField(max_length=100)
    epa = models.CharField(max_length=100)
    total = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"""{self.code_commune},
                 {self.commune}, {self.code_qpv}, 
                 {self.nom_qpv}, {self.departement},
                 {self.region}, {self.statut_geo},
                 {self.code}, {self.federation},
                 {self.clubs}, {self.epa}
                """
class ODS_lic(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    code_commune = models.CharField(max_length=255)
    commune = models.CharField(max_length=255)
    code_qpv = models.CharField(max_length=255)
    nom_qpv = models.CharField(max_length=255)
    departement = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    statut_geo = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    federation = models.CharField(max_length=255)
    f_1_4_ans = models.CharField(max_length=255, default='0')
    f_5_9_ans = models.CharField(max_length=255, default='0')
    f_10_14_ans = models.CharField(max_length=255, default='0')
    f_15_19_ans = models.CharField(max_length=255, default='0')
    f_20_24_ans = models.CharField(max_length=255, default='0')
    f_25_29_ans = models.CharField(max_length=255, default='0')
    f_30_34_ans = models.CharField(max_length=255, default='0')
    f_35_39_ans = models.CharField(max_length=255, default='0')
    f_40_44_ans = models.CharField(max_length=255, default='0')
    f_45_49_ans = models.CharField(max_length=255, default='0')
    f_50_54_ans = models.CharField(max_length=255, default='0')
    f_55_59_ans = models.CharField(max_length=255, default='0')
    f_60_64_ans = models.CharField(max_length=255, default='0')
    f_65_69_ans = models.CharField(max_length=255, default='0')
    f_70_74_ans = models.CharField(max_length=255, default='0')
    f_75_79_ans = models.CharField(max_length=255, default='0')
    f_80_99_ans = models.CharField(max_length=255, default='0')
    f_nr = models.CharField(max_length=255, default='0')
    h_1_4_ans = models.CharField(max_length=255, default='0')
    h_5_9_ans = models.CharField(max_length=255, default='0')
    h_10_14_ans = models.CharField(max_length=255, default='0')
    h_15_19_ans = models.CharField(max_length=255, default='0')
    h_20_24_ans = models.CharField(max_length=255, default='0')
    h_25_29_ans = models.CharField(max_length=255, default='0')
    h_30_34_ans = models.CharField(max_length=255, default='0')
    h_35_39_ans = models.CharField(max_length=255, default='0')
    h_40_44_ans = models.CharField(max_length=255, default='0')
    h_45_49_ans = models.CharField(max_length=255, default='0')
    h_50_54_ans = models.CharField(max_length=255, default='0')
    h_55_59_ans = models.CharField(max_length=255, default='0')
    h_60_64_ans = models.CharField(max_length=255, default='0')
    h_65_69_ans = models.CharField(max_length=255, default='0')
    h_70_74_ans = models.CharField(max_length=255, default='0')
    h_75_79_ans = models.CharField(max_length=255, default='0')
    h_80_99_ans = models.CharField(max_length=255, default='0')
    h_nr = models.CharField(max_length=255, default='0')
    nr_nr = models.CharField(max_length=255, default='0')
    total = models.CharField(max_length=255, default='0')
    # date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.commune} - {self.departement}"
    


class DGeographie(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    code_commune_geo = models.CharField(max_length=255, primary_key=True)
    code_qpv_geo = models.CharField(max_length=255)
    commune_geo = models.CharField(max_length=255)
    departement_geo = models.CharField(max_length=255)
    region_geo = models.CharField(max_length=255)
    statut_geo = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        # Concaténez les champs pour créer la valeur de la clé primaire
        self.code_commune_geo = f"{self.code_commune_geo}-{self.code_qpv_geo}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.commune_geo} - {self.departement_geo}"




class TrancheAge(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """
    code_age = models.CharField(max_length=255, primary_key=True)
    label_age = models.CharField(max_length=255, default='0')
    def __str__(self):
        return f"{self.label_age}"
    

class Federation(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    code_federation = models.CharField(max_length=255, primary_key=True)
    nom_federation = models.CharField(max_length=255)
    # tranche_age_federation = models.ForeignKey(TrancheAge, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.code_federation}, {self.nom_federation}"

class DDates(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    libelle = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.libelle} - {self.date}"

class FLicence(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    Nombre_licence = models.CharField(max_length=500, primary_key=True)
  
    tranche_age_licence = models.ForeignKey(TrancheAge, on_delete=models.CASCADE)
    code_commune_geo = models.ForeignKey(DGeographie, on_delete=models.CASCADE)
    code_federation = models.ForeignKey(Federation, on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        # Concaténez les champs pour créer la valeur de la clé primaire
        self.Nombre_licence = f"{self.code_commune_geo}-{self.code_federation}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.Nombre_licence}, {self.code_commune_geo}"
class Club(models.Model):
    code_club = models.CharField(max_length=255, primary_key=True)
    code_commune_geo = models.ForeignKey(DGeographie, on_delete=models.CASCADE)
    code_federation = models.ForeignKey(Federation, on_delete=models.CASCADE)
    nombre_club = models.IntegerField() 
    nombre_epa = models.IntegerField() 

    def save(self, *args, **kwargs):
       
        self.code_club = f"{self.code_commune_geo}-{self.code_federation}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code_club}, {self.nombre_club}"
    
class City(models.Model):
    """summary

    Args:
        models (type): description
    """
    postal_code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=300)
    department = models.CharField(max_length=300)
    region = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
