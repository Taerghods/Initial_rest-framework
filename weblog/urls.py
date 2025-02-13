from django.urls import path, include
from django.views.generic import TemplateView
import weblog
from weblog.api.v1.views import *

urlpatterns = [
    # path('', TemplateView.as_view(template_name="main.html"), name='main'),
    # path('api/', include('weblog.api.v1.urls'), name='weblog_api'),

]
