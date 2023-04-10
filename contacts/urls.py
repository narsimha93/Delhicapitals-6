from django.urls import path

from . import views

urlpatterns = [
    path('contact/', views.contact, name='contact'),
    path('trans/', views.trans, name='trans'),
    path('reviews/',views.postComment,name="reviews"),
    # apis urls
    path('contactapi/',views.contatviews.as_view()),
    path('transportapi/',views.transportation.as_view()),
    path('reviewapi/',views.reviewsviews.as_view()),

]