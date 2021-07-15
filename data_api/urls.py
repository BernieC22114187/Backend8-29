from django.urls import path
from data_api import views
urlpatterns = [
    # path('new', views.storeMemberNutrition),
    # path('get/<slug:member_id>', views.data),
    path('get/<slug:member_id>/<slug:timestamp>', views.func),
]
