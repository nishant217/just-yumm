from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
# from accounts.views import login_page
# from accounts.views import register_page
from home.views import home_page
urlpatterns = [
    # path("admin/", admin.site.urls),

    path('',home_page,name='home'),
    # path('register/',register_page,name='register'),
    # path("admin/", admin.site.urls),
]