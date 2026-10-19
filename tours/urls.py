from django.urls import path 
from .models import TourPackageModel
from .views import TourPackageView


urlpatterns = [
    path('tourpackages/',TourPackageView.as_view(),name='tourpackagemodel')
]
