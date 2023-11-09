from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings  # Import Django settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('personal/', include('personal.urls')),  # Add a comma here
    path('polls/', include('polls.urls')),
    path('', include('user_auth.urls')),
]
