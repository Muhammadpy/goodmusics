from django.urls import path
from .views import function,article_detail,category_articles

urlpatterns = [
   
    path('', function),
    path('article/<int:article_id>', article_detail),
    path('category/<int:category_id>', category_articles ),
]
