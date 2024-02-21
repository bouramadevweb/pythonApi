from rest_framework import serializers
from app.models import CLUB_ODS
from app.models import ODS_lic
from app.models import DGeographie
from app.models import City,Federation


class CLUB_ODS_Serializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = CLUB_ODS
        fields = '__all__'
        
class ODS_lic_Serializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = ODS_lic
        fields = '__all__'
        
class DGeographie_Serializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """
    class Meta:
        model = DGeographie
        fields = '__all__'
class FederationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Federation
        fields = '__all__'        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

        


