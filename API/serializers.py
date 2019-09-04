from classes.models import Classroom
from rest_framework import serializers


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        exclude=['name']

class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        fields='__all__'


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Classroom
        exclude=['teacher']
        

