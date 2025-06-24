from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('adicionar/', views.adicionar_todo, name='adicionar_todo'),
    path('update/<int:id>/', views.update_todo, name='update'),
    path('delete/<int:id>/', views.delete_todo, name='delete'),
]

