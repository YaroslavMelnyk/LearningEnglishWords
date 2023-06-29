from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'words', views.WordsViewSet)
router.register(r'studying', views.StudyingViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('learning/', views.learning, name='learning'),
    path('testing/', views.testing, name='testing'),
    path('api/', include(router.urls)),
    path('api-main/', include('rest_framework.urls', namespace='rest_framework'))
]