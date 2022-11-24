from django.shortcuts import render
from django.views.generic import ListView

from book.models import BookRead


# Create your views here.


class BlogListView(ListView):
    model = BookRead
    template_name = 'blog/home.html'
    context_object_name = 'books'
    ordering = ['-read_on']  # '-' to descending
    paginate_by = 3


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})
