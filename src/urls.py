from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from weblog.api.v1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('weblog/', include('weblog.urls'), name='weblog'),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('api/', include('weblog.api.v1.urls'), name='weblog_api'),
    path('', TemplateView.as_view(template_name="home.html"), name='main'),
]
