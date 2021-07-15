from django.urls import path
from otherRest_api import views
urlpatterns = [
    path('new', views.storeConstMenu),
    path('get/<slug:restName>', views.get_Menu),
    path('update', views.update_menu),
]      