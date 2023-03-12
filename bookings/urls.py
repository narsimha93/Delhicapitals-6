from . import views
from django.urls import path

urlpatterns = [
    path("book/",views.booking,name="book"),
    path("booking/",views.allbookings,name="allbookings"),

]
