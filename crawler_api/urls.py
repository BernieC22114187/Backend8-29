from django.urls import path
from crawler_api import views
urlpatterns = [
    path('new', views.storeDailyMenu),
    path('get/<slug:date>', views.menu_id),
    # path('input/<slug:index>', views.input_filtDish)

    
    
    
]



