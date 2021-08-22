from django.urls import path
from exercise_api import views
urlpatterns = [
    path('<slug:exercise_name>', views.get_exercise)
    
]




