from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('books', BookModelViewSet, basename='bookss')
# urlpatterns = router.urls
# urlpatterns += [

urlpatterns = [
    path('', include(router.urls)),
    path('category_api/', CategoryAPIView.as_view() , name='category_api'),
    path('article_list_api/', ArticleListGenericAPIView.as_view() , name='article_list_api'),
    path('article_detail_api/<int:id>', ArticleDetailGenericAPIView.as_view() , name='article_detail_api'),
]
