from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView

urlpatterns = [
    #path('', views.main, name="main"),
    #path('about/', views.about, name="about"),
    #path('contact/', views.contact, name="contact")
    path('', HomeView.as_view(), name="index"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail")
]