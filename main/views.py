from django.shortcuts import render
from .models import Words, Studying
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import WordsSerializer, StudyingSerializer


def index(request):
    return render(request, 'main/index.html')


def learning(request):
    data = {
        'words': {'way': 'шлях', 'life': 'життя'}
    }

    words = Words.objects.all()
    return render(request, 'main/learning.html', {'words': words})


def testing(request):
    return render(request, 'main/testing.html')


# REST API

class WordsViewSet(viewsets.ModelViewSet):
    queryset = Words.objects.all()
    serializer_class = WordsSerializer
    #permission_classes = [permissions.IsAuthenticated]


class StudyingViewSet(viewsets.ModelViewSet):
    queryset = Studying.objects.all()
    serializer_class = StudyingSerializer
    #permission_classes = [permissions.IsAuthenticated]
    #depth = 2


