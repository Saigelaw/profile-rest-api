from django.urls import path
from profiles_api import views


urlpatterns = [
    path('hello-apiview/',views.HelloApiView.as_view()),
]