from rest_framework.generics import GenericAPIView, ListAPIView
from stress_test_api.seriarlizers import PersonSerializer
from stress_test_api.models import Person


class PersonGenericApi(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer