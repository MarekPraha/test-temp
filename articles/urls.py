from django.contrib import admin
from django.conf.urls import url, include
from articles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [

   
   url (r'admin/', admin.site.urls),
   url (r'home/', views.homepage, name="home"),
   url (r'(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
   
]


urlpatterns+=staticfiles_urlpatterns()
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)