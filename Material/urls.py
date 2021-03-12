from django.urls import path
from . import views
urlpatterns=[
    path('unit/', views.GetUnitView.as_view(), name='get_unit'),
    path('list_material/', views.CreateMaterialView.as_view(), name="list_material"),
    path('detail_material/<int:pk>', views.UpdateMaterialView.as_view(), name="detail_material"),
    path('search_material/', views.SearchMaterialView.as_view(), name="search_material"),
]