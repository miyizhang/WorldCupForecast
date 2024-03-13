from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('select/', views.select_view, name='select'),
    path('predict/', views.predict_view, name='predict'),
    path("register/", views.register, name="register"),
    path('country_display',views.country_display, name='country_display'),
]
