from rest_framework_mongoengine import serializers
from TASBackend.models import exercise

class ExerciseSerializer (serializers.DocumentSerializer):
    class Meta:
        model = exercise
        fields = '__all__'