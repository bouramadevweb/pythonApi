import requests

from app.models import DGeographie


class Geocoding:

    def get_departement(self, value):
        url = 'https://maps.googleapis.com/maps/api/geocode/json'
        params = {
            'key': 'AIzaSyBC1OnjBomcXWYcCtL6N7LwTWwQiXlFpws',
            'address': value
        }

        result = requests.get(url, params=params)
        data = result.json()

        if 'results' in data and data['results']:
            address_components = data['results'][0]['address_components']
            if len(address_components) >= 2:
                return address_components[1]['long_name']

        return "Département non trouvé"

def run():
    geo = Geocoding()
    geocoding = DGeographie.objects.values_list('pk_geographie', 'code_commune_geo', 'commune_geo').distinct()
    for pk_geographie, code_commune_geo, commune_geo in geocoding:
        value = f"{code_commune_geo} - {commune_geo}"
        department = geo.get_departement(value)
        print(f"Code commune: {code_commune_geo}, Commune: {commune}, Department: {department}")

        instance = DGeographie.objects.get(pk=pk_geographie)
        instance.nom_departement = department
        instance.save()