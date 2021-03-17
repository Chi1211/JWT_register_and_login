from django.urls import path
from . import views
urlpatterns=[
    path('create_category/', views.CreateCategoriesView.as_view(), name='create_category'),
    path('list_category/', views.getCategoriesView.as_view(), name='get_category'),
    path('detail_category/<int:pk>', views.UpdateCategoriesView.as_view(), name='detail_category'),
    path('search_category/', views.SearchCagoriesView.as_view(), name='search_category'),
    path('create_food/', views.CreateFoodView.as_view(), name='create_food'),
    path('list_food/', views.getFoodView.as_view(), name='list_food'),
]