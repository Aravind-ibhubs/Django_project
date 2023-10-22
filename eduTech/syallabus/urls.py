from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainPage, name="Home page"),
    path("syallabus/", views.syallabus, name="syallabus"),
    path('syallabus/details/<int:id>', views.bookDetails, name="Book Details"),
    path('testing/', views.testing, name="testing")
]

