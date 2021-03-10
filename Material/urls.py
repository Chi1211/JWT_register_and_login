from django.urls import path
from . import views

urlpatterns=[
    path('list_material/', views.CreateMaterialView.as_view(), name="list_materia"),
    path('detail_materia/<int:pk>', views.UpdateMaterialView.as_view(), name="detail_materia"),
    path('search_materia/', views.SearchMaterialView.as_view(), name="search_materia"),
    path('list_unit/', views.GetUnitView.as_view(), name='list_unit')
]