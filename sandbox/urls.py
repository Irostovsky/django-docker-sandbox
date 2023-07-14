from django.contrib import admin
from django.contrib import admin
from django.urls import include, path
from django.urls import path

from tracker import views

urlpatterns = [
    path("tracker/", include("tracker.urls")),
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
]