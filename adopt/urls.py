from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('<int:pet_id>/',views.get_pet),
    path('list/', views.list_pets),
]

