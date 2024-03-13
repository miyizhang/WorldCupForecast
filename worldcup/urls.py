from django.urls import path, include
from prediction.admin import custom_admin_site
from django.contrib.auth import views as auth_views
from django.shortcuts import render

def home_page(request):
    return render(request, 'homePage/homePage.html')

urlpatterns = [
    path('admin/', custom_admin_site.urls),
    path('home/', include('prediction.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/home/'), name='logout'),
    path('', home_page, name='home_page'),
]
