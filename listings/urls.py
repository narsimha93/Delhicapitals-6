from django.urls import path

from . import views
from .views import listingAPIView

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path("listing",listingAPIView.as_view()),
    path('listing/<str:pk>', listingAPIView.as_view()), # to capture our ids
]
