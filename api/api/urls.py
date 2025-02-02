from django.contrib import admin
from django.urls import path
from stress_test_api.views import PersonGenericApi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/get_all_people/', PersonGenericApi.as_view()),
]

