from rest_framework_mongoengine import serializers
from TASBackend.models import doExercise

class doExerciseSerializer (serializers.DocumentSerializer):
    class Meta:
        model = doExercise
        fields = '__all__'