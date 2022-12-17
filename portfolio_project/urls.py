from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import SignupView, Login



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='homer')),
    path('login', Login.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignupView.as_view(), name='signup')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

