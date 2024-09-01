from django.urls import path

from . import views

urlpatterns = [
    path( "upscprelims/", views.preQuestions )
]