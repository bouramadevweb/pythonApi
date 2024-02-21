# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
# from rest_framework import status
# from app.models import CLUB_ODS, ODS_lic, DGeographie, City,Federation
# from .serializers import CLUB_ODS_Serializer, ODS_lic_Serializer, DGeographie_Serializer, CitySerializer,FederationSerializer

# class CLUB_ODS_ViewSet(viewsets.ModelViewSet):
#     queryset = CLUB_ODS.objects.all()
#     serializer_class = CLUB_ODS_Serializer

#     @action(detail=True, methods=['GET'])
#     def get_json(self, request, pk=None):
#         instance = self.get_object()
#         serializer = CLUB_ODS_Serializer(instance)
#         return Response(serializer.data)

#     @action(detail=False, methods=['POST'])
#     def custom_post_method(self, request):
#         serializer = CLUB_ODS_Serializer(data=request.data)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(CLUB_ODS_Serializer(instance).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ODS_lic_ViewSet(viewsets.ModelViewSet):
#     queryset = ODS_lic.objects.all()
#     serializer_class = ODS_lic_Serializer

#     @action(detail=True, methods=['GET'])
#     def get_json(self, request, pk=None):
#         instance = self.get_object()
#         serializer = ODS_lic_Serializer(instance)
#         return Response(serializer.data)

#     @action(detail=False, methods=['POST'])
#     def custom_post_method(self, request):
#         serializer = ODS_lic_Serializer(data=request.data)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(ODS_lic_Serializer(instance).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CustomPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# class DGeographie_ViewSet(viewsets.ModelViewSet):
#     """ 

#         Méthode GET :
#         Méthode POST :
#         Méthode PUT :
#         Méthode PATCH :
#         Méthode DELETE :
#     """
#     queryset = DGeographie.objects.all()
#     serializer_class = DGeographie_Serializer
#     pagination_class = CustomPagination

#     @action(detail=False, methods=['GET'])
#     def custom_get_method(self, request):
#         # Logique pour la méthode GET
#         data = {'message': 'This is a custom GET method'}
#         return Response(data, status=status.HTTP_200_OK)

#     @action(detail=True, methods=['POST'])
#     def custom_post_method(self, request):
#         # Logique pour la méthode POST
#         serializer = DGeographie_Serializer(data=request.data)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(DGeographie_Serializer(instance).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     @action(detail=True, methods=['PUT'])
#     def custom_put_method(self, request, pk=None):
#         instance = self.get_object()
#         serializer = DGeographie_Serializer(instance, data=request.data, partial=True)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(DGeographie_Serializer(instance).data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class FederationViewSet(viewsets.ModelViewSet):
#     queryset = Federation.objects.all()
#     serializer_class = FederationSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def retrieve(self, request, pk=None):
#         queryset = Federation.objects.all()
#         instance = get_object_or_404(queryset, pk=pk)
#         serializer = FederationSerializer(instance)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         instance = Federation.objects.get(pk=pk)
#         serializer = FederationSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def destroy(self, request, pk=None):
#         instance = Federation.objects.get(pk=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CityViewSet(viewsets.ModelViewSet):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer

#     @action(detail=True, methods=['GET'])
#     def get_json(self, request, pk=None):
#         instance = self.get_object()
#         serializer = CitySerializer(instance)
#         return Response(serializer.data)

#     @action(detail=False, methods=['POST'])
#     def custom_post_method(self, request):
#         serializer = CitySerializer(data=request.data)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(CitySerializer(instance).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# from rest_framework import viewsets
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from django.http import JsonResponse

# from rest_framework.pagination import PageNumberPagination
# from rest_framework import status
# from django.shortcuts import get_object_or_404
# from app.models import CLUB_ODS, ODS_lic, DGeographie, City, Federation
# from .serializers import CLUB_ODS_Serializer, ODS_lic_Serializer, DGeographie_Serializer, CitySerializer, FederationSerializer

# class CustomPagination(PageNumberPagination):
#     page_size = 20
#     page_size_query_param = 'page_size'
#     max_page_size = 100

# class CLUB_ODS_ViewSet(viewsets.ModelViewSet):
#     queryset = CLUB_ODS.objects.all()
#     serializer_class = CLUB_ODS_Serializer

#     @action(detail=True, methods=['GET'])
#     def get_json(self, request, pk=None):
#         instance = self.get_object()
#         serializer = CLUB_ODS_Serializer(instance)
#         return Response(serializer.data)

#     @action(detail=False, methods=['POST'])
#     def custom_post_method(self, request):
#         serializer = CLUB_ODS_Serializer(data=request.data)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(CLUB_ODS_Serializer(instance).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ODS_lic_ViewSet(viewsets.ModelViewSet):
#     queryset = ODS_lic.objects.all()
#     serializer_class = ODS_lic_Serializer

#     @action(detail=True, methods=['GET'])
#     def get_json(self, request, pk=None):
#         instance = self.get_object()
#         serializer = ODS_lic_Serializer(instance)
#         return Response(serializer.data)

#     @action(detail=False, methods=['POST'])
#     def custom_post_method(self, request):
#         serializer = ODS_lic_Serializer(data=request.data)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(ODS_lic_Serializer(instance).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DGeographie_ViewSet(viewsets.ModelViewSet):
#     queryset = DGeographie.objects.all()
#     serializer_class = DGeographie_Serializer
#     pagination_class = CustomPagination

#     @action(detail=False, methods=['GET'])
#     def custom_get_method(self, request):
#         data = {'message': 'GET'}
#         return Response(data, status=status.HTTP_200_OK)

#     @action(detail=True, methods=['POST'])
#     def custom_post_method(self, request):
#         serializer = DGeographie_Serializer(data=request.data)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(DGeographie_Serializer(instance).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     @action(detail=True, methods=['PUT'])
#     def custom_put_method(self, request, pk=None):
#         instance = self.get_object()
#         serializer = DGeographie_Serializer(instance, data=request.data, partial=True)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(DGeographie_Serializer(instance).data, status=status.HTTP_200_OK)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class FederationViewSet(viewsets.ModelViewSet):
#     queryset = Federation.objects.all()
#     serializer_class = FederationSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#     def retrieve(self, request, pk=None):
#         queryset = Federation.objects.all()
#         instance = get_object_or_404(queryset, pk=pk)
#         serializer = FederationSerializer(instance)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         instance = Federation.objects.get(pk=pk)
#         serializer = FederationSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def destroy(self, request, pk=None):
#         instance = Federation.objects.get(pk=pk)
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class CityViewSet(viewsets.ModelViewSet):
#     queryset = City.objects.all()
#     serializer_class = CitySerializer

#     @action(detail=True, methods=['GET'])
#     def get_json(self, request, pk=None):
#         instance = self.get_object()
#         serializer = CitySerializer(instance)
#         return Response(serializer.data)

#     @action(detail=False, methods=['POST'])
#     def custom_post_method(self, request):
#         serializer = CitySerializer(data=request.data)

#         if serializer.is_valid():
#             instance = serializer.save()
#             return Response(CitySerializer(instance).data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from app.models import CLUB_ODS, ODS_lic, DGeographie, City, Federation
from .serializers import CLUB_ODS_Serializer, ODS_lic_Serializer, DGeographie_Serializer, CitySerializer, FederationSerializer

# Vues génériques pour CLUB_ODS
class CLUB_ODS_List(generics.ListCreateAPIView):
    queryset = CLUB_ODS.objects.all()
    serializer_class = CLUB_ODS_Serializer

class CLUB_ODS_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CLUB_ODS.objects.all()
    serializer_class = CLUB_ODS_Serializer

# Vues génériques pour ODS_lic
class ODS_lic_List(generics.ListCreateAPIView):
    queryset = ODS_lic.objects.all()
    serializer_class = ODS_lic_Serializer

class ODS_lic_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ODS_lic.objects.all()
    serializer_class = ODS_lic_Serializer

# Vues génériques pour DGeographie
class DGeographie_List(generics.ListCreateAPIView):
    queryset = DGeographie.objects.all()
    serializer_class = DGeographie_Serializer

class DGeographie_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DGeographie.objects.all()
    serializer_class = DGeographie_Serializer

# Vues génériques pour Federation
class Federation_List(generics.ListCreateAPIView):
    queryset = Federation.objects.all()
    serializer_class = FederationSerializer

class Federation_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Federation.objects.all()
    serializer_class = FederationSerializer

# Vues génériques pour City
class City_List(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class City_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# Décorateurs d'API pour CLUB_ODS
@api_view(['GET', 'POST'])
def club_ods_list(request):
    if request.method == 'GET':
        return CLUB_ODS_List.as_view()(request).data
    elif request.method == 'POST':
        return CLUB_ODS_List.as_view()(request).data

@api_view(['GET', 'PUT', 'DELETE'])
def club_ods_detail(request, pk):
    return CLUB_ODS_Detail.as_view()(request, pk=pk).data

# Décorateurs d'API pour ODS_lic
@api_view(['GET', 'POST'])
def ods_lic_list(request):
    if request.method == 'GET':
        return ODS_lic_List.as_view()(request).data
    elif request.method == 'POST':
        return ODS_lic_List.as_view()(request).data

@api_view(['GET', 'PUT', 'DELETE'])
def ods_lic_detail(request, pk):
    return ODS_lic_Detail.as_view()(request, pk=pk).data

# Décorateurs d'API pour DGeographie
@api_view(['GET', 'POST'])
def dgeographie_list(request):
    if request.method == 'GET':
        return DGeographie_List.as_view()(request).data
    elif request.method == 'POST':
        return DGeographie_List.as_view()(request).data

@api_view(['GET', 'PUT', 'DELETE'])
def dgeographie_detail(request, pk):
    return DGeographie_Detail.as_view()(request, pk=pk).data

# Décorateurs d'API pour Federation
@api_view(['GET', 'POST'])
def federation_list(request):
    if request.method == 'GET':
        return Federation_List.as_view()(request).data
    elif request.method == 'POST':
        return Federation_List.as_view()(request).data

@api_view(['GET', 'PUT', 'DELETE'])
def federation_detail(request, pk):
    return Federation_Detail.as_view()(request, pk=pk).data

# Décorateurs d'API pour City
@api_view(['GET', 'POST'])
def city_list(request):
    if request.method == 'GET':
        return City_List.as_view()(request).data
    elif request.method == 'POST':
        return City_List.as_view()(request).data

@api_view(['GET', 'PUT', 'DELETE'])
def city_detail(request, pk):
    return City_Detail.as_view()(request, pk=pk).data
