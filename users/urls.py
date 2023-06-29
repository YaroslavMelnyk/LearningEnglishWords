from django.urls import path, include
from .views import SignUpView, LoginVue
from . import views
from django.contrib.auth.models import User
from rest_framework import routers #, serializers, viewsets
from django.contrib.auth.views import LogoutView



# Serializers define the API representation.
#class UserSerializer(serializers.HyperlinkedModelSerializer):
#    class Meta:
#        model = User
#        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
#class UserViewSet(viewsets.ModelViewSet):
#    queryset = User.objects.all()
#    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)



urlpatterns = [
    #path('', include('django.contrib.auth.urls'), name='login'),
    path('login/', LoginVue.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', views.profile, name='profile'),
    path('api/', include(router.urls)),
    path('api/', include('rest_framework.urls'))
]

