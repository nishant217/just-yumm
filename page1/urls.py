from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
# from accounts.views import login_page
# from accounts.views import register_page
from page1.views import page1_page
urlpatterns = [
    # path("admin/", admin.site.urls),

    path('',page1_page,name='page1'),
    # path('register/',register_page,name='register'),
    # path("admin/", admin.site.urls),
]