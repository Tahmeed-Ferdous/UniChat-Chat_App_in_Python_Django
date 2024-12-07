from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from authy.views import UserProfile, follow

urlpatterns = [
    # Admin URL
    path('admin/', admin.site.urls),
    
    # App URLs
    path('post/', include('post.urls')),
    path('direct/', include('direct.urls')),
    path('explore/', include('explore.urls')),  # Place the explore URLs before user-related URLs

    # User Profile URLs (These are user-specific, so they should come after explore)
    path('<username>/', UserProfile, name='profile'),
    path('<username>/saved', UserProfile, name='profilefavorites'),
    path('<username>/follow/<option>', follow, name='follow'),

    # Other URLs can be added as necessary

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
