from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .views import DGeographie_ViewSet, CityViewSet
from app.models import DGeographie, City
from .serializers import DGeographie_Serializer, CitySerializer
import json


class DGeographieTestCase(TestCase):
    """_summary_

    Args:
        TestCase (_type_): _description_
    """
    def setUp(self):
        self.geo_instance = DGeographie(
            code_commune_geo="123",
            code_qpv_geo="456",
            commune_geo="Paris",
            departement_geo="75",
            region_geo="Ile-de-France",
            statut_geo="Test"
        )

    def test_str_method(self):
        """_summary_
        """
        expected_str = "Paris - 75"
        self.assertEqual(str(self.geo_instance), expected_str)

    def test_save_method(self):
        """_summary_
        """
        self.geo_instance.save()
        expected_code_commune = "123-456"
        self.assertEqual(self.geo_instance.code_commune_geo, expected_code_commune)

    def test_geo_instance_creation(self):
        """_summary_
        """
        expected_data = {
            "code_commune_geo": "123",
            "code_qpv_geo": "456",
            "commune_geo": "Paris",
            "departement_geo": "75",
            "region_geo": "Ile-de-France",
            "statut_geo": "Test"
        }
        actual_data = {
            "code_commune_geo": self.geo_instance.code_commune_geo,
            "code_qpv_geo": self.geo_instance.code_qpv_geo,
            "commune_geo": self.geo_instance.commune_geo,
            "departement_geo": self.geo_instance.departement_geo,
            "region_geo": self.geo_instance.region_geo,
            "statut_geo": self.geo_instance.statut_geo,
        }

        self.assertEqual(actual_data, expected_data)

    def test_geo_instance_creation_json_response(self):
        # Convertir les données de l'instance en format JSON
        expected_json_data = json.dumps({
            "code_commune_geo": "123",
            "code_qpv_geo": "456",
            "commune_geo": "Paris",
            "departement_geo": "75",
            "region_geo": "Ile-de-France",
            "statut_geo": "Test"
        })

        actual_json_data = json.dumps({
            "code_commune_geo": self.geo_instance.code_commune_geo,
            "code_qpv_geo": self.geo_instance.code_qpv_geo,
            "commune_geo": self.geo_instance.commune_geo,
            "departement_geo": self.geo_instance.departement_geo,
            "region_geo": self.geo_instance.region_geo,
            "statut_geo": self.geo_instance.statut_geo,
        })

        self.assertEqual(actual_json_data, expected_json_data)

