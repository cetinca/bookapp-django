from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView

from .models import Book, BookRead


# Create your views here.

def home(request):
    context = {
        "books": Book.objects.all()
    }
    return render(request, 'book/home.html', context=context)


class BookListView(ListView):
    model = Book
    template_name = 'book/book_list.html'
    context_object_name = 'books'
    ordering = ['title']  # '-' to descending
    paginate_by = 2


class BookReadView(LoginRequiredMixin, CreateView):
    model = BookRead
    template_name = 'book/book_read.html'
    fields = ['read_book', 'content', 'read_by']

    def get_success_url(self):
        return reverse('blog_home')

    def form_valid(self, form):
        # passing user for book
        form.instance.read_by = self.request.user
        return super().form_valid(form)


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = 'book/book_create.html'
    fields = ['title', 'image']

    def get_success_url(self):
        return reverse('book_list')

    def form_valid(self, form):
        return super().form_valid(form)
