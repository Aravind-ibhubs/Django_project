from django.urls import path
from . import views

urlpatterns = [
    path("syallabus/", views.syallabus, name="syallabus"),
    path('syallabus/details/<int:id>', views.bookDetails, name="Book Details")
]

