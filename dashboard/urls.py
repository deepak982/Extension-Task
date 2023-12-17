from django.contrib import admin
from django.urls import path,include
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product',ProductViewset)
router.register(r'data',DataViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('api/',include(router.urls)),
    path('weather/',weather,name='weather'),
    path('visulization/',visulization,name='visulization'),

    path('login/',login,name='login'),
    path('sign-up/',sign_up,name="sign-up"),
    path('logout/',logout,name="logout"),
    path('verify/<str:token>/',verify,name="verify"),
    
    # Foret Password
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name = 'password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'),name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
