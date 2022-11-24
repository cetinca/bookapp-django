from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home-page"),
    path('', views.BlogListView.as_view(), name="blog_home"),
    path('about/', views.about, name="about"),

]
