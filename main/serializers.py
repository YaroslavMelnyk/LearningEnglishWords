from rest_framework import serializers
from .models import Words, Studying


class WordsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Words
        fields = '__all__'


class StudyingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studying
        fields = '__all__'

