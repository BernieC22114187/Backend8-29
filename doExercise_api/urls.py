from django.urls import path
from doExercise_api import views
urlpatterns = [
    path('store/<slug:member_id>/<slug:timestamp>/<slug:duration>', views.storeMemberExercise),
    path('get/<slug:member_id>/<slug:timestamp>', views.getMemberExercise),
]
