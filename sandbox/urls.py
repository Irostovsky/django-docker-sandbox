from django.contrib import admin
from django.urls import include
from django.urls import path

from tracker import views

urlpatterns = [
    path("tracker/", include("tracker.urls")),
    path("admin/", admin.site.urls),
    path("", views.IndexView.as_view(), name="index"),
]