from django.urls import path
from app import views

urlpatterns = [
    path('delete/<int:id>/',views.DeleteData,name="delete"),
    path('<int:id>/',views.Update,name="update"),
]