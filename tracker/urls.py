from django.urls import path

from tracker import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]