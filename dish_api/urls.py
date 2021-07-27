from django.urls import path
from dish_api import views
urlpatterns = [
    path('new', views.storeNutrition),
    path('<slug:dishID>', views.dish_id),
    path('update', views.update_dish),
    path('delete', views.delete_dish),
    # path('getDish/<slug:dishName>', views.dish_filter),
    # path('input/<slug:index>', views.input_filtDish)
    path('input/<slug:index>/<slug:timestamp>', views.input_filtDish)
    
]




