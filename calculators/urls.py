from django.urls import path
from . import views

app_name = 'calculators'

urlpatterns = [
    path('', views.home, name='home'),
    path('BMI/', views.BMI_calculator, name='BMI'),
    path('BMR/', views.BMR_calculator, name='BMR'),
]