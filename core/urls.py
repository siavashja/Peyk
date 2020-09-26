from django.conf.urls import url
from django.urls import path
from .views import *
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = "core"

schema_view = get_schema_view(
    openapi.Info(
        title="PEyk API",
        default_version='development version',
        description="Peyk API Documentation",
        contact=openapi.Contact(email="alimahdiyar77@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('start_session/', LocationSetCreateView.as_view()),
    path('add_location/', LocationCreateView.as_view()),
    path('end_session/', LocationSetEndView.as_view())
]