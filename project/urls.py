from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path 
from news.views import homepage,about
from news.views import homepage,about,reviews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage,name='homepage'),
    path("about-us/", about,name="about"),
    path("reviews/", reviews,name="reviews"),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


