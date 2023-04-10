from django.urls import path

from . import views


urlpatterns = [
    path('realtor',views.realtorapi.as_view()),
]
