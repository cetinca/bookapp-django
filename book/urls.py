from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home-page"),
    path('new/', views.BookCreateView.as_view(), name="book_create"),
    # path('books/read/', views.BookListView.as_view(), name="book_read"),
    # path('read/<pk>', views.book_read, name="book_read"),
    path('list/', views.BookListView.as_view(), name="book_list"),
    path('read/<pk>', views.BookReadView.as_view(), name="book_read"),
]
