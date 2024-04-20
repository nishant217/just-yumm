from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from accounts.views import login_page
from accounts.views import register_page
urlpatterns = [
    
    # path("admin/", admin.site.urls),
    path('login/',login_page,name='login'),
    path('register/',register_page,name='register'),
    #  path('activate/<email_token>/' , activate_email , name="activate_email"),
]