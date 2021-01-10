from django.urls import path
import markdown2
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:entry>", views.display_entry),
    path("?q<str:entry>", views.search)
]
