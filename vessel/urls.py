from django.urls import path
from .views import (RegisterNewVesselView,
                    ListVesselView,
                    RetrieveVesselView,
                    )

app_name = "api-vessel"

urlpatterns = [
    path('register_vessel', RegisterNewVesselView.as_view(), name='register_vessel'),
    path('list_vessel', ListVesselView.as_view(), name='list_vessel'),
    path('retrieve_vessel/<str:vessel_code>', RetrieveVesselView.as_view(), name='retrieve_vessel'),
]