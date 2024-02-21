from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CLUB_ODS_ViewSet, ODS_lic_ViewSet, DGeographie_ViewSet
# from .views import CityViewSet,FederationViewSet

#,endpoint

# router = DefaultRouter()
# router.register(r'club_ods', CLUB_ODS_ViewSet)
# router.register(r'ods_lic', ODS_lic_ViewSet)
# router.register(r'dgeographie', DGeographie_ViewSet, basename='dgeographie')
# router.register(r'federation', FederationViewSet, basename='federation')
# router.register(r'cities', CityViewSet, basename='city')



# urlpatterns = [
#     # path('', include(router.urls)),
#     # path('endpoint/', endpoint, name='endpoint'),
#     path('', views.index),
# ]
from django.urls import path
from .views import CLUB_ODS_List, CLUB_ODS_Detail, ODS_lic_List, ODS_lic_Detail, DGeographie_List, DGeographie_Detail, Federation_List, Federation_Detail, City_List, City_Detail

urlpatterns = [
    path('club_ods/', CLUB_ODS_List.as_view(), name='club_ods_list'),
    path('club_ods/<int:pk>/', CLUB_ODS_Detail.as_view(), name='club_ods_detail'),
    path('ods_lic/', ODS_lic_List.as_view(), name='ods_lic_list'),
    path('ods_lic/<int:pk>/', ODS_lic_Detail.as_view(), name='ods_lic_detail'),
    path('dgeographie/', DGeographie_List.as_view(), name='dgeographie_list'),
    path('dgeographie/<int:pk>/', DGeographie_Detail.as_view(), name='dgeographie_detail'),
    path('federation/', Federation_List.as_view(), name='federation_list'),
    path('federation/<int:pk>/', Federation_Detail.as_view(), name='federation_detail'),
    path('city/', City_List.as_view(), name='city_list'),
    path('city/<int:pk>/', City_Detail.as_view(), name='city_detail'),
]
