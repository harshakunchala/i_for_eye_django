import patterns as patterns
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('ngo/', views.NGOreg, name='NGOreg'),
    path('vol/',views.volreg,name='volreg'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('loginvol/',views.loginvol,name='loginvol'),
    path('loginngo/',views.login_view,name='loginngo'),
    path('loginvolun/',views.loginvolun,name='loginvolun'),
    path('register/', views.register,name='register'),
    path('Volunteers/', views.Volunteers, name='Volunteers'),
    path('audio/<str:name>/',views.audio,name='audio'),
    path('booksupload/',views.booksupload,name='booksupload'),
    path('dbbook/',views.dbbook,name='dbbook'),
    path('selectaudio/<str:name>/', views.selectaudio,name='selectaudio'),
    path('finalselect/<str:name>/<str:name1>/',views.finalselect,name='finalselect'),
]
print(settings.BASE_DIR)
# urlpatterns= urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
