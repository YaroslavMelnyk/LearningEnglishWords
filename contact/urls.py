from django.urls import path, include
from contact.models import Contact
from rest_framework import routers, serializers, viewsets


# Serializers define the API representation.
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


# ViewSets define the view behavior.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()    # SELECT * FROM contact_contact
    serializer_class = ContactSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'contacts', ContactViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]
